from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"ListNode(val={self.val}, next={self.next.__repr__()}"


def list2ll(list_: List[int]) -> ListNode:
    result = None
    tail = None
    for val in list_:
        node = ListNode(val=val, next=None)
        if result is None:
            result = node
        else:
            tail.next = node
        tail = node
    return result


def ll2list(ll: ListNode) -> List[int]:
    result = []
    while ll:
        result.append(ll.val)
        ll = ll.next
    return result


def list2int(list_: List[int]) -> int:
    result = 0
    for i, val in enumerate(reversed(list_)):
        result += val * (10 ** i)
    return result


def int2list(int_: int) -> List[int]:
    result = []
    while int_ > 0:
        digit = int_ % 10
        result.append(digit)
        int_ = int_ // 10
    return result[::-1]


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        result = None
        tail = None
        carry = 0
        while l1 or l2 or carry:
            if l1 and l2:
                sum_ = l1.val + l2.val + carry
                digit = sum_ % 10
                node = ListNode(val=digit, next=None)
                carry = sum_ // 10
            elif l1:
                sum_ = l1.val + carry
                digit = sum_ % 10
                node = ListNode(val=digit, next=None)
                carry = sum_ // 10
            elif l2:
                sum_ = l2.val + carry
                digit = sum_ % 10
                node = ListNode(val=digit, next=None)
                carry = sum_ // 10
            elif carry:
                sum_ = carry
                digit = sum_ % 10
                node = ListNode(val=digit, next=None)
                carry = sum_ // 10
            if not result:
                result = node
            else:
                tail.next = node
            tail = node
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return result
