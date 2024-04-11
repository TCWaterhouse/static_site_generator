class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("Child classes should override this method to render themselves as HTML")
    
    def props_to_html(self):
        if self.props is None:
            return ""
        else:
            attributes = ""
            for k, v in self.props.items():
                attributes += f' {k}="{v}"'
            return attributes
        
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        if value is None:
            raise ValueError("Leaf Node requires a value")
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"