# use CamelCase for class names
class MyFirstClass:
    pass #placeholder


class Point:
    def reset(self):
        self.x = 0
        self.y = 0


def main():
    p1 = Point()
    # <object>.<attribute> = <value> (dot notation)  Can crreate attributes on the fly
    p1.x = 5
    p1.y = 4

    print(p1.x, p1.y)
    p1.reset()
    print(p1.x, p1.y)


if __name__ == "__main__":
    main()
    exit(0)
