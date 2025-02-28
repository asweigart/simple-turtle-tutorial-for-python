# This script extracts the Python programs out of simple_turtle_tutorial.md and checks their syntax.

import os
import platform
import sys

fo = open('simple_turtle_tutorial.md')
content= fo.read()
fo.close()

while True:
    # find where the next python script is
    start_pos = content.find("```python\n")
    if start_pos == -1:
        break

    end_pos = content.index('```', start_pos + len('```python\n'))
    script = content[start_pos + len('```python\n') : end_pos]

    # remove that script from the file contents
    content = content[end_pos + len('```\n'):]

    # output the python script to a temp file
    temp_script_filename = open('_deleteme.py', 'w')
    temp_script_filename.write(script)
    temp_script_filename.close()

    # compile the code to do a syntax check
    if platform.system() == 'Windows':
        # Check that the code is compatible with Python 2
        os.system('py -2 -m py_compile _deleteme.py')
        os.system('py -3 -m py_compile _deleteme.py')
    else:
        os.system('python3 -m py_compile _deleteme.py')
    sys.stdout.write('.') # Each period marks that we've tested one program.
    sys.stdout.flush()

    os.unlink('_deleteme.py')