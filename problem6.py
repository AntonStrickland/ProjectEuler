# Programmer: Anton Strickland
# Date: 3/1/2016
# Euler Problem 6

# PROBLEM DESCRIPTION:
# Find the difference between the sum of the squares 
# of the first one hundred natural numbers and the square of the sum.

squaredSums = 0
summedSquares = 0

for i in range(1, 101):
  squaredSums += i
  summedSquares += i*i

difference = abs((squaredSums * squaredSums) - summedSquares)

print(difference)