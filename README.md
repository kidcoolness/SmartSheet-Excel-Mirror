# SmartSheet-Excel-Mirror
This program easily replaces a existing smartsheet with a version located on your desktop. 

Setup:
  pip install smartsheet-python-sdk
  
  Place your smartsheet API token inside the auth.py file
  
  ENSURE your excel document is backed up and present in the same directory as the script. 
  
This script is meant to be run from the command line, it can be ran from an IDE if nessecary. 

For python 3.10 users a change needs to be made to the types.py in the smartsheet folder.
  line 18: needs to be colelctions.abc
  line 29: needs to be class TypedList(collections.abc.MutableSequence):




