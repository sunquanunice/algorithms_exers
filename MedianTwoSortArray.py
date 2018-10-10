'''
	Problem : https://leetcode.com/problems/median-of-two-sorted-arrays/description/
	Recommanded anwser : https://leetcode.com/problems/median-of-two-sorted-arrays/discuss/2471/Very-concise-O(log(min(MN)))-iterative-solution-with-detailed-explanation

'''

class MedianSortedArrays(object):
	
	def findMedianSortedArrays(self, nums1, nums2):
		INT_MIN = -100000
		INT_MAX = 100000
		n1 = len(nums1)
		n2 = len(nums2)
		if n1 < n2 :
			return self.findMedianSortedArrays(nums2, nums1)

		lo = 0
		hi = n2 * 2
		while lo <= hi :
			mid2 = (lo + hi) // 2
			mid1 = n1 + n2 - mid2

			l1 = nums1[(mid1 - 1) // 2] if  mid1 > 0 else  INT_MIN
			r1 = nums1[mid1 // 2] if mid1 < n1 * 2 else INT_MAX
			l2 = nums2[(mid2 - 1) // 2 ] if mid2 > 0 else INT_MIN
			r2 = nums2[mid2 // 2] if mid2 < n2 * 2 else INT_MAX
			print("(lo, hi) : ({0}, {1})".format(lo, hi))
			if l1 > r2 :
				lo = mid2 + 1
			elif l2 > r1 :
				hi = mid2 - 1
			else :
				return (max(l1, l2) + min(r1, r2)) / 2

		return -1

def main():
	medianTwoSortedArray = MedianSortedArrays()
	nums1 = [1,2,3, 7, 8]
	nums2 = [4, 5, 6, 7, 100, 112]
	median = medianTwoSortedArray.findMedianSortedArrays(nums1, nums2)
	print("The median number is : {0}".format(median))

if __name__ == "__main__":
	main()
