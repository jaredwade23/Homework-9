
def make_grid(message, rows=5, cols=6):
    message = message.replace(" ", "").upper()
    size = rows * cols

    if len(message) > size:
        raise ValueError("Message exceeds the grid capacity.")

    message = message.ljust(size, "X")

    return [
        list(message[row * cols:(row + 1) * cols])
        for row in range(rows)
    ]


def spiral_path(rows, cols):
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


def encrypt(message):
    rows, cols = 5, 6
    grid = make_grid(message, rows, cols)
    path = spiral_path(rows, cols)

    ciphertext = ""

    for row, col in path:
        ciphertext += grid[row][col]

    return ciphertext


def decrypt(ciphertext):
    rows, cols = 5, 6
    ciphertext = ciphertext.replace(" ", "").upper()

    if len(ciphertext) != rows * cols:
        raise ValueError("Ciphertext must contain 30 characters.")

    grid = [[""] * cols for _ in range(rows)]
    path = spiral_path(rows, cols)

    for index, (row, col) in enumerate(path):
        grid[row][col] = ciphertext[index]

    message = ""

    for row in grid:
        message += "".join(row)

    return message


def main():
    message = input("Enter a message (up to 30 characters): ")

    encrypted = encrypt(message)
    print("Encrypted message:", encrypted)

    ciphertext = input("Enter ciphertext to decrypt: ")
    decrypted = decrypt(ciphertext)

    print("Decrypted message:", decrypted)


if __name__ == "__main__":
    main()

