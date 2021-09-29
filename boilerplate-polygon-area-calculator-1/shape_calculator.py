class Rectangle:
    name = 'Rectangle'

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f"{self.name}(width={self.width}, height={self.height})"

    def set_width(self, width) -> int:
        """
        Set the width of the
        rectangle
        :param width:
        :return:
        """
        self.width = width
        return self.width

    def set_height(self, height) -> int:
        """
        Get the height of the
        rectangle
        :param height:
        :return:
        """
        self.height = height
        return self.height

    def get_area(self) -> int:
        """
        Get the area of the
        shape
        :return:
        """
        return self.width * self.height

    def get_perimeter(self) -> int:
        """
        Get the perimeter of the
        shape
        :return:
        """
        return (2 * self.set_width(self.width)) + (2 * self.set_height(self.height))

    def get_diagonal(self) -> int:
        """
        Get the diagonal of the
        shape
        :return:
        """
        return ((self.set_width(self.width) ** 2) + (self.set_height(self.height) ** 2)) ** .5

    def get_picture(self) -> str:
        """
        Get the graphic representation
        of the rectangle
        :return:
        """
        display = ''
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        for i in range(0, self.height):
            display += '*' * self.width
            display += '\n'
        return display

    def get_amount_inside(self, shape) -> int:
        """
        Get amount of a rectangle or
        square shape that can be fitted
        into the current shape
        :param shape:
        :return:
        """
        return (self.height * self.width) // (shape.height * shape.width)


class Square(Rectangle):
    name = 'Square'

    def __init__(self, side_length):
        self.side_length = side_length
        super().__init__(width=side_length, height=side_length)

    def __str__(self):
        return f"{self.name}(side={self.side_length})"

    def set_side(self, side) -> int:
        """
        Set side dimension of
        square
        :param side:
        :return:
        """
        self.side_length = side
        return self.side_length

    def set_height(self, height) -> int:
        """
        Set height of square
        :param height:
        :return:
        """
        return self.set_side(height)

    def set_width(self, width) -> int:
        """
        Set width of square
        :param width:
        :return:
        """
        return self.set_side(width)

    def get_picture(self) -> str:
        """
        Get the graphic
        representation of the
        shape
        :return:
        """
        display = ''
        if self.side_length > 50:
            return "Too big for picture."
        for i in range(0, self.side_length):
            display += '*' * self.side_length
            display += '\n'
        return display
