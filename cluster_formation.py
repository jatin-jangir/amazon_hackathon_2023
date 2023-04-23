from nltk.corpus import stopwords
import boto3
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from nltk.tokenize import word_tokenize
import nltk
nltk.download('stopwords')
nltk.download('punkt')

# Set up stop words
stop_words = set(stopwords.words('english'))


def get_comman_words(strings):

    # Tokenize and remove stop words from each string
    processed_strings = []
    for string in strings:
        # Tokenize
        words = word_tokenize(string.lower())
        # Remove stop words
        filtered_words = [word for word in words if word not in stop_words]
        # Join filtered words back into a string
        processed_strings.append(' '.join(filtered_words))

    # Use TF-IDF vectorizer to get important words
    vectorizer = TfidfVectorizer()
    tfidf = vectorizer.fit_transform(processed_strings)

    # Get the vocabulary of the vectorizer
    vocab = vectorizer.vocabulary_
    # Get the top 3 important words for each string
    num_top_words = 3
    common = {"the"}
    for i, string in enumerate(strings):
        # Get the TF-IDF scores for each word in the string
        scores = {}
        for word in word_tokenize(string.lower()):
            if word not in stop_words:
                if word in vocab:
                    scores[word] = tfidf[i, vocab[word]]
        # Sort the words by their scores in descending order
        sorted_words = sorted(scores, key=scores.get, reverse=True)
        # Print the top N words
        common.update(sorted_words[:num_top_words])
    return ' '.join(common)


def make_cluster(filename):

    # Read in product data
    product_data = pd.read_csv(
        "https://amazon-hackathon-2023-new.s3.ap-south-1.amazonaws.com/dataset/"+filename)
    # Replace missing values with empty string
    product_data.fillna('', inplace=True)
    try:
        # Create TF-IDF vectorizer
        tfidf_vectorizer = TfidfVectorizer(
            stop_words='english', min_df=1, max_df=0.9)

        # Concatenate columns into a single string column
        product_data['combined_text'] = product_data['TITLE'] + \
            ' ' + product_data['DESCRIPTION'] + " "+product_data["BULLET_POINTS"]

        # Drop the original title and description columns
        product_data.drop(
            ['TITLE', 'DESCRIPTION', 'BULLET_POINTS'], axis=1, inplace=True)

        # Fit and transform product descriptions using TF-IDF vectorizer
        tfidf_matrix = tfidf_vectorizer.fit_transform(product_data['combined_text'])

        # Run K-means clustering algorithm
        print(int((product_data.shape[0])/10))
        num_clusters = 1
        if (int((product_data.shape[0]) > 10000)):
            num_clusters = 50
        elif (int((product_data.shape[0])>100)):
            num_clusters = int((product_data.shape[0])/10)
        else:
            num_clusters = int((product_data.shape[0]))
        km = KMeans(n_clusters=num_clusters)
        km.fit(tfidf_matrix)

        # Add predicted cluster labels to product data
        product_data['cluster'] = km.labels_

        # View clusters
        # for i in range(num_clusters):
        #     cluster = product_data[product_data['cluster'] == i]
        #     print(f"Cluster {i}:")
        #     print(cluster['PRODUCT_ID'].values)
        #     print('-'*50)
        print(filename)

        # Group the dataframe by clusterID
        grouped = product_data.groupby('cluster')
        # Create an empty list to store the arrays of titles
        title_arrays = {}

        # Iterate through each cluster and append an array of the titles to title_arrays
        for cluster_id, group in grouped:
            title_array = group['combined_text'].values
            title_arrays[cluster_id] = get_comman_words(title_array)
        title_arrays = pd.Series(title_arrays)
        avg_lengths = grouped['PRODUCT_LENGTH'].mean()
        frame = {'keywords': title_arrays,
                'avg_length': avg_lengths}
        # Creating Dataframe
        result = pd.DataFrame(frame)

        result.to_csv('cluster/'+filename)
        s3 = boto3.client('s3')
        s3.upload_file('cluster/'+filename,
                    "amazon-hackathon-2023-new", "cluster/"+filename)
    except:
        product_data = pd.read_csv(
            "https://amazon-hackathon-2023-new.s3.ap-south-1.amazonaws.com/dataset/"+filename)
        # Replace missing values with empty string
        product_data.fillna('', inplace=True)
        # Concatenate columns into a single string column
        product_data['combined_text'] = product_data['TITLE'] + \
            ' ' + product_data['DESCRIPTION'] + \
            " "+product_data["BULLET_POINTS"]

        # Drop the original title and description columns
        product_data.drop(
            ['TITLE', 'DESCRIPTION', 'BULLET_POINTS'], axis=1, inplace=True)
        frame = {'keywords': product_data['combined_text'],
                 'avg_length': product_data['PRODUCT_LENGTH']}
        # Creating Dataframe
        result = pd.DataFrame(frame)

        result.to_csv('cluster/'+filename)
        s3 = boto3.client('s3')
        s3.upload_file('cluster/'+filename,
                       "amazon-hackathon-2023-new", "cluster/"+filename)
        

