with open('input.txt') as f:
    lines = f.readlines()

# Define a dictionary that maps the shapes to their corresponding scores.
CONVERT = {
    "A": "R",
    "B": "P",
    "C": "S",
    "X": "R",
    "Y": "P",
    "Z": "S",
}

# Define a dictionary that maps the shapes to their corresponding scores.
SHAPE_SCORES = {
    "R": 1,  # Rock
    "P": 2,  # Paper
    "S": 3,  # Scissors
}

def game_outcome(player: str, opponent: str) -> int:
    # If the player's shape is the same as the opponent's shape, return a tie.
    if player == opponent:
        return 3

    # If the player's shape beats the opponent's shape, return a win.
    if player == "R" and opponent == "S":
        return 6
    if player == "P" and opponent == "R":
        return 6
    if player == "S" and opponent == "P":
        return 6

    # Otherwise, return a loss.
    return 0


def calculate_total_score(lines: list) -> int:
    # Initialize the total score to 0.
    total_score = 0

    # Go through each line in the strategy guide.
    for line in lines:
        # Split the line into the opponent's shape and the recommended shape.
        opponent_shape, recommended_shape = line.split()

        # Convert the opponent's shape and the recommended shape using the CONVERT dictionary.
        opponent_shape = CONVERT[opponent_shape]
        recommended_shape = CONVERT[recommended_shape]

        # Get the scores for the opponent's shape and the recommended shape.
        opponent_score = SHAPE_SCORES[opponent_shape]
        recommended_score = SHAPE_SCORES[recommended_shape]

        # Calculate the round score using the game_outcome() function.
        round_score = game_outcome(recommended_shape, opponent_shape)

        # Add the round score to the total score.
        total_score += round_score + recommended_score

    # Return the total score.
    return total_score

# Print the total score.
print(calculate_total_score(lines))

with open('input.txt') as f:
    lines = f.readlines()


def choose_based_on_outcome(opponent: str, outcome: str) -> str:
    # Choose the shape that causes the outcome provided.
    # X = lose, Y = tie, Z = win
    if opponent == "R" and outcome == "X":
        return "S"
    if opponent == "R" and outcome == "Y":
        return "R"
    if opponent == "R" and outcome == "Z":
        return "P"

    if opponent == "P" and outcome == "X":
        return "R"
    if opponent == "P" and outcome == "Y":
        return "P"
    if opponent == "P" and outcome == "Z":
        return "S"

    if opponent == "S" and outcome == "X":
        return "P"
    if opponent == "S" and outcome == "Y":
        return "S"
    if opponent == "S" and outcome == "Z":
        return "R"


def calculate_total_score(lines: list) -> int:
    # Initialize the total score to 0.
    total_score = 0

    # Go through each line in the strategy guide.
    for line in lines:
        # Split the line into the opponent's shape and the recommended shape.
        opponent_shape, outcome = line.split()

        # Convert the opponent's shape and the recommended shape using the CONVERT dictionary.
        opponent_shape = CONVERT[opponent_shape]

        # Get the scores for the opponent's shape and the recommended shape.
        opponent_score = SHAPE_SCORES[opponent_shape]

        # Calculate the round score using the game_outcome() function.
        chosen_shape = choose_based_on_outcome(opponent_shape, outcome)

        # Add the round score to the total score.
        total_score += game_outcome(chosen_shape, opponent_shape) + SHAPE_SCORES[chosen_shape]

    # Return the total score.
    return total_score

# Print the total score.
print(calculate_total_score(lines))