
from collections import Counter


def feedback(code, guess):
    exact = sum(a == b for a, b in zip(code, guess))

    unmatched_code = [
        code[i] for i in range(len(code))
        if code[i] != guess[i]
    ]
    unmatched_guess = [
        guess[i] for i in range(len(guess))
        if code[i] != guess[i]
    ]

    code_counts = Counter(unmatched_code)
    partial = 0

    for symbol in unmatched_guess:
        if code_counts[symbol] > 0:
            partial += 1
            code_counts[symbol] -= 1

    return exact, partial
