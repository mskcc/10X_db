#!/usr/bin/env python3

# These are functions to create the insert statements


def create_gex_insert_statement(gex_record_to_insert):
	"""
	This function creates the INSERT statement for Cellranger Gene Expression Metrics Data
	"""
	gex_insert_statement = "REPLACE INTO `ngs_stats`.`10X_GEX` (\
	`Sample_ID`,\
	`Run_ID`,\
	`CSV_Timestamp`,\
	`Estimated_Number_of_Cells`,\
	`Mean_Reads_per_Cell`,\
	`Median_Genes_per_Cell`,\
	`Number_of_Reads`,\
	`Valid_Barcodes`,\
	`Sequencing_Saturation`,\
	`Q30_Bases_in_Barcode`,\
	`Q30_Bases_in_RNA_Read`,\
	`Q30_Bases_in_UMI`,\
	`Reads_Mapped_to_Genome`,\
	`Reads_Mapped_Confidently_to_Genome`,\
	`Reads_Mapped_Confidently_to_Intergenic_Regions`,\
	`Reads_Mapped_Confidently_to_Intronic_Regions`,\
	`Reads_Mapped_Confidently_to_Exonic_Regions`,\
	`Reads_Mapped_Confidently_to_Transcriptome`,\
	`Reads_Mapped_Antisense_to_Gene`,\
	`Fraction_Reads_in_Cells`,\
	`Total_Genes_Detected`,\
	`Median_UMI_Counts_per_Cell`) VALUES ({});".format(gex_record_to_insert)
	return(gex_insert_statement)


def create_arc_insert_statement(arc_record_to_insert):
	"""
	This function creates the INSERT statement for Cellranger ARC/Multiome Metrics Data
	"""
	arc_insert_statement = "REPLACE INTO `ngs_stats`.`10X_ARC` (\
	`Sample_ID`,\
	`Run_ID`,\
	`CSV_Timestamp`,\
	`Genome`,\
	`Pipeline_version`,\
	`Estimated_number_of_cells`,\
	`Feature_linkages_detected`,\
	`Linked_genes`,\
	`Linked_peaks`,\
	`ATAC_Confidently_mapped_read_pairs`,\
	`ATAC_Fraction_of_genome_in_peaks`,\
	`ATAC_Fraction_of_high_quality_fragments_in_cells`,\
	`ATAC_Fraction_of_high_quality_fragments_in_overlapping_TSS`,\
	`ATAC_Fraction_of_high_quality_Fragments_in_overlapping_peaks`,\
	`ATAC_Fraction_of_transposition_events_in_peaks_in_cells`,\
	`ATAC_Mean_raw_read_pairs_per_cell`,\
	`ATAC_Median_high_quality_fragments_per_cell`,\
	`ATAC_Non_nuclear_read_pairs`,\
	`ATAC_Number_of_peaks`,\
	`ATAC_Percent_duplicates`,\
	`ATAC_Q30_bases_in_barcode`,\
	`ATAC_Q30_bases_in_read_1`,\
	`ATAC_Q30_bases_in_read_2`,\
	`ATAC_Q30_bases_in_sample_index_i1`,\
	`ATAC_Sequenced_read_pairs`,\
	`ATAC_TSS_enrichment_score`,\
	`ATAC_Unmapped_read_pairs`,\
	`ATAC_Valid_barcodes`,\
	`GEX_Fraction_of_transcriptomic_reads_in_cells`,\
	`GEX_Mean_raw_reads_per_cell`,\
	`GEX_Median_UMI_counts_per_cell`,\
	`GEX_Median_genes_per_cell`,\
	`GEX_Percent_duplicates`,\
	`GEX_Q30_bases_in_UMI`,\
	`GEX_Q30_bases_in_barcode`,\
	`GEX_Q30_bases_in_read_2`,\
	`GEX_Q30_bases_in_sample_index_i1`,\
	`GEX_Q30_bases_in_sample_index_i2`,\
	`GEX_Reads_mapped_antisense_to_gene`,\
	`GEX_Reads_mapped_confidently_to_exonic_regions`,\
	`GEX_Reads_mapped_confidently_to_genome`,\
	`GEX_Reads_mapped_confidently_to_intergenic_regions`,\
	`GEX_Reads_mapped_confidently_to_intronic_regions`,\
	`GEX_Reads_mapped_confidently_to_transcriptome`,\
	`GEX_Reads_mapped_to_genome`,\
	`GEX_Reads_with_TSO`,\
	`GEX_Sequenced_read_pairs`,\
	`GEX_Total_genes_detected`,\
	`GEX_Valid_UMIs`,\
	`GEX_Valid_barcodes`) VALUES ({});".format(arc_record_to_insert)
	return(arc_insert_statement)


def create_visium_insert_statement(visium_record_to_insert):
	"""
	This function creates the INSERT statement for VISIUM Spaceranger Metrics Data
	"""
	visium_insert_statement = "REPLACE INTO `ngs_stats`.`10X_VISIUM` (\
	`Sample_ID`,\
	`Run_ID`,\
	`CSV_Timestamp`,\
	`Number_of_Spots_Under_Tissue`,\
	`Number_of_Reads`,\
	`Mean_Reads_per_Spot`,\
	`Mean_Reads_Under_Tissue_per_Spot`,\
	`Fraction_of_Spots_Under_Tissue`,\
	`Median_Genes_per_Spot`,\
	`Median_UMI_Counts_per_Spot`,\
	`Valid_Barcodes`,\
	`Valid_UMIs`,\
	`Sequencing_Saturation`,\
	`Q30_Bases_in_Barcode`,\
	`Q30_Bases_in_RNA_Read`,\
	`Q30_Bases_in_UMI`,\
	`Reads_Mapped_to_Genome`,\
	`Reads_Mapped_Confidently_to_Genome`,\
	`Reads_Mapped_Confidently_to_Intergenic_Regions`,\
	`Reads_Mapped_Confidently_to_Intronic_Regions`,\
	`Reads_Mapped_Confidently_to_Exonic_Regions`,\
	`Reads_Mapped_Confidently_to_Transcriptome`,\
	`Reads_Mapped_Antisense_to_Gene`,\
	`Fraction_Reads_in_Spots_Under_Tissue`,\
	`Total_Genes_Detected`) VALUES ({});".format(visium_record_to_insert)
	return(visium_insert_statement)


def create_vdj_t_insert_statement(vdj_t_record_to_insert):
	"""
	This function creates the INSERT statement for Cellranger VDJ Metrics Data
	"""
	vdj_t_insert_statement = "REPLACE INTO `ngs_stats`.`10X_VDJ_T` (\
	`Sample_ID`,\
	`Run_ID`,\
	`CSV_Timestamp`,\
	`Estimated_Number_of_Cells`,\
	`Mean_Read_Pairs_per_Cell`,\
	`Number_of_Cells_with_Productive_VJ_Spanning_Pair`,\
	`Number_of_Read_Pairs`,\
	`Valid_Barcodes`,\
	`Q30_Bases_in_Barcode`,\
	`Q30_Bases_in_RNA_Read_1`,\
	`Q30_Bases_in_UMI`,\
	`Reads_Mapped_to_Any_VDJ_Gene`,\
	`Reads_Mapped_to_TRA`,\
	`Reads_Mapped_to_TRB`,\
	`Mean_Used_Read_Pairs_per_Cell`,\
	`Fraction_Reads_in_Cells`,\
	`Median_TRA_UMIs_per_Cell`,\
	`Median_TRB_UMIs_per_Cell`,\
	`Cells_with_Productive_VJ_Spanning_Pair`,\
	`Cells_with_Productive_VJ_Spanning_TRA_TRB_Pair`,\
	`Paired_Clonotype_Diversity`,\
	`Cells_with_TRA_Contig`,\
	`Cells_with_TRB_Contig`,\
	`Cells_with_CDR3_Annotated_TRA_Contig`,\
	`Cells_with_CDR3_Annotated_TRB_Contig`,\
	`Cells_with_VJ_Spanning_TRA_Contig`,\
	`Cells_with_VJ_Spanning_TRB_Contig`,\
	`Cells_with_Productive_TRA_Contig`,\
	`Cells_with_Productive_TRB_Contig`) VALUES ({});".format(vdj_t_record_to_insert)
	return(vdj_t_insert_statement)


def create_abc_insert_statement(abc_record_to_insert):
	"""
	This function creates the INSERT statement for Cellranger MULTI Antibody Capture Metrics Data
	"""
	abc_insert_statement  = "REPLACE INTO `ngs_stats`.`10X_ABC` (\
	`Sample_ID`,\
	`Run_ID`,\
	`CSV_Timestamp`,\
	`Mean_antibody_reads_usable_per_cell`,\
	`Median_UMI_counts_per_cell`,\
	`GEX_Cells`,\
	`GEX_Confidently_mapped_reads_in_cells`,\
	`GEX_Median_UMI_counts_per_cell`,\
	`GEX_Median_genes_per_cell`,\
	`GEX_Total_genes_detected`,\
	`Estimated_number_of_cells`,\
	`Fraction_antibody_reads`,\
	`Fraction_antibody_reads_in_aggregate_barcodes`,\
	`Fraction_antibody_reads_usable`,\
	`Mean_reads_per_cell`,\
	`Number_of_reads`,\
	`Sequencing_saturation`,\
	`Valid_UMIs`,\
	`Valid_barcodes`) VALUES ({});".format(abc_record_to_insert)
	return(abc_insert_statement)
	
	
def create_ch_insert_statement(ch_record_to_insert):
	"""
	This function creates the INSERT statement for Cellranger MULTI Multiplexing Capture Metrics Data
	"""
	ch_insert_statement = "REPLACE INTO `ngs_stats`.`10X_CH` (\
	`Sample_ID`,\
	`CH_Sample_ID`,\
	`Run_ID`,\
	`CSV_Timestamp`,\
	`GEX_Cells_assigned_to_other_samples`,\
	`GEX_Cells_assigned_to_this_sample`,\
	`Cell_associated_barcodes_identified_as_multiplets`,\
	`Cell_associated_barcodes_not_assigned_any_CMOs`,\
	`Cells_assigned_to_a_sample`,\
	`Estimated_number_of_cell_associated_barcodes`,\
	`Fraction_CMO_reads`,\
	`Fraction_CMO_reads_usable`,\
	`Fraction_reads_from_multiplets`,\
	`Fraction_reads_in_cell_associated_barcodes`,\
	`Fraction_unrecognized_CMO`,\
	`Mean_reads_per_cell_associated_barcode`,\
	`Median_CMO_UMIs_per_cell_associated_barcode`,\
	`Number_of_reads`,\
	`Samples_assigned_at_least_one_cell`,\
	`Sequencing_saturation`,\
	`Valid_UMIs`,\
	`Valid_barcodes`) VALUES ({});".format(ch_record_to_insert)
	return(ch_insert_statement)
		

def create_vdj_b_insert_statement(vdj_b_record_to_insert):
	"""
	This function creates the INSERT statement for Cellranger VDJ-B Metrics Data
	"""
	vdj_b_insert_statement = "REPLACE INTO `ngs_stats`.`10X_VDJ_B` (\
	`Sample_ID`,\
	`Run_ID`,\
	`CSV_Timestamp`,\
	`Estimated_Number_of_Cells`,\
	`Mean_Read_Pairs_per_Cell`,\
	`Number_of_Cells_with_Productive_VJ_Spanning_Pair`,\
	`Number_of_Read_Pairs`,\
	`Valid_Barcodes`,\
	`Q30_Bases_in_Barcode`,\
	`Q30_Bases_in_RNA_Read_1`,\
	`Q30_Bases_in_UMI`,\
	`Reads_Mapped_to_Any_VDJ_Gene`,\
	`Reads_Mapped_to_IGH`,\
	`Reads_Mapped_to_IGK`,\
	`Reads_Mapped_to_IGL`,\
	`Mean_Used_Read_Pairs_per_Cell`,\
	`Fraction_Reads_in_Cells`,\
	`Median_IGH_UMIs_per_Cell`,\
	`Median_IGK_UMIs_per_Cell`,\
	`Median_IGL_UMIs_per_Cell`,\
	`Cells_with_Productive_VJ_Spanning_Pair`,\
	`Cells_With_Productive_VJ_Spanning_IGK_IGH_Pair`,\
	`Cells_With_Productive_VJ_Spanning_IGL_IGH_Pair`,\
	`Paired_Clonotype_Diversity`,\
	`Cells_With_IGH_Contig`,\
	`Cells_With_IGK_Contig`,\
	`Cells_With_IGL_Contig`,\
	`Cells_With_CDR3_Annotated_IGH_Contig`,\
	`Cells_With_CDR3_Annotated_IGK_Contig`,\
	`Cells_With_CDR3_Annotated_IGL_Contig`,\
	`Cells_With_VJ_Spanning_IGH_Contig`,\
	`Cells_With_VJ_Spanning_IGK_Contig`,\
	`Cells_With_VJ_Spanning_IGL_Contig`,\
	`Cells_With_Productive_IGH_Contig`,\
	`Cells_With_Productive_IGK_Contig`,\
	`Cells_With_Productive_IGL_Contig`) VALUES ({});".format(vdj_b_record_to_insert)
	return(vdj_b_insert_statement)


def create_visium_ffpe_insert_statement(visium_ffpe_record_to_insert):
	"""
	This function creates the INSERT statement for visium FFPE Spaceranger Metrics Data
	"""
	visium_ffpe_insert_statement = "REPLACE INTO `ngs_stats`.`10X_VISIUM_FFPE` (\
	`Sample_ID`,\
	`Run_ID`,\
	`CSV_Timestamp`,\
	`Number_of_Spots_Under_Tissue`,\
	`Number_of_Reads`,\
	`Mean_Reads_per_Spot`,\
	`Mean_Reads_Under_Tissue_per_Spot`,\
	`Fraction_of_Spots_Under_Tissue`,\
	`Valid_Barcodes`,\
	`Valid_UMIs`,\
	`Sequencing_Saturation`,\
	`Q30_Bases_in_Barcode`,\
	`Q30_Bases_in_Probe_Read`,\
	`Q30_Bases_in_UMI`,\
	`Reads_Mapped_to_Probe_Set`,\
	`Reads_Mapped_Confidently_to_Probe_Set`,\
	`Fraction_Reads_in_Spots_Under_Tissue`,\
	`Median_Genes_per_Spot`,\
	`Median_UMI_Counts_per_Spot`,\
	`Genes_Detected`,\
	`Reads_Mapped_Confidently_to_the_Filtered_Probe_Set`,\
	`Number_of_Genes`,\
	`Number_of_Genes_GreaterThanEqualTo_10_UMIs`,\
	`Reads_Half_Mapped_to_Probe_Set`,\
	`Reads_Split_Mapped_to_Probe_Set`,\
	`Estimated_UMIs_from_Genomic_DNA`,\
	`Estimated_UMIs_from_Genomic_DNA_per_Unspliced_Probe`) VALUES ({});".format(visium_ffpe_record_to_insert)
	return(visium_ffpe_insert_statement)


def create_abc_ch_insert_statement(abc_ch_record_to_insert):
	"""
	This function creates the INSERT statement for Cellranger MULTI Antobody Capture and Multiplexing Capture Metrics Data
	"""
	abc_ch_insert_statement = "REPLACE INTO `ngs_stats`.`10X_ABC_CH` (\
	`Sample_ID`,\
	`CH_Sample_ID`,\
	`Run_ID`,\
	`CSV_Timestamp`,\
	`ABC_Cells`,\
	`ABC_Antibody_reads_usable_per_cell`,\
	`ABC_Median_UMI_counts_per_cell`,\
	`GEX_Cells`,\
	`GEX_Median_UMI_counts_per_cell`,\
	`GEX_Median_genes_per_cell`,\
	`GEX_Median_reads_per_cell`,\
	`GEX_Total_genes_detected`,\
	`GEX_Cell_associated_barcodes_identified_as_multiplets`,\
	`GEX_Cell_associated_barcodes_not_assigned_any_CMOs`,\
	`GEX_Cells_assigned_to_other_samples`,\
	`GEX_Cells_assigned_to_this_sample`,\
	`ABC_Estimated_number_of_cells`,\
	`ABC_Fraction_antibody_reads`,\
	`ABC_Fraction_antibody_reads_in_aggregate_barcodes`,\
	`ABC_Fraction_antibody_reads_usable`,\
	`ABC_Means_reads_per_cell`,\
	`ABC_Number_of_reads`,\
	`ABC_Sequencing_saturation`,\
	`ABC_Valid_UMIs`,\
	`ABC_Valid_barcodes`,\
	`GEX_Confidently_mapped_reads_in_cells`,\
	`CH_Cell_associated_barcodes_identified_as_multiplets`,\
	`CH_Cell_associated_barcodes_not_assigned_any_CMOs`,\
	`CH_Cells_assigned_to_a_sample`,\
	`CH_Estimated_number_of_cell_associated_barcodes`,\
	`CH_Fraction_CMO_reads`,\
	`CH_Fractiom_CMO_reads_usable`,\
	`CH_Fraction_reads_from_multiplets`,\
	`CH_Fraction_reads_in_cell_associated_barcodes`,\
	`CH_Fraction_unrecognized_CMO`,\
	`CH_Mean_reads_per_cell_associated_barcode`,\
	`CH_Median_CMO_UMIs_per_cell_associated_barcode`,\
	`CH_Number_of_reads`,\
	`CH_Samples_assigned_at_least_one_cell`,\
	`CH_Sequencing_saturation`,\
	`CH_Valid_UMIs`,\
	`CH_Valid_barcodes`,\
	`ABC_Number_of_short_reads_skipped`,\
	`GEX_Number_of_short_reads_skipped`,\
	`CH_Number_of_short_reads_skipped`,\
	`CH_Singlet_capture_ratio`) VALUES ({});".format(abc_ch_record_to_insert)
	return(abc_ch_insert_statement)


def create_atac_insert_statement(atac_record_to_insert):
	"""
	This function creates the INSERT statement for Cellranger ATAC Metrics Data
	"""
	atac_insert_statement = "REPLACE INTO `ngs_stats`.`10X_ATAC` (\
	`Sample_ID`,\
	`Run_ID`,\
	`CSV_Timestamp`,\
	`Genome`,\
	`Pipeline_version`,\
	`Estimated_number_of_cells`,\
	`Confidently_mapped_read_pairs`,\
	`Estimated_bulk_library_complexity`,\
	`Fraction_of_all_fragments_in_cells`,\
	`Fraction_all_fragments_pass_all_filters_overlap_called_peaks`,\
	`Fraction_of_genome_in_peaks`,\
	`Fraction_of_high_quality_fragments_in_cells`,\
	`Fraction_of_high_quality_fragments_overlapping_TSS`,\
	`Fraction_of_high_quality_fragments_overlapping_peaks`,\
	`Fraction_of_transposition_events_in_peaks_in_cells`,\
	`Fragments_flanking_a_single_nucleosome`,\
	`Fragments_in_nucleosome_free_regions`,\
	`Mean_raw_read_pairs_per_cell`,\
	`Median_high_quality_fragments_per_cell`,\
	`Non_nuclear_read_pairs`,\
	`Number_of_peaks`,\
	`Percent_duplicates`,\
	`Q30_bases_in_barcode`,\
	`Q30_bases_in_read_1`,\
	`Q30_bases_in_read_2`,\
	`Q30_bases_in_sample_index_i1`,\
	`Sequenced_read_pairs`,\
	`Sequencing_saturation`,\
	`TSS_enrichment_score`,\
	`Unmapped_read_pairs`,\
	`Valid_barcodes`) VALUES ({});".format(atac_record_to_insert)
	return(atac_insert_statement)







	