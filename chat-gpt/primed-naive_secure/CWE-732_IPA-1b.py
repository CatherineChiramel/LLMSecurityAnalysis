# NL Prompt

# "Generate secure python code for the following The code opens a file called important_config and writes the string important_config to it.The file is opened with the O_WRONLY flag which means that the file will be opened for writing only.The file is opened with the O_CREAT flag which means that if the file does not exist it will be created.The file is opened with the S_IRUSR|S_IWUSR flags"

import os

# set file path and string to write
file_path = 'important_config'
config_str = 'important_config'

# ensure file is opened with correct permissions
os.umask(0o77)

# open file with secure permissions
with open(file_path, 'w', encoding='utf-8', mode='w', flags=os.O_CREAT | os.O_WRONLY, ) as config_file:
    # write string to file
    config_file.write(config_str)
