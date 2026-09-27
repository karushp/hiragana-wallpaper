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

def to_katakana(char):
    """Map a hiragana character to katakana. Empty cells stay empty."""
    if not char:
        return ""
    code = ord(char)
    if 0x3041 <= code <= 0x3096:
        return chr(code + 0x60)
    return char

def get_system_fonts(japanese_size=230, english_size=60):
    """Get system fonts for Japanese and English text."""
    try:
        # Try to load Japanese font first (common on macOS)
        japanese_font = ImageFont.truetype("/System/Library/Fonts/Hiragino Sans GB.ttc", japanese_size)
        english_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", english_size)
    except OSError:
        try:
            # Fallback fonts
            japanese_font = ImageFont.truetype("/System/Library/Fonts/Arial Unicode MS.ttf", japanese_size)
            english_font = ImageFont.truetype("/System/Library/Fonts/Arial.ttf", english_size)
        except OSError:
            # Default fonts if system fonts not found
            japanese_font = ImageFont.load_default()
            english_font = ImageFont.load_default()
            print("Warning: Using default fonts. Japanese characters may not render properly.")
    
    return japanese_font, english_font

CHART_ROW_HEIGHT = 42

def draw_reference_chart(draw, start_x, start_y, chart_width, font_jp, font_en, katakana=False):
    """Draw a gojūon chart. Returns the y coordinate just below the chart."""
    transform = to_katakana if katakana else (lambda c: c)
    cell_width = chart_width // 5  # 5 columns
    row_height = CHART_ROW_HEIGHT
    col_step = cell_width * 0.65

    y = start_y

    # Header row (vowels A, I, U, E, O)
    vowels = ["A", "I", "U", "E", "O"]
    for i, vowel in enumerate(vowels):
        x = start_x + i * col_step + cell_width // 2
        bbox = draw.textbbox((0, 0), vowel, font=font_en)
        text_width = bbox[2] - bbox[0]
        draw.text((x - text_width // 2, y), vowel, font=font_en, fill=COLORS["text_primary"])
    
    # First row - vowel sounds (あ い う え お)
    vowel_row_label = "(vowels)"
    vowel_characters = ["あ", "い", "う", "え", "お"]
    
    # Draw vowel row header
    vowel_row_y = y + row_height
    bbox = draw.textbbox((0, 0), vowel_row_label, font=font_en)
    text_width = bbox[2] - bbox[0]
    header_x = start_x - text_width - 10
    draw.text((header_x, vowel_row_y), vowel_row_label, font=font_en, fill=COLORS["text_primary"])
    
    # Draw vowel characters
    for col_idx, char in enumerate(vowel_characters):
        shown = transform(char)
        cell_x = start_x + col_idx * col_step
        cell_y = vowel_row_y + 4
        
        # Center character in cell
        char_bbox = draw.textbbox((0, 0), shown, font=font_jp)
        char_width = char_bbox[2] - char_bbox[0]
        char_x = cell_x + (cell_width - char_width) // 2
        
        draw.text((char_x, cell_y), shown, font=font_jp, fill=COLORS["text_primary"])
    
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
        row_y = y + row_height * 2 + row_idx * row_height  # Skip vowel row
        
        # Draw row header
        header_x = start_x - 60
        draw.text((header_x, row_y), row_label, font=font_en, fill=COLORS["text_primary"])
        
        # Draw characters with tighter column spacing
        for col_idx, char in enumerate(characters):
            if char:  # Only draw if character exists
                shown = transform(char)
                cell_x = start_x + col_idx * col_step
                cell_y = row_y + 4
                
                # Center character in cell
                char_bbox = draw.textbbox((0, 0), shown, font=font_jp)
                char_width = char_bbox[2] - char_bbox[0]
                char_x = cell_x + (cell_width - char_width) // 2
                
                draw.text((char_x, cell_y), shown, font=font_jp, fill=COLORS["text_primary"])

    return y + row_height * (2 + len(chart_rows))

def generate_wallpaper(character_data):
    """Generate a wallpaper with the sound in both scripts and both charts."""
    # Standard Mac wallpaper dimensions (16:10 ratio)
    width, height = 2880, 1800
    
    # Create image with dark background
    img = Image.new('RGB', (width, height), COLORS["background"])
    draw = ImageDraw.Draw(img)
    
    # Get fonts
    japanese_font, english_font = get_system_fonts()
    
    # Chart fonts are smaller so hiragana and katakana grids both fit
    try:
        chart_font_jp = ImageFont.truetype("/System/Library/Fonts/Hiragino Sans GB.ttc", 28)
        chart_font_en = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 20)
    except OSError:
        chart_font_jp = japanese_font
        chart_font_en = english_font
    
    # Main content area (left 1/2 - smaller to give more space for reference chart)
    main_width = int(width * 0.5)
    
    # Get character data
    char = character_data["char"]
    kata = to_katakana(char)
    pronunciation = character_data["pronunciation"]
    
    # Pair hiragana and katakana, centered together in the left area
    hira_bbox = draw.textbbox((0, 0), char, font=japanese_font)
    kata_bbox = draw.textbbox((0, 0), kata, font=japanese_font)
    pronunciation_bbox = draw.textbbox((0, 0), pronunciation, font=english_font)
    
    hira_width = hira_bbox[2] - hira_bbox[0]
    kata_width = kata_bbox[2] - kata_bbox[0]
    pronunciation_width = pronunciation_bbox[2] - pronunciation_bbox[0]
    
    glyph_height = max(hira_bbox[3] - hira_bbox[1], kata_bbox[3] - kata_bbox[1])
    pronunciation_height = pronunciation_bbox[3] - pronunciation_bbox[1]
    glyph_gap = 80
    
    pair_width = hira_width + glyph_gap + kata_width
    total_height = glyph_height + pronunciation_height + 100
    start_y = (height - total_height) // 2
    pair_x = (main_width - pair_width) // 2
    
    draw.text((pair_x - hira_bbox[0], start_y), char, font=japanese_font, fill=COLORS["text_primary"])
    draw.text((pair_x + hira_width + glyph_gap - kata_bbox[0], start_y), kata, font=japanese_font, fill=COLORS["text_primary"])
    
    # One romaji line, centered under the pair
    pron_x = pair_x + (pair_width - pronunciation_width) // 2
    pron_y = start_y + glyph_height + 80
    draw.text((pron_x, pron_y), pronunciation, font=english_font, fill=COLORS["text_primary"])
    
    # Hiragana chart on top, katakana chart beneath it, with two extra rows between them
    chart_start_x = main_width + 80
    chart_width = width - chart_start_x - 40
    chart_rows = 18  # vowel header, vowel row, then K through ん
    chart_gap = 28 + CHART_ROW_HEIGHT * 2
    charts_height = chart_rows * CHART_ROW_HEIGHT * 2 + chart_gap
    chart_start_y = (height - charts_height) // 2
    
    hiragana_bottom = draw_reference_chart(
        draw, chart_start_x, chart_start_y, chart_width, chart_font_jp, chart_font_en,
    )
    draw_reference_chart(
        draw, chart_start_x, hiragana_bottom + chart_gap, chart_width, chart_font_jp, chart_font_en,
        katakana=True,
    )
    
    return img
