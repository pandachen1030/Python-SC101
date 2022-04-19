"""
File: add2.py
Name: Panda
------------------------
TODO: Plus l1 and l2 and return a ListNode
"""

import sys


class ListNode:
    def __init__(self, data=0, pointer=None):
        self.val = data
        self.next = pointer


def add_2_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    """
    :param l1: first ListNode, from header to the end are the ones digit, tens digit...and so on
    :param l2: second ListNode, from header to the end are the ones digit, tens digit...and so on
    :return: ListNode which is made up by la plus l2
    """
    # Convert l1 to a string of numbers
    n1 = 0
    count1 = 0
    cur1 = l1
    while cur1 is not None:
        n1 += cur1.val * (10**count1)
        count1 += 1
        cur1 = cur1.next
    # Convert l2 to a string of numbers
    n2 = 0
    count2 = 0
    cur2 = l2
    while cur2 is not None:
        n2 += cur2.val * (10**count2)
        count2 += 1
        cur2 = cur2.next
    # Calculate l1 plus l2 and covert it to a ListNode
    n3 = n1 + n2
    l3 = None
    if n3 == 0:
        l3 = ListNode(0, None)
        return l3
    else:
        while n3 > 0:
            if l3 is None :
                val = n3 % 10
                l3 = ListNode(val, None)
                cur3 = l3
                n3 //= 10
            else:
                val = n3 % 10
                cur3.next = ListNode(val, None)
                cur3 = cur3.next
                n3 //= 10
    return l3


####### DO NOT EDIT CODE BELOW THIS LINE ########


def traversal(head):
    """
    :param head: ListNode, the first node to a linked list
    -------------------------------------------
    This function prints out the linked list starting with head
    """
    cur = head
    while cur.next is not None:
        print(cur.val, end='->')
        cur = cur.next
    print(cur.val)


def main():
    args = sys.argv[1:]
    if not args:
        print('Error: Please type"python3 add2.py test1"')
    else:
        if args[0] == 'test1':
            l1 = ListNode(2, None)
            l1.next = ListNode(4, None)
            l1.next.next = ListNode(3, None)
            l2 = ListNode(5, None)
            l2.next = ListNode(6, None)
            l2.next.next = ListNode(4, None)
            ans = add_2_numbers(l1, l2)
            print('---------test1---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        elif args[0] == 'test2':
            l1 = ListNode(9, None)
            l1.next = ListNode(9, None)
            l1.next.next = ListNode(9, None)
            l1.next.next.next = ListNode(9, None)
            l1.next.next.next.next = ListNode(9, None)
            l1.next.next.next.next.next = ListNode(9, None)
            l1.next.next.next.next.next.next = ListNode(9, None)
            l2 = ListNode(9, None)
            l2.next = ListNode(9, None)
            l2.next.next = ListNode(9, None)
            l2.next.next.next = ListNode(9, None)
            ans = add_2_numbers(l1, l2)
            print('---------test2---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        elif args[0] == 'test3':
            l1 = ListNode(0, None)
            l2 = ListNode(0, None)
            ans = add_2_numbers(l1, l2)
            print('---------test3---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        else:
            print('Error: Please type"python3 add2.py test1"')


if __name__ == '__main__':
    main()
