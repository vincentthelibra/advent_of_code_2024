from itertools import pairwise


def part_1(file):

    number_of_safe_reports = 0

    for line in file:
        numbers_str = line.strip().split(' ')
        numbers = list(map(int, numbers_str))
        if numbers == sorted(numbers) and all(
                1 <= abs(numbers[i] - numbers[i + 1]) <= 3
                for i in range(len(numbers) - 1)):
            number_of_safe_reports += 1
        elif numbers == sorted(numbers, reverse=True) and all(
                1 <= abs(numbers[i] - numbers[i + 1]) <= 3
                for i in range(len(numbers) - 1)):
            number_of_safe_reports += 1

    print(number_of_safe_reports)


def part_2(file):
    number_of_safe_reports = 0

    for line in file:
        numbers_str = line.strip().split(' ')
        numbers = list(map(int, numbers_str))
        if is_report_true(numbers):
            number_of_safe_reports += 1
        else:
            if invoke_problem_dampener(numbers):
                number_of_safe_reports += 1

    print(number_of_safe_reports)


def invoke_problem_dampener(numbers) -> bool:
    for i in range(len(numbers)):
        updated_numbers = numbers[:]
        updated_numbers.pop(i)
        if is_report_true(updated_numbers):
            return True
    False


def is_report_true(numbers) -> bool:
    if numbers == sorted(numbers) and all(
            1 <= abs(numbers[i] - numbers[i + 1]) <= 3
            for i in range(len(numbers) - 1)):
        return True
    elif numbers == sorted(numbers, reverse=True) and all(
            1 <= abs(numbers[i] - numbers[i + 1]) <= 3
            for i in range(len(numbers) - 1)):
        return True
    else:
        return False


def merry_xmas():
    with open('day_2/data.txt', 'r') as f:
        part_1(f)

    with open('day_2/data.txt', 'r') as f:
        part_2(f)


if __name__ == "__main__":
    merry_xmas()
