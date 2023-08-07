class Parent:
    def __init__(self, child):
        self.val = 'This is from the parent'
        self.child = child(self)


class Child:
    def __init__(self, parent):
        self.parent = parent

parent = Parent(Child)

print(parent.child.parent.val)