#!/usr/bin/env python3

import pandas as pd
import mysql.connector
import glob
import sys
import os
import csv
from INSERT_templates import create_gex_insert_statement, create_arc_insert_statement, create_visium_insert_statement, create_vdj_t_insert_statement, create_abc_insert_statement, create_ch_insert_statement, create_vdj_b_insert_statement, create_visium_ffpe_insert_statement, create_abc_ch_insert_statement, create_atac_insert_statement
from VALUES_templates import create_gex_values_statement, create_arc_values_statement, create_visium_values_statement, create_vdj_t_values_statement, create_abc_values_statement, create_ch_values_statement, create_vdj_b_values_statement, create_visium_ffpe_values_statement, create_abc_ch_values_statement, create_atac_values_statement

# make DB connection global
# database credentials
cnx = mysql.connector.MySQLConnection(user = "ngs_stats", password = "CliffsOfInsanity87!", host = "localhost", database = "ngs_stats")
cursor = cnx.cursor()



def get_all_csv_files(run_id):
	"""
	This function grabs the csv metrics summary files 
	to be parsed and stored in NGS_STATS
	"""
	# grab the renamed metrics summary csv files
	csv_directory = "/home/nabors/STATS/CELLRANGER/{}___P*.csv".format(run_id)
	csv_files = glob.glob(csv_directory)
	return(csv_files)

	
def post_csv_data_to_db(csv_files):
	"""
	This function grabs the metric summary csv file,
	parses the dat and then stores the data into the
	NGS_STATS database
	"""
	for csv_file in csv_files:
		csv_file_data = pd.read_csv(csv_file)
		cellranger_case = csv_file.split("___")[-1:][0]
		
		print(csv_file)
		
		# decision statements to choose the right function for the type of
		# metrics summary file
		if cellranger_case == "GEX.csv":
			insert_statement = post_gex_data_to_db(csv_file, csv_file_data)
		if cellranger_case == "VDJ_T.csv":
			insert_statement = post_vdj_t_data_to_db(csv_file, csv_file_data)
		if cellranger_case == "VISIUM.csv":
			insert_statement = post_visium_data_to_db(csv_file, csv_file_data)
		if cellranger_case == "ARC.csv":
			insert_statement = post_arc_data_to_db(csv_file, csv_file_data)
		if cellranger_case == "ABC.csv":
			insert_statement = post_abc_data_to_db(csv_file, csv_file_data)
		if cellranger_case == "CH.csv":
			insert_statement = post_ch_data_to_db(csv_file, csv_file_data)
		if cellranger_case == "VDJ_B.csv":
			insert_statement = post_vdj_b_data_to_db(csv_file, csv_file_data)
		if cellranger_case == "VISIUM_FFPE.csv":
			insert_statement = post_visium_ffpe_data_to_db(csv_file, csv_file_data)
		if cellranger_case == "ABC_CH.csv":
			insert_statement = post_abc_ch_data_to_db(csv_file, csv_file_data)
		if cellranger_case == "ATAC.csv":
			insert_statement = post_atac_data_to_db(csv_file, csv_file_data)
											
		# commit record to db
		cursor.execute(insert_statement)
		cnx.commit()
		
		
				
def post_gex_data_to_db(csv_file, csv_file_data):
	"""
	This function take the csv file, parses it and stores
	the data into the GEX table.
	"""
	values_statement = create_gex_values_statement(csv_file, csv_file_data)
	insert_statement = create_gex_insert_statement(values_statement)
	return(insert_statement)

	
def post_arc_data_to_db(csv_file, csv_file_data):
	"""
	This function take the csv file, parses it and stores
	the data into the ARC table.
	"""
	values_statement = create_arc_values_statement(csv_file, csv_file_data)
	insert_statement = create_arc_insert_statement(values_statement)
	return(insert_statement)


def post_visium_data_to_db(csv_file, csv_file_data):
	"""
	This function take the csv file, parses it and stores
	the data into the VISIUM table.
	"""
	values_statement = create_visium_values_statement(csv_file, csv_file_data)
	insert_statement = create_visium_insert_statement(values_statement)
	return(insert_statement)

	
def post_vdj_t_data_to_db(csv_file, csv_file_data):
	"""
	This function take the csv file, parses it and stores
	the data into the VDJ table.
	"""
	values_statement = create_vdj_t_values_statement(csv_file, csv_file_data)
	insert_statement = create_vdj_t_insert_statement(values_statement)
	return(insert_statement)

				
def post_abc_data_to_db(csv_file, csv_file_data):
	"""
	This function take the csv file, parses it and stores
	the data into the ABC table.
	"""
	values_statement = create_abc_values_statement(csv_file, csv_file_data)
	insert_statement = create_abc_insert_statement(values_statement)
	return(insert_statement)

	
def post_ch_data_to_db(csv_file, csv_file_data):
	"""
	This function take the csv file, parses it and stores
	the data into the CH table.
	"""
	values_statement = create_ch_values_statement(csv_file, csv_file_data)
	insert_statement = create_ch_insert_statement(values_statement)
	return(insert_statement)


def post_vdj_b_data_to_db(csv_file, csv_file_data):
	"""
	This function take the csv file, parses it and stores
	the data into the VDJ-BCR table.
	"""
	values_statement = create_vdj_b_values_statement(csv_file, csv_file_data)
	insert_statement = create_vdj_b_insert_statement(values_statement)
	return(insert_statement)


def post_visium_ffpe_data_to_db(csv_file, csv_file_data):
	"""
	This function take the csv file, parses it and stores
	the data into the VISIUM-FFPE table.
	"""
	values_statement = create_visium_ffpe_values_statement(csv_file, csv_file_data)
	insert_statement = create_visium_ffpe_insert_statement(values_statement)
	return(insert_statement)

	
def post_abc_ch_data_to_db(csv_file, csv_file_data):
	"""
	This function take the csv file, parses it and stores
	the data into the ABC table.
	"""
	values_statement = create_abc_ch_values_statement(csv_file, csv_file_data)
	insert_statement = create_abc_ch_insert_statement(values_statement)
	return(insert_statement)


def post_atac_data_to_db(csv_file, csv_file_data):
	"""
	This function take the csv file, parses it and stores
	the data into the ATAC table.
	"""
	values_statement = create_atac_values_statement(csv_file, csv_file_data)
	insert_statement = create_atac_insert_statement(values_statement)
	return(insert_statement)




def main(run_id):
	"""
	This is main function.  It will take the run_id
	and get the cvs files of the metrics from 10X pipelines
	and pass those data of to the correct functions for 
	parsing
	"""
	print("Getting CSV files for run >> {}".format(run_id))
	
	csv_files = get_all_csv_files(run_id)
	
	post_csv_data_to_db(csv_files)



if __name__ == "__main__":
	"""
	This script finds the metrics summary csv files
	and parses them and inserts those data
	into NGS_STATS
	"""
	# grab the run ID
	run_id = sys.argv[1]
	
	main(run_id)