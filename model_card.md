# 🧠 Model Card: AI Game Glitch Investigator Assistant

## 📌 Model Name
AI Game Glitch Investigator Assistant

---

## 🎯 Goal / Task
The system analyzes user-described bug scenarios in a number guessing game and provides:
- Root cause explanation
- Suggested fix
- Reliability assessment

---

## 📊 Data Used
This system does not use external datasets.

Instead, it relies on:
- Predefined bug patterns
- Rule-based logic
- Game-specific debugging scenarios

Limitations:
- Cannot generalize beyond known patterns
- Does not learn from new data

---

## ⚙️ Algorithm Summary
The AI is a **rule-based system** that:

1. Converts user input to lowercase
2. Matches keywords against known bug patterns
3. Returns:
   - Cause
   - Fix
   - Confidence level

A reliability checker then evaluates the response and assigns a final result.

---

## ⚠️ Observed Behavior / Biases

- Biased toward predefined bug patterns
- Cannot detect unknown or complex bugs
- May oversimplify debugging explanations

Guardrails:
- Returns “No issue detected” when uncertain
- Uses confidence scoring to indicate reliability

---

## 🧪 Evaluation Process

The system was tested using:

- Known bug scenarios (expected correct detection)
- Edge cases (random text, irrelevant inputs)
- Manual validation of outputs

Results:
- 5/5 known scenarios correctly identified
- Unknown inputs handled safely without false fixes

---

## ✅ Intended Use

- Debugging simple Streamlit applications
- Educational tool for learning debugging concepts
- Demonstrating AI-assisted reasoning systems

---

## ❌ Non-Intended Use

- Complex software debugging
- Production-level debugging automation
- Systems outside predefined scope

---

## 🚀 Ideas for Improvement

- Integrate real LLM (OpenAI / Gemini)
- Add RAG for dynamic bug retrieval
- Learn from new bug patterns
- Improve natural language understanding

---

## 💡 Reflection

This system demonstrates how AI can assist in debugging while highlighting the importance of:
- Guardrails
- Transparency
- Human oversight

It reinforces that AI should support decision-making, not replace it.