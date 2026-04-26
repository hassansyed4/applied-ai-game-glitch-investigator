# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

- Bug 1:
- When I first opened the game window, it showed “Attempts left: 7.” However, when I clicked the “New Game” button, the attempts changed to “Attempts left: 8.” The number of attempts should remain consistent, so this behavior indicates a bug.

- Bug 2:
- The rule says “Guess a number between 1 and 100.” However, when I entered numbers such as 101 or 201, the game still responded with hints like “Guess lower.” Instead, the program should display a message indicating that the number is out of range.

- Bug 3:
- After using all my attempts, I was supposed to click the “New Game” button to start again. However, the button was not working, and I had to reload the page before I could enter guesses again.

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

- Tools: I used this ChatGPT-based assistant (the code helper you interacted with) and GitHub Copilot in VS Code for quick code completions and commit-message suggestions.

- Correct suggestion: The AI recommended moving core game logic (parsing, range validation, guess checking, and scoring) out of `app.py` into a separate module (`logic_utils.py`) and adding explicit input validation. This was correct — after applying the refactor I added `parse_guess` and `check_guess` there, wrote unit tests, and ran `python -m pytest -q` which returned all tests passing; manual play also confirmed out-of-range inputs now show an error message instead of being treated as guesses.

- Incorrect/misleading suggestion: The assistant initially suggested calling `st.experimental_rerun()` after resetting session state to immediately refresh the UI. In my environment that attribute was not present and caused an AttributeError. I verified the failure from the Streamlit error trace, then implemented a safe fallback (call `st.stop()` when `experimental_rerun` is unavailable) and moved the attempts/info banner to render after the reset so the UI shows the updated attempts immediately.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

- Deciding a bug was fixed: I used a combination of automated tests and manual UI checks. For the input-range bug I wrote unit tests for `parse_guess` that assert invalid and out-of-range inputs return errors and do not decrement attempts; for the New Game bug I manually clicked the New Game button and verified the attempts counter updated immediately without reloading the page.

- Example test: `tests/test_game_logic.py` contains tests for `parse_guess`, `check_guess`, and `update_score` (for example, `test_parse_guess_out_of_range` asserts that "150" returns an out-of-range error when the range is 1–100). Running `python -m pytest -q` produced `7 passed`, which gave strong confidence the core logic behaves as expected.

- Role of AI in testing: The assistant suggested isolating logic into `logic_utils.py`, which made writing focused unit tests straightforward. It also suggested concrete test cases (valid number, non-number, out-of-range, win/too-high/too-low, and scoring scenarios), which I adopted and verified with pytest.

Suggested commit message (use Copilot's Generate Commit Message or paste into your commit):

```
Refactor game logic into logic_utils; add validation and tests

- Move parse_guess, check_guess, update_score, and range helpers into logic_utils.py
- Add robust input validation (out-of-range and non-integer handling)
- Fix New Game reset behavior and add safe fallback for st.experimental_rerun
- Add pytest coverage for parsing, guess checks, and scoring (7 tests pass)
```

---

## 4. What did you learn about Streamlit and state?
- In your own words, explain why the secret number kept changing in the original app.

  The secret number kept changing because the app recomputed that value on every Streamlit rerun instead of keeping it in persistent session state. Each time I clicked a widget (for example, the Submit button), Streamlit executed the script top-to-bottom and the code that generated the secret number ran again, producing a new random value. Because the secret wasn't stored in `st.session_state` (or was re-assigned on every run), it had no lasting memory between interactions and appeared to "move" on its own.

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

  Streamlit reruns are like the app re-reading the program from the top every time you interact with it: clicking a button causes the whole script to run again. `st.session_state` is a small, persistent storage box you can use to keep values between those runs — like putting a sticky note on the table so the next time the script runs you still know what the secret number is. Without using session state you get fresh values every run; with it you can preserve user progress, counters, and secrets across interactions.

- What change did you make that finally gave the game a stable secret number?

  I moved the game logic into `logic_utils.py` and ensured the secret number is stored in `st.session_state` and only generated when the key is missing. That way the secret is initialized once per game and survives Streamlit reruns until the user explicitly starts a new game, which prevents the secret from changing unexpectedly.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?

I will consistently separate logic from UI and write small unit tests for core functions. Keeping parsing and game rules in a module like `logic_utils.py` made it easy to test behavior with `pytest` and quickly verify fixes.

- What is one thing you would do differently next time you work with AI on a coding task?

Next time I'll ask for smaller, more targeted edits and write a quick test before applying larger automated refactors. That way I can validate each suggested change with a failing test first, then confirm the fix — minimizing the chance of introducing regressions.

- In one or two sentences, describe how this project changed the way you think about AI generated code.

This project reinforced that AI is a useful collaborator for generating ideas and boilerplate, but its suggestions must be reviewed and tested. I now treat AI output as a draft to be validated with tests and small, careful edits rather than a finished solution.
