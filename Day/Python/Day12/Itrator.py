l1=[1,2,3,4,5]
iterator=l1.__iter__()  #iter() function is used to create an iterator object from an iterable,
while True:
    try:
        print(iterator.__next__())  #next() function is used to retrieve the next item from the iterator.
    except StopIteration:
        break
