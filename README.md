# EZ_Colors
Easy Terminal Colorizing for *most* Terminals

A simple Python package for colorizing text in the terminal.

## Description

`EZ_Colors` makes it easy to add color to your terminal text in Python scripts. It supports standard, bright, 256-color, and true color modes.

## Installation

To install `EZ_Colors`, follow these steps:

1. **Clone the Repository**

    git clone this-repository


2. **Navigate to the Repository Directory**

    cd EZ_Colors


3. **Install the Package**:

    pip install .


Use `sudo` if you need to install the package system-wide (requires administrator privileges):

    sudo pip install .


## Usage

After installation, you can use `EZ_Colors` in your Python scripts as follows:

```python
from EZ_Colors.color_text import red, green, blue, b_red, true_color

print(red("This is red text"))
print(green("This is green text"))
print(blue("This is blue text"))
print(b_red("This is bright red text"))
print(true_color("This is true colored text", 255, 0, 0))  # Example of true color (red)
```
## Features

- Standard colors: 
  <span style="color: red;">red</span>, 
  <span style="color: green;">green</span>, 
  <span style="color: blue;">blue</span>, etc.

- Bright colors: 
  <span style="color: red;">b_red</span>, 
  <span style="color: green;">b_green</span>, 
  <span style="color: blue;">b_blue</span>, etc.

- 256 colors support.
- True color (24-bit) support.

