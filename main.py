from src.rag import answer_question


query = "What is the cement content of M40-B?"


answer, results = answer_question(
    query=query,
    top_k=3
)


print("\nQuestion:")
print(query)

print("\nAnswer:")
print(answer)


print("\nRetrieved Context:")

for document in results["documents"][0]:

    print("\n" + "=" * 60)
    print(document)


print("\nSources:")

seen = set()

for metadata in results["metadatas"][0]:

    source_key = (
        metadata["source"],
        metadata["page"]
    )

    if source_key not in seen:

        print(
            f"- {metadata['source']}, "
            f"Page {metadata['page']}"
        )

        seen.add(source_key)