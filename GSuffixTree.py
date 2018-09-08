class _SNode:
    """Class representing a Node in the Suffix tree."""

    def __init__(self, idx=-1, parent_node=None, depth=-1):
        # Links
        self._suffix_link = None
        self.transition_links = []
        # Properties
        self.idx = idx
        self.depth = depth
        self.parent = parent_node
        self.generalized_idxs = {}

    def __str__(self):
        return ("SNode: idx:" + str(self.idx) + " depth:" + str(self.depth) +
                " transitions:" + str(self.transition_links))

    def add_suffix_link(self, s_node):
        self._suffix_link = s_node

    def get_suffix_link(self):
        if self._suffix_link is not None:
            return self._suffix_link
        else:
            return False

    def get_transition_link(self, suffix):
        for node, _suffix in self.transition_links:
            if _suffix == '__@__' or suffix == _suffix:
                return node
        return False

    def add_transition_link(self, s_node, suffix=''):
        tl = self.get_transition_link(suffix)
        if tl:
            self.transition_links.remove((tl, suffix))
        self.transition_links.append((s_node, suffix))

    def _has_transition(self, suffix):
        for node, _suffix in self.transition_links:
            if _suffix == '__@__' or suffix == _suffix:
                return True
        return False

    def is_leaf(self):
        return self.transition_links == []

    def traverse(self, f):
        for (node, _) in self.transition_links:
            node.traverse(f)
        f(self)

    def get_leaves(self):
        if self.is_leaf():
            return [self]
        else:
            return [x for (n, _) in self.transition_links for x in n.get_leaves()]
