import os
from os import path
import unittest
import shutil
from evernote_generator import EvernoteGenerator

class EvernoteGeneratorUnitTest(unittest.TestCase): 

    def setUp(self): 
        self.mockup_base_dir = "/Users/triettran/playground/joplin-to-evernote-converter/test-mockup"
        self.mockup_joplin_dir = self.mockup_base_dir + "/joplin-dir"
        self.mockup_evernote_dir = self.mockup_base_dir + "/evernote-dir"
        os.mkdir(self.mockup_evernote_dir)
        os.mkdir(self.mockup_joplin_dir)
        for i in range(1,5,1):
            os.mkdir(self.mockup_joplin_dir + '/notebook-' + str(i))
        self.eg = EvernoteGenerator(self.mockup_evernote_dir)
    def tearDown(self): 
        shutil.rmtree(self.mockup_evernote_dir)
        shutil.rmtree(self.mockup_joplin_dir)

    def test_can_write_notebook_with_specified_name_to_disk(self):
        self.eg.add_notebook("evernote-1") 
        self.assertEqual(len(os.listdir(self.mockup_evernote_dir)),1)
        self.assertTrue(path.exists(self.eg.evernote_dir + "/evernote-1"))


if __name__ == '__main__': 
    unittest.main(warnings='ignore') 