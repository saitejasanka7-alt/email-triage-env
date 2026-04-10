def grade_easy(action, expected):
    score = 0.3
    if action["label"] == expected["label"]:
        score += 0.3
    return min(score, 0.9)

def grade_medium(action, expected):
    score = 0.2
    if action["label"] == expected["label"]:
        score += 0.3
    if action["reply"] == expected["reply"]:
        score += 0.3
    return min(score, 0.9)

def grade_hard(action, expected):
    score = 0.2
    if action["label"] == expected["label"]:
        score += 0.3
    if action["reply"] == expected["reply"]:
        score += 0.3
    return min(score, 0.9)
