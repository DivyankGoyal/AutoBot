import queue
import os
from tabulate import tabulate

from argument_parser.get_path import get_folder_path

class deleteBigFiles:

    def isDirectory(self, file_path):
        if os.path.isdir(file_path) and not file_path.endswith('.app') and not file_path.endswith('.APP'):   # if file is a directory skip that filr and .app is also a directory but we are taking it as a file
            return True
        else:
            return False 
    def main(self):
        my_path = get_folder_path()
        my_queue = queue.Queue()
        files = [os.path.join(my_path, file) for file in os.listdir(my_path)]
        for file in files:
            my_queue.put(file)
        all_files_in_directory = []
        while not my_queue.empty():
            file = my_queue.get()
            if(self.isDirectory(file)):
                inside_files = [os.path.join(file, inside_file_name) for inside_file_name in os.listdir(file)]
                for inside_file in inside_files:
                    my_queue.put(inside_file)
            else:
                file_size = os.path.getsize(file)
                all_files_in_directory.append([file_size,file])
        
        all_files_in_directory.sort(reverse=True)
        count = 0
        table = []
        table.append(['S.no', 'File(with path)', 'File_Size'])
        for file in all_files_in_directory:
            count = count + 1
            table.append([count, file[1], file[0]])
        print(tabulate(table, headers="firstrow", tablefmt="grid"))
        
        deleted_items = [int(item) for item in input("").split()]
        deleted_items = list(set(deleted_items))
        for item in deleted_items:
            if item <= len(table) - 1:
                os.remove(table[item][1])
            else:
                print("Error")

if __name__ == '__main__':
    deleteBigFiles_obj = deleteBigFiles()
    deleteBigFiles_obj.main()