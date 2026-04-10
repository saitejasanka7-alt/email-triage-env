def grade_easy(output, expected):
    score = 0.3
    if output.get("label") == expected.get("label"):
        score += 0.3
    return min(score, 0.9)

def grade_medium(output, expected):
    score = 0.2
    if output.get("label") == expected.get("label"):
        score += 0.3
    if output.get("reply") == expected.get("reply"):
        score += 0.3
    return min(score, 0.9)

def grade_hard(output, expected):
    score = 0.2
    if output.get("label") == expected.get("label"):
        score += 0.3
    if output.get("reply") == expected.get("reply"):
        score += 0.3
    return min(score, 0.9)
