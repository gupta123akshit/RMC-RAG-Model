import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_answer(query, retrieved_documents):

    context = "\n\n".join(retrieved_documents)

    prompt = f"""
You are an RMC (Ready-Mix Concrete) technical assistant.

Answer the user's question ONLY using the information
provided in the retrieved RMC documents.

If the retrieved documents do not contain enough information
to answer the question, say:

"I could not find this information in the provided RMC documents."

Do NOT:
- invent quantities
- assume values
- use outside knowledge
- guess missing information

When multiple formulations or mix designs for the same
concrete grade are present:

1. Do not choose one arbitrarily.
2. Clearly state that multiple formulations exist.
3. Present the relevant formulations and their values.
4. If the user specifies a formulation, answer using that
   formulation only.
5. Preserve the units from the source documents.

When giving numerical values, preserve the units exactly
as provided in the documents.

Retrieved RMC Documents:
-------------------------
{context}
-------------------------

User Question:
{query}

Answer:
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt
    )

    return response.text