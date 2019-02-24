import csv
import json
import os

def csv_to_json(directory, original_csvfile):
  json_filename = original_csvfile.replace('.csv', '.json')

  json_array = []

  with open(original_csvfile) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
      json_array.extends(json.dumps(row))

  with open(json_filename) as jsonfile:
    json.dump(json_array, jsonfile, indent=2)

def convert_xlsx_to_csv(directory, filename):
  newfilename = filename.replace('xlsx', 'csv')
  os.system('xlsx2csv '+filename+' > '+newfilename)
