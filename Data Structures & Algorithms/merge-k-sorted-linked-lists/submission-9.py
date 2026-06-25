# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeLList(ll1, ll2):
            dummy = ListNode(0)
            curr = dummy
            while ll1 is not None and ll2 is not None:
                if ll1.val <= ll2.val:
                    curr.next = ll1
                    ll1 = ll1.next
                else:
                    curr.next = ll2
                    ll2 = ll2.next
                curr = curr.next

            if ll1:
                curr.next = ll1
            else:
                curr.next = ll2

            return dummy.next

        s = 0
        k = len(lists)
        e = k - 1

        def divide(lists, s, e):
            if not lists:
                return None
            m = (e + s) // 2

            if s==e:
                return lists[s]
            
            ll1 = divide(lists, s, m)
            ll2 = divide(lists, m+1, e)

            return mergeLList(ll1, ll2)

        return divide(lists, s, e)