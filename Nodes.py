class Node:
    document = None
    parent = None
    output_break = True

    def __init__(self, senior):
        self.id = id(self)
        from HeHtml import Document
        if isinstance(senior, Group):
            self.document = senior.document
            self.document.elements[self.id] = self
            self.parent = senior
            self.parent.children[self.id] = self
        if isinstance(senior, Document):
            self.document = senior
            self.document.elements[self.id] = self
            self.parent = None

    def output(self) -> str:
        return ""

    def level(self) -> int:
        if self.parent is None:
            return 0
        return self.parent.level() + 1


class Group(Node):
    output_break = False

    def __init__(self, senior):
        super().__init__(senior)
        self.children = {}
        self._create = None

    def create(self):
        if self._create is None:
            from HeHtml import _create
            self._create = _create(self)
        return self._create

    def output(self):
        s = ""
        if len(self.children) > 0:
            for key, value in self.children.items():
                if isinstance(value, Node):
                    s += value.output()
        return s


class Text(Node):
    output_break = False

    def __init__(self, senior, content: str = ""):
        super().__init__(senior)
        self.content = content

    def output(self):
        import html
        return f"{html.escape(self.content)}"


class Code(Node):

    output_break = False

    def __init__(self, senior, source: str = ""):
        super().__init__(senior)
        self.source = source

    def output(self):
        return f"{self.source}"


class Comment(Node):
    def __init__(self, senior, comment: str = ""):
        super().__init__(senior)
        self.comment = comment

    def output(self):
        import html
        return f"<!--[{html.escape(self.comment)}]-->"


class Tag(Group):
    name: str
    output_break_inner = True

    def __init__(self, senior, name: str = None, content: str = None):
        super().__init__(senior)
        self.name = name if name is not None else self.__class__.__name__
        if content is not None:
            pass

    def output(self):
        s = ""
        if self.output_break:
            if self.level() != 0:
                s += "\n"
            s += "	" * self.level()
        s += "<" + self.name
        s += ">"
        s += super().output()
        if self.output_break_inner:
            s += "\n" + "	" * self.level()
        s += "</" + self.name + ">"
        return s
