
def create_grid(message, rows, cols):
    message = message.replace(" ", "").upper()
    size = rows * cols

    if len(message) > size:
        raise ValueError("Message is too long for this grid.")

    # Pad unused grid locations with X.
    message = message.ljust(size, "X")

    grid = []
    index = 0

    for row in range(rows):
        current_row = []

        for col in range(cols):
            current_row.append(message[index])
            index += 1

        grid.append(current_row)

    return grid


def column_order(keyword):
    # Sort columns alphabetically by their keyword letters.
    return sorted(range(len(keyword)),
                  key=lambda col: (keyword[col].upper(), col))


def encrypt(message, keyword, rows):
    keyword = keyword.upper()
    cols = len(keyword)

    grid = create_grid(message, rows, cols)
    result = []

    # Read down the columns in keyword order.
    for col in column_order(keyword):
        for row in range(rows):
            result.append(grid[row][col])

    ciphertext = "".join(result)

    # Display groups of five characters.
    return " ".join(ciphertext[i:i + 5]
                    for i in range(0, len(ciphertext), 5))


def decrypt(ciphertext, keyword, rows):
    keyword = keyword.upper()
    cols = len(keyword)
    ciphertext = ciphertext.replace(" ", "").upper()

    if len(ciphertext) != rows * cols:
        raise ValueError("Ciphertext length does not match grid size.")

    grid = [[""] * cols for _ in range(rows)]
    index = 0

    # Restore each column in the same order used for encryption.
    for col in column_order(keyword):
        for row in range(rows):
            grid[row][col] = ciphertext[index]
            index += 1

    # Read the restored grid from left to right.
    message = ""

    for row in range(rows):
        for col in range(cols):
            message += grid[row][col]

    return message


def main():
    message = "PROGRAMMINGWITHPYTHONISCOOL"
    keyword = input("Enter keyword (6 letters): ").upper()

    if len(keyword) != 6 or not keyword.isalpha():
        print("Please enter a six-letter keyword.")
        return

    encrypted = encrypt(message, keyword, 5)
    print("Encrypted message:", encrypted)

    ciphertext = input("Enter ciphertext to decrypt: ")
    decrypted = decrypt(ciphertext, keyword, 5)
    print("Decrypted message:", decrypted)


if __name__ == "__main__":
    main()
