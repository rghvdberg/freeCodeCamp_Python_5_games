# connect4.py
import numpy as np
import pygame
import sys
from pygame import draw

ROW_COUNT = 6
COLUMN_COUNT = 7
BLUE = (0,0,205)
BACK = (43,45,50)


def create_board():
    board = np.zeros((ROW_COUNT, COLUMN_COUNT))
    return board


def drop_piece(board, row, col, piece):
    board[row][col] = piece


def is_valid_location(board, col):
    return board[ROW_COUNT - 1][col] == 0


def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r


def print_board(board):
    print(np.flip(board, 0))


def winning_move(board, piece):
    # check horizontal location
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT):
            if (
                board[r][c] == piece
                and board[r][c + 1] == piece
                and board[r][c + 2] == piece
                and board[r][c + 3] == piece
            ):
                return True
    # check vertical
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT - 3):
            if (
                board[r][c] == piece
                and board[r + 1][c] == piece
                and board[r + 2][c] == piece
                and board[r + 3][c] == piece
            ):
                return True

    # check positive sloped diagonal
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT - 3):
            if (
                board[r][c] == piece
                and board[r + 1][c + 1] == piece
                and board[r + 2][c + 2] == piece
                and board[r + 3][c + 3] == piece
            ):
                return True

    # check positive sloped diagonal
    for c in range(COLUMN_COUNT - 3):
        for r in range(3, ROW_COUNT):
            if (
                board[r][c] == piece
                and board[r - 1][c + 1] == piece
                and board[r - 2][c + 2] == piece
                and board[r - 3][c + 3] == piece
            ):
                return True


def draw_board(board):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            x = c * SQUARE_SIZE
            y = r * SQUARE_SIZE + SQUARE_SIZE
            pygame.draw.rect(screen, BLUE, (x, y, SQUARE_SIZE, SQUARE_SIZE))
            pygame.draw.circle(
                screen,
                BACK,
                (x + SQUARE_SIZE / 2, y + SQUARE_SIZE / 2),
                (SQUARE_SIZE / 2) * 0.90,
            )


board = create_board()
print_board(board)
game_over = False
turn = 0

pygame.init()

SQUARE_SIZE = 100

width = COLUMN_COUNT * SQUARE_SIZE
height = (ROW_COUNT + 1) * SQUARE_SIZE

size = (width, height)

screen = pygame.display.set_mode(size)

while not game_over:

    for event in pygame.event.get():
        screen.fill(BACK)
        draw_board(board)
        screen
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            continue
        #     # Ask for Player 1 Input
        #     if turn == 0:
        #             col = int(input("Player 1 Make your Selection (0-6:)"))
        #             if is_valid_location(board, col):
        #                 row = get_next_open_row(board, col)
        #                 drop_piece(board, row, col, 1)

        #     if winning_move(board, 1):
        #         print("Player 1 Wins! Congrats!")
        #         game_over = True

        #     # Ask for Player 2 Input
        #     else:
        #         col = int(input("Player 2 Make your Selection (0-6:)"))
        #         if is_valid_location(board, col):
        #             row = get_next_open_row(board, col)
        #             drop_piece(board, row, col, 2)

        #         if winning_move(board, 2):
        #             print("Player 2 Wins! Congrats!")
        #             game_over = True

        # print_board(board)

        # turn += 1
        # turn = turn % 2
        pygame.display.flip()
