def check_reliability(ai_output):
    confidence = ai_output.get("confidence", "Low")

    if confidence == "High":
        return "Passed: Solution is reliable and follows best practices."
    elif confidence == "Medium":
        return "Warning: Solution may work but needs testing."
    else:
        return "Failed: Low confidence. Needs manual verification."