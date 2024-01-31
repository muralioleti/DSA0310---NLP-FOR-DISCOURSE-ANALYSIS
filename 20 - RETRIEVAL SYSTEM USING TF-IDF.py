from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Sample documents
documents = [
    "This is the first document.",
    "The second document is shorter.",
    "And this is the third and final document."
]

# Query
query = "This is a query document."

# Vectorize the documents and query using TF-IDF
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform([query] + documents)

# Calculate cosine similarities between the query and each document
cosine_similarities = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1:]).flatten()

# Rank documents based on cosine similarities
document_ranks = sorted(enumerate(cosine_similarities, start=1), key=lambda x: x[1], reverse=True)

# Print the ranked documents
print("Query:", query)
print("Ranked Documents:")
for rank, similarity in document_ranks:
    print(f"Document {rank}: Similarity = {similarity:.4f} - {documents[rank - 1]}")
