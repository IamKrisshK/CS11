def binarySearch(arr, item, ind_=0, right=True):
    n = len(arr)
    ind = n//2
    ind_ += ind if right else -ind

    if arr[ind] == item:
        return ind_
    if n <= 1:
        return False

    if item < arr[ind]:
        return binarySearch(arr[:ind], item, ind_, right=False)
    else:
        return binarySearch(arr[ind:], item, ind_, right=True)
