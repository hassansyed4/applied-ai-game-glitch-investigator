from logic_utils import parse_guess, check_guess, update_score


def test_parse_guess_valid():
    ok, val, err = parse_guess("42", 1, 100)
    assert ok is True
    assert val == 42
    assert err is None


def test_parse_guess_non_number():
    ok, val, err = parse_guess("abc", 1, 100)
    assert ok is False
    assert val is None
    assert "not a number" in err.lower()


def test_parse_guess_out_of_range():
    ok, val, err = parse_guess("150", 1, 100)
    assert ok is False
    assert val is None
    assert "between 1 and 100" in err


def test_check_guess_win():
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert "Correct" in message


def test_check_guess_too_high():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message


def test_check_guess_too_low():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message


def test_update_score_win_and_penalties():
    # Win on attempt 1 -> points = 100 - 10*(1+1) = 80
    score = update_score(0, "Win", 1)
    assert score == 80

    # Too High on even attempt -> +5
    score = update_score(10, "Too High", 2)
    assert score == 15

    # Too High on odd attempt -> -5
    score = update_score(10, "Too High", 3)
    assert score == 5

    # Too Low -> -5
    score = update_score(10, "Too Low", 2)
    assert score == 5
