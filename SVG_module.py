"""A module used to generate svg art"""

from typing import List, Tuple
from HTML_module import HTMLDocument

class SvgCanvas:
    """A class to represent an SVG canvas."""

    def __init__(self, html_doc: HTMLDocument, indent: int, canvas: Tuple[int, int]) -> None:
        """
        Purpose: Initializes an SVG canvas.
        Parameters: html_doc (HTMLDocument) - The HTML document object.
                    indent (int)             - The number of tabs used to indent HTML tags.
                    canvas (Tuple[int, int]) - The dimensions of the SVG canvas (width, height).
        Returns: None
        """
        self.html_doc: HTMLDocument = html_doc
        self.indent: int = indent
        self.width: int = canvas[0]
        self.height: int = canvas[1]
        self.shapes: List[str] = []

    def add_shape(self, shape: str) -> None:
        """
        Purpose: Adds a shape to the SVG canvas.
        Parameters: shape (str) - The SVG tag for the shape to be added.
        Returns: None
        """
        self.shapes.append(shape)

    def gen_art(self) -> None:
        """
        Purpose: Generates the SVG canvas and adds the shapes.
        Parameters: None
        Returns: None
        """
        self.html_doc.add_body_content(self.indent, f'<svg width={self.width} height={self.height} style="display: block; margin: 0 auto;">')
        self.__add_shapes_to_HTML()
        self.html_doc.add_body_content(self.indent, "</svg>")
    
    def __add_shapes_to_HTML(self) -> None:
        """
        Purpose: Adds the shapes to the HTML body.
        Parameters: None
        Returns: None
        """
        for shape in self.shapes:
            self.html_doc.add_body_content(self.indent + 1, shape)