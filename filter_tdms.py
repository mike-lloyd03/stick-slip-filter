from os import path
import pandas as pd
import numpy as np
from pandas import ExcelWriter
from pandas import ExcelFile
from nptdms import TdmsFile

from make_group_plots import make_group_plots

def filter_and_interpolate_data(path_to_file, export_excel=True):
    '''
    Reads in data from a TDMS file, filters out all sequential duplicates,
    and breaks the data up into multiple groups of data.

    Parameters:
    path_to_file (str): A relative or absolute path to the TDMS file to filter

    '''
    pd.options.mode.chained_assignment = None  # default='warn'

    # Read in the TDMS file and set some file name variables we'll use later
    print('Reading TDMS file...', end='\r')
    tdms_file_name = path.splitext(path.basename(path_to_file))[0]
    saving_dir = path.dirname(path_to_file)
    tdms_file = TdmsFile(path_to_file)
    output_file = path.join(saving_dir, tdms_file_name + '_Filtered')
    data_blocks = ((0, 25), (490, 500), (990, 1000))

    # Get the test details from the TDMS file
    test_number = tdms_file.properties['Test Number']
    sample_number = tdms_file.properties['Sample Number']
    description = tdms_file.properties['Description']
    test_title = f"{test_number}-{sample_number} {description}"

    # Create a list of dataframes from each TDMS group
    tdms_data = [group.as_dataframe() for group in tdms_file.groups()]
    tdms_group_names = [group.name for group in tdms_file.groups()]

    dynamic_data = tdms_data[1]

    # Filter out all rows where the CoF value is equal to that in the following row
    print('Filtering data...', end='\r')
    filtered_data = dynamic_data[dynamic_data.CoF != dynamic_data.shift(periods=1, axis=0).CoF]

    # If the next value is greater than the current value by more than 0.5, add 0.5 to it
    # this prevents the interpolator from interpolating between large gaps due to steps in the data
    large_step_arr = (filtered_data.shift(periods=-1, axis=0)['Cycle Count']
                      - filtered_data['Cycle Count'] > .5)
    filtered_data.loc[large_step_arr, 'Cycle Count'] = \
        filtered_data.loc[large_step_arr, 'Cycle Count'] + .5

    # Remove the cycle count values that are duplicates leaving
    # only the first in the range of duplicates
    duplicate_cycle_values = filtered_data['Cycle Count'] == \
        filtered_data.shift(periods=1, axis=0)['Cycle Count']
    filtered_data.loc[duplicate_cycle_values, 'Cycle Count'] = np.nan
    if np.isnan(filtered_data.iloc[-1]['Cycle Count'].item()):
        filtered_data.iloc[-1]['Cycle Count'] = max(filtered_data['Cycle Count']) + .5

    # Interpolate the remaining values
    print('Interpolating cycle counts', end='\r')
    filtered_data['Cycle Count'] = filtered_data['Cycle Count'].interpolate(
        method='values', limit_direction='forward')

    # Append the new dataframe to the tdms_data list
    tdms_data.append(filtered_data)
    tdms_group_names.append('Filtered Data')

    # Create new dataframes with defined blocks of data
    print('Building dataframes...', end='\r')
    for block in data_blocks:
        data_block = filtered_data[(filtered_data['Cycle Count'] >= min(block))
                                   & (filtered_data['Cycle Count'] <= max(block))]
        if len(data_block):
            tdms_data.append(data_block)
        tdms_group_names.append(f'Filtered Data {min(block)} to {max(block)}')

    print('Saving plots...', end='\r')
    output_plot = make_group_plots(data_blocks, tdms_data[3:], test_title)
    output_plot.savefig(output_file + '.png')
    output_plot.close()

    if export_excel:
        # Save the dataframes as separate worksheets in a new Excel file
        print('Saving filtered Excel file...', end='\r')
        with ExcelWriter(output_file + '.xlsx') as writer:
            for df, name in zip(tdms_data, tdms_group_names):
                df.to_excel(writer, sheet_name=name, index=False)
            writer.save()

    print(f"------{path_to_file} Complete------")

    print(path.basename(output_file))
    return path.basename(output_file) + '.png'

if __name__=="__main__":
    input_file = ''
    if not input_file:
        input_file = input("Enter path to file: ")
    filter_and_interpolate_data(input_file)
