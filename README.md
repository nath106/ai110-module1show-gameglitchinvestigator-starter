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

- [ ] Game's Purpose: Game Glitch Investigator is a number guessing game using Streamlit.
- [ ] Bugs Found: 
   - Reversed hint messages.
   - Wrong amount of guess.
   - Difficulty number range not followed.
   - New game button doesn't work.
   - Score and History reset every new game.
- [ ] Explain what fixes you applied.
   - The hint messages were not with their correct outcomes message causing the "Go Higher" or "Go Lower" hints to be swapped.
   - Guess counter was fixed by chaning the initial attempts from 0 to 1.
   - "New game" was hardcoded to randint(1, 100); it now uses low and high from the selected difficulty
   - The handler was missing status= "playing", so after finishing a game the game-over block would catch every subsequent rerun and call st.stop() before the submit logic could run. 

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. User enters a guess of 50
2. Game returns "Too Low", hints "Go Higher"
3. User entera a guess of 75 --> "Too Low, Go Higher"
4. Score updates correctly after each guess
5. Game ends after the number is guessed correctly or all attemps are used.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
