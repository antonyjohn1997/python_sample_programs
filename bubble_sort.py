def bubble_sort(arr):
    n=len(arr)
    print("array length:",n)
    for i in range(n):
        swapped=False#flag to check if any swapping happened
        for j in range(0,n-i-1):#last i element are already in place
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped=True

        if not swapped:
            break
            
        
    

if __name__ == "__main__":
    #arr=[64,34,25,12,22,11,90]
    #print("unsorted array:",arr)
    #bubble_sort(arr)
    #print("Sorted array",arr)

    input_str=input("Enter numbers seperated by spaces :")
    arr=list(map(int,input_str.split()))
    
    print("Unsorted array:", arr)
    # Sort the array
    bubble_sort(arr)
    print("Sorted array:", arr)
