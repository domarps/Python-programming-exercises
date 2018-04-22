# In a quest towards idiomatic python!

Some over-used verses during the first few months of my New Grad ML Engineering role :


- List comprehension

```python
values = [expression for value in collection if condition]
```

- Initialize a two dimensional matrix, `distance` of size M * N

```python
distance = [[-1 for _ in range(N)] for _ in range(M)]
```

- Paths

```python
import os
print('real_path', os.path.realpath(__file__))
print('dir_name', os.path.dirname(os.path.abspath(__file__)))
print('abs_path',os.path.abspath(__file__))
```

- Some embarrassing hack to extract python shared object libraries from full-paths:

```python
import os, sys
BASE_FOLDER = 'change_me'
CURRENT_PATH = os.getcwd()
BASE_PATH = CURRENT_PATH[0:CURRENT_PATH.index(BASE_FOLDER) + len(BASE_FOLDER)]
sys.path.insert(0, BASE_PATH + '/build')
import libAttrib as Attrib  # imports libAttrib from build dir
import libDetect as Detect  # imports libDetect from build dir
sys.path.insert(0, BASE_PATH + '/app')
```

- python supports floating point division by default

```python
5 / 2 # 2.5
5 // 2 # 2 (we use two backslashes)
```
- The python `range` mini-bootcamp (no xrange from python3), `range` is a memory-efficient iterator:

```python
range(3) # does not create a list, rather than an iterator, default starts from 0
a = list(range(3)) # converts iterator to List
list(range(1, len(a))) # output : [1,2]
```

- Easy way to detect python python version

```python
import platform
version = platform.python_version_tuple()  #version[0] == '2' or version[0] == '3'
```

- Confirm tensorflow can actually see the GPU

```python
import tensorflow as tf
device_name = tf.test.gpu_device_name()
if device_name != '/device:GPU:0':
  raise SystemError('GPU device not found')
print('Found GPU at: {}'.format(device_name))
```

- Keyword arguments vs positional arguments:
```
# positional arguments
def test(a,b,c):
     print(a)
     print(b)
     print(c)

test(1,2,3)
#output:
1
2
3

# keyword arguments
def test(a=0,b=0,c=0):
     print(a)
     print(b)
     print(c)
     print('-------------------------')

test(a=1,b=2,c=3)
#output :
1
2
3
-------------------------
```

- Use of `*` operator in function call
```
def sum(a,b):  #receive args from function calls as sum(1,2) or sum(a=1,b=2)
    print(a+b)

# Unpack data structure of list or tuple or dict into arguments with help of '*' operator
sum(*my_tuple)   # becomes same as sum(1,2) after unpacking my_tuple with '*'
sum(*my_list)    # becomes same as sum(1,2) after unpacking my_list with  '*'
sum(**my_dict)   # becomes same as sum(a=1,b=2) after unpacking by '**' NOTE!!!
```
