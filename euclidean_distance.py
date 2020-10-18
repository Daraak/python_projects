import math


def compute_distance(x1, y1, x2, y2):
    distance = math.sqrt((x1 - y1) ** 2 + (x2 - y2) ** 2)
    print("Distance:", format(distance, ".2f"))


if __name__ == '__main__':
    test_cases = int(input())
    for i in range(test_cases):
        values = list(map(int, input().split()))
        x1, y1, x2, y2 = values
        compute_distance(x1, y1, x2, y2)