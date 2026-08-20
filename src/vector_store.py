import chromadb


def create_vector_store():
    client = chromadb.PersistentClient(
        path="./chroma_db"
    )

    collection = client.get_or_create_collection(
        name="rmc_documents"
    )

    return collection


def add_documents(collection, chunks, embeddings):

    documents = []
    metadatas = []
    ids = []

    for i, chunk in enumerate(chunks):

        documents.append(chunk["text"])
        metadatas.append(chunk["metadata"])

        source = chunk["metadata"]["source"]
        page = chunk["metadata"]["page"]

        safe_source = source.replace(" ", "_")

        chunk_id = f"{safe_source}_page_{page}_chunk_{i}"

        ids.append(chunk_id)

    collection.upsert(
        ids=ids,
        documents=documents,
        embeddings=embeddings.tolist(),
        metadatas=metadatas
    )