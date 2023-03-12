class Solution(object):
    def findMedianSortedArrays(self,nums1, nums2):
        mid = len(nums1+nums2)
        def sum(nums1,nums2):
            val1 = 0
            val2 = 0
            for x in range(0,len(nums1)):
                val1 = nums1[x] 
            for y in range(0,len(nums2)):
                val2 += nums2[y]
            return val1+val2
        return sum(nums1,nums2)/mid

nums1 = [1,2,4]
nums2 = [3,4]
z = Solution().findMedianSortedArrays(nums1,nums2)
print("method_1 = %s " %
 z)


total_nums = nums1 + nums2
mid2=  len(total_nums)
sum = sum(total_nums)/mid2
print("mwthod_2 = %s" %sum)

def test(sum,z):
    if sum == z:
        return "test passed!"
    else:
        return "test failed!!"
        

run  = test(sum,z)
print(run)