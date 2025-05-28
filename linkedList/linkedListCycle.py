from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Helper function to create a linked list from a Python list


def create_linked_list(values):

    if not values:
        return None

    head = ListNode(values[0])
    current = head

    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next

    return head

# Helper function to print a linked list


def print_linked_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


class Solution:
    # Soultion 1 O(n) time O(n) space
    # Adds nodes to a set
    def hasCycleSet(self, head: Optional[ListNode]) -> bool:
        seen = set()
        cur = head
        while cur:
            if cur in seen:
                return True
            seen.add(cur)
            cur = cur.next
        return False

    # Soultion 2 O(n) time O(1) space
    # two pointer  tortsite and hare algo
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fp, sp = head, head

        while fp:
            temp = fp.next
            if temp == None:
                return False
            fp = temp.next
            sp = sp.next
            if fp == sp:
                return True

        return False


# Test the solution
obj = Solution()

# Create a linked list from the list
linked_list = create_linked_list([3, 2, 0, -4])

# Print original list
print("Original:", print_linked_list(linked_list))

# Reverse the linked list
linked_list = obj.hasCycle(linked_list)

# Print reversed list
print(print_linked_list(linked_list))
