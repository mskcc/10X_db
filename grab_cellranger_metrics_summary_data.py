#!/usr/bin/env python3

import pandas as pd
import glob
import sys
import os
import csv
import pathlib
import time
import pox
from subprocess import call
import numpy as np
from datetime import datetime

# These are the column headings to match the columns to the csv file to determine what particular cellranger pipeline was run

VISIUM_FFPE = ['Number of Spots Under Tissue', 'Number of Reads', 'Mean Reads per Spot', 'Mean Reads Under Tissue per Spot', 'Fraction of Spots Under Tissue', 'Valid Barcodes', 'Valid UMIs', 'Sequencing Saturation', 'Q30 Bases in Barcode', 'Q30 Bases in Probe Read', 'Q30 Bases in UMI', 'Reads Mapped to Probe Set', 'Reads Mapped Confidently to Probe Set', 'Fraction Reads in Spots Under Tissue', 'Median Genes per Spot', 'Median UMI Counts per Spot', 'Genes Detected', 'Reads Mapped Confidently to the Filtered Probe Set', 'Number of Genes', 'Number of Genes >= 10 UMIs', "Reads Half-Mapped to Probe Set", "Reads Split-Mapped to Probe Set", "Estimated UMIs from Genomic DNA", "Estimated UMIs from Genomic DNA per Unspliced Probe"]

VISIUM = ['Number of Spots Under Tissue', 'Number of Reads', 'Mean Reads per Spot', 'Mean Reads Under Tissue per Spot', 'Fraction of Spots Under Tissue', 'Median Genes per Spot', 'Median UMI Counts per Spot', 'Valid Barcodes', 'Valid UMIs', 'Sequencing Saturation', 'Q30 Bases in Barcode', 'Q30 Bases in RNA Read', 'Q30 Bases in UMI', 'Reads Mapped to Genome', 'Reads Mapped Confidently to Genome', 'Reads Mapped Confidently to Intergenic Regions', 'Reads Mapped Confidently to Intronic Regions', 'Reads Mapped Confidently to Exonic Regions', 'Reads Mapped Confidently to Transcriptome', 'Reads Mapped Antisense to Gene', 'Fraction Reads in Spots Under Tissue', 'Total Genes Detected']

VDJ_T = ['Mean Read Pairs per Cell', 'Number of Cells With Productive V-J Spanning Pair', 'Number of Read Pairs', 'Valid Barcodes', 'Q30 Bases in Barcode', 'Q30 Bases in RNA Read 1', 'Q30 Bases in UMI', 'Reads Mapped to Any V(D)J Gene', 'Reads Mapped to TRA', 'Reads Mapped to TRB', 'Mean Used Read Pairs per Cell', 'Fraction Reads in Cells', 'Median TRA UMIs per Cell', 'Median TRB UMIs per Cell', 'Cells With Productive V-J Spanning Pair', 'Cells With Productive V-J Spanning (TRA, TRB) Pair', 'Paired Clonotype Diversity', 'Cells With TRA Contig', 'Cells With TRB Contig', 'Cells With CDR3-annotated TRA Contig', 'Cells With CDR3-annotated TRB Contig', 'Cells With V-J Spanning TRA Contig', 'Cells With V-J Spanning TRB Contig', 'Cells With Productive TRA Contig', 'Cells With Productive TRB Contig']

VDJ_B = ['Mean Read Pairs per Cell', 'Number of Cells With Productive V-J Spanning Pair', 'Number of Read Pairs', 'Valid Barcodes', 'Q30 Bases in Barcode', 'Q30 Bases in RNA Read 1', 'Q30 Bases in UMI', 'Reads Mapped to Any V(D)J Gene', 'Reads Mapped to IGH', 'Reads Mapped to IGK', 'Reads Mapped to IGL', 'Mean Used Read Pairs per Cell', 'Fraction Reads in Cells', 'Median IGH UMIs per Cell', 'Median IGK UMIs per Cell', 'Median IGL UMIs per Cell', 'Cells With Productive V-J Spanning Pair', 'Cells With Productive V-J Spanning (IGK, IGH) Pair', 'Cells With Productive V-J Spanning (IGL, IGH) Pair', 'Paired Clonotype Diversity', 'Cells With IGH Contig', 'Cells With IGK Contig', 'Cells With IGL Contig', 'Cells With CDR3-annotated IGH Contig', 'Cells With CDR3-annotated IGK Contig', 'Cells With CDR3-annotated IGL Contig', 'Cells With V-J Spanning IGH Contig', 'Cells With V-J Spanning IGK Contig', 'Cells With V-J Spanning IGL Contig', 'Cells With Productive IGH Contig', 'Cells With Productive IGK Contig', 'Cells With Productive IGL Contig']

GEX = ['Mean Reads per Cell', 'Median Genes per Cell', 'Number of Reads', 'Valid Barcodes', 'Sequencing Saturation', 'Q30 Bases in Barcode', 'Q30 Bases in RNA Read', 'Q30 Bases in UMI', 'Reads Mapped to Genome', 'Reads Mapped Confidently to Genome', 'Reads Mapped Confidently to Intergenic Regions', 'Reads Mapped Confidently to Intronic Regions', 'Reads Mapped Confidently to Exonic Regions', 'Reads Mapped Confidently to Transcriptome', 'Reads Mapped Antisense to Gene', 'Fraction Reads in Cells', 'Total Genes Detected', 'Median UMI Counts per Cell']

ARC = ['Genome', 'Pipeline version', 'Estimated number of cells', 'Feature linkages detected', 'Linked genes', 'Linked peaks', 'ATAC Confidently mapped read pairs', 'ATAC Fraction of genome in peaks', 'ATAC Fraction of high-quality fragments in cells', 'ATAC Fraction of high-quality fragments overlapping TSS', 'ATAC Fraction of high-quality fragments overlapping peaks', 'ATAC Fraction of transposition events in peaks in cells', 'ATAC Mean raw read pairs per cell', 'ATAC Median high-quality fragments per cell', 'ATAC Non-nuclear read pairs', 'ATAC Number of peaks', 'ATAC Percent duplicates', 'ATAC Q30 bases in barcode', 'ATAC Q30 bases in read 1', 'ATAC Q30 bases in read 2', 'ATAC Q30 bases in sample index i1', 'ATAC Sequenced read pairs', 'ATAC TSS enrichment score', 'ATAC Unmapped read pairs', 'ATAC Valid barcodes', 'GEX Fraction of transcriptomic reads in cells', 'GEX Mean raw reads per cell', 'GEX Median UMI counts per cell', 'GEX Median genes per cell', 'GEX Percent duplicates', 'GEX Q30 bases in UMI', 'GEX Q30 bases in barcode', 'GEX Q30 bases in read 2', 'GEX Q30 bases in sample index i1', 'GEX Q30 bases in sample index i2', 'GEX Reads mapped antisense to gene', 'GEX Reads mapped confidently to exonic regions', 'GEX Reads mapped confidently to genome', 'GEX Reads mapped confidently to intergenic regions', 'GEX Reads mapped confidently to intronic regions', 'GEX Reads mapped confidently to transcriptome', 'GEX Reads mapped to genome', 'GEX Reads with TSO', 'GEX Sequenced read pairs', 'GEX Total genes detected', 'GEX Valid UMIs', 'GEX Valid barcodes']

ATAC = ['Genome', 'Pipeline version', 'Estimated number of cells', 'Confidently mapped read pairs', 'Estimated bulk library complexity', 'Fraction of all fragments in cells', 'Fraction of all fragments that pass all filters and overlap called peaks', 'Fraction of genome in peaks', 'Fraction of high-quality fragments in cells', 'Fraction of high-quality fragments overlapping TSS', 'Fraction of high-quality fragments overlapping peaks', 'Fraction of transposition events in peaks in cells', 'Fragments flanking a single nucleosome', 'Fragments in nucleosome-free regions', 'Mean raw read pairs per cell', 'Median high-quality fragments per cell', 'Non-nuclear read pairs', 'Number of peaks', 'Percent duplicates', 'Q30 bases in barcode', 'Q30 bases in read 1', 'Q30 bases in read 2', 'Q30 bases in sample index i1', 'Sequenced read pairs', 'Sequencing saturation', 'TSS enrichment score', 'Unmapped read pairs', 'Valid barcodes']

# lists of the column names of the csv files and their associated extensions
ALL_METRICS_CSV_COLUMNS = [ARC, GEX, VDJ_T, VDJ_B, VISIUM, VISIUM_FFPE, ATAC]
EXTENSIONS = ["ARC.csv", "GEX.csv", "VDJ_T.csv", "VDJ_B.csv", "VISIUM.csv", "VISIUM_FFPE.csv", "ATAC.csv"]

# we do not want to process any directories or files with the contents of the DO NOT PROCESS list
DO_NOT_PROCESS = {"DONE", "12437", "15500"}


def grab_latest_metrics_csv(metrics_csv):
	"""
	This routine will determine the latest metrics_csv file
	if the cellranger pipeline was run multiple times on one sample
	"""
	print(metrics_csv)
	csv_sample_data = metrics_csv.split("/")
	# grab the sample ID
	sample_id = csv_sample_data[-3]
	# get the correct name of the csv file (metrics_summary.csv or summary.csv)
	real_csv_name = "{}/{}".format(csv_sample_data[-2], csv_sample_data[-1])

	print("&&&&&&&&&&&&")
	print(sample_id)
	print(real_csv_name)
	print("&&&&&&&&&&&&")
	
	sample_metrics_files = pox.find(sample_id, recurse = 3, root = "/igo/staging/CELLRANGER/")
	print(sample_metrics_files)
	
	timestamps = list()
	
	for smpl in sample_metrics_files:
		mtimestamp = os.path.getmtime(smpl)
		timestamps.append(mtimestamp)
	
	# get the index of the latest time stamp
	maxIndex = int(np.argmax(timestamps))
	
	# get csv file with latest time stamp
	csv_file_to_parse = sample_metrics_files[maxIndex]
	
	print(">>>>>>")
	print(csv_file_to_parse)
	print("<<<<<<")
	
	# grab the timestamp to put into a filename
	maxTimeStamp = datetime.fromtimestamp(timestamps[maxIndex])
	fileTimeStamp = maxTimeStamp.strftime("%Y-%m-%d_%H-%M-%S")
	
	# store the metrics file data into a list
	metricsCsvFileData = list()
	metricsCsvFileData.append("{}/{}".format(csv_file_to_parse, real_csv_name))
	metricsCsvFileData.append(fileTimeStamp)
	
	print("*****")
	print(metricsCsvFileData)
	print("*****")
	
	return(metricsCsvFileData)



def get_library_type(multi_metrics_csv, multi_extension):
	"""
	This routine gets the library type of a csv file that has been processed 
	thru the cellranger multi pipeline which includes:
	Antibody Capture
	Multiplexing Capture
	"""
	library_type = pd.read_csv(multi_metrics_csv, usecols = ["Library Type"])
	library_type_list = library_type["Library Type"].tolist()
	if ("Antibody Capture") in library_type_list:
		multi_extension["capture_data"] = True
		multi_extension["extension"] = "ABC.csv"
	if ("Multiplexing Capture") in library_type_list:
		multi_extension["capture_data"] = True
		multi_extension["extension"] = "CH.csv"
	if (("Antibody Capture" in library_type_list) and ("Multiplexing Capture" in library_type_list)):
		multi_extension["capture_data"] = True
		multi_extension["extension"] = "ABC_CH.csv"
	
	return(multi_extension)


def get_multi_projects(cellranger_outs_dir, cellranger_run_dir):
	"""
	This function grabs the projects that potentially have had the 
	cellranger multi pipeline run on its samples
	"""
	# lets find the multi cellranger multi project directories and rename those metrics summary csv files
	cellranger_outs_dir = glob.glob(cellranger_outs_dir)
	cellranger_project_dirs = set(os.listdir(cellranger_run_dir))
	
	# find the project that had a metrics summary file
	projects_with_metrics_csvs = set()
	for metrics_csv in cellranger_outs_dir:
		project = metrics_csv.split("/")[5]
		projects_with_metrics_csvs.add(project)
		
	# grab the projects that don't have an outs directory
	projects_without_outs_dir = cellranger_project_dirs.difference(projects_with_metrics_csvs)
	
	# grab the potential projects that have multi output
	multi_projects = set()
	for  project_without_outs_dir in projects_without_outs_dir:
		if (not any(request_id in project_without_outs_dir for request_id in DO_NOT_PROCESS)):
			multi_projects.add(project_without_outs_dir)
			
	# add any projects that have a "step1 file attached to it"
	step1_prjs = set()
	pipeline_dir = "/igo/staging/PIPELINE"
	for mprj in multi_projects:
		step1_dir = "{}_step1".format(mprj)
		pipeline_projects_dir = os.listdir(pipeline_dir)
		if(step1_dir in pipeline_projects_dir):
			step1_prjs.add(step1_dir)
			
	# add any step1 project directories to the multi projects list
	multi_projects.update(step1_prjs)
	print("***********************")
	print(multi_projects)
	print("***********************")
	return(multi_projects)
	


def main(run_id):
	"""
	This is the main routine.  
	Here, we take in the run ID and determine how
	the metric summary files should be named.
	Then, the files are copied and renamed and
	stored in another directory to be parsed.
	"""
	cellranger_outs_dir =  "/igo/staging/CELLRANGER/{}/*/Sample_*/outs/*summary.csv".format(run_id)
	# cellranger_arc_outs_dir =  "/igo/staging/CELLRANGER/{}/*/Sample_*/outs/summary.csv".format(run_id)
	cellranger_run_dir = "/igo/staging/CELLRANGER/{}".format(run_id)
	
	# grab a list of the metrics csv files
	metrics_csvs = glob.glob(cellranger_outs_dir)
	
	print(metrics_csvs)
	
	# create a directory in which to copy the data - this may change in the future
	cellranger_done_dir = "/home/nabors/STATS/CELLRANGER"
	# pathlib.Path(csv_data_dir).mkdir(parents = True, exist_ok = True)
	
	# first, grab and rename the metrics summary csv files in the /igo/staging/CELLRANGER
	for metrics_csv in metrics_csvs:
		# pass the metrics csv file to make sure we are grabbing the latest text file
		metricsCsvFileData = grab_latest_metrics_csv(metrics_csv)
		
		# get items from list and rename for readibility
		metrics_csv = metricsCsvFileData[0]
		csvFileTimeStamp = metricsCsvFileData[1] 
		
		metrics_csv_columns = pd.read_csv(metrics_csv, index_col = 0, nrows = 0).columns.tolist()
		# getting files and sample names to insert in the new file name
		metrics_csv_meta = metrics_csv.split("/")
		csv_meta_run = metrics_csv_meta[4]
		csv_meta_project = metrics_csv_meta[5][8:]
		# get the  metrics summary files that reside in /igo/staging/CELLRANGER
		new_metrics_csv = ""
		for metrics_columns in range(0, len(ALL_METRICS_CSV_COLUMNS), 1):
			if metrics_csv_columns == ALL_METRICS_CSV_COLUMNS[metrics_columns]:
				extension = EXTENSIONS[metrics_columns]
				if ("__count" in metrics_csv_meta[6]):
					sample_id = metrics_csv_meta[6][7:-7]
				else:
					sample_id = metrics_csv_meta[6][7:]
				new_metrics_csv = "{}___P{}___{}___{}___{}".format(csv_meta_run, csv_meta_project, sample_id, csvFileTimeStamp, extension)
				# rename old metrics file to new metrics file
				copy_metrics_csv = "cp -rv {} {}/{}".format(metrics_csv, cellranger_done_dir, new_metrics_csv)
				print(copy_metrics_csv)
				call(copy_metrics_csv, shell = True)
	
	# grab the projects that could have the multi pipeline run on them
	multi_projects = get_multi_projects(cellranger_outs_dir, cellranger_run_dir)
	
	# copy and rename csv files from cellranger multi pipeline
	for mp in multi_projects:
		multi_prj = "/igo/staging/PIPELINE/{}/*/outs/per_sample_outs/*/metrics_summary.csv".format(mp)
		multi_metrics_csvs = glob.glob(multi_prj)
		new_multi_metrics_csv = ""
		
		for multi_metrics_csv in multi_metrics_csvs:
			multi_metrics_csv_columns = pd.read_csv(multi_metrics_csv, index_col = 0, nrows = 0).columns.tolist()
			# multi extension test list to help determine if we need a multi (ABC or CMO) or not
			multi_extension = {"capture_data": False, "extension": ""}
			multi_extension =  get_library_type(multi_metrics_csv, multi_extension)
			if not multi_extension["capture_data"]:
				break
			else:
				multi_metrics_csv_meta = multi_metrics_csv.split("/")
				new_multi_metrics_csv = "{}___P{}___{}___{}___{}___{}".format(csv_meta_run, multi_metrics_csv_meta[4][8:], multi_metrics_csv_meta[5], multi_metrics_csv_meta[8], csvFileTimeStamp, multi_extension["extension"])
				copy_multi_metrics_csv = "cp -rv {} {}/{}".format(multi_metrics_csv, cellranger_done_dir, new_multi_metrics_csv)
				print(copy_multi_metrics_csv)
				call(copy_multi_metrics_csv, shell = True)

		

if __name__ == "__main__":
	"""
	This script grabs the metric summary csv files from a run directory in /igo/staging/CELLRANGER and renames them
	so that they may be parsed by a script that posts those stats to NGS_STATS on igodb.mskcc.org
	"""
	# grab the run directory name where the csv files are stored
	run_id = sys.argv[1]
	
	main(run_id)