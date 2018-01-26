# py_skip_list

base on https://github.com/toastdriven/pyskip/blob/master/pyskip.py

### Usage

```
>>> import skip_list
>>> skip = skip_list.Skiplist()
>>> len(skip)
0
>>> 6 in skip
False
>>> skip.insert(0)
>>> skip.insert(7)
>>> skip.insert(3)
>>> skip.insert(6)
>>> skip.insert(245)
>>> len(skip)
5
>>> 6 in skip
True
>>> skip.remove(245)
>>> len(skip)
4
>>> skip.find(3)
<Skiplist: 3>

```
