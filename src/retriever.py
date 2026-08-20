from src.embeddings import load_embedding_model


def retrieve_documents(
    collection,
    query,
    top_k=3,
    grade=None,
    formulation=None,
    document_type=None
):

    model = load_embedding_model()

    query_embedding = model.encode([query])

    conditions = []

    if grade:
        conditions.append({
            "grade": grade
        })

    if formulation:
        conditions.append({
            "formulation": formulation
        })

    if document_type:
        conditions.append({
            "document_type": document_type
        })

    where_filter = None

    if len(conditions) == 1:

        where_filter = conditions[0]

    elif len(conditions) > 1:

        where_filter = {
            "$and": conditions
        }

    results = collection.query(
        query_embeddings=query_embedding.tolist(),
        n_results=top_k,
        where=where_filter
    )

    return results