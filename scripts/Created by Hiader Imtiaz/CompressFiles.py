# Compress Files
import zlib
import os
def Compress(file):
    with open(file, 'rb') as f:
        data = f.read()
    compressed = zlib.compress(data)
    with open(file, 'wb') as f:
        f.write(compressed)
def Decompress(file):
    with open(file, 'rb') as f:
        data = f.read()
    decompressed = zlib.decompress(data)
    with open(file, 'wb') as f:
        f.write(decompressed)
Compress("Data.pdf")
Decompress("Data.pdf")