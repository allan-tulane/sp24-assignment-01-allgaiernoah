"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
    if x <= 1:
        return x
    else:
        return foo(x-1) + foo(x-2)

def longest_run(mylist, key):
    current_run = 0
    max_run = 0
    for num in myarray:
        if num == key:
            current_run += 1
            max_run = max(max_run, current_run)
        else:
            current_run = 0
    return max_run


class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
    

def to_value(v):
    """
    if it is a Result object, return longest_size.
    else return v
    """
    if type(v) == Result:
        return v.longest_size
    else:
        return int(v)
        
def longest_run_recursive(mylist, key):
    if not myarray:
        return 0
    mid = len(myarray) // 2
    left_run = longest_run_recursive(myarray[:mid], key)
    right_run = longest_run_recursive(myarray[mid+1:], key)
    
    middle_run = 1 if myarray[mid] == key else 0
    
    if middle_run == 0:
        return max(left_run, right_run)
    else:
        return max(left_run, right_run, middle_run)



