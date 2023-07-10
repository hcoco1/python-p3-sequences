#!/usr/bin/env python3




def print_fibonacci(length):
    sequence = []
    if length == 0:
        print(sequence)
    elif length == 1:
        sequence = [0]
        print(sequence)
    elif length == 2:
        sequence = [0, 1]
        print(sequence)
    else:
        sequence = [0, 1]
        i = 3
        while i <= length:
            sequence.append(sequence[-2] + sequence[- 1])
            i+= 1
        print(sequence)





  
  
  

