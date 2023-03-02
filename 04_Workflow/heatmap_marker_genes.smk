####################################################################
######         Heatmap of the marker genes expression        #######
####################################################################

rule heatmap:
  input:
    norm_count_zscore = RAWDATA + "Scran_normalised_counts.zScores.txt",

  output:
    rule_heatmap = OUTPUTDIR + "01_heatmap_marker_genes/heatmap_marker_genes.txt",

  params:
    heatmap_pdf = OUTPUTDIR + "01_heatmap_marker_genes/heatmap_marker_genes2.txt",

  conda:
    CONTAINER + "heatmap_marker_genes.yaml"
  
  message: 
    "Produce the heatmap of the marker genes expression"  
  
  shell:
    """
    Rscript {SCRIPTDIR}heatmmap_marker_genes.R {input.norm_count_zscore} {params.heatmap_pdf} 
    echo "Heatmap of the marker genes expression step is FINISH" > {output.rule_heatmap}
    """