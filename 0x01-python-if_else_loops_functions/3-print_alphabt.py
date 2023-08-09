#!/usr/bin/python3
for a in range(ord('a'), ord('z') + 1):
    if chr(a) != 'e' and chr(a) != 'q':
        continue
        
        print("{:c}".format(a), end="")
