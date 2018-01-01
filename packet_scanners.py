firewall = {}

with open("packet_scanners.txt") as file:
    for line in file:
        line = line.rstrip('\n')
        depth, scan_range = line.split(":")
        depth, scan_range = int(depth.strip()), int(scan_range.strip())
        firewall[depth] = scan_range

# Key point is that scanner of range r visits the top at 0, 2(r-1), 4(r-1), 6(r-1), ...

score = 0

for T in firewall.keys():
    if T % (2 * (firewall[T] - 1)) == 0:
        score += T * firewall[T]

print("Total severity: ",score)

shift = 0

while not all([(T + shift) % (2 * (firewall[T] - 1)) for T in firewall.keys()]):
    shift += 1
    if shift % 1000 == 0:
        print(shift)

print("Required delay is: ", shift)
