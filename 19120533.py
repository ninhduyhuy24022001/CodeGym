import pickle
from math import sqrt

def wbfile_1(M, filename):
    with open(filename, 'wb') as f:
        for i in range(1, M):
            f.write((i+2020).to_bytes(4, byteorder='big', signed=False))


def rbfile_1(filename):
    bytes = []
    with open(filename, 'rb') as f:
        while True:
            b = f.read(4)
            if not b:
                break
            bytes.append(int.from_bytes(b, byteorder='big'))
    return bytes

wbfile_1(10,"test.txt")
print(rbfile_1("test.txt"))
