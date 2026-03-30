from collections import  defaultdict

def flatten(nested):
   # for list in nested:
   #     for item in list:
   #        print('')

    return [item for list in nested for item in list] 
    

def word_lengths(sentence):

    return {word: len(word) for word in sentence.split()}

def evens_squared(numbers):
    return [x**2 for x in numbers if x % 2 == 0]

def matrix_transpose(matrix):              
      
    return [[row[col] for row in matrix] for col in range(len(matrix[0]))]
    

def log_reader(lines):                                                                                                                               
      for line in lines:
          line = line.strip()
          if "ERROR" in line:
            yield line
        


def chunk(iterable, size):
    shoot = list()
    for i in iterable:
        shoot.append(i)
        if(len(shoot) >= size):
            yield shoot
            shoot = list()
    yield shoot

def scoring(people): 
    def passed(score): 
        if score >= 90:
            return "A"
        if score >= 80:
            return "B"
        if score >= 70:
            return "C"
        if score >= 60:
            return "D"
        return "(F)ailure" \
        ""
    return {person: passed(sc) for person,sc in people.items() if sc >= 60}

print(flatten([[1, 2], [3, 4], [5]]))
print(word_lengths("the quick brown fox"))
print(evens_squared([1, 2, 3, 4, 5, 6]))
print(matrix_transpose([[1, 2, 3], [4, 5, 6]]))
print(list(chunk(range(10), 3)))

print(scoring({"alice": 85, "bob": 42, "carol": 91, "dave": 58, "eve": 73}))

logs = [
    "  INFO: started  ",
    "  ERROR: disk full  ",
    "  INFO: retrying  ",
    "  ERROR: timeout  ",
]
print(list(log_reader(logs)))