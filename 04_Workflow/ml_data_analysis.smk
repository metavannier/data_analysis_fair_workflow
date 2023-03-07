####################################################################
######             Support Vector Machines (SVM)             #######
####################################################################

rule svm:
  input:
    iris = RAWDATA + "iris.txt",

  output:
    decision_boundaries = OUTPUTDIR + "01_svn/decision_boundaries.pdf",
    training_points = OUTPUTDIR + "01_svn/training_points.pdf"

  params:
    kernel = config["svm"]["kernel"],

  conda:
    CONTAINER + "ml_data_analysis.yaml"
  
  message: 
    "Use sklearn to fit SVM model"  
  
  script:
    SCRIPTDIR +  "ml_data_analysis.py"
