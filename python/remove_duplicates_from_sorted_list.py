class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        ptr = head
        while ptr is not None and ptr.next is not None:
            if ptr.val == ptr.next.val:
                ptr.next = ptr.next.next
            else:
                ptr = ptr.next
        return head