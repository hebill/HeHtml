class Document:
    def __init__(self):
        self. elements = {}
        self._create = None
        import HeHtml.Tags
        self.html_root = HeHtml.Tags.html(self)
        self.output_break = True
        self.output_retraction = "	"
        self.output_next_breakable = True

    def create(self):
        if self._create is None:
            self._create = _create(self)
        return self._create

    def HtmlRoot(self):
        return self.html_root

    def output(self):
        s = ""
        return self.HtmlRoot().output()


# 创建节点
class _create_nodes:
    def __init__(self, senior):
        self.senior = senior

    def Group(self):
        from HeHtml.Nodes import Group
        return Group(self.senior)

    def Text(self, content: str = None):
        from HeHtml.Nodes import Text
        return Text(self.senior, content)

    def Code(self, source: str = None):
        from HeHtml.Nodes import Code
        return Code(self.senior, source)

    def Comment(self, comment: str = None):
        from HeHtml.Nodes import Comment
        return Comment(self.senior, comment)

    def Tag(self, name: str, content: str = None):
        from HeHtml.Nodes import Tag
        return Tag(self.senior, name, content)


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

    def link(self, url: str = None):
        from HeHtml.Tags import link
        return link(self.senior, url)

    def span(self, content: str = None):
        from HeHtml.Tags import span
        return span(self.senior, content)

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
