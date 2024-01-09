from typing import Union

import HeHtml.Nodes


class a(HeHtml.Nodes.Tag):
    output_break_inner = False

    def __init__(self, senior):
        super().__init__(senior)


class body(HeHtml.Nodes.Tag):
    def __init__(self, senior):
        super().__init__(senior)


class head(HeHtml.Nodes.Tag):
    def __init__(self, senior):
        super().__init__(senior)
        self.child_title: Union['title', None] = None
        self.reserved_group_for_metas = self.create().Node().Group()
        self.reserved_group_for_libraries = self.create().Node().Group()
        self.reserved_group_for_child_title = self.create().Node().Group()

    def ChildTitle(self) -> 'title':
        if self.child_title is None:
            self.child_title = self.reserved_group_for_child_title.create().Tag().title()
        return self.child_title

    def addLibraryFile(self, url: str = None):
        e = self.create().Tag().link(url)
        if e is not None:
            pass


class html(HeHtml.Nodes.Tag):
    def __init__(self, senior):
        super().__init__(senior)
        self.reserved_group_for_child_head = self.create().Node().Group()
        self.child_body: Union['body', None] = None
        self.child_head: Union['head', None] = None

    def ChildHead(self) -> head:
        if self.child_head is None:
            self.child_head = self.reserved_group_for_child_head.create().Tag().head()
        return self.child_head

    def ChildBody(self) -> body:
        if self.child_body is None:
            self.child_body = self.create().Tag().body()
        return self.child_body


class link(HeHtml.Nodes.Tag):
    def __init__(self, senior, url: str = None):
        super().__init__(senior)
        self.url = url


class span(HeHtml.Nodes.Tag):
    def __init__(self, senior, content: str = None):
        super().__init__(senior, None, content)
        self.output_break_inner = False


class title(HeHtml.Nodes.Tag):
    def __init__(self, senior):
        super().__init__(senior)
        self.output_break_inner = False
