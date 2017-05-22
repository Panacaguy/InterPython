# Task: Define a function that takes a string as input parameter,
# defines a local function that returns the last letter of the string.
# Your main function returns a sorted list based on that last letter.

store = []


def sort_by_last_letter(string):
    """
    Takes a string as input parameter,
    defines a local function that returns the last letter of the string.
    :param string: A list of strings
    :return: sorted list based on that last letter
    """

    def last_letter(s):
        return s[-1]

    store.append(last_letter)
    print(last_letter)

    return sorted(string, key=last_letter)


def logger(msg):
    def log_message():
        print("Log:", msg)
    return log_message


def html_tag(tag):
    """
    Creates an HTML tag based on input
    :param tag: Tag
    :return: callable function
    """
    def wrap_text(msg):
        print("<{0}>{1}</{0}>".format(tag, msg))

    return wrap_text


def main():
    names = ["Hugo", "Maria", "Peter", "El Chapo", "Mario"]
    print(sort_by_last_letter(names))
    print(sort_by_last_letter(names))
    print(sort_by_last_letter(names))

if __name__ == '__main__':
    main()
    exit(0)

