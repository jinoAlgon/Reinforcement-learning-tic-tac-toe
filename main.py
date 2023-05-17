from tic_tac_toe import TicTacToe
from human_player import play_human_vs_agent
from rl_agent import RLAgent
from rl_agent import train_agent  # Explicitly import the train_agent function

# Create a new RL agent
agent = RLAgent()

# Train the agent1

train_agent(agent, episodes=100000)

# Play against the RL agent
play_human_vs_agent(agent)

