# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
  The game prompts the user to guess a number. The game states the user has 8 guess, but the user only has 7. Once the game finishes, a message pops up letting the user know if they guess correctly.
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
  When the user submits a guess, the attemps left are delayed.
  The hints were backwards.
  Pressing 'New Game' button does not start a new game after the game has finished.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| | 40| | Go Higher            Go Lower         none
| | 86  | Go Higher            Go Lower         none
| | 50  | Go Lower             Go Higher        none

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
Claude and Claude Code were the AI tools used for their project.

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

A bug that AI found was that the original code that the hints "Go HIGHER!" and "Go LOWER!" were opposite. This caused the user to get further from the secret number. The AI found that the outcome messages and hint messages were reversed leading to the wrong hints being given. After excepting the changes, I tested to see if I could win with the given hints. My manual test past and I used pytest to do more test.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).


---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
To verify if a bug was fixed, I would do a manual test to ensure that all the changes made it into the final game. Pytest is a great way to test multiple test-cases, but I always made sure to verify those fixes were made. Going in manual also allowed me to discover other bugs that I didn't notice at first.

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  Manual tests were where I discovered the most errors. In the first manual test, I played the game how it was intended to be played and took note of all the errors that the player would see. Those bugs include wrong hints, wrong number of attempts left, and errors in game instructions. I'm able to verify that these are bugs by using the dev debug info.

- Did AI help you design or understand any tests? How?
  Yes, AI did help me when creating pytest. I've used pytest in the past, but the examples that the AI created helped as a refresher. Asking Claude for pytest ideas helped me see common test cases that I may have missed.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

Streamlit is a framework that can create a UI quickly through lines of Python code. Streamlit "reruns" refer to the re-execution of the entire Python script when intereacting with a Streamlit app. When a "rerun" occurs, normal Python variables rest to zero every time. To avoid the reset of certain variables, a session state can be used.



---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.

  One habit that I will reuse in future labs is getting the AI to explain what certain things do. Getting it to explain parts of the code and how certai changes improve the quality of the code will help me understand the system better.

- What is one thing you would do differently next time you work with AI on a coding task?

I would probably try to use multiple AI agents for different things to optimize the amount of tokens I have. For example, I would use Claude for mostly Claude Code to save my tokens. If I need to get a deeper explanation on what parts of the code do or need a lighter task done, I would ask another agent.

- In one or two sentences, describe how this project changed the way you think about AI generated code.

AI generated code is a powerful tool that can improve work ethic, but also harm it. It is up to the user to work with AI to complete projects and goals efficiently, but not to soley rely on it. As it is shown in the AI generate game, there were still many bugs in a simple game. If there was a human working along side the AI agent to manage what was being created, these bougs could have been avoided.