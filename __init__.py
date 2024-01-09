class Document:
    import HeHtml.Tags
    html: HeHtml.Tags.html

    def __init__(self):
        self. elements = {}
        self._create = None
        self.title = ""
        import HeHtml.Tags
        self.html = HeHtml.Tags.html(self)
        self.html.head = self.html.create().Tag().head()
        self.html.head.title = self.html.head.create().Tag().title()
        self.html.body = self.html.create().Tag().body()

    def create(self):
        if self._create is None:
            self._create = _create(self)
        return self._create

    def output(self):
        return self.html.output()


# 创建节点
class _create_nodes:
    def __init__(self, senior):
        self.senior = senior

    def Group(self):
        from HeHtml.Nodes import Group
        return Group(self.senior)

    def Tag(self, name: str):
        from HeHtml.Nodes import Tag
        return Tag(self.senior, name)


# 创建节点标签
class _create_tags:
    def __init__(self, senior):
        self.senior = senior

    def body(self):
        from HeHtml.Tags import body
        return body(self.senior)

    def html(self):
        from HeHtml.Tags import html
        return html(self.senior)

    def head(self):
        from HeHtml.Tags import head
        return head(self.senior)

    def span(self):
        from HeHtml.Tags import span
        return span(self.senior)

    def title(self):
        from HeHtml.Tags import title
        return title(self.senior)


# 创建
class _create:
    def __init__(self, senior):
        self._create_nodes = _create_nodes(senior)
        self._create_tags = _create_tags(senior)

    def Node(self):
        return self._create_nodes

    def Tag(self):
        return self._create_tags
