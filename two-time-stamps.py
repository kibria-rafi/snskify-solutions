h = int(input())
m = int(input())
s = int(input())
h1 = int(input())
m1 = int(input())
s1 = int(input())

t = h * 3600 + m * 60 + s
t1 = h1 * 3600 + m1 * 60 + s1

if t <= t1:
    difference = t1 - t
    print(difference)