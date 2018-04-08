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
