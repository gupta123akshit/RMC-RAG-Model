import re


def parse_query(query):

    grade = None
    formulation = None

    # Detect concrete grade
    grade_match = re.search(
        r"\bM(10|15|20|25|30|35|40|45|50)\b",
        query,
        re.IGNORECASE
    )

    if grade_match:
        grade = f"M{grade_match.group(1)}"

    # Detect formulation such as M40-A, M40-B, M40-C
    formulation_match = re.search(
        r"\bM(10|15|20|25|30|35|40|45|50)[-_]([A-Za-z0-9]+)\b",
        query,
        re.IGNORECASE
    )

    if formulation_match:
        formulation = (
            f"M{formulation_match.group(1)}-"
            f"{formulation_match.group(2)}"
        )

    return {
        "grade": grade,
        "formulation": formulation
    }