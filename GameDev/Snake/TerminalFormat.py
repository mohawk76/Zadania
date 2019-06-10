def move_cursor(x, y):
    print("\x1b[{};{}H".format(y + 1, x + 1), end='')
