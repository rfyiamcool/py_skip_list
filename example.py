# coding: utf-8

import skip_list


def main():
    skip = skip_list.Skiplist()
    print(6 in skip)
    skip.insert(0)
    skip.insert(7)
    skip.insert(3)
    skip.insert(6)
    skip.insert(245)
    print(6 in skip)
    skip.remove(245)
    print(skip.find(3))


if __name__ == "__main__":
    main()
