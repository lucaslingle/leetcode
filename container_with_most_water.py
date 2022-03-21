# algo:
# sort heights in ascending order.
# associate the original indices to each height.
# know that for each item in the sorted array,
#    the best area it can give, using itself as the smaller height,
#    is given by its height, times width using max or min of all indices of items to the right.
#
# time complexity: O(nlogn) to sort, linear to pool -> O(nlogn).

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        sorted_ = sorted(enumerate(height), key=lambda x: x[1])
        tail_idx_mins, tail_idx_min = [], float('inf')
        tail_idx_maxs, tail_idx_max = [], float('-inf')
        for i, height in reversed(sorted_):
            tail_idx_min = min(tail_idx_min, i)
            tail_idx_max = max(tail_idx_max, i)
            tail_idx_mins.append(tail_idx_min)
            tail_idx_maxs.append(tail_idx_max)
        tail_idx_mins.reverse()
        tail_idx_maxs.reverse()
        zipped = zip(sorted_, tail_idx_mins, tail_idx_maxs)
        max_area = 0
        for (original_idx, shorter_height), tail_idx_min, tail_idx_max in zipped:
            w1 = original_idx - tail_idx_min
            w2 = tail_idx_max - original_idx
            area = shorter_height * max(w1, w2)
            max_area = max(max_area, area)
        return max_area
