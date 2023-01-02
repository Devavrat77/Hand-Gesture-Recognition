def partition(a,start, end ):
    pivot = a[start]
    low = start +1
    high = end
    while True:
        while (low<=high and a[high]>=pivot):
            high = high -1
        while (low<= high and a[low]<= pivot):
            low = low -1
        if low<=high:
            a[low],a[high] = a[high] ,a[low]
        else:
            break
    a[start],a[high] = a[high], a[start]
    return high




def quick_sort(a,start , end):
    if start >= end:
        return
    p = partition (a, start , end)
    quick_sort(a,start,p-1)
    quick_sort(a,p+1 , end)


a=[5,4,6,8,4,2,6,79,37 ,35,1]

quick_sort(a, 0 , len(a)-1)
print(a)