from src.vector_store import create_vector_store
from src.retriever import retrieve_documents
from src.generation import generate_answer
from src.query_parser import parse_query


def answer_question(query, top_k=5):

    collection = create_vector_store()

    parsed_query = parse_query(query)

    grade = parsed_query["grade"]
    formulation = parsed_query["formulation"]

    results = retrieve_documents(
        collection=collection,
        query=query,
        top_k=5,
        grade=grade,
        formulation=formulation,
        document_type=None
    )

    retrieved_documents = results["documents"][0]

    answer = generate_answer(
        query,
        retrieved_documents
    )

    return answer, results