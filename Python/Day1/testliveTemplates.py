class Point:
    """
    Represents a point in 2-D geometric space
    """
    def __init__(self, x=0, y=0):  # Assigns default values.  Can use 0,0 or whatever is passed in
        """
        Initializes the position of a new point.
        If they are not specified, the point defaults to 0,0
        :param x: x coordinate
        :param y: y coordinate
        """
        self.x = x
        self.y = y

    def reset(self):
        """
        Reset the point to the origin in 2-D space.
        :return: Nothing
        """
        self.move(0,0)

    def move(self, x, y):
        """
        Moves the point to a new location in 2-D space
        :param x: x coordinate
        :param y: y coordinate
        :return: Nothing
        """
        self.x = x
        self.y = y

    def calculate_distance(self, other_point):
        """
        Calculate the distance from this point to a second point passed
        as a parameter. This function uses Pythagorean Theorem to calculate
        the distance.
        :param other_point: second point to calculate distance (as Point)
        :return: Distance between 2 points as a float
        """
        import math
        xspan = other_point.x-self.x
        yspan = other_point.y-self.y
        distance = math.sqrt(xspan**2 + yspan**2)
        return distance # Or you  can just do it all in one line


def main():
    p1 = Point()
    print(p1.x, p1.y)
    p2 = Point(3, 4)
    print(p2.x, p2.y)
    dist = p1.calculate_distance(p2)
    print(dist)
    # Test tool (assert)
    # program will exit if False (or zero or empty or None)
    assert(p2.calculate_distance(p1) ==
           p1.calculate_distance(p2))


if __name__ == '__main__':
    main()
    exit(0)