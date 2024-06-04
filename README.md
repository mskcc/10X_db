# 10X Database implementation into LIMS


 This is code to parse and store 10X Cellranger data into ngs_stats and LIMS
 

These python script process the summary data from the various 10X pipelines and stores that data into tables that are in the ngs-stats database.

The pipeline data that is stored in the database is listed below:

1. Gene Expression
2. VDJ (TCR, BCR)
3. ARC (Multiome - ATAC + GEX)
4. Visium, Visium FFPE (Spaceranger)
5. ATAC
6. Antibody Capture
7. Cell Multiplexing (Cell Hashing)


The pipeline data is stored in the 10X data tables that are stored in NGS stats

1. 10X_GEX - Gene expression data from Cellranger Count pipeline
2. 10X_VDJ_B - VDJ BCR data from Cellranger VDJ pipeline
3. 10X_VDJ_T - VDJ TCR data from Cellranger VDJ pipeline
4. 10X_ARC - Multiome data from Cellranger ARC pipeline
5. 10X_CH - Cell Multiplexing Data from the Cellranger Multi pipeline
6. 10X_ABC - Antibody Capture Data from the Cellranger Multi pipeline
7. 10X_ABC_CH - Antibody Capture/Cell Multiplexing Cellranger Multi pipeline
8. 10X_VISIUM - Spatial transcriptomic data from Spaceranger Count pipeline
9. 10X_VISUIM_FFPE - Spatial transcriptomic data from Spaceranger Count pipeline (for FFPE samples)
10. 10X_ATAC - ATAC data from the Cellranger ATAC pipeline

Note:

For the Cellranger pipelines, version 8.0.0 is the latest version

For the Spaceranger pipelines, 3.0.0 is the latest version

for the ARC (Multiome pipeline) 2.0.1 is the latest version

For the cellranger Multi pipeline when Antibody Capture and Cell Hashing Cellranger version 7.0.0 is being used.



##  Renaming the Metrics Summary Files

The first step in inserting the 10X pipeline metrics into the 10X database is to gather the files and rename them.  The script that does this is the grab_cellranger_metrics_summary_data script.  This script takes in the RUN-ID as input.  Next, it searches in the /igo/staging/CELLRANGER/{RUNID} directory and gathers all of the metrics_summary.csv file and the summary.csv files.  In the script, it keeps track of the RUN-ID and sample names to rename the script from the generic metrics_summary file name to a name that includes the RUN-ID, sample name, time stamp of the file and an acronym of the pipeline from which the data was produced.  Once the file is renamed, it is placed in a folder on the IGODB server called /home/nabors/STATS/CELLRANGER.  From this folder, the import_records_into_db python script will search for files for the particular RUN-ID and parse only those files and store that data in to the 10X tables in NGS stats.

example:

/home/nabors/pyvenv/bin/python3 /home/nabors/database_testing/official_scripts/grab_cellranger_metrics_summary_data.py FAUCI_0143_B22GC3KLT3




## Placing the 10X stats from the Metrics Summary Files in NGS stats DB

As input, the the import_records_into_db python script takes in the RUN-ID, then searches in the /home/nabors/STATS/CELLRANGER directory for renamed csv files that have the desired RUN-ID as the file name. Once those files are gathered, it takes those files and parses them one by one, placing the file from the corresponding pipeline into its 10X table in NGS stats.

example:

/home/nabors/pyvenv/bin/python3 /home/nabors/database_testing/official_scripts/import_records_into_db.py FAUCI_0143_B22GC3KLT3