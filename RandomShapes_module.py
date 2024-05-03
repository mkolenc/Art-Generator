"""A Module used to generate random shape objects"""

from typing import List, Tuple
from ArtConfig_module import PyArtConfig
import random

class RandomShape:
    """Class to define ranges for different parameters of the generated random art."""

    # A class variable to keep tract of the number of shapes generated
    num_shapes: int = 0 

    def __init__(self, config: PyArtConfig) -> None:
        """
        Purpose: Initialize and instance of a RandomShape
        Parameters: config - A PyArtConfig object which will be used to define the random shape
        Returns: None
        """
        self.config = config
        self.shape: int = random.randint(0, len(config.shape_types) - 1)
        self.x: int = random.randint(config.shape_pos_range[0], config.shape_pos_range[1])
        self.y: int = random.randint(config.shape_pos_range[0], config.shape_pos_range[1])
        self.rad: int = random.randint(config.circle_rad_range[0], config.circle_rad_range[1])
        self.rx: int = random.randint(config.ellipse_rad_range[0], config.ellipse_rad_range[1])
        self.ry: int = random.randint(config.ellipse_rad_range[0], config.ellipse_rad_range[1])
        self.width: int = random.randint(config.rect_size_range[0], config.rect_size_range[1])
        self.height: int = random.randint(config.rect_size_range[0], config.rect_size_range[1])
        self.red: int = random.randint(config.shape_color_range[0][0], config.shape_color_range[1][0])
        self.green: int = random.randint(config.shape_color_range[0][1], config.shape_color_range[1][1])
        self.blue: int = random.randint(config.shape_color_range[0][2], config.shape_color_range[1][2])
        self.op: float = round(random.uniform(config.shape_color_range[0][3], config.shape_color_range[1][3]), 1)  # rounds to one decimal place
        RandomShape.num_shapes += 1
    
    @classmethod
    def get_num_shapes(cls) -> int:
        """
        Purpose: Get the number of shapes generated
        Parameters: None
        Returns: The number of shapes
        """
        return cls.num_shapes

    def __str__(self) -> str:
        """
        Purpose: Represent the shape and its attributes across multiple lines
        Parameters: None
        Returns: A string representing the shape object
        """
        if self.shape == 0: # Circle
            return f"Shape: Circle\nPosition: ({self.x}, {self.y})\nRadius: {self.rad}\nColours (rgba): ({self.red}, {self.green}, {self.blue}, {self.op})"

        if self.shape == 1: # Rectangle
            return f"Shape: Rectangle\nPosition: ({self.x}, {self.y})\nWidth: {self.width}\nHeight: {self.height}\nColours (rgba): ({self.red}, {self.green}, {self.blue}, {self.op})"

        if self.shape == 2: # Ellipse
            return f"Shape: Ellipse\nPosition: ({self.x}, {self.y})\nRadiusX: {self.rx}\nRadiusY: {self.ry}\nColours (rgba): ({self.red}, {self.green}, {self.blue}, {self.op})"

    def as_Part2_line(self):
        """
        Purpose: Represent the shape and its attributes on one line, formatted
        Parameters: None
        Returns: A string representing the shape object
        """
        return f"{self.get_num_shapes():>10}{self.shape:>10}{self.x:>10}{self.y:>10}{self.rad:>10}{self.rx:>10}{self.ry:>10}{self.width:>10}{self.height:>10}{self.red:>10}{self.green:>10}{self.blue:>10}{self.op:>10}"


    def as_svg(self) -> str:
        """
        Purpose: Represent the shape object in a displayable svg format
        Parameters: None
        Returns: A string representing the object in svg format
        """
        if self.shape == 0: # Circle
            return f'<circle cx="{self.x}" cy="{self.y}" r="{self.rad}" fill="rgba({self.red}, {self.green}, {self.blue}, {self.op})"/>'

        if self.shape == 1: # Rectangle
            return f'<rect x="{self.x}" y="{self.y}" width="{self.width}" height="{self.height}" fill="rgba({self.red}, {self.green}, {self.blue}, {self.op})"/>'

        if self.shape == 2: # Ellipse
            return f'<ellipse cx="{self.x}" cy="{self.y}" rx="{self.rx}" ry="{self.ry}" fill="rgba({self.red}, {self.green}, {self.blue}, {self.op})"/>'