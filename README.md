#!/bin/bash

cat <<EOF >README.md
# Emoji Number Guessing Game

Welcome to the Emoji Number Guessing Game! 🎮 This game challenges you to guess the secret number chosen by the computer. Are you ready to test your guessing skills?

## About

The Emoji Number Guessing Game is a fun and interactive Python project that lets you play a guessing game with a computer-generated secret number. It's designed to provide an enjoyable and engaging experience for players of all ages.

## How to Play

1. Run the \`main.py\` file to start the game.
2. You will be prompted to guess the secret number.
3. Enter your guess and press Enter.
4. You will receive feedback on whether your guess is too high or too low.
5. Keep guessing until you correctly guess the secret number!
6. Enjoy the game and have fun! 😊

## Example Inputs

- Example 1: Guessing a number too low:
  \`\`\`
  Your guess: 5
  Too low! Try again. 📉
  \`\`\`

- Example 2: Guessing a number too high:
  \`\`\`
  Your guess: 15
  Too high! Try again. 📈
  \`\`\`

- Example 3: Correct guess:
  \`\`\`
  Your guess: 10
  Congratulations! 🎉 You guessed the number in 3 attempts.
  \`\`\`

## Features

- Randomly generated secret number for each game.
- Simple and intuitive user interface.
- Feedback on each guess to help you narrow down the correct number.
- Easy-to-understand instructions.
- Enjoyable gaming experience with emoji-based visuals.

## Technologies Used

- Python programming language
- Random module for generating random numbers
- Command-line interface (CLI) for user interaction

## Installation

1. Clone the repository to your local machine:
   \`\`\`
   git clone https://github.com/AdRohal/Guess_game.git
   \`\`\`

2. Navigate to the project directory:
   \`\`\`
   cd Guess_game
   \`\`\`

3. Run the game by executing the \`main.py\` file:
   \`\`\`
   python main.py
   \`\`\`

## Contribution

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
EOF
