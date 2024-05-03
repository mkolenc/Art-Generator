"""A module used to write html"""

from typing import IO, List, Tuple

class HTMLDocument:
    """A class for creating and writing HTML documents."""

    def __init__(self) -> None:
        """
        Purpose: Initializes an instance of the HTMLDocument class.
        Parameters: None
        Returns: None
        """
        self.head_content: List[str] = []
        self.body_content: List[str] = []

    def add_head_content(self, num_tabs: int, content: str) -> None:
        """
        Purpose: Adds content to the head of the HTML document.
        Parameters: num_tabs - An integer representing the number of tabs to use for indentation.
                    content - A string representing the content to be added to the head of the HTML document.
        Returns: None
        """
        indentation: str = "    " * num_tabs
        self.head_content.append(indentation + content)
    
    def add_body_content(self, num_tabs: int, content: str) -> None:
        """
        Purpose: Adds content to the body of the HTML document.
        Parameters: num_tabs - An integer representing the number of tabs to use for indentation.
                    content - A string representing the content to be added to the body of the HTML document.
        Returns: None
        """
        indentation: str = "    " * num_tabs
        self.body_content.append(indentation + content)

    def create_html_comment(self, comment: str) -> str:
        """
        Purpose: Returns the HTML comment form of the input string.
        Parameters: comment - A string representing the comment to be added to the HTML document.
        Returns: A string representing the HTML comment form of the input string.
        """
        return f"<!--{comment}-->"

    def write_html_document(self, filename: str) -> None:
        """
        Purpose: Writes the contents of the HTML document to a file.
        Parameters: filename - A string representing the name of the file to be written.
        Returns: None
        """
        with open(filename, "w") as f:
            f.write("<!DOCTYPE html>\n")
            f.write("<html>\n")
            self.__write_head(f)
            self.__write_body(f)
            f.write("</html>\n")

    def __write_head(self, f: IO[str]) -> None:
        """
        Purpose: Writes the head content to the HTML document file.
        Parameters: f - A file object representing the file to be written.
        Returns: None
        """
        f.write("<head>\n")
        for line in self.head_content:
            f.write(line + "\n")
        f.write("</head>\n")

    def __write_body(self, f: IO[str]) -> None:
        """
        Purpose: Writes the body content to the HTML document file.
        Parameters: f - A file object representing the file to be written.
        Returns: None
        """
        f.write("<body>\n")
        for line in self.body_content:
            f.write(line + "\n")
        f.write("</body>\n")