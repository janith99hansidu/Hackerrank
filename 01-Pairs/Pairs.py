# brute force method
def pairs(k, arr):
    num_times = 0
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            if(abs(arr[i]-arr[j]) == k):
                num_times = num_times + 1
    return num_times

if __name__ == '__main__':
    print(pairs(2, [1, 5, 3]))