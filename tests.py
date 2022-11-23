import unittest
import os.path
from DOBFormGrab import DOBFormGrab, FORMS_URL, OUTPUT_FOLDER

dobFormGrab = DOBFormGrab()

class TestSettings(unittest.TestCase):

    def test_init_request(self,):
        self.assertTrue(dobFormGrab.status_code, 200)

    def test_output_folder_exists(self,):
        self.assertTrue(os.path.exists(OUTPUT_FOLDER))
    
    def test_links_exist(self,):
        self.assertTrue(len(dobFormGrab.links) > 0)
    

if __name__ == '__main__':
    unittest.main()