import pygame
import sys
from tic_tac_toe import TicTacToe
from rl_agent import RLAgent, train_agent
from mv_human_input import get_finger_count
from tkinter import messagebox

pygame.init()

# Set up the display
width, height = 300, 300
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tic Tac Toe")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Helper functions
def draw_board(board):
    cell_size = width // 3
    for x in range(1, 3):
        pygame.draw.line(screen, BLACK, (x * cell_size, 0), (x * cell_size, height), 5)
        pygame.draw.line(screen, BLACK, (0, x * cell_size), (width, x * cell_size), 5)

    for i, cell in enumerate(board):
        x = i % 3
        y = i // 3
        if cell == "X":
            pygame.draw.line(screen, BLACK, (x * cell_size + 10, y * cell_size + 10),
                             ((x + 1) * cell_size - 10, (y + 1) * cell_size - 10), 5)
            pygame.draw.line(screen, BLACK, (x * cell_size + 10, (y + 1) * cell_size - 10),
                             ((x + 1) * cell_size - 10, y * cell_size + 10), 5)
        elif cell == "O":
            pygame.draw.circle(screen, BLACK, (x * cell_size + cell_size // 2, y * cell_size + cell_size // 2), cell_size // 2 - 10, 5)

def handle_click(pos, game, agent):
    x, y = pos
    cell_size = width // 3
    move = (y // cell_size) * 3 + x // cell_size

    if game.is_valid_move(move):
        game.make_move(move)

        if not game.winner:
            agent_move = agent.get_move(game)
            game.make_move(agent_move)

def handle_click(move, game, agent):
    cell_size = width // 3
    x = move % 3
    y = move // 3

    if game.is_valid_move(move):
        game.make_move(move)

        if not game.winner:
            agent_move = agent.get_move(game)
            game.make_move(agent_move)


def main():
    game = TicTacToe()
    agent = RLAgent()
    train_agent(agent, episodes=100000)

    running = True
    game_over = False

    while running:
        screen.fill(WHITE)
        draw_board(game.board)
        pygame.display.flip()

        if game.winner:
            if not game_over:
                if game.winner == "draw":
                    message = "It's a draw!"
                elif game.winner == "X":
                    message = "Congratulations! You won!"
                else:
                    message = "Sorry, you lost."
                messagebox.showinfo("Game Over", message)
                game_over = True
                running = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if game_over:
                        game = TicTacToe()
                        game_over = False
                        running = True
                    elif not game.winner:
                        move = get_finger_count()
                        if move >= 1 and move <= 9:
                            handle_click(move - 1, game, agent)


    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
