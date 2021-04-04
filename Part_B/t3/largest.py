def heap(a, size, largest=0):
    if size == 1:
        nArr = []
        for i in a:
            nArr.append(str(i))
        sep = ''
        sep = sep.join(nArr)
        if largest < int(sep):
            largest = int(sep)
        return largest
    for i in range(size):
        largest = heap(a, size-1, largest)
        if size & 1:
            a[0], a[size-1] = a[size-1], a[0]
        else:
            a[i], a[size-1] = a[size-1], a[i]
    return largest

def largest(arr):
    n = len(arr)
    a = heap(arr, n)
    return a

def testLargest():
    arrs = [
        [1,10,100],
        [5, 200, 54]
    ]

    for a in arrs:
        print(largest(a))

testLargest()
