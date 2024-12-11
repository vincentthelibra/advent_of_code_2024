import re


def has_xmas(lines, n, m, i, j, d):
    dx, dy = d
    for k, x in enumerate("XMAS"):
        # calculate new coordinates
        ii = i + k * dx
        jj = j + k * dy
        if not (0 <= ii < n and 0 <= jj < m):
            return False
        if lines[ii][jj] != x:
            return False
    return True


def part_1(file):
    xmas_count = 0
    content = file.read()

    # horizontal lines
    lines = content.split("\n")
    n = len(lines)
    m = len(lines[0])

    # list all directions
    # dd is a list of Tuples
    dd = []
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if dx != 0 or dy != 0:
                dd.append((dx, dy))

    for i in range(n):
        for j in range(m):
            for d in dd:
                xmas_count += has_xmas(lines, n, m, i, j, d)

    print(xmas_count)


def part_2(file):
    pass


def merry_xmas():
    with open("day_4/data.txt", "r") as f:
        part_1(f)

    with open("day_4/data.txt", "r") as f:
        part_2(f)


if __name__ == "__main__":
    merry_xmas()
