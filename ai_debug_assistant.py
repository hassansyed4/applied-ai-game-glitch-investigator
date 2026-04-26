def analyze_bug(bug_description: str):
    bug_description = bug_description.lower()

    # NEW: detect "no bug" cases
    if "working fine" in bug_description or "no bug" in bug_description:
        return {
            "cause": "No issue detected. The game appears to be functioning correctly.",
            "fix": "No fix required.",
            "confidence": "High"
        }

    if "secret number changes" in bug_description:
        return {
            "cause": "Streamlit reruns the script on each interaction, resetting variables.",
            "fix": """Use st.session_state to store the secret number:
if "secret_number" not in st.session_state:
    st.session_state.secret_number = random.randint(1, 100)
""",
            "confidence": "High"
        }

    elif "wrong hint" in bug_description:
        return {
            "cause": "Comparison logic in check_guess() is incorrect.",
            "fix": """Fix logic:
if guess < secret:
    return "Higher"
elif guess > secret:
    return "Lower"
else:
    return "Correct"
""",
            "confidence": "High"
        }

    elif "attempts not resetting" in bug_description:
        return {
            "cause": "Session state not properly reset on new game.",
            "fix": """Reset state:
st.session_state.attempts = 0
st.session_state.secret_number = random.randint(1, 100)
""",
            "confidence": "Medium"
        }

    # UPDATED DEFAULT CASE
    else:
        return {
            "cause": "No clear bug detected based on the description.",
            "fix": "The system appears to be working as expected. No fix required.",
            "confidence": "High"
        }