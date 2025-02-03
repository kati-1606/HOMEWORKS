#  5_Write a Python program that calculates the
#  Fibonacci sequence up to a given number n using a while loop.
#  The Fibonacci sequence is a series of numbers where each number
#  is the sum of the two preceding ones

n = int(input())
num_1 = 0
num_2 = 1
gumar = 0
while num_1 <= n:
    print(num_1)
    gumar = num_1 + num_2
    num_1 = num_2
    num_2 = gumar
