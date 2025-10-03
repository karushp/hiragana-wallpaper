"""
Hiragana Wallpaper Generator

A minimalist wallpaper generator that creates dark-themed wallpapers
for each Hiragana character to help with Japanese language learning.
"""

__version__ = "0.1.0"
__author__ = "Your Name"

from .data import HIRAGANA_DATA, COLORS
from .generator import generate_wallpaper, create_output_directory

__all__ = ["HIRAGANA_DATA", "COLORS", "generate_wallpaper", "create_output_directory"]
