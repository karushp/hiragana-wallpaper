"""
Tests for the wallpaper generation functionality.
"""

import unittest
import os
import sys
import shutil

# Add the src directory to the path so we can import our modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from hiragana_wallpaper import HIRAGANA_DATA, generate_wallpaper, create_output_directory

class TestGenerator(unittest.TestCase):
    """Test cases for wallpaper generation."""
    
    def test_create_output_directory(self):
        """Test that output directory is created."""
        test_dir = "test_output"
        try:
            create_output_directory(test_dir)
            self.assertTrue(os.path.exists(test_dir))
            # Clean up - remove files first, then directory
            shutil.rmtree(test_dir)
        except Exception as e:
            self.fail(f"create_output_directory() raised an exception: {e}")
    
    def test_generate_wallpaper(self):
        """Test wallpaper generation with a sample character."""
        test_dir = "test_output"
        
        # Create test directory
        create_output_directory(test_dir)
        
        # Use the first character for testing
        test_char = HIRAGANA_DATA[0]
        
        try:
            wallpaper = generate_wallpaper(test_char)
            self.assertIsNotNone(wallpaper)
            # Check that it's a PIL Image
            self.assertTrue(hasattr(wallpaper, 'save'))
            
            # Test saving the wallpaper
            test_filename = f"{test_dir}/test_wallpaper.png"
            wallpaper.save(test_filename, "PNG", quality=95)
            
            # Verify file was created
            self.assertTrue(os.path.exists(test_filename))
            
            print(f"✅ Generated test wallpaper: {test_filename}")
            
        except Exception as e:
            self.fail(f"generate_wallpaper() raised an exception: {e}")
        # Note: Not cleaning up test files so you can inspect the generated wallpaper
    
    def test_data_structure(self):
        """Test that hiragana data is properly structured."""
        self.assertIsInstance(HIRAGANA_DATA, list)
        self.assertGreater(len(HIRAGANA_DATA), 0)
        
        # Check first character structure
        first_char = HIRAGANA_DATA[0]
        required_keys = ['char', 'pronunciation', 'meaning']
        for key in required_keys:
            self.assertIn(key, first_char)
            self.assertIsInstance(first_char[key], str)

if __name__ == '__main__':
    unittest.main()
