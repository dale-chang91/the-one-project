#!/bin/python

import .constants

# Reading-TCAP-Gender-2014.csv
# ${subject}-${program}-${aggregation}-${year}

FILENAME_SEPARATOR = '-'

# eventually convert these into database items
SUBJECTS = ['Reading', 'Writing', 'Math', 'Science', 'Lectura', 'Escritura']
PROGRAMS = ['CSAP', 'TCAP']
AGGREGATIONS = ['Gender', 'ETH', 'FRLUN', 'IEP', 'LANGPROF', 'MIGRANT', 'GT']
YEARS = ['2014', '2013', '2012', '2011', '2010', '2009']

class FileParts():
  '''
    
  '''
  __init__(self, filename):
    base_filename = filename.replace('.csv', '')
    filename_parts = base_filename.split(FILENAME_SEPARATOR)

    if len(filename_parts) == 4:
      self.subject = filename_parts[0]
      self.program = filename_parts[1]
      self.aggregation = filename_parts[2]
      self.year = filename_parts[3]
    else:
      raise ValueError("Filename does not have four parts")
