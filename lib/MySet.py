class MySet:
    def __init__(self,enumerable = []):
        self.dictionary = {}
        for value in enumerable:
            self.dictionary[value] = True
    
    def has(self, value):
        return value in self.dictionary
    
    def add(self, value):
        self.dictionary[value] = True
        return self
    
    def delete(self, value):
        self.dictionary.pop(value, None)
        return self
    
    def size(self):
        return len(self.dictionary)
    
    def clear(self):
        self.dictionary.clear()
    
    # I did not do this one
    def __str__(self):
        list_of_the_set = []
        for key, value in self.dictionary.items():
            list_of_the_set.append(str(key))
        return f'MySet: {{{",".join(list_of_the_set)}}}'