symbols ='$¢£€¥'
codes = []

for symbol in symbols:
    codes.append(ord(symbol))

print(codes)
import array
print(array.array('I', (ord(symbol) for symbol in symbols)))
