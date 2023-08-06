# texttofont
Take a .ttf file and generate ascii art using the font for text. Use any symbols for generating the font + fun mode where each character is built up of itself in ascii art

## Instructions
Run `pip install text-to-font`

The following code prints the ascii art for `"Hello!"` in string format

```python
from text_to_font.transformations import word_to_ascii

print(word_to_ascii(
    phrase='Hello!', 
    font_size=12, 
    kerning=1,
    font_path='~/fonts/somefont.ttf'  # defaults to built-in 'slkscr.ttf' (SilkScreen) font
))
```
