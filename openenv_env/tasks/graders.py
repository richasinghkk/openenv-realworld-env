# Email grading
def grade_email(pred, truth):

    if not pred:
        return -0.2

    pred = pred.lower()

    if pred == truth:
        return 1.0

    elif truth in pred:
        return 0.5

    elif pred in ["urgent", "normal", "spam"]:
        return 0.2

    return 0.0


# Cleaning grading
def grade_cleaning(pred, truth):

    if not pred:
        return -0.2

    pred = pred.strip()

    if pred == truth:
        return 1.0

    elif truth in pred:
        return 0.5

    elif "," in pred:
        return 0.2

    return 0.0


# Code grading
def grade_code(pred, truth):

    if not pred:
        return -0.2

    pred = pred.strip()

    if pred == truth:
        return 1.0

    elif "return" in pred:
        return 0.5

    elif "def" in pred:
        return 0.2

    return 0.0