from typing import List


class Solution:
    def deflate(self, nums: List[int]) -> List[int]:
        dict_ = dict()
        deflated = list()
        for num in nums:
            if num not in dict_:
                deflated.append(num)
                dict_[num] = 1
            else:
                if dict_[num] == 1:
                    deflated.append(num)
                if dict_[num] == 2 and num == 0:
                    deflated.append(num)
                dict_[num] += 1
        return deflated

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = self.deflate(nums)
        dict_ = dict()
        for i, num in enumerate(nums):
            if num not in dict_:
                dict_[num] = list()
            dict_[num].append(i)

        triples = set()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                ni = nums[i]
                nj = nums[j]
                key = -(ni + nj)
                ks = dict_[key] if key in dict_ else list()
                for k in ks:
                    if k != i and k != j:
                        triple = tuple(sorted([ni, nj, -(ni + nj)]))
                        triples.add(triple)

        return [list(tuple_) for tuple_ in triples]
