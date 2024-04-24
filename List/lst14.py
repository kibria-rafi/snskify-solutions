def knock_down_pins(pins, start, stop):
    for i in range(start - 1, stop):
        pins[i] = '.'
N, K = map(int, input("Enter the number of pins and the number of balls (N K): ").split())

pins = ['I'] * N

for _ in range(K):
    start, stop = map(int, input().split())
    knock_down_pins(pins, start, stop)

print("".join(pins))
