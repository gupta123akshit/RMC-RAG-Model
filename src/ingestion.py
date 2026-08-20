import fitz
from pathlib import Path


def load_pdf(file_path: str):

    document = fitz.open(file_path)

    pages = []

    for page_number, page in enumerate(document, start=1):

        text = page.get_text().strip()

        if text:

            pages.append({
                "text": text,
                "page": page_number,
                "source": Path(file_path).name
            })

    document.close()

    return pages


def load_all_pdfs(data_directory: str):

    data_path = Path(data_directory)

    all_pages = []

    pdf_files = list(data_path.glob("*.pdf"))

    print(f"Found {len(pdf_files)} PDF files.")

    for pdf_file in pdf_files:

        print(f"Loading: {pdf_file.name}")

        pages = load_pdf(str(pdf_file))

        all_pages.extend(pages)

    return all_pages