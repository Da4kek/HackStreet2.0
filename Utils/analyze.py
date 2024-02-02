def base_analyzer(text,positive,negative):
    words = text.lower().split() 
    score = 0

    for word in words:
        if word in positive:
            score += 1
        elif word in negative:
            score -= 1
    
    if score > 0:
        return "Positive"
    elif score < 0:
        return "Negative"
    else:
        return "Neutral"