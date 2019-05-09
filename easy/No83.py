# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # 题意: 给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。
        # 思路: 记录当前值, 如果next的值与当前值相同, p.next=p.next.next, 不同则遍历到p.next, 并重新记录当前值
        if not head:
            return
        p = head
        now = head.val
        while p.next:
            if p.next.val == now:
                p.next = p.next.next
            else:
                p = p.next
                now = p.val
        return head