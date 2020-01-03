class Node(object):   
    def __init__(self, name, parent=None, checked=False):

        self._name = name
        self._children = []
        self._parent = parent
        self._checked = checked

        if parent is not None:
            parent.addChild(self)

    def addChild(self, child):
        self._children.append(child)

    def insertChild(self, position, child):
        if position < 0 or position > len(self._children):
            return False

        self._children.insert(position, child)
        child._parent = self
        return True

    def name(self):
        return self._name

    def checked(self):
        return self._checked

    def setChecked(self, state):
        self._checked = state

        for c in self._children:
            c.setChecked(state)

    def child(self, row):
        return self._children[row]

    def childCount(self):
        return len(self._children)

    def parent(self):
        return self._parent

    def row(self):
        if self._parent is not None:
            return self._parent._children.index(self)

    def get_child(self, child_name):
        for child in self._children:
            if child.name() == child_name:
                return child
        return None

