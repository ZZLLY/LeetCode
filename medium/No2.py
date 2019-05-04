# Definition for singly-linked list.
class ListNode:
  def __init__(self, x):
      self.val = x
      self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode)-> ListNode:
        p1 = l1
        p2 = l2
        tmp = 0
        while p1.next and p2.next:
            num = p1.val
            p1.val = (p1.val+p2.val+tmp)%10
            tmp = (num + p2.val) // 10
            p1 = p1.next
            p2 = p2.next
        if not p1 and not p2:
            if tmp != 0:
                p1 = ListNode(tmp)
        elif p2:
            p1 = ListNode(tmp)
            p2.val += tmp
            p1.val = p2.val
            p1.next = p2.next
        return l1