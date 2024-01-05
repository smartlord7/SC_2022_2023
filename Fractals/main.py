import math


def gen_pascal_triangle(n: int = 15) -> list:
    triangle_data = [[1], [1, 1]]

    for i in range(2, n + 2):
        row = [1]
        for j in range(1, i - 1):
            row.append(triangle_data[i - 1][j - 1] + triangle_data[i - 1][j])
        row.append(1)
        triangle_data.append(row)

    triangle_data.pop(1)

    return triangle_data


def pascal_triangle_to_string(triangle_data: list, div: int = None, replacer: str = '_') -> str:
    n = len(triangle_data)
    triangle_str = []
    offset = 150
    if n % 2 == 0:
        max_value_idx = n // 2 - 1
    else:
        max_value_idx = math.floor(n / 2)
    max_value_length = len(str(math.comb(n - 1, max_value_idx))) + 1
    space = ' ' * max_value_length

    for row in triangle_data:
        row_string = space.join(str(v) if div is None or v % div != 0 else replacer * len(str(v)) for v in row)
        width = 2 * n - 1 + offset
        centered_row_string = row_string.center(width)
        triangle_str.append(centered_row_string)

    return '\n'.join(triangle_str)


def main() -> None:
    triangle = gen_pascal_triangle(15)
    print(pascal_triangle_to_string(triangle, div=2))


if __name__ == '__main__':
    main()