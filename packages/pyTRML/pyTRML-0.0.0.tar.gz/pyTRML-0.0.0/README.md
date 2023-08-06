# CTML
(Color Text Markup Language)


```python

from trml import format


string = """
My Normal Text
<text color="red" on="black">Some characters</text>
"""


colored = format(string)

print(colored)

```

![Example1](https://raw.githubusercontent.com/GrandMoff100/PyTRML/master/images/example1.png)
