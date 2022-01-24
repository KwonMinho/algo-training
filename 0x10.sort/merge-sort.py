
arr = []
tmp = []

def merge(st, en):
    mid = (st+en)//2
    l = st
    r = mid

    for i in range(st,en):
        if r == en:
            tmp[i] = arr[l]
            l+=1
        elif l == mid:
            tmp[i] = arr[r]
            r+=1
        elif arr[l] <= arr[r]: # 여기서 같다는 표현 때문에 stable sort가 된다.
            tmp[i] = arr[l]
            l+=1
        else:
            tmp[i] = arr[r]
            r+=1
    
    for i in range(st, en):
        arr[i] = tmp[i]

def merge_sort(st, en):
    if en == st+1: return
    mid = (st+en)//2
    merge_sort(st, mid)
    merge_sort(mid, en)
    merge(st, en)