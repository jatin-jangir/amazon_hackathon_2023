The solution to the problem given in Amazon ML Challenge 2023, by the team bugBUTCHERS is explained as follows :

Dataset partitions : 

For evaluating and changing the parameters : 
Only a fraction of the given dataset is considered for tuning the variables/ parameters that affect the ML algorithm, for faster execution.

For evaluating the model finally : 
The given training dataset is split into a 80-20 ratio for training and testing respectively.

For final submission :
The final model to be submitted is trained on the entire given dataset.


Approach :

Building the Model : 

By analyzing the dataset, we observed that there are a few broad product types containing various products. We first divided the given training data csv into various csv(s), grouping the records by the 'product type id' attribute. We observed that in a given product type, there are various products and the information that separates them from one another is contained in the 'title', 'description', and 'bullet points' attributes. So we concatenated these strings into a single string for further processing. We then preprocessed these strings to eliminate the unnecessary words which do not sensibly contribute or contribute very less towards separating the records in a given product type with their English meaning. This step includes removing the stopwords, tokenizing, and other NLP data preprocessing techniques. As a result, we got a set of strings containing only the keywords which describe the product and serve as a distinguishing feature for separating the product from other non-similar products within the same product type. After this, we took these set of strings(string are basically keyword sets) for all the products within a particular product type and applied some clustering algorithms to cluster them and then applied various set operations like union and intersection to derive various sets of keywords to describe and identify a cluster (referred henceforth as the Cluster Keyword Set or CKS). We then took the average of the lengths of a the records that fell in a cluster and stored the CKS and average length of each cluster in a separate file for all the clusters in a particular product type. We thus got various files for different product types containing details about the clustersin a particular product type. The rationale behind the clustering process was to reduce the time and increase the accuracy when testing the test dataset with the model. Now the model is ready, which is, the various csv files for all the product type IDs containing details about the clusters of records of that product type, like the average length and the CKS. 

Predicting the Length : 

We shall apply the keyword extraction algorithm mentioned above to each record of concatenated string (title, description and bullet points) of the test dataset to consider only the main set of keywords which describe a particular record. We then take this set of keywords and match it with the CKS of all the clusters of the file having the same product type ID from the set of files which constitute our model. We consider the top clusters with match percentage more than n%, where the value of n is found by experimenting for maximum accuracy. The resultant answer for predicting the length shall be the average of the average length attributes of the most-matched clusters. 
