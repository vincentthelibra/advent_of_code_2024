import re


def mul(x, y) -> int:
    return x * y


def part_1(file):
    re_pattern = r"mul\(\d{1,3},\d{1,3}\)"
    content = file.read()
    mul_list_initial = re.findall(re_pattern, content)
    mul_list_final = []
    for pair in mul_list_initial:
        print(pair)
        mul_a = int(pair.split(",")[0][4:])
        mul_b = int(pair.split(",")[1][:-1])

        # alternatively use eval as a 'smart way' but less secured
        # mul_result = eval(pair)
        mul_result = mul(mul_a, mul_b)

        mul_list_final.append(mul_result)

    print(sum(mul_list_final))


def part_2(file):
    pass


def merry_xmas():
    with open('day_3/data.txt', 'r') as f:
        part_1(f)

    with open('day_3/data.txt', 'r') as f:
        part_2(f)


if __name__ == "__main__":
    merry_xmas()