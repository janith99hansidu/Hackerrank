def miniMaxSum(arr):
    # Write your code here
    arr.sort()
    length = len(arr)
    
    min_sum = arr[0]+arr[1]+arr[2]+arr[3]
    max_sum = arr[length-1]+arr[length-2]+arr[length-3]+arr[length-4]
    
    print(min_sum,max_sum)

if __name__ == '__main__':
    miniMaxSum([1,2,3,4,5,6,7])
