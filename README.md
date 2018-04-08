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
