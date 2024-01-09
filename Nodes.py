class Node:
    def __init__(self, senior):
        self.id = id(self)
        self.document = None
        self.parent = None
        self.output_breakable = True
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
        if type(self) is Group:
            return self.parent.level()
        return self.parent.level() + 1


class Group(Node):
    def __init__(self, senior):
        super().__init__(senior)
        self.children = {}
        self.output_break = False
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
    def __init__(self, senior, content: str = None):
        super().__init__(senior)
        self.output_break = False
        self.content = content if content is not None else ""

    def output(self):
        import html
        self.document.output_next_breakable = False
        return f"{html.escape(self.content)}"


class Code(Node):
    def __init__(self, senior, source: str = None):
        super().__init__(senior)
        self.output_break = False
        self.source = source if source is not None else ""

    def output(self):
        self.document.output_next_breakable = False
        return f"{self.source}"


class Comment(Node):
    def __init__(self, senior, comment: str = None):
        super().__init__(senior)
        self.comment = comment if comment is not None else ""

    def output(self):
        import html
        s = ""
        if self.document.output_break:
            s += "\n" + self.document.output_retraction * self.level()
        s += f"<!--[{html.escape(self.comment)}]-->"
        self.document.output_next_breakable = True
        return s


class Tag(Group):
    def __init__(self, senior, name: str = None, content: str = None):
        super().__init__(senior)
        self.output_breakable = True
        self.name = name if name is not None else self.__class__.__name__
        if content is not None:
            self.create().Node().Text(content)

    def output(self):
        s = ""
        if self.document.output_break:
            if self.output_breakable and self.document.output_next_breakable:
                if self.level() > 0:
                    s += "\n"
            s += self.document.output_retraction * self.level()
        s += "<" + self.name
        s += ">"
        self.document.output_next_breakable = True
        si = super().output()
        s += si
        if self.document.output_break:
            if si != "" and self.document.output_next_breakable:
                s += "\n" + "	" * self.level()
        s += "</" + self.name + ">"
        self.document.output_next_breakable = True
        return s
