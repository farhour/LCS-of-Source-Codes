class STree:
    """Class representing the Suffix Tree."""

    def __init__(self, input_list=''):
        self.root = _SNode()
        self.root.depth = 0
        self.root.idx = 0
        self.root.parent = self.root
        self.root.add_suffix_link(self.root)
        self._build_generalized(input_list)

    def _build(self, x):
        """Builds a Suffix Tree."""
        self.word = x
        self._build_mcc(x)

    def _build_mcc(self, x):
        """Builds a Suffix Tree using McCreight O(n) algorithm.

        Algorithm based on:
        McCreight, Edward M. "A space-economical suffix tree construction algorithm." - ACM, 1976.
        Implementation based on:
        UH CS - 58093 String Processing Algorithms Lecture Notes
        """
        u = self.root
        d = 0
        for i in range(len(x)):
            while u.depth == d and u._has_transition(x[d + i]):
                u = u.get_transition_link(x[d + i])
                d = d + 1
                while d < u.depth and x[u.idx + d] == x[i + d]:
                    d = d + 1
            if d < u.depth:
                u = self._create_node(x, u, d)
            self._create_leaf(x, i, u, d)
            if not u.get_suffix_link():
                self._compute_slink(x, u)
            u = u.get_suffix_link()
            d = d - 1
            if d < 0:
                d = 0

    def _compute_slink(self, x, u):
        d = u.depth
        v = u.parent.get_suffix_link()
        while v.depth < d - 1:
            v = v.get_transition_link(x[u.idx + v.depth + 1])
        if v.depth > d - 1:
            v = self._create_node(x, v, d - 1)
        u.add_suffix_link(v)

    def _build_generalized(self, xs):
        """Builds a Generalized Suffix Tree (GST) from the array of tokens provided.
        """
        terminal_gen = self.__terminal_symbols_generator()
        _xs = ''
        k = list()
        for x in xs:
            gen = next(terminal_gen)
            for ch in x:
                k.append(ch)
                _xs += ch
            _xs += gen
            k.append(gen)
        self.word = k
        self._generalized_word_starts(xs)
        self._build(k)
        self.root.traverse(self._label_generalized)

    def _label_generalized(self, node):
        """Helper method that labels the nodes of GST with indexes of strings
        found in their descendants.
        """
        if node.is_leaf():
            x = {self._get_word_start_index(node.idx)}
        else:
            x = {n for ns in node.transition_links for n in ns[0].generalized_idxs}
        node.generalized_idxs = x

    def _get_word_start_index(self, idx):
        """Helper method that returns the index of the string based on node's
        starting index"""
        i = 0
        for _idx in self.word_starts[1:]:
            if idx < _idx:
                return i
            else:
                i += 1
        return i

    def lcs(self, string_idxs=-1):
        """Returns the Largest Common Substring of Strings provided in string_idxs.
        If string_idxs is not provided, the LCS of all strings is returned.

        ::param string_idxs: Optional: List of indexes of strings.
        """
        if string_idxs == -1 or not isinstance(string_idxs, list):
            string_idxs = set(range(len(self.word_starts)))
        else:
            string_idxs = set(string_idxs)

        return self._find_lcs(self.root, string_idxs)

    def _find_deepest_node(self, node, string_idxs):
        """Helper method that finds the deepest node by traversing the labeled GSD."""
        nodes = [self._find_deepest_node(n, string_idxs)
                 for (n, _) in node.transition_links
                 if n.generalized_idxs.issuperset(string_idxs)]

        if len(nodes) == 0:
            return node
        deepest_node = max(nodes, key=lambda n: n.depth)
        return deepest_node

    def _find_lcs(self, node, string_idxs):
        """Helper method that finds LCS by traversing the labeled GSD."""
        lcs_list = list()
        nodes = [self._find_deepest_node(n, string_idxs)
                 for (n, _) in node.transition_links
                 if n.generalized_idxs.issuperset(string_idxs)]
        if len(nodes) == 0:
            return node
        deepest_node = max(nodes, key=lambda n: n.depth)
        deep = deepest_node.depth
        for node in nodes:
            if node.depth == deep:
                start = node.idx
                end = node.idx + node.depth
                # print(self.word[start:end])
                lcs_list.append(self.word[start:end])
        return lcs_list

    def _generalized_word_starts(self, xs):
        """Helper method returns the starting indexes of strings in GST"""
        self.word_starts = []
        i = 0
        for n in range(len(xs)):
            self.word_starts.append(i)
            i += len(xs[n]) + 1

    def find(self, y):
        """Returns starting position of the substring y in the string used for
        building the Suffix tree.

        :param y: String
        :return: Index of the starting position of string y in the string used for building the Suffix tree
                 -1 if y is not a substring.
        """
        node = self.root
        while True:
            edge = self._edge_label(node, node.parent)
            edge_string = ''.join(edge)
            y_string = ''.join(y)
            if edge_string.startswith(y_string):
                return node.idx

            i = 0
            while i < len(edge) and edge[i] == y[0]:
                y = y[1:]
                i += 1

            if i != 0:
                if i == len(edge) and y != '':
                    pass
                else:
                    return -1

            node = node.get_transition_link(y[0])
            if not node:
                return -1

    def find_all(self, y):
        node = self.root
        while True:
            edge = self._edge_label(node, node.parent)
            edge_string = ''.join(edge)
            y_string = ''.join(y)
            if edge_string.startswith(y_string):
                break

            i = 0
            while i < len(edge) and edge[i] == y[0]:
                y = y[1:]
                i += 1

            if i != 0:
                if i == len(edge) and y != '':
                    pass
                else:
                    return []

            node = node.get_transition_link(y[0])
            if not node:
                return []

        leaves = node.get_leaves()
        return [n.idx for n in leaves]

    def _edge_label(self, node, parent):
        """Helper method, returns the edge label between a node and it's parent"""
        return self.word[node.idx + parent.depth: node.idx + node.depth]

    @staticmethod
    def __terminal_symbols_generator():
        """Generator of unique terminal symbols used for building the Generalized Suffix Tree.
        Unicode Private Use Area U+E000..U+F8FF is used to ensure that terminal symbols
        are not part of the input string.
        """
        markers = list(
            list(range(0xE000, 0xF8FF + 1)) + list(range(0xF0000, 0xFFFFD + 1)) + list(range(0x100000, 0x10FFFD + 1)))
        for i in markers:
            yield (chr(i))
        raise ValueError("To many input strings.")

    @staticmethod
    def _create_node(x, u, d):
        i = u.idx
        p = u.parent
        v = _SNode(idx=i, depth=d)
        v.add_transition_link(u, x[i + d])
        u.parent = v
        p.add_transition_link(v, x[i + p.depth])
        v.parent = p
        return v

    @staticmethod
    def _create_leaf(x, i, u, d):
        w = _SNode()
        w.idx = i
        w.depth = len(x) - i
        u.add_transition_link(w, x[i + d])
        w.parent = u
        return w


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
