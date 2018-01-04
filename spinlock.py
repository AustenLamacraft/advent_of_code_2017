import bisect

my_input = 354

spinlock = [0]
pos = 0

# This version is slow... can't be used for 50000000
for j in range(1,2018):
    pos = (pos + my_input) % len(spinlock)
    spinlock.insert(pos + 1, j)
    pos += 1
    if j % 1000000 == 0:
        print(j // 1000000, " million")

print(spinlock[spinlock.index(2017) + 1])


# For the second part, since we only need the value after 0, it's enough to keep
# track of the last value added after zero.

after_zero = 0

for j in range(1,50000001):
    pos = (pos + my_input) % j
    if pos == 0:
        after_zero = j
    pos += 1
    if j % 1000000 == 0:
        print(j // 1000000, " million")

print(after_zero)
