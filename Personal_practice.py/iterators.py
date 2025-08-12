print("Iterators")

# An iterator is an object that contains a countable numbers of values.
# An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.

# my_list = ["muqoddim","eniola","deborah"]
# my_it = iter(my_list)

# print(next(my_it))

class Iterator():
    def __init__(self, parameter):
        self.current = 0
        self.parameter = parameter

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < len(self.parameter):
            char = self.parameter[self.current]
            self.current += 1
            return char
        else :
            raise StopIteration
        
my_iter = Iterator("muqoddim")
print(my_iter.__next__())
print(my_iter.__next__())
print(my_iter.__next__())
print(my_iter.__next__())
print(my_iter.__next__())
print(my_iter.__next__())
print(my_iter.__next__())
print(my_iter.__next__())
print(my_iter.__next__())

        