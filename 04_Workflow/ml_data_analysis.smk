
####################################################################
######                      Preprocessing                    #######
####################################################################

rule preprocessing:
  input:
    iris = RAWDATA + "iris.txt",

  output:
    X_train = OUTPUTDIR + "00_preprocessing/X_train.txt",
    y_train = OUTPUTDIR + "00_preprocessing/y_train.npy",

  conda:
    CONTAINER + "ml_data_analysis.yaml"
  
  message: 
    "Preprocessing: prepare the data to apply machine learning classification models"  
  
  script:
    SCRIPTDIR +  "preprocessing.py"



####################################################################
######             Support Vector Machines (SVM)             #######
####################################################################

rule svm:
  input:
    X_train = OUTPUTDIR + "00_preprocessing/X_train.txt",
    y_train = OUTPUTDIR + "00_preprocessing/y_train.npy",
    
  output:
    decision_boundaries = OUTPUTDIR + "01_svn/decision_boundaries.pdf",

  params:
    kernel = config["svm"]["kernel"],

  conda:
    CONTAINER + "ml_data_analysis.yaml"
  
  message: 
    "Use sklearn to fit SVM model"  
  
  script:
    SCRIPTDIR +  "ml_data_analysis.py"
