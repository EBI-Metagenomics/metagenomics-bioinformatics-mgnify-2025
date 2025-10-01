# Answers to MAGs practical

### Binning

MetaBAT2 returned 10 bins. You can count number of sequences with command:
```commandline
grep '>' bin.0.fa | wc -l
```

### CheckM
![checkm1_table.png](answers%2Fcheckm1_table.png)

### CheckM2
![checkm2_table.png](answers%2Fcheckm2_table.png)

### Comparing CheckM and CheckM2

CheckM plot:
![checkm1.png](answers%2Fcheckm1.png)
CheckM2 plot:
![checkm2.png](answers%2Fcheckm2.png)

### GTDB-Tk taxonomy
![gtdb.png](answers%2Fgtdb.png)
### NCBI taxonomy
![ncbi.png](answers%2Fncbi.png)

### Defining Taxonomy Identifier (TaxID)


| bin    | taxonomy           | taxID |
|--------|--------------------|-------|
| bin.1  | Unclassified Bacteria | 2
| bin.2  | Unclassified Bacteria | 2
| bin.3  | s__Lachnospira eligens | 39485
| bin.4  | s__Bacteroides uniformis | 820
| bin.5  | g__Ruminococcus | 1263
| bin.6  | c__Alphaproteobacteria | 28211
| bin.7  | s__Phocaeicola dorei | 357276
| bin.8  | s__Phocaeicola plebeius | 310297
| bin.9  | Unclassified Bacteria | 2
| bin.10 | f__Lachnospiraceae | 186803




### Visualizing the phylogenetic tree

Unrooted tree

![unrooted_tree.png](answers/unrooted_tree.png)

Search for **bin.7**

![search-bin.png](answers/search-bin.png)

**Note:**

**bin.5** might have different species name on the tree because taxonomy has changed between versions.
`s__Ruminococcoides intestinalis` can be searched as `s__Ruminococcus_E intestinalis`

**bin.6** is missing in the tree :)