import shutil
import os

from datetime import datetime
from argument_parser.get_path import get_file_path

class backingUpFolder:

    def updateName(self, file):
        file_without_extension = os.path.splitext(file)[0]
        file_extension = os.path.splitext(file)[1]
        current_datetime = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
        new_file_path = file_without_extension + '_' + str(current_datetime) + file_extension
        return new_file_path
    
    def main(self):
        source_path = get_file_path()
        destination_path = '/Users/divyank31agoyalgmail.com/Documents/backup/' + os.path.basename(source_path);
        if os.path.exists(destination_path):
            destination_path = self.updateName(destination_path) 
        shutil.copyfile(source_path, destination_path)
        
if __name__ == '__main__':
    backingUpFolder_obj = backingUpFolder()
    backingUpFolder_obj.main()
