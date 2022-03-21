from three_sum import Solution


def test_soln():
    soln = Solution()
    assert sorted(soln.threeSum(nums=[-1, 0, 1, 2, -1, -4])) == [[-1,-1,2],[-1,0,1]]
    assert sorted(soln.threeSum(nums=[])) == []
    assert sorted(soln.threeSum(nums=[0])) == []
