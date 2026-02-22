print("Hello")


def linear_search(items, target):
    if not items:
        return -1
    for index, item in enumerate(items):
        if item == target:
            return index
    return -1


items = ["haycorn", "haycorn", "haycorn", "hunny", "haycorn"]
target = "hunny"
print(linear_search(items, target))

items = ["bed", "blue jacket", "red shirt", "hunny"]
target = "red balloon"
print(linear_search(items, target))
