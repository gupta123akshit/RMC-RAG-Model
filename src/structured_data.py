import re


def extract_number_after_label(text, label):
    """
    Find a numeric value appearing immediately after a material label.
    """

    lines = [
        line.strip()
        for line in text.splitlines()
        if line.strip()
    ]

    for i, line in enumerate(lines):

        if line.lower() == label.lower():

            if i + 1 < len(lines):

                value = lines[i + 1]

                match = re.search(
                    r"\d+(?:\.\d+)?",
                    value
                )

                if match:
                    return float(match.group())

    return None


def extract_formulation(text):

    match = re.search(
        r"Mix\s+Design\s+([A-Za-z0-9_-]+)",
        text,
        re.IGNORECASE
    )

    if match:
        return match.group(1)

    return None


def extract_mix_data(text):

    return {
        "formulation": extract_formulation(text),

        "cement": extract_number_after_label(
            text,
            "Cement"
        ),

        "fly_ash": extract_number_after_label(
            text,
            "Fly Ash"
        ),

        "water": extract_number_after_label(
            text,
            "Water"
        ),

        "sand": extract_number_after_label(
            text,
            "Fine Aggregate / Sand"
        ),

        "aggregate_10mm": extract_number_after_label(
            text,
            "10 mm Coarse Aggregate"
        ),

        "aggregate_20mm": extract_number_after_label(
            text,
            "20 mm Coarse Aggregate"
        )
    }