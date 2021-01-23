import os
class EvernoteGenerator:

    def __init__(self, evernote_dir):
        self.evernote_dir = evernote_dir
        print("evernote notebooks will be written to {}".format(self.evernote_dir))
        pass

    def add_notebook(self, nb_name):
        filename = nb_name
        with open(os.path.join(self.evernote_dir, filename), 'w') as temp_file:
            temp_file.write("some-content")
        pass
