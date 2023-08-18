import numpy as np

test_arr = [1, 3, 2, 5, 4]
test_sorted = [1, 2, 3, 4, 5]

class State:
    def __init__(self, init_array):
        self.present = 0
        self.board = [[init_array]]
    
    def present_row(self):
        return self.board[self.present]

# Current sorting algorithm: Bubble Sort
# Swaps up to 1 value pair
def sort_iteration(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            break
    return arr

def get_first_sorted(present_row):
    for arr in present_row:
        if(is_sorted(arr)):
            return arr
    return []
            
        
def is_sorted(arr):
    return all(b >= a for a, b in zip(arr, arr[1:]))

def main(arr):
    if(arr == []):
        return arr
    sorted_arr = []
    state = State(arr)
    while(sorted_arr == []):
        sort_iteration(state.board[0][0])
        sorted_arr =  get_first_sorted(state.present_row())
    return sorted_arr

def test(arr):
    if(arr == []):
        return arr
    return [-1]
print(test([]))