

#generator is function which return the generator object
#generator is iterator but iterator is not generator
#generator function contain one or more yield statements
#when we call the generator function it return the generator object without executing the function

def f1():
    yield 10
    yield 20
    yield 30
    #return 50 #once we return the value from the generator function it will stop the execution of the function and it will not execute the next yield statement
    yield 40
    return 60 #so return statement is used to stop the execution of the generator function and it will not execute the next yield statement
print(f1())  # Output: <generator object f1 at 0x7f8c8c8c8c8c>

it=f1()
print(it)  # Output: <generator object f1 at 0x7f8c8c8c8c8c>
print(next(it))  # Output: 10
print(next(it)) # Output: 20
print(next(it)) # Output: 30
print(next(it)) # Output: 40
print(next(it)) # StopIteration Error