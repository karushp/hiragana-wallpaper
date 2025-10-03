#!/usr/bin/env python3
"""
Example: Generate a single Hiragana wallpaper for preview.

To run this script:
uv run examples/single_wallpaper.py
"""

import sys
import os

# Add the src directory to the path path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from hiragana_wallpaper import generate_wallpaper, create_output_directory, HIRAGANA_DATA

def test_single_character():
    """Generate just one wallpaper for testing."""
    print("🎌 Testing single Hiragana wallpaper generation...")
    
    # Create output directory
    create_output_directory("test_output")
    
    # Pick the first character (あ) for testing
    test_char = HIRAGANA_DATA[0]
    char = test_char["char"]
    pronunciation = test_char["pronunciation"]
    meaning = test_char["meaning"]
    
    print(f"Generating wallpaper for: {char} ({pronunciation}) - {meaning}")
    
    # Generate the wallpaper
    wallpaper = generate_wallpaper(test_char)
    
    # Save it
    test_filename = f"test_output/test_hiragana_{pronunciation}_{char}.png"
    wallpaper.save(test_filename, "PNG", quality=95)
    
    print(f"✅ Test wallpaper saved as: {test_filename}")
    print("📱 Open this file to see how the layout looks!")
    print("🔧 If you like the result, run the full script: uv run main.py")

if __name__ == "__main__":
    test_single_character()
