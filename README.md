# Math Adventures - AI-Powered Adaptive Learning Prototype

This project is a functional prototype of an adaptive learning system, as part of an assignment. It simulates a "Math Adventures" game for children (ages 5-10) that dynamically adjusts the difficulty of math puzzles based on the user's real-time performance.

The core of the project is the **adaptive engine**, which uses rule-based logic to keep the learner in their optimal challenge zone ("Zone of Proximal Development").

##  Key Features

  * **Adaptive Difficulty**: The system automatically increases or decreases puzzle difficulty based on user performance (correctness and response time).
  * **Three Difficulty Levels**: Puzzles are generated across 3 levels:
      * **Easy**: Single-digit addition.
      * **Medium**: Double-digit addition/subtraction.
      * **Hard**: Multiplication and division.
  * **Performance Tracking**: Logs every attempt, tracking the problem, correctness, and time taken.
  * **Session Summary**: Provides a summary report at the end of the session showing overall accuracy and average response time.

## ⚙️ How to Run

This project is built using only standard Python libraries, so no external packages are required.

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/[Your-Username]/math-adaptive-prototype.git
    cd math-adaptive-prototype
    ```

2.  **Run the application:**
    You must run the `main.py` script as a module from the root directory. This allows the relative imports to work correctly.

    ```bash
    python -m src.main
    ```

3.  **Follow the prompts:**
    The console will ask you to select a starting difficulty (1, 2, or 3) and then begin the 10-puzzle session.

## 📁 Project Structure

The code is organized into a modular `src/` directory as recommended[cite: 36].

```
math-adaptive-prototype/
├── README.md
├── requirements.txt
└── src/
    ├── __init__.py           (You may need to add this empty file)
    ├── main.py               (Runs the main game loop and coordinates modules)
    ├── puzzle_generator.py   (Generates new math problems)
    ├── tracker.py            (Logs performance and generates summary)
    └── adaptive_engine.py    (Contains the core adaptive logic)
```

##  Adaptive Logic

The adaptive engine (`adaptive_engine.py`) uses a rule-based "Level Score" system to determine the next puzzle's difficulty.

  * A user's performance (correctness and speed) updates a score.
  * If the score passes a **Level Up Threshold** (`+5`), the difficulty increases.
  * If the score drops below a **Level Down Threshold** (`-3`), the difficulty decreases.

A full explanation of this logic, the metrics tracked, and the design justification is available in the **`Technical_Note.md`** file.

