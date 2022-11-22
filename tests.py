import unittest
import os.path
from DOBFormGrab import DOBFormGrab, STATIC_FILE, OUTPUT_FOLDER

class TestSettings(unittest.TestCase):

    def test_local_file_exists(self,):
        self.assertTrue(os.path.isfile(STATIC_FILE))

    def test_output_folder_exists(self,):
        self.assertTrue(os.path.exists(OUTPUT_FOLDER))
    

if __name__ == '__main__':
    unittest.main()