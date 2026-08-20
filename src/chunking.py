import re


def create_chunks(pages):

    chunks = []

    for page in pages:

        text = page["text"]

        # Find headings such as:
        # M40 Concrete – Mix Design M40-B
        pattern = r"(?=M\d+\s+Concrete\s*[-–])"

        sections = re.split(pattern, text, flags=re.IGNORECASE)

        for section in sections:

            section = section.strip()

            if not section:
                continue

            chunks.append({
                "text": section,
                "page": page["page"],
                "source": page["source"],
                "page_text": text
            })

    return chunks