import smartsheet
from auth import TOKEN,FILE_NAME,SMART_SHEET_NAME
import os.path

def main():
  #Log into API
  try:
    smartsheet_client = smartsheet.Smartsheet(TOKEN)
  except ValueError:
    print('Please Enter your Token in the auth.py file.')
    return
  response = smartsheet_client.Sheets.list_sheets()
  sheets = response.data


  #Get information
  file_name =   FILE_NAME
  sheet_name = SMART_SHEET_NAME


  #Find the target sheet in all possible sheets
  for i in sheets:
    if i.name == sheet_name:



    #verify sheet exists in path first
      try:
        assert os.path.isfile(file_name)
      except AssertionError:
        print('Origin file does not exist, create or check input....killing program')
        return



    #delete old sheet
      smartsheet_client.Sheets.delete_sheet(i.id) 
    else:
      print("Sheet Not Found")

  #upload updated sheet
  imported_sheet = smartsheet_client.Sheets.import_csv_sheet('test.csv','test',header_row_index=0)


main()
