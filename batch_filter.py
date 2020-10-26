import sys
from filter_tdms import filter_and_interpolate_data

print('Running batch filter...')
# Get a list of files which were dropped on the script
file_list = sys.argv[1:]

# Strip out any files that don't end in 'tdms' because I don't know 
# what would happen if we ran this on another filetype but it would
# probably be bad
file_list = [file_name
             for file_name in file_list
             if file_name[-4:] == 'tdms']

for file in file_list:
    filter_and_interpolate_data(file, export_excel=False)

print("Batch process done")
