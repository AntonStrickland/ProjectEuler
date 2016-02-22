# Programmer: Anton Strickland
# Date: 2/22/2016
# Euler Problem 4

# PROBLEM DESCRIPTION:
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def checkPalindrome(num):
  for i in range( len(num) ):
    if num[i] != num[len(num)-i-1]:
      return False
  return True
  
def main():

  pList = []
  for i in reversed(range(999)):
    for j in reversed(range(999)):
      if checkPalindrome( str(i*j) ):
        pList.append(i*j)
    
  return max(pList)

print( main() )