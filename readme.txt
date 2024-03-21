Compositional and Functional Trends in Activated Sludge Bacterial Communities

This repository hosts code and files used for analysis in this project completed for the BGMP internship program.

To use program run these files in order:
 1. combined.rmd (an R script with DADA2 and alpha/beta diversity figures)
 2. FAPROTAX: Run Faprotax on the command line. You will need numpy installed. 
  ./collapse_table.py -i <normalized & filtered taxonomy table as a tsv> -g FAPROTAX.txt -o <tsv output name> -r <report output name> -d "Taxonomy" -v
 3. Bacteria_Class_Counter.py (takes in FAPROTAX output and formats it for use in R)
 4. faprotax_figures.rmd (creates figures on FAPROTAX functionality)

Authors: Farris Tedder, Ruben Lancaster, Leyla Cufurovic. 

In collaboration with Dr. Erik Coats at the University of Idaho and advised by Dr. Maxine Wren at the University of Oregon.
