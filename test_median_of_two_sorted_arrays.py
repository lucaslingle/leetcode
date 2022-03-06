from median_of_two_sorted_arrays import Solution


def test_soln():
    soln = Solution()
    assert soln.findMedianSortedArrays(nums1=[1, 3], nums2=[2]) == 2.0
    assert soln.findMedianSortedArrays(nums1=[1, 2], nums2=[3, 4]) == 2.5
    assert soln.findMedianSortedArrays(nums1=[], nums2=[3, 4, 5]) == 4.0
    assert soln.findMedianSortedArrays(nums1=[], nums2=[3, 4, 5, 6, 7]) == 5.0
