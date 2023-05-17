from collections import defaultdict
from tic_tac_toe import TicTacToe
import random

class QTable:
    def __init__(self):
        self.table = defaultdict(lambda: [0] * 9)

    def get_value(self, state, action):
        return self.table[state][action]

    def set_value(self, state, action, value):
        self.table[state][action] = value

class RLAgent:
    def __init__(self, epsilon=0.1, alpha=0.5, gamma=1):
        self.epsilon = epsilon
        self.alpha = alpha
        self.gamma = gamma
        self.q_table = QTable()

    def get_move(self, game):
        state = tuple(game.board)
        valid_moves = [i for i in range(9) if game.is_valid_move(i)]

        # Exploration or exploitation
        if random.random() < self.epsilon:
            return random.choice(valid_moves)
        else:
            # Greedy action
            q_values = [self.q_table.get_value(state, action) for action in valid_moves]
            max_q_value = max(q_values)
            if q_values.count(max_q_value) > 1:
                # Multiple actions have the same max q value, choose randomly among them
                best_moves = [i for i in range(len(valid_moves)) if q_values[i] == max_q_value]
                best_move_index = random.choice(best_moves)
            else:
                best_move_index = q_values.index(max_q_value)
            return valid_moves[best_move_index]

    def update_q_table(self, old_state, action, reward, new_state):
        old_value = self.q_table.get_value(old_state, action)
        next_max = max([self.q_table.get_value(new_state, a) for a in range(9)])
        new_value = (1 - self.alpha) * old_value + self.alpha * (reward + self.gamma * next_max)
        self.q_table.set_value(old_state, action, new_value)


def print_q_table(q_table):
    print("Final Q-table:")
    for state, q_values in q_table.table.items():
        print(f"State: {state} - Q-values: {q_values}")
    print()

def train_agent(agent, episodes=10000):
    wins = 0
    draws = 0
    losses = 0
    
    for episode in range(episodes):
        game = TicTacToe()
        old_state = None
        action = None
        while not game.winner:
            state = tuple(game.board)
            if old_state is not None:
                agent.update_q_table(old_state, action, -1, state)
            move = agent.get_move(game)
            old_state = state
            action = move
            game.make_move(move)

        if game.winner == "O":
            wins += 1
            agent.update_q_table(old_state, action, 100, tuple(game.board))
        elif game.winner == "X":
            losses += 1
            agent.update_q_table(old_state, action, -100, tuple(game.board))
        else:
            draws += 1
            agent.update_q_table(old_state, action, 0, tuple(game.board))

        if (episode + 1) % 1000 == 0:
            print(f"Episode {episode + 1}: Wins={wins}, Draws={draws}, Losses={losses}")
            wins, draws, losses = 0, 0, 0

    print_q_table(agent.q_table)