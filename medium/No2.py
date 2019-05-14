# Definition for singly-linked list.
class ListNode:
  def __init__(self, x):
      self.val = x
      self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode)-> ListNode:
        # 题意: 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
        #      如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
        # 限制: 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
        # 思路: 模拟, 根据题意, 先用新链表把l1与l2加起来, 然后考虑进位
        #       注意最后一位进位不为空时, 要接一个值为进位数的新节点
        res = ListNode(0)
        p = res
        while l1 and l2:
            p.next = ListNode(l1.val+l2.val)
            p = p.next
            l1 = l1.next
            l2 = l2.next
        p.next = l2 if l2 else l1
        p = res.next
        tmp = 0
        while p.next:
            p.val, tmp = (p.val+tmp) % 10, (p.val+tmp)//10
            p = p.next
        p.val, tmp = (p.val + tmp) % 10, (p.val + tmp) // 10
        if tmp != 0:
            p.next = ListNode(tmp)
        return res.next