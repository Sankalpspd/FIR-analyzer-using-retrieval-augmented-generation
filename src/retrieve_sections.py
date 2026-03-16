import numpy as np
import nltk
from nltk.tokenize import sent_tokenize
import pickle
import faiss
import pandas as pd
from sentence_transformers import SentenceTransformer

# load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")
def retrieve_sections(fir_text):
 sentences = sent_tokenize(fir_text)
 sentence_embeddings = [model.encode(sentence) for sentence in sentences]

 sentence_embeddings = np.array(sentence_embeddings).astype("float32")
 faiss.normalize_L2(sentence_embeddings)

 # Load FAISS index
 faiss_index = faiss.read_index("faiss_db/faiss_index.bin")

 # Load embeddings if needed
 with open("faiss_db/section_embeddings.pkl", "rb") as f:
    embeddings = pickle.load(f)
 top_k = 7
 distances, indices = offence_index.search(sentence_embeddings, top_k)

 retrieved_ids_offence = []

 for idx_list in indices:
    for idx in idx_list:
        retrieved_ids_offence.append(idx)
 
 retrieved_ids_offence = list(dict.fromkeys(retrieved_ids_offence))
 retrieved_ids_offence = list(set(retrieved_ids_offence))
 return retrieved_ids_offence

