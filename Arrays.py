def FindLargest(arr:list[int])->int:
    """
    This Python function finds the index of the largest element in a given list.
    
    :param arr: The function `FindLargest` takes a list of integers `arr` as input and returns the index
    of the largest element in the list
    :type arr: list[int]
    :return: The function `FindLargest` returns the index of the largest element in the input list
    `arr`.
    """
    largest = 0
    for i in range(len(arr)):
        if arr[i] > arr[largest]:
            largest = i
    return largest

def SecondLargest(arr:list[int])->int:
    largest = FindLargest(arr)
    resul = -1
    for i in range(len(arr)):
        if arr[i] != arr[largest]:
            if resul == -1:
                resul = i
            elif arr[i] > arr[resul]:
                resul = i
    return resul

def RemoveDuplicate(arr:list[int]):
    i = 0
    for j in range(len(arr)):
        if arr[i] != arr[j]:
            i +=1
            arr[i] = arr[j]
            
    arr = arr[:i+1]
    return arr

def Rotate(arr:list[int], k:int)->list:
    def reverse(arr:list[int], left:int, right:int):
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
    k = k % len(arr)
    reverse(arr, 0, len(arr)-1)
    reverse(arr, 0, k-1)
    reverse(arr, k, len(arr)-1)
    return arr

def BinarySearch(arr:list[int],target:int):
    low = 0
    hight = len(arr) - 1
    while low <= hight:
        Mid = (low+hight) // 2
        if arr[Mid] == target:
            return Mid
        elif arr[Mid] < target:
            low = Mid + 1
        else:
            hight = Mid - 1
    return - 1


def TwoSum(arr:list[int], target:int)->list[int]:
    '''
    two Sum problem. The function `TwoSum` takes a
    list of integers `arr` and a target integer `target` as input. It then initializes two pointers,
    'left' pointing to the start of the list and `right` pointing to the end of the list.
    
    @params: list[int], target:int
    @return: list[int]
    '''
    left = 0
    right = len(arr)-1
    while left < right:
        Sum = arr[left] + arr[right]
        if Sum == target:
            return [left, right]
        elif Sum <= target:
            left +=1
        else:
            right -=1
    return [0,0]

print(TwoSum.__doc__)