class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        numbers = sorted(nums1+nums2)
        numbersLength = len(numbers)
        if numbersLength % 2 == 1:
            return numbers[(numbersLength - 1) // 2]
        else:
            return((numbers[(numbersLength // 2) - 1] + numbers[numbersLength // 2]) / 2)







