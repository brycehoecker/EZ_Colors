import os
import re

class Color:
    # Standard 16 colors (8 normal and 8 bright/bold)
    COLORS = {
        "black": "\033[30m",
        "red": "\033[31m",
        "green": "\033[32m",
        "yellow": "\033[33m",
        "blue": "\033[34m",
        "magenta": "\033[35m",
        "cyan": "\033[36m",
        "white": "\033[37m",
        "b_black": "\033[90m",
        "b_red": "\033[91m",
        "b_green": "\033[92m",
        "b_yellow": "\033[93m",
        "b_blue": "\033[94m",
        "b_magenta": "\033[95m",
        "b_cyan": "\033[96m",
        "b_white": "\033[97m"
    }

    def __init__(self):
        self.colors = self.COLORS.copy()

    def add_256color_support(self):
        for i in range(256):
            self.colors[f"color{i}"] = f"\033[38;5;{i}m"

    def add_truecolor_support(self):
        self.colors["true_color"] = lambda r, g, b: f"\033[38;2;{r};{g};{b}m"

def detect_terminal_capabilities():
    color = Color()
    term = os.environ.get("TERM", "")

    if "256color" in term:
        color.add_256color_support()

    if re.match(r"^(xterm|screen|tmux|rxvt).*-truecolor$", term):
        color.add_truecolor_support()

    return color

color = detect_terminal_capabilities()

def colorize(text, color_code):
    return f"{color_code}{text}\033[0m"

# Standard color functions
def black(text): return colorize(text, color.colors["black"])
def red(text): return colorize(text, color.colors["red"])
def green(text): return colorize(text, color.colors["green"])
def yellow(text): return colorize(text, color.colors["yellow"])
def blue(text): return colorize(text, color.colors["blue"])
def magenta(text): return colorize(text, color.colors["magenta"])
def cyan(text): return colorize(text, color.colors["cyan"])
def white(text): return colorize(text, color.colors["white"])

# Bright color functions
def b_black(text): return colorize(text, color.colors["b_black"])
def b_red(text): return colorize(text, color.colors["b_red"])
def b_green(text): return colorize(text, color.colors["b_green"])
def b_yellow(text): return colorize(text, color.colors["b_yellow"])
def b_blue(text): return colorize(text, color.colors["b_blue"])
def b_magenta(text): return colorize(text, color.colors["b_magenta"])
def b_cyan(text): return colorize(text, color.colors["b_cyan"])
def b_white(text): return colorize(text, color.colors["b_white"])

# True color function
def true_color(text, r, g, b):
    if "true_color" in color.colors:
        return colorize(text, color.colors["true_color"](r, g, b))
    else:
        return text  # Return the original text if true color is not supported

## Example usage
#print(red("This is red text"))
#print(b_blue("This is bright blue text"))
#print(true_color("This is true colored text", 255, 0, 0))  # Red color
