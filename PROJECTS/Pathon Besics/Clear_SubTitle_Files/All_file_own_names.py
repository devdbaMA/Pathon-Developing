import re
import glob
import os

# Specify the directory path
directory_path = r"D:\My_DOC\data_text\Clear_text"

def clean_subtitle_files(input_files):
    for path_file in input_files:
        cleaned_lines = []
        with open(path_file, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        for line in lines:
            # Remove timestamps
            line = re.sub(r'\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}', '', line)
            # Remove line numbers
            line = re.sub(r'^\d+$', '', line)
            # Remove extra spaces
            line = line.strip()
            if line:  # Only add non-empty lines
                cleaned_lines.append(line)

        cleaned_text = ' '.join(cleaned_lines)

        # Create output file name with .txt extension
        base_name = os.path.basename(path_file)
        file_name, _ = os.path.splitext(base_name)
        output_file = os.path.join(directory_path, f"{file_name}.txt")

        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(cleaned_text)

# Usage example:
input_files = glob.glob(r"D:\My_DOC\data_text\Clear_text\*.srt")
clean_subtitle_files(input_files)
