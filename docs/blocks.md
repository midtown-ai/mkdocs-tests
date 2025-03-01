# Standard and Code Blocks

## Standard Block

Indented block (old way!)

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.

Triple ticks (new way!)

```
import tensorflow as tf
def watever
```


## Code Block

Highlight in an inline block `#!python range()` is used to generate a sequence of numbers

Some code with the `file.py` or `py` extension at the start:

```py
import tensorflow as tf
def watever
```

```python {hl_lines="4-5 10" linenums="100" title="My cool header"}
"""some_file.py"""
import tensorflow as tf

def highlighted_block():
    self.destruct()

def not_highlighted():
    pass

def highlighted_line():
    pass
```

with code annotation

``` yaml
theme:
  features:
    - content.code.annotate # (1)! 
```

1.  :man_raising_hand: I'm a code annotation! I can contain `code`, __formatted
    text__, images, ... basically anything that can be written in Markdown.

``` yaml
# (1)!
# (2)!
```

1.  Look ma, less line noise!
2.  Look ma, more noise!


## Tab-Linked code blocks

=== "C"

    C code linked tab

=== "C++"

    C++ code linked tab

===! "C"

    ``` c
    #include <stdio.h>

    int main(void) {
      printf("Hello world!\n");
      return 0;
    }
    ```

=== "C++"

    ``` c++
    #include <iostream>

    int main(void) {
      std::cout << "Hello world!" << std::endl;
      return 0;
    }
    ```
