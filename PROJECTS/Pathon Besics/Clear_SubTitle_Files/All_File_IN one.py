import re
import glob


def clean_subtitle_files(input_files, output_file):
    cleaned_lines = []

    for path_file in input_files:
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

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(cleaned_text)

file_name = input("Enter file name ")
# Usage example:
input_files = glob.glob(r"D:\My_DOC\data_text\Clear_text\*.srt")
output_file = fr'D:\My_DOC\data_text\Clear_text\{file_name}.txt'

clean_subtitle_files(input_files, output_file)
