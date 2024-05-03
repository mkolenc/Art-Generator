#!/usr/bin/env python3

from HTML_module import HTMLDocument
from SVG_module import SvgCanvas
from Shapes_module import CircleShape, RectangleShape, EllipseShape
from ArtConfig_module import PyArtConfig
from RandomShapes_module import RandomShape

def get_art_theme(name: str) -> PyArtConfig:
    """
    Purpose: Get the configuration for a particular art theme
    Parameters: name - The string of the art theme
    Returns: PyArtConfig - The configurations for the theme
    """
    themes: dict = {
        "forest": PyArtConfig(shape_color_range=((50, 0, 0, 0.1), (100, 200, 100, 1.0)), circle_rad_range=(0, 0), rect_size_range=(0, 0)),
        "random": PyArtConfig(),
        "sea": PyArtConfig(shape_color_range=((0, 150, 150, 0.1), (100, 255, 255, 1.0)))
    }
    return themes[name]

def generate_html_file(filename: str, theme: str) -> None:
    """
    Purpose: Generate an html file to show completion for a4, part 3
    Parameters: filename - A string of the filename to create
                theme    - A string of the theme to generate
    Returns: None
    """
    # Create an html document
    doc: HTMLDocument = HTMLDocument()

    # Write the documents title, and a main body heading
    doc.add_head_content(1, "<title>A4 Part 3</title>")
    doc.add_body_content(1, doc.create_html_comment("The main content of the page"))
    doc.add_body_content(1, f'<h1 style="text-align: center;">Theme: {theme}</h1>\n')
    doc.add_body_content(1, doc.create_html_comment("This is the svg portion"))

    # Create a svgCanvas object on our document of size 1000 x 600
    svg_canvas: SvgCanvas = SvgCanvas(doc, 1, (1000, 600))

    num_shapes: int = 10000
    if theme == "forest":
        config: PyArtConfig = get_art_theme("forest")
        num_shapes = 100000
    if theme == "random":
        config: PyArtConfig = get_art_theme("random")
    if theme == "sea":
        config: PyArtConfig = get_art_theme("sea")

    for i in range(num_shapes):
        svg_canvas.add_shape(RandomShape(config).as_svg())

    # write the shapes to the document and create the html file
    svg_canvas.gen_art()
    doc.write_html_document(filename)

def main() -> None:
    "The main entry point of this program"
    # Generate 3 html files with shape-art
    generate_html_file("forest.html", theme="forest")
    generate_html_file("random.html", theme="random")
    generate_html_file("sea.html", theme="sea")

if __name__ == "__main__":
    main()