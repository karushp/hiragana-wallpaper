# Hiragana characters data structure with related variants
# Including character, pronunciation (romaji), and English meaning/word

# Complete Hiragana chart data (base + voiced + half-voiced)
HIRAGANA_CHART_DATA = {
    # Vowel sounds (no variants)
    "a": [{"char": "あ", "pronunciation": "a", "meaning": "ah"}],
    "i": [{"char": "い", "pronunciation": "i", "meaning": "tree"}],
    "u": [{"char": "う", "pronunciation": "u", "meaning": "rain"}],
    "e": [{"char": "え", "pronunciation": "e", "meaning": "picture"}],
    "o": [{"char": "お", "pronunciation": "o", "meaning": "tail"}],
    
    # K/G column (base + voiced)
    "ka": [{"char": "か", "pronunciation": "ka", "meaning": "mosquito"}, {"char": "が", "pronunciation": "ga", "meaning": "moth"}],
    "ki": [{"char": "き", "pronunciation": "ki", "meaning": "tree"}, {"char": "ぎ", "pronunciation": "gi", "meaning": "skill"}],
    "ku": [{"char": "く", "pronunciation": "ku", "meaning": "mouth"}, {"char": "ぐ", "pronunciation": "gu", "meaning": "shoe"}],
    "ke": [{"char": "け", "pronunciation": "ke", "meaning": "hair"}, {"char": "げ", "pronunciation": "ge", "meaning": "fur"}],
    "ko": [{"char": "こ", "pronunciation": "ko", "meaning": "child"}, {"char": "ご", "pronunciation": "go", "meaning": "go"}],
    
    # S/Z column (base + voiced)
    "sa": [{"char": "さ", "pronunciation": "sa", "meaning": "work"}, {"char": "ざ", "pronunciation": "za", "meaning": "seat"}],
    "shi": [{"char": "し", "pronunciation": "shi", "meaning": "death"}, {"char": "じ", "pronunciation": "ji", "meaning": "time"}],
    "su": [{"char": "す", "pronunciation": "su", "meaning": "vinegar"}, {"char": "ず", "pronunciation": "zu", "meaning": "cool"}],
    "se": [{"char": "せ", "pronunciation": "se", "meaning": "small river"}, {"char": "ぜ", "pronunciation": "ze", "meaning": "is"}],
    "so": [{"char": "そ", "pronunciation": "so", "meaning": "hemp"}, {"char": "ぞ", "pronunciation": "zo", "meaning": "like"}],
    
    # T/D column (base + voiced)
    "ta": [{"char": "た", "pronunciation": "ta", "meaning": "rice field"}, {"char": "だ", "pronunciation": "da", "meaning": "who"}],
    "chi": [{"char": "ち", "pronunciation": "chi", "meaning": "blood"}, {"char": "ぢ", "pronunciation": "ji", "meaning": "ground"}],
    "tsu": [{"char": "つ", "pronunciation": "tsu", "meaning": "canoe"}, {"char": "づ", "pronunciation": "dzu", "meaning": "clothing"}],
    "te": [{"char": "て", "pronunciation": "te", "meaning": "hand"}, {"char": "で", "pronunciation": "de", "meaning": "exit"}],
    "to": [{"char": "と", "pronunciation": "to", "meaning": "door"}, {"char": "ど", "pronunciation": "do", "meaning": "place"}],
    
    # N column (no variants)
    "na": [{"char": "な", "pronunciation": "na", "meaning": "greens"}],
    "ni": [{"char": "に", "pronunciation": "ni", "meaning": "load"}],
    "nu": [{"char": "ぬ", "pronunciation": "nu", "meaning": "slave"}],
    "ne": [{"char": "ね", "pronunciation": "ne", "meaning": "root"}],
    "no": [{"char": "の", "pronunciation": "no", "meaning": "field"}],
    
    # H/B/P column (base + voiced + half-voiced)
    "ha": [{"char": "は", "pronunciation": "ha", "meaning": "leaf"}, {"char": "ば", "pronunciation": "ba", "meaning": "horse"}, {"char": "ぱ", "pronunciation": "pa", "meaning": "wave"}],
    "hi": [{"char": "ひ", "pronunciation": "hi", "meaning": "fire"}, {"char": "び", "pronunciation": "bi", "meaning": "America"}, {"char": "ぴ", "pronunciation": "pi", "meaning": "skin"}],
    "fu": [{"char": "ふ", "pronunciation": "fu", "meaning": "rain"}, {"char": "ぶ", "pronunciation": "bu", "meaning": "culture"}, {"char": "ぷ", "pronunciation": "pu", "meaning": "part"}],
    "he": [{"char": "へ", "pronunciation": "he", "meaning": "arm"}, {"char": "べ", "pronunciation": "be", "meaning": "hen"}, {"char": "ぺ", "pronunciation": "pe", "meaning": "pen"}],
    "ho": [{"char": "ほ", "pronunciation": "ho", "meaning": "step"}, {"char": "ぼ", "pronunciation": "bo", "meaning": "lake"}, {"char": "ぽ", "pronunciation": "po", "meaning": "store"}],
    
    # M column (no variants)
    "ma": [{"char": "ま", "pronunciation": "ma", "meaning": "demon"}],
    "mi": [{"char": "み", "pronunciation": "mi", "meaning": "eye"}],
    "mu": [{"char": "む", "pronunciation": "mu", "meaning": "nothing"}],
    "me": [{"char": "め", "pronunciation": "me", "meaning": "eye"}],
    "mo": [{"char": "も", "pronunciation": "mo", "meaning": "hair"}],
    
    # Y column (no variants, missing yi/ye)
    "ya": [{"char": "や", "pronunciation": "ya", "meaning": "arrow"}],
    "yu": [{"char": "ゆ", "pronunciation": "yu", "meaning": "hot water"}],
    "yo": [{"char": "よ", "pronunciation": "yo", "meaning": "night"}],
    
    # R column (no variants)
    "ra": [{"char": "ら", "pronunciation": "ra", "meaning": "bad"}],
    "ri": [{"char": "り", "pronunciation": "ri", "meaning": "advantage"}],
    "ru": [{"char": "る", "pronunciation": "ru", "meaning": "tear"}],
    "re": [{"char": "れ", "pronunciation": "re", "meaning": "tear"}],
    "ro": [{"char": "ろ", "pronunciation": "ro", "meaning": "road"}],
    
    # W column (no variants, missing wi/we)
    "wa": [{"char": "わ", "pronunciation": "wa", "meaning": "ring"}],
    "wo": [{"char": "を", "pronunciation": "wo", "meaning": "tail"}],
    
    # N-sound
    "n": [{"char": "ん", "pronunciation": "n", "meaning": "what"}]
}

# Main list for individual wallpaper generation (one entry per character we'll highlight)
HIRAGANA_DATA = []
for sounds in HIRAGANA_CHART_DATA.values():
    for entry in sounds:
        HIRAGANA_DATA.append(entry)

# Color scheme (dark theme with 3 colors)
COLORS = {
    "background": "#1a1a1a",      # Very dark gray/black
    "text_primary": "#ffffff",    # White
    "text_secondary": "#888888"   # Medium gray
}
