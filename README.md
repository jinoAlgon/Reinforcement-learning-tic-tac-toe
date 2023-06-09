﻿# Reinforcement-learning-tic-tac-toe

This project demonstrates the use of reinforcement learning to train an intelligent agent to play the classic game of Tic Tac Toe. The agent uses Q-learning to learn from its experiences and improve its gameplay. Additionally, the project incorporates a finger counting system using the MediaPipe library to enable the human player to input their moves through a webcam.

## Requirements

- Python 3.x
- OpenCV
- MediaPipe
- NumPy

## Installation

1. Clone the repository to your local machine
2. Install the required dependencies

## Usage

1. Train the RL agent
2. Play Tic Tac Toe against the trained agent

## Project Structure

- `train_agent.py`: Script to train the reinforcement learning agent.
- `play_game.py`: Script to play Tic Tac Toe against the trained agent.
- `rl_agent.py`: Contains the RLAgent class and QTable class.
- `tic_tac_toe.py`: Contains the TicTacToe game logic.
- `finger_counting.py`: Implements the finger counting system using MediaPipe and OpenCV.

## Output

1. Human player input 

![Alt text](https://github.com/jinoAlgon/Reinforcement-learning-tic-tac-toe/blob/main/screenshots/medipipie.jpg "human_player")

2. Agent input and final Result

![Alt text](https://github.com/jinoAlgon/Reinforcement-learning-tic-tac-toe/blob/main/screenshots/final_output.jpg "final_result")

## Future Enhancements

1. Improve the finger counting system to handle different lighting conditions and hand orientations.
2. Implement other reinforcement learning algorithms, such as SARSA or DDPG, for comparison.
3. Train the agent on more complex games to demonstrate the versatility of reinforcement learning.

## References

- [Reinforcement Learning: An Introduction by Richard S. Sutton and Andrew G. Barto](http://incompleteideas.net/book/RLbook2020.pdf)
- [MediaPipe Hands: On-device Real-time Hand Tracking](https://ai.googleblog.com/2019/08/on-device-real-time-hand-tracking-with.html)
