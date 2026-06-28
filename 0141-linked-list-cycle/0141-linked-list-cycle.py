# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
1 → 2 → 3 → 4
    ↑       |
    └───────┘
(4 points back to 2)
Step 0: slow=1, fast=1
Step 1: slow=2, fast=3   (slow: 1→2, fast: 1→2→3)
Step 2: slow=3, fast=2   (slow: 2→3, fast: 3→4→2)
Step 3: slow=4, fast=4   (slow: 3→4, fast: 2→3→4)
                          ↑ MEET!

'''
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # has cycle if there's a backedge
        fast, slow = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            # cycle detected
            if slow == fast:
                return True
        # they never meet, fast goes to the end of the LL
        return False

        