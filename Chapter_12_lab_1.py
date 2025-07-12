def state_capital_game():
    # Dictionary of states and capitals
    state_capitals = {
        "Alabama": "Montgomery",
        "Arkansas": "Little Rock",
        "Iowa": "Des Moines",
        "Michigan": "Lansing",
        "Washington": "Olympia"
    }

    correct = 0
    incorrect = 0

    print("State Capital's Game\n")

    # Loop through the dictionary
    for state, capital in state_capitals.items():
        answer = input(f"What is the capital of {state}? ").strip()

        if answer.lower() == capital.lower():
            print("Good Job! \n")
            correct += 1
        else:
            print(f"Sorry the answer is {capital}.\n")
            incorrect += 1

    print(f"You answered {correct} correctly and {incorrect} incorrectly.\n")

if __name__ == "__main__":
    state_capital_game()
