class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("HTMLNode: Doesn't Have Feature!!")

    def props_to_html(self):
        if not self.props:
            return ""
        return " ".join(f'{key}="{value}"' for key, value in self.props.items())

    def __repr__(self):
        return f'HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})'


class LeafNode(HTMLNode):
    # Tags that are self-closing and don't need values
    SELF_CLOSING_TAGS = {"img", "br", "hr", "input", "meta", "link"}

    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self):
        if not self.value and self.tag not in self.SELF_CLOSING_TAGS:
            raise ValueError("LeafNode: Missing Value!!")
        if not self.tag:
            return self.value
        
        props_to_html = self.props_to_html()
        props_str = f" {props_to_html}" if props_to_html else ""
        
        # Handle self-closing tags
        if self.tag in self.SELF_CLOSING_TAGS:
            return f"<{self.tag}{props_str}/>"
        
        # Handle regular tags
        return f"<{self.tag}{props_str}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f'LeafNode({self.tag}, {self.value}, {self.children}, {self.props})'



class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):
        if not self.tag:
            raise ValueError("ParentNode: Missing Tag!!")
        if not self.children:
            raise ValueError("ParentNode: Missing Children!!")
        child_convert = [child.to_html() for child in self.children]
        props_to_html = self.props_to_html()
        
        if props_to_html:
            return f"<{self.tag} {props_to_html}>{''.join(child_convert)}</{self.tag}>"
        return f"<{self.tag}>{''.join(child_convert)}</{self.tag}>"

    def __repr__(self):
        return f'ParentNode({self.tag}, {self.value}, {self.children}, {self.props})'