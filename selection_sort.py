def selection_sort(arr):
   n=len(arr)
   print("lenth is:",n)
   for i in range(n):
       min_index=i
       for j in range(i+1,n):
           if arr[j]<arr[min_index]:
           
              min_index=j
              print("min_index:",arr[min_index])
       arr[i],arr[min_index]=arr[min_index],arr[i]         



if __name__ == "__main__":

 #arr=[64,24,12,22,11]
 #print("unsorted array:",arr)
 #selection_sort(arr)
 #print("Sorted array",arr)   
 input_str=input("enter nos seperated by spaces:")
 arr=list(map(int,input_str.split()))
 print("unsorted array:",arr)
 selection_sort(arr)
 print("sorted array:",arr)
