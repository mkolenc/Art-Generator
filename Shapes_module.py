"""A module containing different geometric shapes"""

from typing import List, Tuple

class CircleShape:
    """A class representing a circle shape."""

    def __init__(self, circle: Tuple[int, int, int], colour: Tuple[int, int, int, int]) -> None:
        """
        Purpose: Initialize CircleShape class.
        Parameters: circle - A tuple of (cx, cy, radius), where cx and cy are the coordinates of the center of the circle, 
                             and radius is the radius of the circle.
                    colour - A tuple of (r, g, b, alpha), where r, g, and b are the red, green, and blue color channels (0-255), 
                             and alpha is the transparency (0-1) of the circle.
        Returns: None
        """
        self.cx: int = circle[0]
        self.cy: int = circle[1]
        self.radius: int = circle[2]
        self.colour: Tuple[int, int, int, int] = colour

    def draw(self) -> str:
        """
        Purpose: Draw a circle using SVG syntax.
        Parameters: None
        Returns: A string containing the SVG code for drawing the circle.
        """
        return f'<circle cx="{self.cx}" cy="{self.cy}" r="{self.radius}" fill="rgba{self.colour}"></circle>'


class RectangleShape:
    """A class representing a rectangle shape."""

    def __init__(self, rect: Tuple[int, int, int, int], colour: Tuple[int, int, int, int]) -> None:
        """
        Purpose: Initialize RectangleShape class.
        Parameters: rect   - A tuple of (x, y, width, height), where x and y are the coordinates of the top-left corner of the rectangle, and width and height are the dimensions of the rectangle.
                    colour - A tuple of (r, g, b, alpha), where r, g, and b are the red, green, and blue color channels (0-255), and alpha is the transparency (0-1) of the rectangle.
        Returns: None
        """
        self.x: int = rect[0]
        self.y: int = rect[1]
        self.width: int = rect[2]
        self.height: int = rect[3]
        self.colour: Tuple[int, int, int, int] = colour

    def draw(self) -> str:
        """
        Purpose: Draw a rectangle using SVG syntax.
        Parameters: None
        Returns: A string containing the SVG code for drawing the rectangle.
        """
        return f'<rect x="{self.x}" y="{self.y}" width="{self.width}" height="{self.height}" fill="rgba{self.colour}"/>'


class EllipseShape:
    """A class representing an ellipse shape."""

    def __init__(self, ellipse: Tuple[int, int, int, int], colour: Tuple[int, int, int, int]) -> None:
        """
        Purpose: Initialize EllipseShape class.
        Parameters: ellipse - A tuple of (cx, cy, rx, ry), where cx and cy are the coordinates of the center of the ellipse, 
                              and rx and ry are the radii of the ellipse in the x and y directions.
                    colour  - Atuple of (r, g, b, alpha), where r, g, and b are the red, green, and blue color channels (0-255), 
                              and alpha is the transparency (0-1) of the ellipse.
        Returns: None
        """
        self.x: int = ellipse[0]
        self.y: int = ellipse[1]
        self.rx: int = ellipse[2]
        self.ry: int = ellipse[3]
        self.colour: Tuple[int, int, int, int] = colour
    
    def draw(self) -> str:
        """
        Purpose: Draw a rectangle using SVG syntax.
        Parameters: None
        Returns: A string containing the SVG code for drawing the rectangle.
        """
        return f'<ellipse cx="{self.x}" cy="{self.y}" rx="{self.rx}" ry="{self.ry}" fill="rgba{self.colour}"/>'