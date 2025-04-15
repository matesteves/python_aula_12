import os
import pandas as pd
from FilesSources import FilesSources

class TxtSource(FilesSources):
    def create_path(self):
        current_directory = os.getcwd()
        self.folder_path = os.path.join(current_directory, 'data', 'txt_files')
        if not os.path.exists(self.folder_path):
            os.makedirs(self.folder_path)

    def check_for_new_files(self):
        current_files = os.listdir(self.folder_path)
        new_files = [file for file in current_files if file not in self.previous_files and file.endswith('.txt')]

        if new_files:
            print("New txt files detected:", new_files)
            # Update the list of previous files
            self.previous_files = current_files
            self.get_data()
        else:
            print("No new txt files detected")

    def get_data(self):
        # Implement getting data from txt files in the specified folder
        data_frames = []
        for file_path in self.previous_files:
            try:
                path = os.path.join(self.folder_path, file_path)
                data = pd.read_csv(path, sep='\t')
                data_frames.append(data)
            except Exception as e:
                print("An error ocurred while reading the txt file:", e)
            if data_frames:
                self.combined_data = pd.concat(data_frames, ignore_index=True)
                print(self.combined_data)
                return self.combined_data
            else:
                return None