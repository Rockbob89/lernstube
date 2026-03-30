from collections import Counter, defaultdict, namedtuple

def unique_words(text = ""):
    ret = set()
    cleanSring = (text.replace('.', '')
                  .replace(',', '')
                  .replace('!', '')
                  .replace('?', '')
                  .replace(';', '')
                  .replace(':', '')
                  .split())
    for word in cleanSring:
        ret.add(word.lower())

    return ret

def top_n(items, n):
    c = Counter(items)
    return c.most_common(n)

def group_by_length(words):
    ret = defaultdict(list)
    for word in words:
        ret[len(word)].append(word)

    return dict(ret)

def make_record(fields, values):
    Person = namedtuple("person", fields)
    ret = Person(*values)
    return ret


def set_ops(a, b):
    union = set(a|b)
    intersection = set(a&b)
    only_a = set(a-b)
    only_b = set(b-a)

    return (union, intersection, only_a, only_b)


print(unique_words("Hello world! Hello, Python."))
print(top_n(["a", "b", "a", "c", "b", "a"], 2))
print(group_by_length(["hi", "hey", "go", "wow"]))
r = make_record(["name", "age"], ["Alice", 30])
print(r.name, r.age)
print(set_ops({1, 2, 3}, {2, 3, 4}))
