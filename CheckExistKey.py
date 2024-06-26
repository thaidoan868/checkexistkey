import math, random
def CheckExistKey(A, start, end, key):
    """"
    This procedure check if a key exists in an already sorted array A, return -1 if the key does not exist in the array, otherwise return an index.
    Conditions before call the function: 
    - The key must satisfy the condition A[start] < key < A[end]
    - The end value must be greater than the start value (e.g start < end)
    The correctness the CheckExistKey:
    - Invariant - before the next call:
        A[start] < key < A[end]. 
        key ∉ {A[start+1] ... A[end-1]} => key ∉ {A[0] ... A[n]}
    We need to prove that if we continue call the function recursively it will end up with end = start + 1
    - Termination - at the final recursive:
        Because end == start + 1
        key ∉ {empty} => key ∉ {A[0] ... A[n]}
    Running time:
    - The running time is O(lgn). If you use the linear search method it would take O(n).
    """
    print('+')
    if end == start + 1: return -1
    median =  math.ceil((end+start)/2)
    if key == A[median]: return median
    elif key < A[median]: return CheckExistKey(A, start, median, key)
    else: return CheckExistKey(A, median, end, key)
A = [random.randint(1, 1000) for i in range(3000)]
A.sort()
print(A)
print(CheckExistKey(A, 0, len(A)-1, 2000))

