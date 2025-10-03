"""
Core wallpaper generation functionality for Hiragana characters.
"""

import os
from PIL import Image, ImageDraw, ImageFont
from .data import HIRAGANA_DATA, COLORS

def create_output_directory(output_dir="hiragana_wallpapers"):
    """Create the output directory if it doesn't exist."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Created directory: {output_dir}")
    else:
        print(f"Directory {output_dir} already exists")

def get_system_fonts():
    """Get system fonts for Japanese and English text."""
    try:
        # Try to load Japanese font first (common on macOS) - even larger main character size
        japanese_font = ImageFont.truetype("/System/Library/Fonts/Hiragino Sans GB.ttc", 260)
        english_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 60)
    except OSError:
        try:
            # Fallback fonts
            japanese_font = ImageFont.truetype("/System/Library/Fonts/Arial Unicode MS.ttf", 260)
            english_font = ImageFont.truetype("/System/Library/Fonts/Arial.ttf", 60)
        except OSError:
            # Default fonts if system fonts not found
            japanese_font = ImageFont.load_default()
            english_font = ImageFont.load_default()
            print("Warning: Using default fonts. Japanese characters may not render properly.")
    
    return japanese_font, english_font

def draw_reference_chart(draw, start_x, start_y, chart_width, font_jp, font_en):
    """Draw a simplified reference chart on the right side."""
    # Chart dimensions
    cell_width = chart_width // 5  # 5 columns
    row_height = 55  # increased for larger fonts
    
    # Header row (vowels A, I, U, E, O) - with tighter spacing
    vowels = ["A", "I", "U", "E", "O"]
    for i, vowel in enumerate(vowels):
        x = start_x + i * (cell_width * 0.65) + cell_width // 2  # match the tighter column spacing
        y = start_y
        bbox = draw.textbbox((0, 0), vowel, font=font_en)
        text_width = bbox[2] - bbox[0]
        draw.text((x - text_width // 2, y), vowel, font=font_en, fill=COLORS["text_primary"])
    
    # First row - vowel sounds (あ い う え お)
    vowel_row_label = "(vowels)"
    vowel_characters = ["あ", "い", "う", "え", "お"]
    
    # Draw vowel row header
    vowel_row_y = start_y + row_height
    bbox = draw.textbbox((0, 0), vowel_row_label, font=font_en)
    text_width = bbox[2] - bbox[0]
    header_x = start_x - text_width - 10
    draw.text((header_x, vowel_row_y), vowel_row_label, font=font_en, fill=COLORS["text_primary"])
    
    # Draw vowel characters
    for col_idx, char in enumerate(vowel_characters):
        cell_x = start_x + col_idx * (cell_width * 0.65)
        cell_y = vowel_row_y + 5
        
        # Center character in cell
        char_bbox = draw.textbbox((0, 0), char, font=font_jp)
        char_width = char_bbox[2] - char_bbox[0]
        char_x = cell_x + (cell_width - char_width) // 2
        
        draw.text((char_x, cell_y), char, font=font_jp, fill=COLORS["text_primary"])
    
    # Simplified chart data - organized by vowel columns (A,I,U,E,O)
    chart_rows = [
        # K-G sound rows (showing k/g variants)
        ("K", ["か", "き", "く", "け", "こ"]),
        ("G", ["が", "ぎ", "ぐ", "げ", "ご"]),
        # S-Z sound rows
        ("S", ["さ", "し", "す", "せ", "そ"]),
        ("Z", ["ざ", "じ", "ず", "ぜ", "ぞ"]),
        # T-D sound rows
        ("T", ["た", "ち", "つ", "て", "と"]),
        ("D", ["だ", "ぢ", "づ", "で", "ど"]),
        # N sound row
        ("N", ["な", "に", "ぬ", "ね", "の"]),
        # H sound rows (showing h/b/p variants)
        ("H", ["は", "ひ", "ふ", "へ", "ほ"]),
        ("B", ["ば", "び", "ぶ", "べ", "ぼ"]),
        ("P", ["ぱ", "ぴ", "ぷ", "ぺ", "ぽ"]),
        # M sound row
        ("M", ["ま", "み", "む", "め", "も"]),
        # Y sound row
        ("Y", ["や", "", "ゆ", "", "よ"]),
        # R sound row
        ("R", ["ら", "り", "る", "れ", "ろ"]),
        # W sound row
        ("W", ["わ", "", "", "", "を"]),
        # Final row (n sound)
        ("N", ["ん", "", "", "", ""])
    ]
    
    # Draw rows (adjusted for vowel row)
    for row_idx, (row_label, characters) in enumerate(chart_rows):
        row_y = start_y + row_height * 2 + row_idx * row_height  # Skip vowel row
        
        # Draw row header
        header_x = start_x - 60
        draw.text((header_x, row_y), row_label, font=font_en, fill=COLORS["text_primary"])
        
        # Draw characters with tighter column spacing
        for col_idx, char in enumerate(characters):
            if char:  # Only draw if character exists
                # Reduce the cell spacing for tighter layout
                cell_x = start_x + col_idx * (cell_width * 0.65)  # reduce spacing between columns even more
                cell_y = row_y + 5  # Small vertical offset
                
                # Center character in cell
                char_bbox = draw.textbbox((0, 0), char, font=font_jp)
                char_width = char_bbox[2] + char_bbox[0]
                char_x = cell_x + (cell_width - char_width) // 2
                
                draw.text((char_x, cell_y), char, font=font_jp, fill=COLORS["text_primary"])

def generate_wallpaper(character_data):
    """Generate a single wallpaper image with main character and reference chart."""
    # Standard Mac wallpaper dimensions (16:10 ratio)
    width, height = 2880, 1800
    
    # Create image with dark background
    img = Image.new('RGB', (width, height), COLORS["background"])
    draw = ImageDraw.Draw(img)
    
    # Get fonts
    japanese_font, english_font = get_system_fonts()
    
    # Try to get chart fonts, fallback to system fonts if needed: larger chart fonts
    try:
        chart_font_jp = ImageFont.truetype("/System/Library/Fonts/Hiragino Sans GB.ttc", 36)
        chart_font_en = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 20)
    except OSError:
        chart_font_jp = japanese_font
        chart_font_en = english_font
    
    # Main content area (left 1/2 - smaller to give more space for reference chart)
    main_width = int(width * 0.5)
    
    # Get character data
    char = character_data["char"]
    pronunciation = character_data["pronunciation"]
    meaning = character_data["meaning"]
    
    # Calculate positions for main character (centered in left area)
    char_bbox = draw.textbbox((0, 0), char, font=japanese_font)
    pronunciation_bbox = draw.textbbox((0, 0), pronunciation, font=english_font)
    meaning_bbox = draw.textbbox((0, 0), meaning, font=english_font)
    
    char_width = char_bbox[2] - char_bbox[0]
    pronunciation_width = pronunciation_bbox[2] - pronunciation_bbox[0]
    meaning_width = meaning_bbox[2] - meaning_bbox[0]
    
    char_height = char_bbox[3] - char_bbox[1]
    pronunciation_height = pronunciation_bbox[3] - pronunciation_bbox[1]
    meaning_height = meaning_bbox[3] - meaning_bbox[1]
    
    # Center main content vertically in left area - increased spacing for larger character
    total_height = char_height + pronunciation_height + meaning_height + 180  # even more spacing
    start_y = (height - total_height) // 2
    
    # Draw the main Hiragana character (large, white) in left area
    char_x = (main_width - char_width) // 2
    char_y = start_y
    draw.text((char_x, char_y), char, font=japanese_font, fill=COLORS["text_primary"])
    
    # Draw pronunciation (with more space after character)
    pron_x = (main_width - pronunciation_width) // 2
    pron_y = char_y + char_height + 50  # increased spacing for larger character
    draw.text((pron_x, pron_y), pronunciation, font=english_font, fill=COLORS["text_primary"])
    
    # Draw meaning (with more space after pronunciation)
    meaning_x = (main_width - meaning_width) // 2
    meaning_y = pron_y + pronunciation_height + 35  # increased spacing
    draw.text((meaning_x, meaning_y), meaning, font=english_font, fill=COLORS["text_secondary"])
    
    # Draw reference chart (right side) - moved down and larger
    chart_start_x = main_width + 20
    chart_start_y = 150  # moved down significantly
    chart_width = width - chart_start_x - 20
    
    draw_reference_chart(draw, chart_start_x, chart_start_y, chart_width, chart_font_jp, chart_font_en)
    
    return img
