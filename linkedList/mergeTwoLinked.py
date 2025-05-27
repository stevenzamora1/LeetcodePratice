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
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list1Curr, list2Curr = list1, list2
        pos = ListNode()
        cur = pos
        while list1Curr or list2Curr:
            if list1Curr == None:
                pos.next = list2Curr
                list2Curr = list2Curr.next
                pos = pos.next
            elif list2Curr == None:
                pos.next = list1Curr
                list1Curr = list1Curr.next
                pos = pos.next

            elif list1Curr.val <= list2Curr.val:
                pos.next = list1Curr
                pos = pos.next
                list1Curr = list1Curr.next

            elif list2Curr.val < list1Curr.val:
                pos.next = list2Curr
                pos = pos.next
                list2Curr = list2Curr.next

        return cur.next


linked_list1 = create_linked_list([-9, 3])
linked_list2 = create_linked_list([5, 7])
obj = Solution()
objPrint = obj.mergeTwoLists(linked_list1, linked_list2)

print(print_linked_list(objPrint))
