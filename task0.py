#printing number from 1-100
def numbers(count):
    while count <= 100:
      print(count)
      count=count+3;
      if count > 100:
          count = 100
numbers(0)
#for multiples
def fizz_buzz(num):
 if num % 3 == 0:
        return 'Fizz'

    elif num % 5==0:
        return 'Buzz'
    elif num%3==0 and num%5==0:
        return 'FizzBuzz'
    else:
        return num

for n in range(1,100):
    print(fizz_buzz(n))
