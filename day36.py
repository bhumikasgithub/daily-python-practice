# program sort the element by their frequency

'''
from collections import Counter   
list_int=[12,12,88,88,88,88,23,23,56,5,65,656,1,3,2,5,5,5,5,12,12,1,2,12]
result=[item for item,c in Counter(list_int).most_common() for item in [item]*c]
print(str(result))
'''
from collections import Counter
from itertools import repeat, chain
ini_list = [10, 20, 30, 40, 40, 50, 50, 50]

# sorting on bais of frequency of elements
result = list(chain.from_iterable(repeat(i, c) for i, c in Counter(ini_list).most_common()))

# printing final result
print(str(result))