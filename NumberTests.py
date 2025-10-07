#NumberTests.py

def isThreeOrFive(n):
  """Returns boolean determination if number is multiple of 3 or 5"""

  if n % 3 == 0 or n % 5 == 0:
    return True
  else:
    return False

def isPrime(p):
  """Returns boolean (True/False) if the value given is prime."""
  for i in range(1, p+1):
    if p % i == 0 and i != 1 and i != p:
      return False
  return True

def oneThousandFirstPrime():
  prime_count = 0
  i = 2
  while True:
    if isPrime(i):
      prime_count += 1
      if prime_count == 10_001:
        return i
    i+=1

def palindromeProduct():
  largest = 0
  for i in range(100, 1000):
    for j in range(100, 1000):
      prod = i*j
      if str(prod) == str(prod)[::-1] and prod > largest:
        largest = prod
  return largest

def isEven(n):
  """Returns boolean about given value being even."""

  if n % 2 == 0:
    return True
  else:
    return False

def addNum(numList, num):
  """Adds the given number to the given list. Does not add duplicate values."""

  numList.append(num)


def fibonacciSequence(value):
  """Returns a list of numbers in the fibonacci sequence up to the given value"""

  nums = [1, 2]
  size = 2
  n = nums[size - 1] + nums[size - 2]

  while n < value:
    addNum(nums, n)
    size = len(nums)
    n = nums[size - 1] + nums[size - 2]

  return nums

#Test your new functions in this main
def main():
  
  #print("10001st prime: "+str(oneThousandFirstPrime()))

  print("largest palindrome product: "+str(palindromeProduct()))
  #num = int(input("Enter a number: "))

  #if isPrime(num):
  #  print("%d is a prime number" %(num))

  #if isEven(num):
  #  print("%d is an even number" %(num))


if __name__ == '__main__':
    main()
