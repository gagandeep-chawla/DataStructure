import random

#Stack implementation
class Stack:

    def __init__(self):
        self.items = []

    def __len__(self):
        return len(self.items)

    def __getitem__(self, pos):
        print(self.items[pos])

    def insert(self, data):
        self.items.append(data)

    def pop(self, pos=None):
        if pos is None:
            self.items.pop()
            return
        self.items.pop(pos)
        return

    def lists(self):
        print(self.items)

    def reverse(self):
        self.items = self.items[::-1]

def main():
    st = Stack()
    for i in range(10):
        st.insert(random.randint(1, 10))
    st.lists()
    st.pop()
    st.lists()
    st.pop(1)
    st.lists()
    st[1]
    st.reverse()
    st.lists()
    print(len(st))

if __name__ == "__main__":
    main()    