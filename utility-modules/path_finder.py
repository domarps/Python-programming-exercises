import os
'''
Working your way upwards from current file
'''
print('real_path', os.path.realpath(__file__))
print('dir_name', os.path.dirname(os.path.abspath(__file__)))
print('abs_path',os.path.abspath(__file__))
