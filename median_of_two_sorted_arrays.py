from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        tophalf = []
        total_nums = len(nums1) + len(nums2)
        for _ in range(total_nums // 2):
            if nums1 and nums2:
                n1 = nums1.pop()
                n2 = nums2.pop()
                if n1 >= n2:
                    tophalf.append(n1)
                    nums2.append(n2)
                else:
                    tophalf.append(n2)
                    nums1.append(n1)
            elif nums1:
                n1 = nums1.pop()
                tophalf.append(n1)
            elif nums2:
                n2 = nums2.pop()
                tophalf.append(n2)
            else:
                raise ValueError("Shouldnt ever reach this line.")
        if total_nums % 2 == 0:
            nearest_right = tophalf[-1]
            if nums1 and nums2:
                n1 = nums1.pop()
                n2 = nums2.pop()
                if n1 >= n2:
                    nearest_left = n1
                else:
                    nearest_left = n2
            elif nums1:
                nearest_left = nums1.pop()
            elif nums2:
                nearest_left = nums2.pop()
            else:
                raise ValueError("Shouldnt ever reach this line.")
            return (nearest_left + nearest_right) / 2
        else:
            if nums1 and nums2:
                n1 = nums1.pop()
                n2 = nums2.pop()
                if n1 >= n2:
                    center = n1
                else:
                    center = n2
            elif nums1:
                center = nums1.pop()
            elif nums2:
                center = nums2.pop()
            return float(center)
