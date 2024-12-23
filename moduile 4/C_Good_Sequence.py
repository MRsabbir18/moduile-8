from collections import Counter
def min_removals_to_good_sequence(N, a):
    frequency = Counter(a)
    removals = 0
    for x, count in frequency.items():
        if count > x:
            removals += count - x
        else:
            removals += count
    return removals
N = int(input().strip())
a = list(map(int, input().strip().split()))
result = min_removals_to_good_sequence(N, a)
print(result)