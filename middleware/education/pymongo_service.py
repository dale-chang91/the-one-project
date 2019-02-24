#!/bin/python

import pymongo

COLORADO_EDUCATION_DB = "colorado_education_db"
MATH_TCAP_GT_2014_COLLECTION = "math_tcap_gt_2014"

mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")

# Creates database if doesn't exist
colorado_db = mongo_client[COLORADO_EDUCATION_DB]

# Create collection
# Currently a collection corresponds to a single document until we find a better way to normalize the data
collection = colorado_db[MATH_TCAP_GT_2014_COLLECTION]

#####
# Common methods
#####

def add_single_record(db_name, collection_name, record):
  
  return
