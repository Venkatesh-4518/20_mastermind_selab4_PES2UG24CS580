# Scenario 20 — Mastermind

## Project Overview
Mastermind is a terminal-based code-breaking game in Python. The player attempts to guess a randomly generated secret code and receives feedback showing exact and partial matches.

## How to Run
1. Ensure Python is installed.
2. Open a terminal in the project directory.
3. Run:

```bash
python main.py
```

## Features Implemented
- **Difficulty levels:** Easy, Medium, and Hard.
- **Exact and partial feedback:** Duplicate symbols are handled without double-counting.
- **Input validation:** Invalid guesses are rejected without consuming turns.
- **Guess history:** Type `h` to view accepted guesses and their feedback.
- **Win handling:** The game ends when the secret code is cracked.
- **Loss handling:** The secret code is revealed when the allowed turns run out.
- **Quit option:** Type `q` to quit the game.

## Difficulty Settings

| Difficulty | Code Length | Symbols | Allowed Turns |
|---|---:|---|---:|
| Easy | 3 | 1–4 | 10 |
| Medium | 4 | 1–6 | 10 |
| Hard | 5 | 1–6 | 8 |

## Project Files
- `main.py` — Entry point for starting the game.
- `game.py` — Game loop, difficulty selection, input validation, history, and win/loss handling.
- `logic.py` — Calculates exact and partial matches.
- `requirements.txt` — Lists project dependencies.

## Testing
The following behaviors were tested:
- Exact matches, partial matches, no matches, and repeated symbols.
- Invalid input handling.
- All three difficulty levels.
- Guess history.
- Winning, losing, and quitting.

## Submission Deliverables
- Before video showing the original game.
- After video showing the updated game.
- Updated source code.
- AI-assisted coding report in PDF format.
- Complete AI chat-history link, as required by the lab instructions.

**AI Chat History Link:** [Insert your shareable conversation link here]

## Implementation Notes
The project retains its terminal-based structure and in-memory game state. No external database or persistent storage is required.
