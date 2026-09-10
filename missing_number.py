tests = [[3, 0, 1], [0, 1], [9, 6, 4, 2, 3, 5, 7, 0, 1], [1], [0]]
print("Running missing-number tests from Jenkins")
def find_missing_number(numbers):
    n = len(numbers)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(numbers)

    return expected_sum - actual_sum

for test in tests:
    print(find_missing_number(test))