# Hiragana Wallpaper Generator

A Python script that generates minimalist, dark-themed wallpaper images for each Hiragana character. Perfect for learning Japanese through daily wallpaper exposure!

## Features

- **Dark minimalist theme** with only 3 colors
- **High resolution** (2880x1800) optimized for Mac retina displays
- **Individual wallpapers** - one character per image
- **Educational content** - includes character, pronunciation, and English meaning
- **Auto-rotation ready** - designed for macOS wallpaper cycling

## Setup

1. Install dependencies with uv:
```bash
uv add pillow
```

2. Run the generator:
```bash
uv run main.py
```

## Alternative Usage

- **Generate all wallpapers**: `uv run main.py`
- **Test single wallpaper**: `uv run examples/single_wallpaper.py`
- **Run tests**: `uv run tests/test_generator.py`

## Images Generated

- Each wallpaper shows the Hiragana character, its pronunciation (romaji), and English meaning
- Files are named: `hiragana_[pronunciation]_[character].png`
- All images saved in `hiragana_wallpapers/` folder

## Using as Wallpaper

1. Open **System Preferences** > **Desktop & Screen Saver**
2. Select **Folder** and choose the `hiragana_wallpapers` folder
3. Enable **Change wallpaper** and set interval (recommended: every 1-3 minutes)
4. Enjoy learning Hiragana naturally throughout your day!

## What's Included

- 47 Hiragana characters total
- Vowels (あいうえお) through N-sound (ん)
- Complete K, S, T, N, H, M, Y, R, W columns
- Standard pronunciations and English meanings

## Project Structure

```
src/hiragana_wallpaper/
├── data.py          # Hiragana character data and colors
├── generator.py     # Core wallpaper generation logic
└── cli.py           # Command-line interface
```

## Customization

Edit `src/hiragana_wallpaper/data.py` to modify:
- Characters and pronunciations
- English meanings
- Color scheme (3-color dark theme)

Edit `src/hiragana_wallpaper/generator.py` to modify:
- Image dimensions
- Font sizes
- Layout positioning
- Chart appearance
