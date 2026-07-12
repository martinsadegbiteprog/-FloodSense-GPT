from sentence_transformers import SentenceTransformer
import faiss
import pickle

docs = [
    "Flooding occurs when rainfall exceeds drainage capacity.",
    "Urban flooding in Lagos is caused by poor drainage and heavy rainfall.",
    "Green-Ampt model explains infiltration in soils.",
    "High soil moisture increases runoff and flood risk.",
    "Drainage systems reduce flood impact."
]

model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = model.encode(docs)

index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)

faiss.write_index(index, "rag_index.faiss")

with open("docs.pkl", "wb") as f:
    pickle.dump(docs, f)

print("RAG index built ✅")
