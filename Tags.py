import HeHtml.Nodes


class a(HeHtml.Nodes.Tag):
    def __init__(self, senior):
        super().__init__(senior)


class body(HeHtml.Nodes.Tag):
    def __init__(self, senior):
        super().__init__(senior)


class head(HeHtml.Nodes.Tag):
    def __init__(self, senior):
        super().__init__(senior)


class html(HeHtml.Nodes.Tag):
    def __init__(self, senior):
        super().__init__(senior)


class span(HeHtml.Nodes.Tag):
    output_break_inner = False

    def __init__(self, senior):
        super().__init__(senior)


class title(HeHtml.Nodes.Tag):
    output_break_inner = False

    def __init__(self, senior):
        super().__init__(senior)
