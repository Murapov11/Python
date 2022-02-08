n = input()
a = [int (n) for n in input().split(' ')]
a.sort()
print(a[-1] * a[-2])