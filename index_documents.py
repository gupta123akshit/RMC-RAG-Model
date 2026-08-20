from src.ingestion import load_all_pdfs
from src.chunking import create_chunks
from src.metadata import enrich_chunks
from src.embeddings import load_embedding_model
from src.vector_store import create_vector_store, add_documents


# 1. Load all PDFs
pages = load_all_pdfs("data/pdfs")

print(f"\nTotal pages loaded: {len(pages)}")


# 2. Create chunks
chunks = create_chunks(pages)

print(f"Total chunks created: {len(chunks)}")


# 3. Add metadata
chunks = enrich_chunks(chunks)

print("Metadata added.")


# 4. Load embedding model
model = load_embedding_model()

texts = [chunk["text"] for chunk in chunks]

embeddings = model.encode(texts)

print(f"Embeddings created: {len(embeddings)}")


# 5. Connect to ChromaDB
collection = create_vector_store()

print("Connected to ChromaDB.")


# 6. Store everything
add_documents(
    collection,
    chunks,
    embeddings
)


print("\nDocuments indexed successfully!")
print("Total chunks in database:", collection.count())