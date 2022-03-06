from add_two_numbers import ListNode, list2ll, ll2list, list2int, int2list, Solution


def test_listnode():
    ll = ListNode(val=0, next=None)
    assert ll.val == 0
    assert ll.next is None
    next = ListNode(val=1, next=None)
    ll.next = next
    assert ll.next.val == next.val


def test_list2ll():
    list_ = [1, 2, 3]
    ll = list2ll(list_)
    assert ll.val == 1
    assert ll.next.val == 2
    assert ll.next.next.val == 3


def test_ll2list():
    ll = ListNode(val=1, next=ListNode(val=2, next=ListNode(val=3, next=None)))
    list_ = ll2list(ll)
    assert list_ == [1, 2, 3]


def test_list2int():
    list_ = [1, 2, 3]
    assert list2int(list_) == 123


def test_int2list():
    int_ = 123
    assert int2list(int_) == [1, 2, 3]


def test_soln():
    soln = Solution()
    a, b = 342, 465
    result = soln.addTwoNumbers(
        l1=list2ll(int2list(a)[::-1]), l2=list2ll(int2list(b)[::-1])
    )
    actual = list2int(ll2list(result)[::-1])
    expected = a + b
    print(actual)
    print(expected)
    assert actual == expected

    a, b = 9999999, 9999
    result = soln.addTwoNumbers(
        l1=list2ll(int2list(a)[::-1]), l2=list2ll(int2list(b)[::-1])
    )
    print(result)
    actual = list2int(ll2list(result)[::-1])
    expected = a + b
    print(actual)
    print(expected)
    assert actual == expected
