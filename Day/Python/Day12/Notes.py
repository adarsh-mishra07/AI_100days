#itrator is a object which can be iterated upon, meaning that you can traverse through all the values.
#iterable is an object which can return an iterator, meaning that it can be iterated upon. 
# Examples of iterables include lists, tuples, strings, and dictionaries.
#when we use for loop to iterate over an iterable, it automatically creates an iterator object and calls the next() method on it to get the next value until there are no more values to iterate over.
#an iterator can be seen as a pointer that points to the current element in the iterable. When we call next() on the iterator, it moves the pointer to the next element and returns its value. If there are no more elements to iterate over, it raises a StopIteration exception.
#without iterator , set and dictionary are not possible because they are not index based data structure.
#iterators are used in for loop, list comprehension, generator expressions, and many other places in Python to iterate over collections of data. They provide a convenient and efficient way to access and manipulate data without having to worry about the underlying implementation details of the iterable.
#iterator is an abstration that allows us to traverse through a collection of data without having to worry about the underlying implementation details of the iterable. It provides a consistent interface for accessing elements in a collection, regardless of how the collection is implemented.
# This makes it easier to write code that can work with different types of collections, such as lists, tuples, sets, and dictionaries, without having to worry about the specific details of how those collections are implemented.

# iter() is a built-in function in Python that is used to create an iterator object from an iterable. 
# It takes an iterable as an argument and returns an iterator object that can be used to iterate over the elements of the iterable.
# For example, if we have a list of numbers, we can create an iterator object from it using the iter() function like this:


numbers = [1, 2, 3, 4, 5]
iterator = iter(numbers)
print(iterator)  # Output: <list_iterator object at 0x7f8c8c8c8c8c>

# We can then use the next() function to get the next element from the iterator:
# print(next(iterator))  # Output: 1    

#iter return the object what we store the element in it and next return the element what we store in the object of iter
#there are each container own iterator object like list has list_iterator, tuple has tuple_iterator, set has set_iterator and dictionary has dict_iterator.
#iter() function is used to create an iterator object from an iterable, 

# while next() function is used to retrieve the next item from the iterator. 
#  The iter() function takes an iterable as an argument and returns an iterator object, while the next() function takes an iterator as an argument and returns the next item from the iterator. If there are no more items to return, next() raises a StopIteration exception.


l1=[1,2,3,4,5]
iterator=iter(l1)
while True:
    try:
     print(next(iterator))
    except StopIteration:
        break

#Generator is a special type of iterator that allows you to create an iterable sequence of values on-the-fly, without having to store them all in memory at once.
# A generator is defined using a function that contains one or more yield statements. When the generator
# function is called, it returns a generator object that can be used to iterate over the sequence of values produced by the yield statements. Each time the generator's __next__() method is called, the function executes until it reaches a yield statement, at which point it returns the value specified by the yield and pauses execution until the next call to __next__().
# Generators are useful for working with large datasets or infinite sequences, as they allow you to generate values on demand without having to store them all in memory at once. They can also be used to create more efficient and readable code for certain types of problems, such as iterating over a sequence of values or generating a stream of data.
#whose fun inside the yield keyword is called generator function and it return the generator object when we call it.