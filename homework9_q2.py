def create_board():
    letters = "ABCDEFGHIJKLMNOPQRXTUVWXYZ"

    board = []
    index = 0

    for row in range(5):
        current_row = []

        for col in range(5):
            current_row.append(letters[index])
            index += 1

        board.append(current_row)

    return board


def find_letter(board, letter):
    letter = letter.upper()


    if letter == "J":
        letter = "I"

    for row in range(5):
        for col in range(5):
            if board[row][col] == letter:
                return (row + 1, col + 1)

    return None


def encode(message, board):
    result = []

    for letter in message.upper():
        if letter.isalpha():
            position = find_letter(board, letter)

            if position is not None:
                result.append(str(position[0]) + str(position[1]))

    return "".join(result)


def decode(code, board):
    result = []

    for pair in code.split():
        row, col = int(pair[0]), int(pair[1])
        result.append(board[row - 1][col - 1])

    return "".join(result)


def main():
    board = create_board()

    print("Polybius Checkerboard")
    for row in board:
        print(row)

    message = input("Enter a message to encode: ")
    encrypted = encode(message, board)
    print("Encoded message:", encrypted)

    code = input("Enter row-column pairs to decode: ")
    print("Decoded message:", decode(code, board))


if __name__ == "__main__":
    main()
          
