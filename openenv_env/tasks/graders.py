def grade_email(pred, truth):

    if pred.lower() == truth.lower():
        return 1.0

    return 0.0


def grade_cleaning(pred, truth):

    if pred.strip() == truth.strip():
        return 1.0

    return 0.0


def grade_code(pred, truth):

    if pred.strip() == truth.strip():
        return 1.0

    return 0.0