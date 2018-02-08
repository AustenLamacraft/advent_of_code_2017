
b = 106500
c = 123500
d, e, f, h = 0, 0, 0, 0

for b in range(106500, c+1,17):

    f = 1

    # Is it prime?
    for d in range(2,b):
        if b % d == 0:
            f = 0

    if f == 0:
        h += 1

print(h)
