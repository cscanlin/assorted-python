import timeit

set_operation_script = """
first = set(xrange(100000000))
second = set(xrange(0,100000000,2))
result = first - second
"""
set_operation_time = timeit.timeit(set_operation_script, number=1)
print('set operation time: {0}'.format(set_operation_time))

list_comprehension_script = """
first = range(1000)
second = range(0,1000,2)
result = [num for num in first if num not in second]
"""
list_comprehension_time = timeit.timeit(list_comprehension_script, number=1)
print('list comprehension time: {0}'.format(list_comprehension_time))
