# ♟️ Python Chess Capture Program

## 🧾 Project Description

In this project, I built a Python program that determines which black chess pieces a white piece can capture, based on user input. It was my first graded practical task and helped me practice structuring user input, working with conditionals, loops, and basic game logic.

## ✅ What I Did

- I created a console-based program where the user first inputs **one white piece** (either a knight or rook, as per my design).
- The user then adds **1 to 16 black pieces** by entering their type and position.
- I implemented input validation to ensure correct formats like `knight a5` or `rook h8`.
- The user could type `done` once at least one black piece was added.
- After all pieces were placed, my program analyzed which black pieces the white one could legally capture.
- I printed out the list of capturable black pieces (if any).

## 💡 Key Features

- Input handled in format: `<piece> <location>` (e.g., `knight a5`)
- Board validation (e.g., coordinates between a1–h8)
- Detection of legal captures based on basic chess rules
- Clear feedback to the user for every piece added
- Graceful handling of early `done` or overlapping pieces

## 🧠 What I Learned

- How to write and structure a complete Python program
- Creating functions and using conditionals effectively
- Validating and sanitizing user input
- Translating real-world rules (chess logic) into program logic
- Making reasonable assumptions when requirements are ambiguous
- Adding helpful comments and documenting logic in the code

## ⚙️ Technologies Used

- Python 3
- IDE: VS Code

## 🧪 Example Questions I Can Now Answer

- How to define and test Python functions
- Differences between lists and dictionaries
- What pseudocode is and how to write it
- How to debug and make changes to improve the program

## 📎 Assumptions I Made

These are listed as comments at the end of my Python file, but include:
- Assuming only valid chess pieces like `rook`, `knight`, etc.
- Assuming that the white piece cannot occupy the same space as a black one
- Assuming basic movement rules only (no special moves like castling)

---

