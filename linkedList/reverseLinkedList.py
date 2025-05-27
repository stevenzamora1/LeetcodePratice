
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
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev


# Test the solution
obj = Solution()

# Create a linked list from the list [1, 2, 3, 4, 5]
linked_list = create_linked_list([1, 2, 3, 4, 5])

# Print original list
print("Original:", print_linked_list(linked_list))

# Reverse the linked list
reversed_list = obj.reverseList(linked_list)

# Print reversed list
print("Reversed:", print_linked_list(reversed_list))
