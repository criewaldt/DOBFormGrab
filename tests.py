import unittest
import os.path
from DOBFormGrab import DOBFormGrab, STATIC_FILE

class TestSettings(unittest.TestCase):

    def test_local_file_exists(self,):
        self.assertTrue(os.path.isfile(STATIC_FILE))

    
    


if __name__ == '__main__':
    unittest.main()