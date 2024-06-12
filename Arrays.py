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
    """
    This function finds and returns the index of the second largest element in a given list.
    
    :param arr: The function `SecondLargest` takes a list of integers `arr` as input and returns the
    index of the second largest element in the list
    :type arr: list[int]
    :return: The function `SecondLargest` is returning the index of the second largest element in the
    input list `arr`.
    """
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

def PeakElement(arr):
    if len(arr) == 1:
        return 0
    if arr[0] > arr[1]:
        return 1
    if arr[len(arr)-1] > arr[len(arr)-2]:
        return len(arr) - 1
    low = 1
    high = len(arr) - 2
    while low <= high:
        mid = (low+high) // 2
        if (arr[mid-1]<arr[mid]) and (arr[mid]>arr[mid+1]):
            return mid
        elif arr[mid]>arr[mid-1]:
            low = mid+1
        else:
            high = mid - 1
    return -1
 
def MajorityElement(arr:list[int]):
    freq = {}
    Len = len(arr) // 2
    for i in arr:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1

    for key, val in freq.items():
        if val > Len:
            print(key)

def ShiftZeros(arr:list[int])->list[int]:
    # temp = []
    # NoZeros = len(arr)
    # for i in range(len(arr)):
    #     if arr[i] != 0:
    #         temp.append(arr[i])
    # for i in range(len(temp)):
    #     arr[i] = temp[i]
    # for i in range(len(temp), len(arr)):
    #     arr[i] = 0

    if len(arr) == 0:
        raise ValueError("Given List is empty")

    j = -1
    for i in range(len(arr)):
        if arr[i] == 0:
            j = i
            break
    if j == -1: return arr
    for i in range(j+1, len(arr)):
        if arr[i] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
    return arr
    
def UnionOfArray(arr1:list[int], arr2:list[int])->list[int]:
    """
    Finds the union of two integer lists efficiently.

    @params:
        arr1: The first list of integers.
        arr2: The second list of integers.

    @return:
        A list containing the unique elements from both input lists.
  """
    # st = set()
    # union = []

    # if len(arr1) == 0 or len(arr2) == 0:
    #     raise ValueError("Empty List")
    
    # for i in range(len(arr1)):
    #     st.add(arr1[i])

    # for j in range(len(arr2)):
    #     st.add(arr2[j])
    
    # for i in st:
    #     union.append(i)
    
    # return union
    union = []
    i = 0
    prev = None
    combine = sorted(arr1+arr2)
    while i < len(combine):
        curr = combine[i]
        if curr != prev:
            union.append(curr)
            prev = curr
        i += 1
    return union

def MissingValues(arr:list[int])->int:
    """
    The function MissingValues calculates the missing value in an array of integers using XOR
    operations.
    
    :param arr: The function `MissingValues` takes a list of integers as input. The function calculates
    the missing value in the list by performing XOR operations on the elements of the list and the
    indices of the elements
    :type arr: list[int]
    :return: int
    """
    XOR1 = 0
    XOR2 = 0
    n = len(arr) - 1
    for i in range(len(arr)):
        XOR2 = XOR2 ^ arr[i]
        XOR1 = XOR1 ^ (i+1)
    return (XOR1 ^ XOR2)          


def MaxConsecutiveOnes(arr:list[int])->int:
    """
    The function `MaxConsecutiveOnes` takes a list of integers and returns the maximum number of
    consecutive ones in the list.
    
    :param arr: The function `MaxConsecutiveOnes` takes a list of integers as input and returns the
    maximum number of consecutive ones in the list.
    :type arr: list[int]
    :return: int -> NUMBERS OF MAXIMUM CONSECUTIVE ONES.
    """
    count = 0
    MaxOnes = 0
    for i in range(len(arr)):
        if arr[i] == 1:
            count += 1
            MaxOnes = max(MaxOnes, count)
        else:
            count = 0
    return MaxOnes

def FindSingleNumber(arr:list[int])->int:
    freq = {}
    for i in range(len(arr)):
        if arr[i] in freq:
            freq[arr[i]] += 1
        else:
            freq[arr[i]] = 1
    
    for key, val in freq.items():
        if val == 1:
            return key
