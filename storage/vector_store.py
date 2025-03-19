import faiss
import numpy as np

class VectorStore:
    def __init__(self, dimension):
        self.index = faiss.IndexFlatL2(dimension)
        self.data = []

    def add(self, vectors, metadata):
        self.index.add(np.array(vectors).astype('float32'))
        self.data.extend(metadata)

    def search(self, query_vector, top_k=5):
        distances, indices = self.index.search(np.array([query_vector]).astype('float32'), top_k)
        results = [self.data[i] for i in indices[0]]
        return results
