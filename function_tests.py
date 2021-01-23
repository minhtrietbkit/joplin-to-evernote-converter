import os
import unittest
import shutil
import main
class WriteToFile(unittest.TestCase): 

    def setUp(self): 
        self.mockup_base_dir = "/Users/triettran/playground/joplin-to-evernote-converter/test-mockup"
        self.mockup_joplin_dir = self.mockup_base_dir + "/joplin-dir"
        self.mockup_evernote_dir = self.mockup_base_dir + "/evernote-dir"
        os.mkdir(self.mockup_evernote_dir)
        os.mkdir(self.mockup_joplin_dir)
        self.mockup_number_of_joplin_nb = 5
        for i in range(0,self.mockup_number_of_joplin_nb,1):
            os.mkdir(self.mockup_joplin_dir + '/notebook-' + str(i))

    def tearDown(self): 
        shutil.rmtree(self.mockup_evernote_dir)
        shutil.rmtree(self.mockup_joplin_dir)
    def test_tool_can_generate_evernote_file_for_each_joplin_notebook(self):
        # I have run python main.py  <absolute-path-to-joplin-export-dir> <absoluate-path-to-evernote-output-dir>, now I run the test to verify that the evernote files are written correctly.
        # I expect the number of evernote files in output dir is the same as the number of directories in joplin dir
        main.main(self.mockup_joplin_dir,self.mockup_evernote_dir) 
        self.assertEqual(len(os.listdir(self.mockup_evernote_dir)),self.mockup_number_of_joplin_nb)

if __name__ == '__main__': 
    unittest.main(warnings='ignore') 