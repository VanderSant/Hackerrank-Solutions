# Complete the mergeLists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def mergeLists(head1, head2):
    li3 = SinglyLinkedList()
    while(head1 or head2):
        if(head1 and head2):
            if(head1.data<=head2.data):
                li3.insert_node(head1.data)
                head1 = head1.next
            else:
                li3.insert_node(head2.data)
                head2 = head2.next        
        elif(head1):
            li3.insert_node(head1.data)
            head1 = head1.next
        else:
            li3.insert_node(head2.data)
            head2 = head2.next
    return li3.head 