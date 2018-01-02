gen_a = 873
gen_b = 583

fac_a = 16807
fac_b = 48271

def binarize(input):
    output = bin(input)[2:]
    if len(output) < 16:
        output = (16-len(output))*"0" + output
    return output

def generate(last, factor):
    return (last * factor) % 2147483647

def generator_a(last):
    cand_a = generate(last, fac_a)
    if cand_a % 4 == 0:
        return cand_a
    else:
        return generator_a(cand_a)

def generator_b(last):
    cand_b = generate(last, fac_b)
    if cand_b % 8 == 0:
        return cand_b
    else:
        return generator_b(cand_b)

count = 0

for j in range(5000000):
    gen_a, gen_b = generator_a(gen_a), generator_b(gen_b)
    if binarize(gen_a)[-16:] == binarize(gen_b)[-16:]:
        count += 1
    if j % 1000000 == 0:
        print(j//1000000, " million pairs")

print("Final count: ", count)
