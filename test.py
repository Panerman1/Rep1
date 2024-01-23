import streamlit as st
import numpy as np
from PIL import Image
import random

def display_board(board):
    img = np.zeros((300, 300, 3), dtype=np.uint8)

    for i in range(1, 3):
        img[i * 100:i * 100 + 5, :] = 255
        img[:, i * 100:i * 100 + 5] = 255

    for i in range(3):
        for j in range(3):
            if board[i][j] == 'X':
                img[i * 100:(i + 1) * 100, j * 100:(j + 1) * 100, 0] = 255
            elif board[i][j] == 'O':
                img[i * 100:(i + 1) * 100, j * 100:(j + 1) * 100, 2] = 255

    return Image.fromarray(img)

def get_ai_move(board):
    # Replace this logic with your Google AI model
    available_moves = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']
    
    if not available_moves:
        return None
    
    return random.choice(available_moves)

def main():
    st.title("Tic Tac Toe with Google AI")

    board = [[' ' for _ in range(3)] for _ in range(3)]

    while True:
        st.image(display_board(board))

        if any(' ' in row for row in board):
            st.warning("Game Over - It's a Tie!")
            break

        st.info("Your Move - Choose an empty cell:")
        row, col = st.number_input("Row (0, 1, 2):", min_value=0, max_value=2), st.number_input("Column (0, 1, 2):", min_value=0, max_value=2)

        if board[row][col] == ' ':
            board[row][col] = 'X'
        else:
            st.warning("Invalid Move! Cell already occupied. Try again.")
            continue

        if any(all(cell == 'X' for cell in row) for row in board) or any(all(row[i] == 'X' for row in board) for i in range(3)) or all(board[i][i] == 'X' for i in range(3)) or all(board[i][2 - i] == 'X' for i in range(3)):
            st.success("Congratulations! You Win!")
            st.image(display_board(board))
            break

        ai_move = get_ai_move(board)
        if ai_move is not None:
            ai_row, ai_col = ai_move
            board[ai_row][ai_col] = 'O'
        else:
            st.warning("Game Over - It's a Tie!")
            st.image(display_board(board))
            break

        if any(all(cell == 'O' for cell in row) for row in board) or any(all(row[i] == 'O' for row in board) for i in range(3)) or all(board[i][i] == 'O' for i in range(3)) or all(board[i][2 - i] == 'O' for i in range(3)):
            st.error("AI Wins! Better luck next time.")
            st.image(display_board(board))
            break

if __name__ == "__main__":
    main()

