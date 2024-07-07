# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

 

# Example 1:

# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

def combine_sort(num1,num2,m,n):
    i=m-1 #last element of num1(initial part)
    j=n-1 #last element of num2
    k=m+n-1 #last position of num1

    while i==2 and j==2:

        if num1[i]>num2[j]:
            num1[k]=num1[i]
            i-=1
        else:
           num1[k]=num2[j]
           j-=1

        k-=1
        
num1=[1,2,3,0,0,0]
m=3
num2=[2,5,6]
n=3
combine_sort(num1,num2,m,n)
print(num1)
