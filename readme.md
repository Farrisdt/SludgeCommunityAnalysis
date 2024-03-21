### Compositional and Functional Trends in Activated Sludge Bacterial Communities
Authors: Farris Tedder, Ruben Lancaster, Leyla Cufurovic.   
  
In collaboration with Dr. Erik Coats at the University of Idaho and advised by Dr. Maxine Wren at the University of Oregon.  


This repository hosts code and files used for analysis in this project completed for the BGMP internship program.

#### Running this program

To use program run these files in order:
 1. combined.rmd (an R script with DADA2 and alpha/beta diversity figures)
 2. FAPROTAX: Run Faprotax on the command line. You will need numpy installed. 
 ```
  ./collapse_table.py -i <normalized & filtered taxonomy table as a tsv> -g FAPROTAX.txt -o <tsv output name> -r <report output name> -d "Taxonomy" -v
 ```
 3. Bacteria_Class_Counter.py (takes in FAPROTAX output and formats it for use in R)
 4. faprotax_figures.rmd (creates figures on FAPROTAX functionality)

#### File descriptions

| File | Description |
| ---- | ----------- |
| Illumina_Reads_updated_3_20_24.xlsx | metadata |
| asv_counts.tsv | ASV counts file |
| taxa_silva_dada2.tsv | taxonomy file, using the SILVA database |
| silva_allgroups_taxtable_1-27-24-filt-norm.tsv | taxonomy table input for FAPROTAX |
| silva_allgroups_taxtable_1-27-24-filt-norm_out.tsv| tabular output from FAPROTAX |
| silva_allgroups_taxtable_1-27-24-filt-norm_report.txt | text report output from FAPROTAX |
| Funtional_Taxonomy_Report.txt | tabular output of FAPROTAX report from Bacteria_Class_Counter.py |

