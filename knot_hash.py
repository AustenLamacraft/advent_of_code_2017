import numpy as np

class Circ(list):
    "Periodic list class"

    def ceildiv(self, a, b):
        "From https://stackoverflow.com/questions/14822184/is-there-a-ceiling-equivalent-of-operator-in-python"
        return -(-a // b)

    def circ_indices(self, slice):

        if slice.start != None:
            circ_start = slice.start % len(self)
        else:
            circ_start = 0

        if slice.stop != None:
            circ_stop = slice.stop % len(self)
        else:
            circ_stop = len(self)

        if slice.step != None:
            step = slice.step
        else:
            step = 1

        return circ_start, circ_stop, step

    def __getitem__(self, key):
        "From https://stackoverflow.com/questions/2936863/python-implementing-slicing-in-getitem"
        if isinstance(key, slice):

            circ_start, circ_stop, step = self.circ_indices(key)

            if (circ_stop >= circ_start and step > 0) or (circ_stop <= circ_start and step < 0):
                return super(Circ, self).__getitem__(slice(circ_start, circ_stop, step))
            else:
                return super(Circ, self).__getitem__(slice(circ_start, None, step)) + super(Circ, self).__getitem__(slice(None, circ_stop, step))
        elif isinstance(key, int):
            return super(Circ, self).__getitem__(key % len(self))
        else:
            raise TypeError("Invalid argument type.")

    def __setitem__(self, key, value):
        if isinstance(key, int):
            super(Circ, self).__setitem__(key % len(self), value)

        elif isinstance(key, slice):

            circ_start, circ_stop, step = self.circ_indices(key)

            if (circ_stop >= circ_start and step > 0) or (circ_stop <= circ_start and step < 0):
                super(Circ, self).__setitem__(slice(circ_start, circ_stop, step), value)
            else:
                super(Circ, self).__setitem__(slice(circ_start, None, step), value[:self.ceildiv(len(self) - circ_start, step)])
                super(Circ, self).__setitem__(slice(None, circ_stop, step), value[self.ceildiv(len(self) - circ_start, step):])



# with open("knot_hash.txt") as file:
#     lengths = [int(length) for length in file.readline()[:-1].split(",")]

with open("knot_hash.txt") as file:
    my_lengths = [ord(char) for char in list(file.readline()[:-1])]

def knot_hash(lengths):

    lengths += [17, 31, 73, 47, 23]

    string = Circ(list(range(256)))
    skip = 0
    pos = 0


    for _ in range(64):

        for length in lengths:

            string[pos:pos+length] = string[pos+length-1:pos-1:-1]
            pos = pos + length + skip
            skip += 1

    dense_hash = []

    for i in range(16):
        xors = 0
        for j in range(16):
            xors = xors ^ string[16*i + j]

        dense_hash.append(xors)

    hex_hash = [hex(entry) for entry in dense_hash]

    hex_string = ""

    for entry in hex_hash:
        prefix = ""
        if len(entry) == 3: # Detect single digits
            prefix = "0"
        hex_string += prefix + entry[2:]

    return hex_string
