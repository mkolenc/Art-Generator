"""A module defining the configurations for shape-art"""

from typing import List, Tuple

class PyArtConfig:
    """Class to define ranges for different parameters of the generated random art."""
    # go back to here
    # Default ranges for different parameters
    SHAPE_TYPES: List[str] = ["circle", "rectangle", "ellipse"]  # Possible shapes
    SHAPE_POS_RANGE: Tuple[int, int] = (0, 1100)  # Range of shape position
    CIRCLE_RAD_RANGE: Tuple[int, int] = (0, 100)  # Range of circle radius
    ELLIPSE_RAD_RANGE: Tuple[int, int] = (0, 30)  # Range of ellipse radius
    RECT_SIZE_RANGE: Tuple[int, int] = (10, 100)  # Range of shape size
    SHAPE_COLOR_RANGE: Tuple[Tuple[int, int, int, float], Tuple[int, int, int, float]] = ((0, 0, 0, 0.1), (255, 255, 255, 1.0))  # Range of shape color and opacity

    def __init__(
        self,
        shape_types: List[str] = SHAPE_TYPES,
        shape_pos_range: Tuple[int, int] = SHAPE_POS_RANGE,
        circle_rad_range: Tuple[int, int] = CIRCLE_RAD_RANGE,
        ellipse_rad_range: Tuple[int, int] = ELLIPSE_RAD_RANGE,
        rect_size_range: Tuple[int, int] = RECT_SIZE_RANGE,
        shape_color_range: Tuple[Tuple[int, int, int, float], Tuple[int, int, int, float]] = SHAPE_COLOR_RANGE
    ) -> None:
        """
        Purpose: Initialize an instance of the PyArtConfig class. Uses default values if nothing passed.
        Parameters: shape_types       - A list of strings containg the shape names
                    shape_pos_range   - A tuple containing min and max x and y values
                    circle_rad_range  - A tuple containing min and max radius ranges
                    ellipse_rad_range - A tuple containg min and max ellipse radius ranges
                    rect_size_range   - A tuple containing min and max rectangle size ranges
                    shape_color_range - A tuple of tuples where the first correspont to rgba min values
                                        and the second corresespong to rgba max values
        Returns: None
        """
        self.shape_types = shape_types
        self.shape_pos_range = shape_pos_range
        self.circle_rad_range = circle_rad_range
        self.ellipse_rad_range = ellipse_rad_range
        self.rect_size_range = rect_size_range
        self.shape_color_range = shape_color_range