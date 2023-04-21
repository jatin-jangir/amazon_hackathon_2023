import torch
from transformers import BertTokenizer, BertModel
from scipy.spatial.distance import cosine

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')


def product_similarity(title1, title2):
    # tokenize the titles
    tokens1 = tokenizer.encode(title1, add_special_tokens=True)
    tokens2 = tokenizer.encode(title2, add_special_tokens=True)

    # convert tokens to tensors
    input1 = torch.tensor(tokens1).unsqueeze(0)
    input2 = torch.tensor(tokens2).unsqueeze(0)

    # pass the inputs through the model
    with torch.no_grad():
        output1 = model(input1)
        output2 = model(input2)

    # get the embeddings for the [CLS] tokens
    cls1_embedding = output1.last_hidden_state[0][0]
    cls2_embedding = output2.last_hidden_state[0][0]

    # calculate the cosine similarity between the embeddings
    similarity = 1 - cosine(cls1_embedding.numpy(), cls2_embedding.numpy())
    return similarity


