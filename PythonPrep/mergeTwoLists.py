'''
21. Merge Two Sorted Lists
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list.
The list should be made by splicing together the nodes of the
 first two lists.

Return the head of the merged linked list.

'''

'''
EXAMPLE 1
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
'''


'''
GIVEN: two SORTED linked lists
STEPS:
    edge cases:
        issues that stems from insterting into a empty list
            create a dummy Node
        if lists dont have equal length:
                take the remaining portion from the non-empty list and add it to the end of result list

    create a dummy Node that represents the head of your output list

    while l1 and l1 are not null:
        if the value of the current node in list1 is less than the value of the current node in list2:
            add value of l1 Node to the next node in the node out
                to do this: set the next Node in our outpit list as the value of l1
            move on to the next node in the l1

        else:
            add value of l2 Node to the next node in the node out
             move on to the next node in the l2

        move to the next node in your outputList

    if the are any remainders in any of the given lists
        add them to the output list

    return the dummy.next
        thsi will return the next nodes, one at a time
RETURN: the head of the merged linked list


TIME COMP: O(n)
SPACE COMP: O(n)
'''

class ListNode:
    def __init__(self, val = 0, next=None):
        self.val = val
        self.next = next


def mergeTwoList(l1, l2):
    dummy = ListNode()
    tail = dummy

    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
        else:
            tail.next = l2
            l2 =l2.next

        tail = tail.next

        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2

        return dummy.next

l1 = [1,2,4]
l2 = [1,3,4]
print(mergeTwoList(l1, l2))