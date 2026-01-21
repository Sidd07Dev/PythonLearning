def myFuns():
    print("in function ")

myFuns()


#calculate square of a number 

def square(num=1):
   return num ** 2

print(square(6))

def multiply(p1,p2):
    return p1 * p2

print(multiply(5,8))
print(multiply('a',8))
print(multiply(8,'b'))


#lambda func
cube = lambda x: x**3
print(cube(5))

def fact(num):
    if num == 0 or num ==1:
        return 1;
    return num * fact(num-1)

print(fact(5))