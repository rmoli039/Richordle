import requests

BOLD = '\033[1m'
MATCH = '\033[92m'
HINT = '\033[93m'
END_FORMATTING = '\033[0m'
MAX_GUESSES = 6
DICTIONARY_API = "https://api.dictionaryapi.dev/api/v2/entries/en/"

answer = "STORY"
answer_list = list(answer)
answered = False
num_guesses = 0

print("\n\nWelcome to Richordle :)\n")

while num_guesses < MAX_GUESSES:
    num_guesses += 1

    current_guess = input(f"({num_guesses}) ").upper()
    output = (f"({num_guesses}) ")

    if(len(current_guess) != 5):
        print("Guess must be exactly 5 letters long.")
        num_guesses -= 1
        continue

    if(requests.get(f"{DICTIONARY_API}{current_guess}").status_code == 404):
        print("Guess must be a real word.")
        num_guesses -= 1
        continue

    for i in range(5):
        if current_guess[i] == answer[i]:
            output += (f"{MATCH}{BOLD}{current_guess[i]}{END_FORMATTING}")
        elif current_guess[i] in answer:
            output += (f"{HINT}{BOLD}{current_guess[i]}{END_FORMATTING}")
        else:
            output += (f"{BOLD}{current_guess[i]}{END_FORMATTING}")

    print(output)
    if current_guess == answer:
        answered = True
        break

if answered:
    print("Nice job!")
else:
    print("Better luck next time!")