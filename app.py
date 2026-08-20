import streamlit as st

from src.rag import answer_question


st.set_page_config(
    page_title="RMC Knowledge Assistant",
    page_icon="🏗️",
    layout="wide"
)


st.title("🏗️ RMC Knowledge Assistant")

st.write(
    "Ask questions about RMC mix designs, material quantities, "
    "concrete grades, and related documents."
)


query = st.text_input(
    "Ask your question",
    placeholder="Example: How much cement is used in M40?"
)


if st.button("Ask"):

    if not query.strip():

        st.warning("Please enter a question.")

    else:

        with st.spinner("Searching RMC documents..."):

            answer, results = answer_question(
                query=query,
                top_k=5
            )

        st.subheader("Answer")

        st.write(answer)

        st.subheader("Sources")

        seen = set()

        for metadata in results["metadatas"][0]:

            source_key = (
                metadata["source"],
                metadata["page"]
            )

            if source_key not in seen:

                st.write(
                    f"📄 {metadata['source']} — "
                    f"Page {metadata['page']}"
                )

                seen.add(source_key)