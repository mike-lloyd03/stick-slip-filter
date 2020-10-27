# Stick Slip Batch Filter

## How to Use
There are three Python scripts in here. The only one you really need to use is `batch_filter.py`. If Python is installed correctly on your system, you _should_ be able to to just drag and drop `.tdms` files onto `batch_filter.py`. You should also be able to drag multiple files at a time onto this script. If you shift-select more than one `.tdms` file and drop it on the script, it'll run through all the files and generate images and Excel files. The script will process the data and save an image file and a new Excel file in the same location as the `.tdms` file. These files will have the same name as the tdms file but will have "_Filtered" appended to the end.

### Download
Towards the top of this page you should see a green button titled `Code`. Click that and select "Download ZIP". This will be a zip of all the files that you need to run the filter script.

### Dependencies
Anaconda is a distribution of Python that includes just about everything you need with it. Unfortunately, it doesn't come with the dependency we need for reading `.tdms` files. Fortunately, it comes with a package manager that will install it for us. Open the Anaconda Navigator. Click on `Qt Console` and when the prompt loads, enter the following lines of code hitting enter after each line (there will be a bunch of stuff happenning after each line):

```bash
conda install -c conda-forge nptdms
conda install openpyxl
```

This will install the tdms package we need and another one (openpyxl) for exporting to Excel. Chances are that if you're on the company network, the dependencies won't install because of a network error or something. There's a way to overcome this by editing some configuration files but the easier way is to just jump off the company network and install it on regular wifi. You can use a phone hotspot. In addition to choosing another network in the wifi menu, you'll also need to either take your laptop off the dock or unplug the ethernet cable plugged into the dock.

### File Structure
There are only three files that do all the magic:
1. `batch_filter.py`: This file reads in the files you drop on it and runs the filter script on each file.
2. `filter_tdms.py`: This script actually does all the math and data processing. After the data is processed, it sends the data to the next file for graphing.
3. `make_group_plots.py`: This script generates the plots. It's where you can modify the axis ranges and stuff. The plotting syntax is a lot like plotting in Matlab so if you want to edit things, it'll be similar to that. It uses the `matplotlib` library.

## If No Worky
If drag and drop doesn't do anything or you can't drag and drop, it's likely that Python is not configured to open `.py` files in Windows. All you should have to do is right click on the `.py` file, select "Open with", then "Choose another app". From here, select "Python Launcher" or "Python 3 Launcher". There should be a checkbox for "Make this my default" or some such nonsense. Click that. You should be good to go now. If it still doesn't work, we may need to do more technical things. Text/email me.

## Say You Don't Want Excel Files...
Exporting to Excel is processor intensive and actually takes a few seconds to do. If you were to run this script on like 20 files, it'll take a while because of the Excel export. You can deactivate the Excel export pretty easily if you only want images and are impatient.

Python `.py` files are really just text files. You can edit the code just opening `batch_filter.py` in Notepad and changing the following text from:

```python
for file in file_list:
    filter_and_interpolate_data(file, export_excel=True)
```
to:

```python
for file in file_list:
    filter_and_interpolate_data(file, export_excel=False)
```

You're just changing `True` to `False`.

## Modifying the Code
I put comments throughout the document (any line that begins with `#` is a comment). This should help walk you through the code and you can make changes wherever you need to. If you screw it up, you can just download this repository again. Python is a user friendly language in that it should be pretty readable. Sometimes it's not but Google is your friend (actually Google is reading all your emails and tracking all your web usage and is not your friend but that's another conversation.)

### Code Editors
Again, you can edit any of these files with just any text editor. But there's some cool tools that help make editing the code easier. Spyder is a coding program which comes installed with Anaconda and is kinda popular among data science people. If you open the Anaconda Navigator, it should be in there. Microsoft Visual Studio Code is probably the most popular code editor in the world and is pretty cool too. These tools help highlight where you made errors and how to fix them or they make suggestions for you while you type.

## Summary
1. Download and unzip the code file
2. Install the `nptdms` and `openpyxl` packages on the command line
3. Drag and drop `.tdms` files onto `batch_filter.py`
4. ...
5. Profit
