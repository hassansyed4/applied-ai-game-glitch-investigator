# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

 - [x] Describe the game's purpose.
    - A simple Streamlit number-guessing game: the app chooses a secret number and the player has a limited number of attempts to guess it. The UI shows higher/lower hints, an attempts counter, and a simple scoring system.
 - [x] Detail which bugs you found.
    - Attempts counter behaved inconsistently (clicking New Game sometimes changed the attempts number unexpectedly).
    - Out-of-range inputs (e.g., 101) were treated as valid guesses and produced higher/lower hints instead of an error message.
    - The New Game button did not reliably reset the game state after the last attempt — the user had to reload the page to play again.
 - [x] Explain what fixes you applied.
    - Refactored core logic into `logic_utils.py` (parse/validate guesses, check_guess, scoring, range helpers).
    - Added robust input validation (`parse_guess`) so non-integers and out-of-range values return clear errors and do not consume attempts.
    - Fixed guess comparison logic in `check_guess` to always return correct higher/lower hints.
    - Updated `app.py` to reset `st.session_state` on New Game, moved the attempts/info banner so it reflects updated state immediately, and added a safe fallback when `st.experimental_rerun()` is unavailable.
    - Added unit tests in `tests/test_game_logic.py` and verified all tests pass (`python -m pytest -q`).

## 📸 Demo

![alt text](image.png)

## 🚀 Stretch Features

![alt text](image-1.png)
