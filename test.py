# Install the smartsheet sdk with the command: pip install smartsheet-python-sdk
import smartsheet
import csv
import pandas as pd
from auth import TOKEN
from pprint import pprint
import os
import re
#if data local but not online ADD
#if data online but not Local DELETE
#data needs to be loaded into an IDENTICAL format

def download_ss():
  smartsheet_client = smartsheet.Smartsheet(TOKEN)
  response = smartsheet_client.Sheets.list_sheets()
  sheets = response.data
  target = int(sheets[0].id)
  #TODO ADD FUNC SO CLIENT CAN SEARCH BY NAME
  smartsheet_client.Sheets.get_sheet_as_csv(target,'C:\\Users\\ethan\\simpleSheetUpdate\\')

#THIS WILL BE A HELPER FUNCTION
#load excel data
def load_local(file_name):
  dic = {}
  idx = 1
  # pd.set_option('max_columns', None)
  data = pd.read_csv('test_.csv')
  for i in data.values:
    dic[idx] = i
    idx += 1
  return dic,data.columns

  


#load smartsheet data
def load_online():
  pass

#compare the two
def compare_data():
  pass

#perform add or remove
def update_smartsheet():
  pass

loc_dic,loc_col = load_local('test_.csv')

onl_dic,onl_col =  load_local('test.csv')