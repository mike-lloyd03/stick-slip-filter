# Stick Slip Batch Filter

## How to Use
There are three python scripts in here. The only one you really need to use is `batch_filter.py`. If Python is installed correctly on your system, you _should_ be able to to just drag and drop `.tdms` files onto `batch_filter.py`. You should also be able to drag multiple files at a time onto this script. If you shift-select more than one `.tdms` file and drop it on the script, it'll run through all the files and generate images and excel files.

## If No Worky
If drag and drop doesn't do anything or you can't drag and drop, it's likely that Python is not configured to open `.py` files in Windows. All you should have to do it right click and `.py` file, select "Open with", then "Choose another app". From here, select "Python Launcher" or "Python 3 Launcher". There should be a checkbox for "Make this my default" or some such nonsense. Click that. You should be good to go now. If it still doesn't work, we may need to do more technical things. Text/email me.

## Say You Don't Want Excel Files...
Exporting to Excel is processor intensive and actually takes a few seconds to do. Making a `.png` file takes only a few ms. If you were to run this script on like 20 files, it'll slow down because of the Excel export. You can deactivate it pretty easily.
Python `.py` files are really just text files. You too can be a hax0r coder by just opening `batch_filter.py` in Notepad and changing the following text from:
```python
for file in file_list:
    filter_and_interpolate_data(file, export_excel=True)
```
to:

```python
for file in file_list:
    filter_and_interpolate_data(file, export_excel=False)
```

You're just changing `True` to `False` incase you missed it.

## Say you wanna do more stuff with this...
I put comments throughout the document (any line that begins with `#` is a comment). This should help walk you through the code and you can make changes wherever you need to. If you screw it up, you can just download this repository again. Python is a user friendly language in that it should be pretty readable. Sometimes it's not but Google is your friend (actually Google is reading all your emails and tracking all your web usage and is not your friend but that's another conversation.)

### Code Editors
Again, you can edit any of these files with just any text editor. But there's some cool tools that help make editing the code easier. Spyder is a coding program which comes installed with Anaconda and is kinda popular among data science people. If you open the Anaconda Navigator, it should be in there. Microsoft Visual Studio Code is probably the most popular code editor in the world and is pretty cool too. These tools help highlight where you made errors and how to fix them or they make suggestions for you while you type.
