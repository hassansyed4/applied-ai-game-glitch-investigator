# 🎮🤖 AI Game Glitch Investigator Assistant

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.  
It wrote the code, ran away, and initially left behind a buggy system.

This project not only fixes those issues but evolves the system into an **AI-powered debugging assistant**.

---

## 📌 Original Project (Module 1)

This project extends my original project: **"Game Glitch Investigator"**

The original system was a Streamlit-based number guessing game designed to demonstrate debugging and testing concepts. It included gameplay features like difficulty levels, scoring, and attempts tracking, but intentionally contained bugs in state management, input validation, and logic. The goal was to identify and fix these issues using structured debugging and testing.

---

## 🎯 Project Summary

This project transforms a buggy guessing game into an **Applied AI System** that:

- Detects and explains bugs
- Suggests fixes
- Evaluates reliability
- Logs system behavior

It demonstrates how AI can assist developers in debugging and validating systems.

---

## 🎮 Features

### Core Game
- Number guessing game with difficulty levels
- Attempts tracking and scoring
- Input validation

### AI Debug Assistant
- Accepts bug descriptions
- Explains root causes
- Suggests fixes
- Handles unknown inputs safely

### Reliability System
- Confidence scoring (High / Medium / Low)
- Detects "no bug" scenarios
- Prevents incorrect suggestions

### Logging
- Saves outputs in `debug_log.txt`
- Tracks bug → cause → fix → result

### Testing
- Unit tests using `pytest`

---

## 🏗️ System Architecture

![System Architecture](assets/system_architecture.png)

### Architecture Explanation

The system follows a modular AI workflow:

User → Streamlit App → AI Debug Assistant → Reliability Checker → Output → Logger

- The user inputs a bug description
- The AI analyzes and suggests a fix
- The reliability system evaluates the confidence
- The result is displayed and logged

---

## ⚙️ Setup Instructions

```bash
pip install -r requirements.txt
streamlit run app.py
