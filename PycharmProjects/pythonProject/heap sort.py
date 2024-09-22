def heapify(arr,n,i):
    largest = i
    right = 2*i+2
    left = 2*i+1

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[largest],arr[i] = arr[i],arr[largest]

        heapify(arr,n,i)

def heap_sort(arr):
    n = len(arr)

    for i in range(n//2-1,-1,-1):
        heapify(arr,n,i)
    for i in range(n-1,0,-1):
        arr[i],arr[0] = arr[0],arr[i]
        heapify(arr,i,0)


arr = [12, 11, 13, 5, 6, 7]
heap_sort(arr)
print("Sorted array is:", arr)