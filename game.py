
import random
from logic import feedback


DIFFICULTIES = {
    "1": {"name": "Easy", "length": 3, "symbols": "1234", "turns": 10},
    "2": {"name": "Medium", "length": 4, "symbols": "123456", "turns": 10},
    "3": {"name": "Hard", "length": 5, "symbols": "123456", "turns": 8},
}


class Mastermind:
    def __init__(self):
        print("Choose difficulty:")
        for key, level in DIFFICULTIES.items():
            print(
                f"{key}. {level['name']} "
                f"({level['length']} digits, symbols {level['symbols']}, "
                f"{level['turns']} turns)"
            )

        while True:
            choice = input("Difficulty (1-3, default 2): ").strip() or "2"
            if choice in DIFFICULTIES:
                break
            print("Choose 1, 2, or 3.")

        self.difficulty = DIFFICULTIES[choice]
        self.code = [
            random.choice(self.difficulty["symbols"])
            for _ in range(self.difficulty["length"])
        ]
        self.history = []
        self.turns = self.difficulty["turns"]
        self.finished = False

    def show_history(self):
        print("\nGuess history:")
        if not self.history:
            print("No guesses yet.")
        else:
            for number, (guess, exact, partial) in enumerate(self.history, 1):
                print(
                    f"{number}. {guess} -> "
                    f"Exact: {exact}, Partial: {partial}"
                )
        print()

    def run(self):
        level = self.difficulty
        print(
            f"\nMastermind — {level['name']}: enter {level['length']} "
            f"digits using {level['symbols']}."
        )
        print("Type 'h' to view history or 'q' to quit.")

        while self.turns > 0 and not self.finished:
            raw = input(f"{self.turns} turns left > ").strip()

            if raw.lower() == "q":
                self.finished = True
                print("Game ended. The code was", "".join(self.code))
                return

            if raw.lower() == "h":
                self.show_history()
                continue

            if (
                len(raw) != level["length"]
                or any(ch not in level["symbols"] for ch in raw)
            ):
                print(
                    f"Enter exactly {level['length']} digits using "
                    f"{level['symbols']}."
                )
                continue

            exact, partial = feedback(self.code, list(raw))
            self.history.append((raw, exact, partial))
            self.turns -= 1
            print("Exact:", exact, " Partial:", partial)

            if exact == level["length"]:
                self.finished = True
                print("Cracked the code!")
                self.show_history()
                return

        if not self.finished:
            self.finished = True
            print("Out of turns! The code was", "".join(self.code))
            self.show_history()
