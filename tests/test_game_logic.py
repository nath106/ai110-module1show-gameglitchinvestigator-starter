import pytest
from logic_utils import check_guess, parse_guess, update_score


# --- Existing baseline tests (fixed to unpack the tuple) ---

def test_winning_guess():
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


# --- Bug 1: hint direction was reversed ---
# When guess > secret the old code said "Go HIGHER!" (wrong).
# When guess < secret the old code said "Go LOWER!" (wrong).

def test_too_high_hint_says_lower():
    # Guess 66, secret 50 → player should be told to go LOWER
    outcome, message = check_guess(66, 50)
    assert outcome == "Too High"
    assert "LOWER" in message, f"Expected 'LOWER' in hint, got: {message!r}"

def test_too_low_hint_says_higher():
    # Guess 66, secret 67 → player should be told to go HIGHER
    outcome, message = check_guess(66, 67)
    assert outcome == "Too Low"
    assert "HIGHER" in message, f"Expected 'HIGHER' in hint, got: {message!r}"

def test_correct_guess_hint():
    outcome, message = check_guess(42, 42)
    assert outcome == "Win"
    assert "Correct" in message


# --- Bug 2: secret was cast to str on even attempts causing string comparison ---
# Lexicographic comparison: "9" > "10" is True, so the old code returned
# "Too High" for guess=9 / secret=10 on even attempts.

def test_numeric_comparison_single_vs_double_digit():
    # 9 < 10 numerically → must be "Too Low"
    # Under the old string-coercion bug "9" > "10" → would return "Too High"
    outcome, message = check_guess(9, 10)
    assert outcome == "Too Low"
    assert "HIGHER" in message

def test_numeric_comparison_consistent_across_values():
    # A selection of cases where int vs string ordering diverges
    cases = [
        (9, 10),   # "9" > "10" lexicographically but 9 < 10 numerically
        (19, 20),  # "19" < "20" — same either way (sanity check)
        (9, 100),  # "9" > "100" lexicographically but 9 < 100 numerically
    ]
    for guess, secret in cases:
        outcome, _ = check_guess(guess, secret)
        assert outcome == "Too Low", (
            f"check_guess({guess}, {secret}) returned {outcome!r}, expected 'Too Low'"
        )

def test_check_guess_always_accepts_ints():
    # check_guess should never raise TypeError — both args are ints
    try:
        check_guess(5, 10)
        check_guess(10, 5)
        check_guess(7, 7)
    except TypeError:
        pytest.fail("check_guess raised TypeError; secret may have been passed as str")


# --- Bug 3: attempts initialized to 1 instead of 0 ---
# The UI state bug can't be directly unit-tested, but update_score is called
# with attempt_number starting at 1 (first real submit). Verify it behaves
# correctly for early attempts so a regression would be caught here.

def test_update_score_win_on_first_attempt():
    # attempt_number=1 → points = 100 - 10*(1+1) = 80
    new_score = update_score(0, "Win", 1)
    assert new_score == 80

def test_update_score_win_on_last_attempt():
    # attempt_number=8 → points = 100 - 10*9 = 10 (floored at 10)
    new_score = update_score(0, "Win", 8)
    assert new_score == 10

def test_update_score_win_never_below_minimum():
    # Even at a very high attempt number, minimum points awarded is 10
    new_score = update_score(0, "Win", 50)
    assert new_score == 10
