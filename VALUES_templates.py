
#!/usr/bin/env python3
import pandas
import csv

def convert_percentage(percentage_of_value):
	"""
	This function takes away the percent symbol on percentage data
	and converts the data to a float data type for storage
	in NGS_STATS
	"""
	converted_percentage_of_value = round((float(percentage_of_value[:-1]) / 100), 5)
	return(converted_percentage_of_value)


def remove_commas(numpy_value):
	"""
	This function removes commas from integer/string data and 
	converts this data to integer
	"""
	numpy_to_str_value = str(numpy_value)
	if ("," in numpy_to_str_value):
		integer_value_without_commas = numpy_to_str_value.replace(",", "")
		return(integer_value_without_commas)
	else:
		return(numpy_to_str_value)
	
	
def convert_to_date_time(timestamp_from_file):
	"""
	This function converst the timestamp
	from the file name and converts it
	to datetime format for the 10X DB tables
	"""
	timestamp_in_date_time_format = "{} {}".format(timestamp_from_file.split("_")[0], timestamp_from_file.split("_")[1].replace("-", ":"))
	return(timestamp_in_date_time_format)


def create_gex_values_statement(csv_file, csv_file_data):
	"""
	This function takes the data in the csv
	file and create the Gene Expression Values Statement 
	for insertion into the GEX Table
	in NGS_STATS
	"""
	gex_values_to_insert = "\"{}\", \"{}\", \"{}\", {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}".format(\
	csv_file.split("___")[2],\
	csv_file.split("/")[-1].split("___")[0],\
	convert_to_date_time(csv_file.split("___")[3]),\
	remove_commas(csv_file_data["Estimated Number of Cells"][0]),\
	remove_commas(csv_file_data["Mean Reads per Cell"][0]),\
	remove_commas(csv_file_data["Median Genes per Cell"][0]),\
	remove_commas(csv_file_data["Number of Reads"][0]),\
	convert_percentage(csv_file_data["Valid Barcodes"][0]),\
	convert_percentage(csv_file_data["Sequencing Saturation"][0]),\
	convert_percentage(csv_file_data["Q30 Bases in Barcode"][0]),\
	convert_percentage(csv_file_data["Q30 Bases in RNA Read"][0]),\
	convert_percentage(csv_file_data["Q30 Bases in UMI"][0]),\
	convert_percentage(csv_file_data["Reads Mapped to Genome"][0]),\
	convert_percentage(csv_file_data["Reads Mapped Confidently to Genome"][0]),\
	convert_percentage(csv_file_data["Reads Mapped Confidently to Intergenic Regions"][0]),\
	convert_percentage(csv_file_data["Reads Mapped Confidently to Intronic Regions"][0]),\
	convert_percentage(csv_file_data["Reads Mapped Confidently to Exonic Regions"][0]),\
	convert_percentage(csv_file_data["Reads Mapped Confidently to Transcriptome"][0]),\
	convert_percentage(csv_file_data["Reads Mapped Antisense to Gene"][0]),\
	convert_percentage(csv_file_data["Fraction Reads in Cells"][0]),\
	remove_commas(csv_file_data["Total Genes Detected"][0]),\
	remove_commas(csv_file_data["Median UMI Counts per Cell"][0]))
	return(gex_values_to_insert)
	
	
def create_arc_values_statement(csv_file, csv_file_data):
	"""
	This function takes the data in the csv
	file and create the ARC Values Statement 
	for insertion into the ARC Table
	in NGS_STATS
	"""
	arc_values_to_insert = "\"{}\", \"{}\", \"{}\", \"{}\", \"{}\", {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}".format(\
	csv_file.split("___")[2],\
	csv_file.split("/")[-1].split("___")[0],\
	convert_to_date_time(csv_file.split("___")[3]),\
	csv_file_data["Genome"][0],\
	csv_file_data["Pipeline version"][0],\
	csv_file_data["Estimated number of cells"][0],\
	csv_file_data["Feature linkages detected"][0],\
	csv_file_data["Linked genes"][0],\
	csv_file_data["Linked peaks"][0],\
	csv_file_data["ATAC Confidently mapped read pairs"][0],\
	csv_file_data["ATAC Fraction of genome in peaks"][0],\
	csv_file_data["ATAC Fraction of high-quality fragments in cells"][0],\
	csv_file_data["ATAC Fraction of high-quality fragments overlapping TSS"][0],\
	csv_file_data["ATAC Fraction of high-quality fragments overlapping peaks"][0],\
	csv_file_data["ATAC Fraction of transposition events in peaks in cells"][0],\
	csv_file_data["ATAC Mean raw read pairs per cell"][0],\
	csv_file_data["ATAC Median high-quality fragments per cell"][0],\
	csv_file_data["ATAC Non-nuclear read pairs"][0],\
	csv_file_data["ATAC Number of peaks"][0],\
	csv_file_data["ATAC Percent duplicates"][0],\
	csv_file_data["ATAC Q30 bases in barcode"][0],\
	csv_file_data["ATAC Q30 bases in read 1"][0],\
	csv_file_data["ATAC Q30 bases in read 2"][0],\
	csv_file_data["ATAC Q30 bases in sample index i1"][0],\
	csv_file_data["ATAC Sequenced read pairs"][0],\
	csv_file_data["ATAC TSS enrichment score"][0],\
	csv_file_data["ATAC Unmapped read pairs"][0],\
	csv_file_data["ATAC Valid barcodes"][0],\
	csv_file_data["GEX Fraction of transcriptomic reads in cells"][0],\
	csv_file_data["GEX Mean raw reads per cell"][0],\
	csv_file_data["GEX Median UMI counts per cell"][0],\
	csv_file_data["GEX Median genes per cell"][0],\
	csv_file_data["GEX Percent duplicates"][0],\
	csv_file_data["GEX Q30 bases in UMI"][0],\
	csv_file_data["GEX Q30 bases in barcode"][0],\
	csv_file_data["GEX Q30 bases in read 2"][0],\
	csv_file_data["GEX Q30 bases in sample index i1"][0],\
	csv_file_data["GEX Q30 bases in sample index i2"][0],\
	csv_file_data["GEX Reads mapped antisense to gene"][0],\
	csv_file_data["GEX Reads mapped confidently to exonic regions"][0],\
	csv_file_data["GEX Reads mapped confidently to genome"][0],\
	csv_file_data["GEX Reads mapped confidently to intergenic regions"][0],\
	csv_file_data["GEX Reads mapped confidently to intronic regions"][0],\
	csv_file_data["GEX Reads mapped confidently to transcriptome"][0],\
	csv_file_data["GEX Reads mapped to genome"][0],\
	csv_file_data["GEX Reads with TSO"][0],\
	csv_file_data["GEX Sequenced read pairs"][0],\
	csv_file_data["GEX Total genes detected"][0],\
	csv_file_data["GEX Valid UMIs"][0],\
	csv_file_data["GEX Valid barcodes"][0])
	return(arc_values_to_insert)


def create_visium_values_statement(csv_file, csv_file_data):
	"""
	This function takes the data in the csv
	file and create the VISIUM Spaceranger Values Statement 
	for insertion into the VISIUM Table
	in NGS_STATS
	"""
	visium_values_to_insert = "\"{}\", \"{}\", \"{}\", {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}".format(\
	csv_file.split("___")[2],\
	csv_file.split("/")[-1].split("___")[0],\
	convert_to_date_time(csv_file.split("___")[3]),\
	csv_file_data["Number of Spots Under Tissue"][0],\
	csv_file_data["Number of Reads"][0],\
	csv_file_data["Mean Reads per Spot"][0],\
	csv_file_data["Mean Reads Under Tissue per Spot"][0],\
	csv_file_data["Fraction of Spots Under Tissue"][0],\
	csv_file_data["Median Genes per Spot"][0],\
	csv_file_data["Median UMI Counts per Spot"][0],\
	csv_file_data["Valid Barcodes"][0],\
	csv_file_data["Valid UMIs"][0],\
	csv_file_data["Sequencing Saturation"][0],\
	csv_file_data["Q30 Bases in Barcode"][0],\
	csv_file_data["Q30 Bases in RNA Read"][0],\
	csv_file_data["Q30 Bases in UMI"][0],\
	csv_file_data["Reads Mapped to Genome"][0],\
	csv_file_data["Reads Mapped Confidently to Genome"][0],\
	csv_file_data["Reads Mapped Confidently to Intergenic Regions"][0],\
	csv_file_data["Reads Mapped Confidently to Intronic Regions"][0],\
	csv_file_data["Reads Mapped Confidently to Exonic Regions"][0],\
	csv_file_data["Reads Mapped Confidently to Transcriptome"][0],\
	csv_file_data["Reads Mapped Antisense to Gene"][0],\
	csv_file_data["Fraction Reads in Spots Under Tissue"][0],\
	csv_file_data["Total Genes Detected"][0])
	return(visium_values_to_insert)


def create_vdj_t_values_statement(csv_file, csv_file_data):
	"""
	This function takes the data in the csv
	file and create the VDJ Values Statement 
	for insertion into the VDJ Table
	in NGS_STATS
	"""
	vdj_t_values_to_insert = "\"{}\", \"{}\", \"{}\", {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}".format(\
	csv_file.split("___")[2],\
	csv_file.split("/")[-1].split("___")[0],\
	convert_to_date_time(csv_file.split("___")[3]),\
	remove_commas(csv_file_data["Estimated Number of Cells"][0]),\
	remove_commas(csv_file_data["Mean Read Pairs per Cell"][0]),\
	remove_commas(csv_file_data["Number of Cells With Productive V-J Spanning Pair"][0]),\
	remove_commas(csv_file_data["Number of Read Pairs"][0]),\
	convert_percentage(csv_file_data["Valid Barcodes"][0]),\
	convert_percentage(csv_file_data["Q30 Bases in Barcode"][0]),\
	convert_percentage(csv_file_data["Q30 Bases in RNA Read 1"][0]),\
	convert_percentage(csv_file_data["Q30 Bases in UMI"][0]),\
	convert_percentage(csv_file_data["Reads Mapped to Any V(D)J Gene"][0]),\
	convert_percentage(csv_file_data["Reads Mapped to TRA"][0]),\
	convert_percentage(csv_file_data["Reads Mapped to TRB"][0]),\
	remove_commas(csv_file_data["Mean Used Read Pairs per Cell"][0]),\
	convert_percentage(csv_file_data["Fraction Reads in Cells"][0]),\
	csv_file_data["Median TRA UMIs per Cell"][0],\
	csv_file_data["Median TRB UMIs per Cell"][0],\
	convert_percentage(csv_file_data["Cells With Productive V-J Spanning Pair"][0]),\
	convert_percentage(csv_file_data["Cells With Productive V-J Spanning (TRA, TRB) Pair"][0]),\
	csv_file_data["Paired Clonotype Diversity"][0],\
	convert_percentage(csv_file_data["Cells With TRA Contig"][0]),\
	convert_percentage(csv_file_data["Cells With TRB Contig"][0]),\
	convert_percentage(csv_file_data["Cells With CDR3-annotated TRA Contig"][0]),\
	convert_percentage(csv_file_data["Cells With CDR3-annotated TRB Contig"][0]),\
	convert_percentage(csv_file_data["Cells With V-J Spanning TRA Contig"][0]),\
	convert_percentage(csv_file_data["Cells With V-J Spanning TRB Contig"][0]),\
	convert_percentage(csv_file_data["Cells With Productive TRA Contig"][0]),\
	convert_percentage(csv_file_data["Cells With Productive TRB Contig"][0]))
	return(vdj_t_values_to_insert)


def create_abc_values_statement(csv_file, csv_file_data):
	"""
	This function takes the data in the csv
	file and create the Cellranger MULTI Antibody Capture Values Statement 
	for insertion into the ABC Table
	in NGS_STATS
	"""
	abc_values_to_insert ="\"{}\", \"{}\", \"{}\", {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}".format(\
	csv_file.split("___")[2],\
	csv_file.split("/")[-1].split("___")[0],\
	convert_to_date_time(csv_file.split("___")[4]),\
	remove_commas(csv_file_data[(csv_file_data["Category"] == "Cells") & (csv_file_data["Library Type"] == "Antibody Capture") & (csv_file_data["Metric Name"] == "Mean antibody reads usable per cell")]["Metric Value"].iloc[0]),\
	remove_commas(csv_file_data[(csv_file_data["Category"] == "Cells") & (csv_file_data["Library Type"] == "Antibody Capture") & (csv_file_data["Metric Name"] == "Median UMI counts per cell")]["Metric Value"].iloc[0]),\
	remove_commas(csv_file_data[(csv_file_data["Category"] == "Cells") & (csv_file_data["Library Type"] == "Gene Expression") & (csv_file_data["Metric Name"] == "Cells")]["Metric Value"].iloc[0]),\
	convert_percentage(csv_file_data[(csv_file_data["Category"] == "Cells") & (csv_file_data["Library Type"] == "Gene Expression") & (csv_file_data["Metric Name"] == "Confidently mapped reads in cells")]["Metric Value"].iloc[0]),\
	remove_commas(csv_file_data[(csv_file_data["Category"] == "Cells") & (csv_file_data["Library Type"] == "Gene Expression") & (csv_file_data["Metric Name"] == "Median UMI counts per cell")]["Metric Value"].iloc[0]),\
	remove_commas(csv_file_data[(csv_file_data["Category"] == "Cells") & (csv_file_data["Library Type"] == "Gene Expression") & (csv_file_data["Metric Name"] == "Median genes per cell")]["Metric Value"].iloc[0]),\
	remove_commas(csv_file_data[(csv_file_data["Category"] == "Cells") & (csv_file_data["Library Type"] == "Gene Expression") & (csv_file_data["Metric Name"] == "Total genes detected")]["Metric Value"].iloc[0]),\
	remove_commas(csv_file_data[(csv_file_data["Category"] == "Library") & (csv_file_data["Library Type"] == "Antibody Capture") & (csv_file_data["Grouped By"] == "Physical library ID") & (csv_file_data["Group Name"] == "ABC_1") & (csv_file_data["Metric Name"] == "Estimated number of cells")]["Metric Value"].iloc[0]),\
	convert_percentage(csv_file_data[(csv_file_data["Category"] == "Library") & (csv_file_data["Library Type"] == "Antibody Capture") & (csv_file_data["Grouped By"] == "Physical library ID") & (csv_file_data["Group Name"] == "ABC_1") & (csv_file_data["Metric Name"] == "Fraction antibody reads")]["Metric Value"].iloc[0]),\
	convert_percentage(csv_file_data[(csv_file_data["Category"] == "Library") & (csv_file_data["Library Type"] == "Antibody Capture") & (csv_file_data["Grouped By"] == "Physical library ID") & (csv_file_data["Group Name"] == "ABC_1") & (csv_file_data["Metric Name"] == "Fraction antibody reads in aggregate barcodes")]["Metric Value"].iloc[0]),\
	convert_percentage(csv_file_data[(csv_file_data["Category"] == "Library") & (csv_file_data["Library Type"] == "Antibody Capture") & (csv_file_data["Grouped By"] == "Physical library ID") & (csv_file_data["Group Name"] == "ABC_1") & (csv_file_data["Metric Name"] == "Fraction antibody reads usable")]["Metric Value"].iloc[0]),\
	remove_commas(csv_file_data[(csv_file_data["Category"] == "Library") & (csv_file_data["Library Type"] == "Antibody Capture") & (csv_file_data["Grouped By"] == "Physical library ID") & (csv_file_data["Group Name"] == "ABC_1") & (csv_file_data["Metric Name"] == "Mean reads per cell")]["Metric Value"].iloc[0]),\
	remove_commas(csv_file_data[(csv_file_data["Category"] == "Library") & (csv_file_data["Library Type"] == "Antibody Capture") & (csv_file_data["Grouped By"] == "Physical library ID") & (csv_file_data["Group Name"] == "ABC_1") & (csv_file_data["Metric Name"] == "Number of reads")]["Metric Value"].iloc[0]),\
	convert_percentage(csv_file_data[(csv_file_data["Category"] == "Library") & (csv_file_data["Library Type"] == "Antibody Capture") & (csv_file_data["Grouped By"] == "Physical library ID") & (csv_file_data["Group Name"] == "ABC_1") & (csv_file_data["Metric Name"] == "Sequencing saturation")]["Metric Value"].iloc[0]),\
	convert_percentage(csv_file_data[(csv_file_data["Category"] == "Library") & (csv_file_data["Library Type"] == "Antibody Capture") & (csv_file_data["Grouped By"] == "Physical library ID") & (csv_file_data["Group Name"] == "ABC_1") & (csv_file_data["Metric Name"] == "Valid UMIs")]["Metric Value"].iloc[0]),\
	convert_percentage(csv_file_data[(csv_file_data["Category"] == "Library") & (csv_file_data["Library Type"] == "Antibody Capture") & (csv_file_data["Grouped By"] == "Physical library ID") & (csv_file_data["Group Name"] == "ABC_1") & (csv_file_data["Metric Name"] == "Valid barcodes")]["Metric Value"].iloc[0]))
	return(abc_values_to_insert)

def create_ch_values_statement(csv_file, csv_file_data):
	"""
	This function takes the data in the csv
	file and create the Cellranger MULTI Cell-Multiplexing Capture Values Statement 
	for insertion into the CMO Table
	in NGS_STATS
	"""
	ch_values_to_insert ="\"{}\", \"{}\", \"{}\", \"{}\", \"{}\", \"{}\", \"{}\", \"{}\", \"{}\", {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}".format(\
	csv_file.split("___")[2],\
	csv_file.split("___")[3],\
	csv_file.split("/")[-1].split("___")[0],\
	convert_to_date_time(csv_file.split("___")[4]),\
	csv_file_data[(csv_file_data["Category"] == "Cells") & (csv_file_data["Library Type"] == "Gene Expression") & (csv_file_data["Grouped By"] == "Physical library ID") & (csv_file_data["Group Name"] == "GEX_1") & (csv_file_data["Metric Name"] == "Cells assigned to other samples")]["Metric Value"].iloc[0],\
	csv_file_data[(csv_file_data["Category"] == "Cells") & (csv_file_data["Library Type"] == "Gene Expression") & (csv_file_data["Grouped By"] == "Physical library ID") & (csv_file_data["Group Name"] == "GEX_1") & (csv_file_data["Metric Name"] == "Cells assigned to this sample")]["Metric Value"].iloc[0],\
	csv_file_data[(csv_file_data["Category"] == "Library") & (csv_file_data["Library Type"] == "Multiplexing Capture") & (csv_file_data["Grouped By"] == "Physical library ID") & (csv_file_data["Group Name"] == "CMO_1") & (csv_file_data["Metric Name"] == "Cell-associated barcodes identified as multiplets")]["Metric Value"].iloc[0],\
	csv_file_data[(csv_file_data["Category"] == "Library") & (csv_file_data["Library Type"] == "Multiplexing Capture") & (csv_file_data["Grouped By"] == "Physical library ID") & (csv_file_data["Group Name"] == "CMO_1") & (csv_file_data["Metric Name"] == "Cell-associated barcodes not assigned any CMOs")]["Metric Value"].iloc[0],\
	csv_file_data[(csv_file_data["Category"] == "Library") & (csv_file_data["Library Type"] == "Multiplexing Capture") & (csv_file_data["Grouped By"] == "Physical library ID") & (csv_file_data["Group Name"] == "CMO_1") & (csv_file_data["Metric Name"] == "Cells assigned to a sample")]["Metric Value"].iloc[0],\
	remove_commas(csv_file_data[(csv_file_data["Category"] == "Library") & (csv_file_data["Library Type"] == "Multiplexing Capture") & (csv_file_data["Grouped By"] == "Physical library ID") & (csv_file_data["Group Name"] == "CMO_1") & (csv_file_data["Metric Name"] == "Estimated number of cell-associated barcodes")]["Metric Value"].iloc[0]),\
	convert_percentage(csv_file_data[(csv_file_data["Category"] == "Library") & (csv_file_data["Library Type"] == "Multiplexing Capture") & (csv_file_data["Grouped By"] == "Physical library ID") & (csv_file_data["Group Name"] == "CMO_1") & (csv_file_data["Metric Name"] == "Fraction CMO reads")]["Metric Value"].iloc[0]),\
	convert_percentage(csv_file_data[(csv_file_data["Category"] == "Library") & (csv_file_data["Library Type"] == "Multiplexing Capture") & (csv_file_data["Grouped By"] == "Physical library ID") & (csv_file_data["Group Name"] == "CMO_1") & (csv_file_data["Metric Name"] == "Fraction CMO reads usable")]["Metric Value"].iloc[0]),\
	convert_percentage(csv_file_data[(csv_file_data["Category"] == "Library") & (csv_file_data["Library Type"] == "Multiplexing Capture") & (csv_file_data["Grouped By"] == "Physical library ID") & (csv_file_data["Group Name"] == "CMO_1") & (csv_file_data["Metric Name"] == "Fraction reads from multiplets")]["Metric Value"].iloc[0]),\
	convert_percentage(csv_file_data[(csv_file_data["Category"] == "Library") & (csv_file_data["Library Type"] == "Multiplexing Capture") & (csv_file_data["Grouped By"] == "Physical library ID") & (csv_file_data["Group Name"] == "CMO_1") & (csv_file_data["Metric Name"] == "Fraction reads in cell-associated barcodes")]["Metric Value"].iloc[0]),\
	convert_percentage(csv_file_data[(csv_file_data["Category"] == "Library") & (csv_file_data["Library Type"] == "Multiplexing Capture") & (csv_file_data["Grouped By"] == "Physical library ID") & (csv_file_data["Group Name"] == "CMO_1") & (csv_file_data["Metric Name"] == "Fraction unrecognized CMO")]["Metric Value"].iloc[0]),\
	remove_commas(csv_file_data[(csv_file_data["Category"] == "Library") & (csv_file_data["Library Type"] == "Multiplexing Capture") & (csv_file_data["Grouped By"] == "Physical library ID") & (csv_file_data["Group Name"] == "CMO_1") & (csv_file_data["Metric Name"] == "Mean reads per cell-associated barcode")]["Metric Value"].iloc[0]),\
	remove_commas(csv_file_data[(csv_file_data["Category"] == "Library") & (csv_file_data["Library Type"] == "Multiplexing Capture") & (csv_file_data["Grouped By"] == "Physical library ID") & (csv_file_data["Group Name"] == "CMO_1") & (csv_file_data["Metric Name"] == "Median CMO UMIs per cell-associated barcode")]["Metric Value"].iloc[0]),\
	remove_commas(csv_file_data[(csv_file_data["Category"] == "Library") & (csv_file_data["Library Type"] == "Multiplexing Capture") & (csv_file_data["Grouped By"] == "Physical library ID") & (csv_file_data["Group Name"] == "CMO_1") & (csv_file_data["Metric Name"] == "Number of reads")]["Metric Value"].iloc[0]),\
	remove_commas(csv_file_data[(csv_file_data["Category"] == "Library") & (csv_file_data["Library Type"] == "Multiplexing Capture") & (csv_file_data["Grouped By"] == "Physical library ID") & (csv_file_data["Group Name"] == "CMO_1") & (csv_file_data["Metric Name"] == "Samples assigned at least one cell")]["Metric Value"].iloc[0]),\
	convert_percentage(csv_file_data[(csv_file_data["Category"] == "Library") & (csv_file_data["Library Type"] == "Multiplexing Capture") & (csv_file_data["Grouped By"] == "Physical library ID") & (csv_file_data["Group Name"] == "CMO_1") & (csv_file_data["Metric Name"] == "Sequencing saturation")]["Metric Value"].iloc[0]),\
	convert_percentage(csv_file_data[(csv_file_data["Category"] == "Library") & (csv_file_data["Library Type"] == "Multiplexing Capture") & (csv_file_data["Grouped By"] == "Physical library ID") & (csv_file_data["Group Name"] == "CMO_1") & (csv_file_data["Metric Name"] == "Valid UMIs")]["Metric Value"].iloc[0]),\
	convert_percentage(csv_file_data[(csv_file_data["Category"] == "Library") & (csv_file_data["Library Type"] == "Multiplexing Capture") & (csv_file_data["Grouped By"] == "Physical library ID") & (csv_file_data["Group Name"] == "CMO_1") & (csv_file_data["Metric Name"] == "Valid barcodes")]["Metric Value"].iloc[0]))
	return(ch_values_to_insert)


def create_vdj_b_values_statement(csv_file, csv_file_data):
	"""
	This function takes the data in the csv
	file and create the VDJ-BCR Values Statement 
	for insertion into the VDJ-BCR Table
	in NGS_STATS
	"""
	vdj_b_values_to_insert = "\"{}\", \"{}\", \"{}\", {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}".format(\
	csv_file.split("___")[2],\
	csv_file.split("/")[-1].split("___")[0],\
	convert_to_date_time(csv_file.split("___")[3]),\
	remove_commas(csv_file_data["Estimated Number of Cells"][0]),\
	remove_commas(csv_file_data["Mean Read Pairs per Cell"][0]),\
	remove_commas(csv_file_data["Number of Cells With Productive V-J Spanning Pair"][0]),\
	remove_commas(csv_file_data["Number of Read Pairs"][0]),\
	convert_percentage(csv_file_data["Valid Barcodes"][0]),\
	convert_percentage(csv_file_data["Q30 Bases in Barcode"][0]),\
	convert_percentage(csv_file_data["Q30 Bases in RNA Read 1"][0]),\
	convert_percentage(csv_file_data["Q30 Bases in UMI"][0]),\
	convert_percentage(csv_file_data["Reads Mapped to Any V(D)J Gene"][0]),\
	convert_percentage(csv_file_data["Reads Mapped to IGH"][0]),\
	convert_percentage(csv_file_data["Reads Mapped to IGK"][0]),\
	convert_percentage(csv_file_data["Reads Mapped to IGL"][0]),\
	remove_commas(csv_file_data["Mean Used Read Pairs per Cell"][0]),\
	convert_percentage(csv_file_data["Fraction Reads in Cells"][0]),\
	csv_file_data["Median IGH UMIs per Cell"][0],\
	csv_file_data["Median IGK UMIs per Cell"][0],\
	csv_file_data["Median IGL UMIs per Cell"][0],\
	convert_percentage(csv_file_data["Cells With Productive V-J Spanning Pair"][0]),\
	convert_percentage(csv_file_data["Cells With Productive V-J Spanning (IGK, IGH) Pair"][0]),\
	convert_percentage(csv_file_data["Cells With Productive V-J Spanning (IGL, IGH) Pair"][0]),\
	csv_file_data["Paired Clonotype Diversity"][0],\
	convert_percentage(csv_file_data["Cells With IGH Contig"][0]),\
	convert_percentage(csv_file_data["Cells With IGK Contig"][0]),\
	convert_percentage(csv_file_data["Cells With IGL Contig"][0]),\
	convert_percentage(csv_file_data["Cells With CDR3-annotated IGH Contig"][0]),\
	convert_percentage(csv_file_data["Cells With CDR3-annotated IGK Contig"][0]),\
	convert_percentage(csv_file_data["Cells With CDR3-annotated IGL Contig"][0]),\
	convert_percentage(csv_file_data["Cells With V-J Spanning IGH Contig"][0]),\
	convert_percentage(csv_file_data["Cells With V-J Spanning IGK Contig"][0]),\
	convert_percentage(csv_file_data["Cells With V-J Spanning IGL Contig"][0]),\
	convert_percentage(csv_file_data["Cells With Productive IGH Contig"][0]),\
	convert_percentage(csv_file_data["Cells With Productive IGK Contig"][0]),\
	convert_percentage(csv_file_data["Cells With Productive IGL Contig"][0]))
	return(vdj_b_values_to_insert)


def create_visium_ffpe_values_statement(csv_file, csv_file_data):
	"""
	This function takes the data in the csv
	file and create the VISIUM-FFPE Spaceranger Values Statement 
	for insertion into the VISIUM-FFPE Table
	in NGS_STATS
	"""
	visium_ffpe_values_to_insert = "\"{}\", \"{}\", \"{}\", {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}".format(\
	csv_file.split("___")[2],\
	csv_file.split("/")[-1].split("___")[0],\
	convert_to_date_time(csv_file.split("___")[3]),\
	csv_file_data["Number of Spots Under Tissue"][0],\
	csv_file_data["Number of Reads"][0],\
	csv_file_data["Mean Reads per Spot"][0],\
	csv_file_data["Mean Reads Under Tissue per Spot"][0],\
	csv_file_data["Fraction of Spots Under Tissue"][0],\
	csv_file_data["Valid Barcodes"][0],\
	csv_file_data["Valid UMIs"][0],\
	csv_file_data["Sequencing Saturation"][0],\
	csv_file_data["Q30 Bases in Barcode"][0],\
	csv_file_data["Q30 Bases in Probe Read"][0],\
	csv_file_data["Q30 Bases in UMI"][0],\
	csv_file_data["Reads Mapped to Probe Set"][0],\
	csv_file_data["Reads Mapped Confidently to Probe Set"][0],\
	csv_file_data["Fraction Reads in Spots Under Tissue"][0],\
	csv_file_data["Median Genes per Spot"][0],\
	csv_file_data["Median UMI Counts per Spot"][0],\
	csv_file_data["Genes Detected"][0],\
	csv_file_data["Reads Mapped Confidently to the Filtered Probe Set"][0],\
	csv_file_data["Number of Genes"][0],\
	csv_file_data["Number of Genes >= 10 UMIs"][0],\
	csv_file_data["Reads Half-Mapped to Probe Set"][0],\
	csv_file_data["Reads Split-Mapped to Probe Set"][0],\
	csv_file_data["Estimated UMIs from Genomic DNA"][0],\
	csv_file_data["Estimated UMIs from Genomic DNA per Unspliced Probe"][0])
	return(visium_ffpe_values_to_insert)


def create_abc_ch_values_statement(csv_file, csv_file_data):
	"""
	This function takes the data in the csv
	file and create the Cellranger MULTI Antibody Capture/Cell-Multiplexing Capture Values Statement
	for insertion into the ABC-CH Table
	in NGS_STATS
	"""
	abc_ch_values_to_insert = "\"{}\", \"{}\", \"{}\", \"{}\", {}, {}, {}, {}, {}, {}, {}, {}, \"{}\", \"{}\", \"{}\", \"{}\", {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, \"{}\", \"{}\", \"{}\", {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}".format(\
	csv_file.split("___")[2],\
	csv_file.split("___")[3],\
	csv_file.split("/")[-1].split("___")[0],\
	convert_to_date_time(csv_file.split("___")[4]),\
	remove_commas(csv_file_data[(csv_file_data["Category"] == "Cells") & (csv_file_data["Library Type"] == "Antibody Capture") & (csv_file_data["Metric Name"] == "Cells")]["Metric Value"].iloc[0]),\
	remove_commas(csv_file_data[(csv_file_data["Category"] == "Cells") & (csv_file_data["Library Type"] == "Antibody Capture") & (csv_file_data["Metric Name"] == "Antibody reads usable per cell")]["Metric Value"].iloc[0]),\
	remove_commas(csv_file_data[(csv_file_data["Category"] == "Cells") & (csv_file_data["Library Type"] == "Antibody Capture") & (csv_file_data["Metric Name"] == "Median UMI counts per cell")]["Metric Value"].iloc[0]),\
	remove_commas(csv_file_data[(csv_file_data["Category"] == "Cells") & (csv_file_data["Library Type"] == "Gene Expression") & (csv_file_data["Metric Name"] == "Cells")]["Metric Value"].iloc[0]),\
	remove_commas(csv_file_data[(csv_file_data["Category"] == "Cells") & (csv_file_data["Library Type"] == "Gene Expression") & (csv_file_data["Metric Name"] == "Median UMI counts per cell")]["Metric Value"].iloc[0]),\
	remove_commas(csv_file_data[(csv_file_data["Category"] == "Cells") & (csv_file_data["Library Type"] == "Gene Expression") & (csv_file_data["Metric Name"] == "Median genes per cell")]["Metric Value"].iloc[0]),\
	remove_commas(csv_file_data[(csv_file_data["Category"] == "Cells") & (csv_file_data["Library Type"] == "Gene Expression") & (csv_file_data["Metric Name"] == "Median reads per cell")]["Metric Value"].iloc[0]),\
	remove_commas(csv_file_data[(csv_file_data["Category"] == "Cells") & (csv_file_data["Library Type"] == "Gene Expression") & (csv_file_data["Metric Name"] == "Total genes detected")]["Metric Value"].iloc[0]),\
	csv_file_data[(csv_file_data["Category"] == "Cells") & (csv_file_data["Library Type"] == "Gene Expression") & (csv_file_data["Grouped By"] == "Physical library ID") & (csv_file_data["Group Name"] == "GEX_1") & (csv_file_data["Metric Name"] == "Cell-associated barcodes identified as multiplets")]["Metric Value"].iloc[0],\
	csv_file_data[(csv_file_data["Category"] == "Cells") & (csv_file_data["Library Type"] == "Gene Expression") & (csv_file_data["Grouped By"] == "Physical library ID") & (csv_file_data["Group Name"] == "GEX_1") & (csv_file_data["Metric Name"] == "Cell-associated barcodes not assigned any CMOs")]["Metric Value"].iloc[0],\
	csv_file_data[(csv_file_data["Category"] == "Cells") & (csv_file_data["Library Type"] == "Gene Expression") & (csv_file_data["Grouped By"] == "Physical library ID") & (csv_file_data["Group Name"] == "GEX_1") & (csv_file_data["Metric Name"] == "Cells assigned to other samples")]["Metric Value"].iloc[0],\
	csv_file_data[(csv_file_data["Category"] == "Cells") & (csv_file_data["Library Type"] == "Gene Expression") & (csv_file_data["Grouped By"] == "Physical library ID") & (csv_file_data["Group Name"] == "GEX_1") & (csv_file_data["Metric Name"] == "Cells assigned to this sample")]["Metric Value"].iloc[0],\
	remove_commas(csv_file_data[(csv_file_data["Category"] == "Library") & (csv_file_data["Library Type"] == "Antibody Capture") & (csv_file_data["Grouped By"] == "Physical library ID") & (csv_file_data["Group Name"] == "ABC_1") & (csv_file_data["Metric Name"] == "Estimated number of cells")]["Metric Value"].iloc[0]),\
	convert_percentage(csv_file_data[(csv_file_data["Category"] == "Library") & (csv_file_data["Library Type"] == "Antibody Capture") & (csv_file_data["Grouped By"] == "Physical library ID") & (csv_file_data["Group Name"] == "ABC_1") & (csv_file_data["Metric Name"] == "Fraction antibody reads")]["Metric Value"].iloc[0]),\
	convert_percentage(csv_file_data[(csv_file_data["Category"] == "Library") & (csv_file_data["Library Type"] == "Antibody Capture") & (csv_file_data["Grouped By"] == "Physical library ID") & (csv_file_data["Group Name"] == "ABC_1") & (csv_file_data["Metric Name"] == "Fraction antibody reads in aggregate barcodes")]["Metric Value"].iloc[0]),\
	convert_percentage(csv_file_data[(csv_file_data["Category"] == "Library") & (csv_file_data["Library Type"] == "Antibody Capture") & (csv_file_data["Grouped By"] == "Physical library ID") & (csv_file_data["Group Name"] == "ABC_1") & (csv_file_data["Metric Name"] == "Fraction antibody reads usable")]["Metric Value"].iloc[0]),\
	remove_commas(csv_file_data[(csv_file_data["Category"] == "Library") & (csv_file_data["Library Type"] == "Antibody Capture") & (csv_file_data["Grouped By"] == "Physical library ID") & (csv_file_data["Group Name"] == "ABC_1") & (csv_file_data["Metric Name"] == "Mean reads per cell")]["Metric Value"].iloc[0]),\
	remove_commas(csv_file_data[(csv_file_data["Category"] == "Library") & (csv_file_data["Library Type"] == "Antibody Capture") & (csv_file_data["Grouped By"] == "Physical library ID") & (csv_file_data["Group Name"] == "ABC_1") & (csv_file_data["Metric Name"] == "Number of reads")]["Metric Value"].iloc[0]),\
	convert_percentage(csv_file_data[(csv_file_data["Category"] == "Library") & (csv_file_data["Library Type"] == "Antibody Capture") & (csv_file_data["Grouped By"] == "Physical library ID") & (csv_file_data["Group Name"] == "ABC_1") & (csv_file_data["Metric Name"] == "Sequencing saturation")]["Metric Value"].iloc[0]),\
	convert_percentage(csv_file_data[(csv_file_data["Category"] == "Library") & (csv_file_data["Library Type"] == "Antibody Capture") & (csv_file_data["Grouped By"] == "Physical library ID") & (csv_file_data["Group Name"] == "ABC_1") & (csv_file_data["Metric Name"] == "Valid UMIs")]["Metric Value"].iloc[0]),\
	convert_percentage(csv_file_data[(csv_file_data["Category"] == "Library") & (csv_file_data["Library Type"] == "Antibody Capture") & (csv_file_data["Grouped By"] == "Physical library ID") & (csv_file_data["Group Name"] == "ABC_1") & (csv_file_data["Metric Name"] == "Valid barcodes")]["Metric Value"].iloc[0]),\
	convert_percentage(csv_file_data[(csv_file_data["Category"] == "Library") & (csv_file_data["Library Type"] == "Gene Expression") & (csv_file_data["Grouped By"] == "Physical library ID") & (csv_file_data["Group Name"] == "GEX_1") & (csv_file_data["Metric Name"] == "Confidently mapped reads in cells")]["Metric Value"].iloc[0]),\
	csv_file_data[(csv_file_data["Category"] == "Library") & (csv_file_data["Library Type"] == "Multiplexing Capture") & (csv_file_data["Grouped By"] == "Physical library ID") & (csv_file_data["Group Name"] == "CMO_1") & (csv_file_data["Metric Name"] == "Cell-associated barcodes identified as multiplets")]["Metric Value"].iloc[0],\
	csv_file_data[(csv_file_data["Category"] == "Library") & (csv_file_data["Library Type"] == "Multiplexing Capture") & (csv_file_data["Grouped By"] == "Physical library ID") & (csv_file_data["Group Name"] == "CMO_1") & (csv_file_data["Metric Name"] == "Cell-associated barcodes not assigned any CMOs")]["Metric Value"].iloc[0],\
	csv_file_data[(csv_file_data["Category"] == "Library") & (csv_file_data["Library Type"] == "Multiplexing Capture") & (csv_file_data["Grouped By"] == "Physical library ID") & (csv_file_data["Group Name"] == "CMO_1") & (csv_file_data["Metric Name"] == "Cells assigned to a sample")]["Metric Value"].iloc[0],\
	remove_commas(csv_file_data[(csv_file_data["Category"] == "Library") & (csv_file_data["Library Type"] == "Multiplexing Capture") & (csv_file_data["Grouped By"] == "Physical library ID") & (csv_file_data["Group Name"] == "CMO_1") & (csv_file_data["Metric Name"] == "Estimated number of cell-associated barcodes")]["Metric Value"].iloc[0]),\
	convert_percentage(csv_file_data[(csv_file_data["Category"] == "Library") & (csv_file_data["Library Type"] == "Multiplexing Capture") & (csv_file_data["Grouped By"] == "Physical library ID") & (csv_file_data["Group Name"] == "CMO_1") & (csv_file_data["Metric Name"] == "Fraction CMO reads")]["Metric Value"].iloc[0]),\
	convert_percentage(csv_file_data[(csv_file_data["Category"] == "Library") & (csv_file_data["Library Type"] == "Multiplexing Capture") & (csv_file_data["Grouped By"] == "Physical library ID") & (csv_file_data["Group Name"] == "CMO_1") & (csv_file_data["Metric Name"] == "Fraction CMO reads usable")]["Metric Value"].iloc[0]),\
	convert_percentage(csv_file_data[(csv_file_data["Category"] == "Library") & (csv_file_data["Library Type"] == "Multiplexing Capture") & (csv_file_data["Grouped By"] == "Physical library ID") & (csv_file_data["Group Name"] == "CMO_1") & (csv_file_data["Metric Name"] == "Fraction reads from multiplets")]["Metric Value"].iloc[0]),\
	convert_percentage(csv_file_data[(csv_file_data["Category"] == "Library") & (csv_file_data["Library Type"] == "Multiplexing Capture") & (csv_file_data["Grouped By"] == "Physical library ID") & (csv_file_data["Group Name"] == "CMO_1") & (csv_file_data["Metric Name"] == "Fraction reads in cell-associated barcodes")]["Metric Value"].iloc[0]),\
	convert_percentage(csv_file_data[(csv_file_data["Category"] == "Library") & (csv_file_data["Library Type"] == "Multiplexing Capture") & (csv_file_data["Grouped By"] == "Physical library ID") & (csv_file_data["Group Name"] == "CMO_1") & (csv_file_data["Metric Name"] == "Fraction unrecognized CMO")]["Metric Value"].iloc[0]),\
	remove_commas(csv_file_data[(csv_file_data["Category"] == "Library") & (csv_file_data["Library Type"] == "Multiplexing Capture") & (csv_file_data["Grouped By"] == "Physical library ID") & (csv_file_data["Group Name"] == "CMO_1") & (csv_file_data["Metric Name"] == "Mean reads per cell-associated barcode")]["Metric Value"].iloc[0]),\
	remove_commas(csv_file_data[(csv_file_data["Category"] == "Library") & (csv_file_data["Library Type"] == "Multiplexing Capture") & (csv_file_data["Grouped By"] == "Physical library ID") & (csv_file_data["Group Name"] == "CMO_1") & (csv_file_data["Metric Name"] == "Median CMO UMIs per cell-associated barcode")]["Metric Value"].iloc[0]),\
	remove_commas(csv_file_data[(csv_file_data["Category"] == "Library") & (csv_file_data["Library Type"] == "Multiplexing Capture") & (csv_file_data["Grouped By"] == "Physical library ID") & (csv_file_data["Group Name"] == "CMO_1") & (csv_file_data["Metric Name"] == "Number of reads")]["Metric Value"].iloc[0]),\
	remove_commas(csv_file_data[(csv_file_data["Category"] == "Library") & (csv_file_data["Library Type"] == "Multiplexing Capture") & (csv_file_data["Grouped By"] == "Physical library ID") & (csv_file_data["Group Name"] == "CMO_1") & (csv_file_data["Metric Name"] == "Samples assigned at least one cell")]["Metric Value"].iloc[0]),\
	convert_percentage(csv_file_data[(csv_file_data["Category"] == "Library") & (csv_file_data["Library Type"] == "Multiplexing Capture") & (csv_file_data["Grouped By"] == "Physical library ID") & (csv_file_data["Group Name"] == "CMO_1") & (csv_file_data["Metric Name"] == "Sequencing saturation")]["Metric Value"].iloc[0]),\
	convert_percentage(csv_file_data[(csv_file_data["Category"] == "Library") & (csv_file_data["Library Type"] == "Multiplexing Capture") & (csv_file_data["Grouped By"] == "Physical library ID") & (csv_file_data["Group Name"] == "CMO_1") & (csv_file_data["Metric Name"] == "Valid UMIs")]["Metric Value"].iloc[0]),\
	convert_percentage(csv_file_data[(csv_file_data["Category"] == "Library") & (csv_file_data["Library Type"] == "Multiplexing Capture") & (csv_file_data["Grouped By"] == "Physical library ID") & (csv_file_data["Group Name"] == "CMO_1") & (csv_file_data["Metric Name"] == "Valid barcodes")]["Metric Value"].iloc[0]),\
	remove_commas(csv_file_data[(csv_file_data["Category"] == "Library") & (csv_file_data["Library Type"] == "Antibody Capture") & (csv_file_data["Metric Name"] == "Number of short reads skipped")]["Metric Value"].iloc[0]),\
	remove_commas(csv_file_data[(csv_file_data["Category"] == "Library") & (csv_file_data["Library Type"] == "Gene Expression") & (csv_file_data["Metric Name"] == "Number of short reads skipped")]["Metric Value"].iloc[0]),\
	remove_commas(csv_file_data[(csv_file_data["Category"] == "Library") & (csv_file_data["Library Type"] == "Multiplexing Capture") & (csv_file_data["Metric Name"] == "Number of short reads skipped")]["Metric Value"].iloc[0]),\
	convert_percentage(csv_file_data[(csv_file_data["Category"] == "Library") & (csv_file_data["Library Type"] == "Multiplexing Capture") & (csv_file_data["Metric Name"] == "Singlet capture ratio")]["Metric Value"].iloc[0]))
	return(abc_ch_values_to_insert)
	
	
def create_atac_values_statement(csv_file, csv_file_data):
	"""
	This function takes the data in the csv
	file and create the Cellranger ATAC Values Statement 
	for insertion into the ATAC Table
	in NGS_STATS
	"""
	atac_values_to_insert = "\"{}\", \"{}\", \"{}\", \"{}\", \"{}\", {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}".format(\
	csv_file.split("___")[2],\
	csv_file.split("/")[-1].split("___")[0],\
	convert_to_date_time(csv_file.split("___")[3]),\
	csv_file_data["Genome"][0],\
	csv_file_data["Pipeline version"][0],\
	csv_file_data["Estimated number of cells"][0],\
	csv_file_data["Confidently mapped read pairs"][0],\
	csv_file_data["Estimated bulk library complexity"][0],\
	csv_file_data["Fraction of all fragments in cells"][0],\
	csv_file_data["Fraction of all fragments that pass all filters and overlap called peaks"][0],\
	csv_file_data["Fraction of genome in peaks"][0],\
	csv_file_data["Fraction of high-quality fragments in cells"][0],\
	csv_file_data["Fraction of high-quality fragments overlapping TSS"][0],\
	csv_file_data["Fraction of high-quality fragments overlapping peaks"][0],\
	csv_file_data["Fraction of transposition events in peaks in cells"][0],\
	csv_file_data["Fragments flanking a single nucleosome"][0],\
	csv_file_data["Fragments in nucleosome-free regions"][0],\
	csv_file_data["Mean raw read pairs per cell"][0],\
	csv_file_data["Median high-quality fragments per cell"][0],\
	csv_file_data["Non-nuclear read pairs"][0],\
	csv_file_data["Number of peaks"][0],\
	csv_file_data["Percent duplicates"][0],\
	csv_file_data["Q30 bases in barcode"][0],\
	csv_file_data["Q30 bases in read 1"][0],\
	csv_file_data["Q30 bases in read 2"][0],\
	csv_file_data["Q30 bases in sample index i1"][0],\
	csv_file_data["Sequenced read pairs"][0],\
	csv_file_data["Sequencing saturation"][0],\
	csv_file_data["TSS enrichment score"][0],\
	csv_file_data["Unmapped read pairs"][0],\
	csv_file_data["Valid barcodes"][0])
	return(atac_values_to_insert)
	

	
	