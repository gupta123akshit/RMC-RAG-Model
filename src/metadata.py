from src.structured_data import extract_mix_data
import re


def detect_grade(text):

    match = re.search(
        r"\bM(20|25|30|35|40|45|50)\b",
        text,
        re.IGNORECASE
    )

    if match:
        return f"M{match.group(1)}"

    return None


def detect_formulation(text):

    match = re.search(
        r"Mix\s+Design\s+([A-Za-z0-9_-]+)",
        text,
        re.IGNORECASE
    )

    if match:
        return match.group(1)

    return None


def detect_document_type(source):

    source_lower = source.lower()

    if "mix" in source_lower:
        return "mix_design"

    return "general"


def enrich_chunks(chunks):

    enriched_chunks = []

    for chunk in chunks:

        text = chunk["text"]

        mix_data = extract_mix_data(text)

        metadata = {
            "source": chunk["source"],
            "page": chunk["page"],
            "domain": "RMC",
            "document_type": detect_document_type(
                chunk["source"]
            ),
            "grade": detect_grade(text),
            "formulation": mix_data["formulation"],
        }

        # Add extracted numerical values only
        # when they actually exist.
        if mix_data["cement"] is not None:
            metadata["cement"] = mix_data["cement"]

        if mix_data["fly_ash"] is not None:
            metadata["fly_ash"] = mix_data["fly_ash"]

        if mix_data["water"] is not None:
            metadata["water"] = mix_data["water"]

        if mix_data["sand"] is not None:
            metadata["sand"] = mix_data["sand"]

        if mix_data["aggregate_10mm"] is not None:
            metadata["aggregate_10mm"] = mix_data["aggregate_10mm"]

        if mix_data["aggregate_20mm"] is not None:
            metadata["aggregate_20mm"] = mix_data["aggregate_20mm"]

        enriched_chunks.append({
            "text": text,
            "metadata": metadata
        })

    return enriched_chunks
   