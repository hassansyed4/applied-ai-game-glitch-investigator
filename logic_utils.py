import typing
import random


def get_range_for_difficulty(difficulty: str) -> typing.Tuple[int, int]:
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100


def parse_guess(raw: str, low: int, high: int) -> typing.Tuple[bool, typing.Optional[int], typing.Optional[str]]:
    """
    Parse raw user input into an integer and validate range.

    Returns: (ok, guess_int, error_message)
    - ok False and error_message set when input invalid or out of range.
    - ok True and guess_int set when input is a valid in-range integer.
    """
    if raw is None or raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    if value < low or value > high:
        return False, None, f"Please enter a number between {low} and {high}."

    return True, value, None


def check_guess(guess: int, secret: typing.Union[int, str]) -> typing.Tuple[str, str]:
    """
    Compare guess to secret and return (outcome, message).

    secret may be an int or a str (the app sometimes casts it).
    outcome: "Win", "Too High", or "Too Low".
    message: human-readable hint.
    """
    # normalize secret to int when possible
    try:
        secret_int = int(secret)
    except Exception:
        secret_int = None

    if secret_int is not None:
        if guess == secret_int:
            return "Win", "🎉 Correct!"
        if guess > secret_int:
            return "Too High", "📉 Go LOWER!"
        return "Too Low", "📈 Go HIGHER!"

    # fallback: compare as strings
    s_guess = str(guess)
    s_secret = str(secret)
    if s_guess == s_secret:
        return "Win", "🎉 Correct!"
    if s_guess > s_secret:
        return "Too High", "📉 Go LOWER!"
    return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int) -> int:
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score


def new_secret(low: int, high: int) -> int:
    """Generate a new secret number in range."""
    return random.randint(low, high)
