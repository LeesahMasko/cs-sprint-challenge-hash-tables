import os
import pathlib
# Your code here


cache = {}
def finder(files, queries):
    for file in files:
        f = file[1]
        if f not in cache:
            cache[file]
        else:
            index[file_search].append(f)


    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
