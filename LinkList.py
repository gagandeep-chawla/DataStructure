class Node:

    def __init__(self, data):
        self.next = None
        self.data = data


class LinkedList:

    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        old_node = self.head
        while old_node.next:
            old_node = old_node.next
        old_node.next = new_node

    def prepand(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        pre_node = self.head
        self.head = new_node
        self.head.next = pre_node
    
        
    def insert_between_node(self,old_node,new_node):
        new_node = Node(new_node)
        node = self.head
        while True:
            if node.next.data == old_node:
                new_node.next = node.next
                node.next = new_node
                break
            elif node.next is None:
                break
            else:
                node = node.next

    def print_list(self):
        llist = self.head
        while llist:
            print(llist.data)
            if llist.next is None:
                break
            llist = llist.next

    def delete_node(self, node):
        cur_node = self.head
        if self.head and self.head.data == node:
            self.head = cur_node.next
            cur_node = None
        while True:
            try:
                if cur_node.next == None:
                    break
                elif cur_node.next.data == node:
                    cur_node.next = cur_node.next.next
                    break
                else:
                    cur_node = cur_node.next
            except AttributeError:
                break
        return

def main():
    ll = LinkedList()
    ll.append('a')
    ll.print_list()
    ll.prepand('b')
    ll.print_list()
    ll.append('c')
    ll.print_list()
    ll.append('e')
    ll.print_list()
    ll.insert_between_node('a', 'd')
    ll.print_list()
    ll.insert_between_node('d', 'g')
    ll.print_list()
    ll.append('f')
    ll.print_list()
    ll.delete_node('f')
    ll.print_list()
    
if __name__ == "__main__":
    main()
