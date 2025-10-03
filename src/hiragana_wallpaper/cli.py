"""
Command-line interface for the Hiragana Wallpaper Generator.
"""

import os
from . import HIRAGANA_DATA, generate_wallpaper, create_output_directory

# Configuration
IMAGES_DIR = "hiragana_wallpapers"
IMAGES_PER_MINUTE = 3  # How often to change wallpapers (roughly)

def main():
    """Main function to generate all Hiragana wallpapers."""
    print("🎌 Generating Hiragana wallpapers...")
    print(f"📁 Output directory: {IMAGES_DIR}")
    print(f"🎨 Theme: Dark minimalist (3 colors)")
    print(f"📐 Resolution: 2880x1800 (Mac retina)")
    print()
    
    # Create output directory
    create_output_directory(IMAGES_DIR)
    
    # Track progress
    total_chars = len(HIRAGANA_DATA)
    generated_count = 0
    
    # Generate wallpaper for each character
    for character_data in HIRAGANA_DATA:
        char = character_data["char"]
        pronunciation = character_data["pronunciation"]
        
        print(f"Generating {char} ({pronunciation})...")
        
        # Generate the image
        wallpaper = generate_wallpaper(character_data)
        
        # Save with descriptive filename
        filename = f"hiragana_{character_data['pronunciation']}_{char}.png"
        filepath = os.path.join(IMAGES_DIR, filename)
        
        wallpaper.save(filepath, "PNG", quality=95)
        
        generated_count += 1
        
        # Show progress
        if generated_count % 10 == 0:
            print(f"Progress: {generated_count}/{total_chars} completed")
    
    print()
    print(f"✅ Generation complete!")
    print(f"📊 Generated {generated_count} wallpapers")
    print(f"📂 Saved in: {os.path.abspath(IMAGES_DIR)}")
    print()
    print("🎯 Usage tips:")
    print(f"• Set macOS to rotate wallpapers every {IMAGES_PER_MINUTE} minute(s)")
    print(f"• Select the '{IMAGES_DIR}' folder as wallpaper source")
    print(f"• Enable 'Change wallpaper' in System Preferences > Desktop & Screen Saver")
