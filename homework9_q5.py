
def create_grid(message, rows, cols):
    message = message.replace(" ", "").upper()
    size = rows * cols

    if len(message) > size:
        raise ValueError("Message is too long for the grid.")

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


def get_path(rows, cols):
    path = []
    top, bottom = 0, rows - 1
    left, right = 0, cols - 1

    while top <= bottom and left <= right:
        for col in range(left, right + 1):
            path.append((top, col))
        top += 1

        for row in range(top, bottom + 1):
            path.append((row, right))
        right -= 1

        if top <= bottom:
            for col in range(right, left - 1, -1):
                path.append((bottom, col))
            bottom -= 1

        if left <= right:
            for row in range(bottom, top - 1, -1):
                path.append((row, left))
            left += 1

    return path


def get_keyword_order(keyword):
    return sorted(
        range(len(keyword)),
        key=lambda col: (keyword[col].upper(), col)
    )


def combined_path(rows, cols, keyword):
    path = get_path(rows, cols)
    order = get_keyword_order(keyword)

    # Keep the agreed path order within each column,
    # but process columns in keyword order.
    ordered_path = []

    for col in order:
        for row, path_col in path:
            if path_col == col:
                ordered_path.append((row, path_col))

    return ordered_path


def encrypt(message, keyword, rows):
    cols = len(keyword)
    grid = create_grid(message, rows, cols)
    path = combined_path(rows, cols, keyword)

    ciphertext = ""

    for row, col in path:
        ciphertext += grid[row][col]

    return ciphertext


def decrypt(ciphertext, keyword, rows):
    cols = len(keyword)
    ciphertext = ciphertext.replace(" ", "").upper()

    if len(ciphertext) != rows * cols:
        raise ValueError("Ciphertext length does not match grid size.")

    grid = [[""] * cols for _ in range(rows)]
    path = combined_path(rows, cols, keyword)

    # Put each encrypted character back into its location.
    for index, (row, col) in enumerate(path):
        grid[row][col] = ciphertext[index]

    message = ""

    for row in grid:
        message += "".join(row)

    return message


def main():
    message = input("Enter the message: ")
    keyword = input("Enter the keyword: ").upper()
    rows = int(input("Enter the number of rows: "))

    if not keyword.isalpha() or rows < 1:
        print("Enter a valid keyword and positive row count.")
        return

    if len(message.replace(" ", "")) > rows * len(keyword):
        print("The message is too long for this grid.")
        return

    encrypted = encrypt(message, keyword, rows)
    print("Encrypted message:", encrypted)

    decrypted = decrypt(encrypted, keyword, rows)
    print("Decrypted message:", decrypted)


if __name__ == "__main__":
    main()
