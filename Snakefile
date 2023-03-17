# Docker container based on a minimal Ubuntu installation that includes conda-forge's mambaforge installer.
container: "docker://condaforge/mambaforge:22.11.1-4"

from snakemake.utils import validate, min_version
##### set minimum snakemake version #####
min_version("5.1.2")

##### load config and sample sheets #####
configfile: "config.yaml"
validate(config, schema="06_Schemas/config.schema.yaml")

##### Set variables ####
ROOTDIR = os.getcwd()
RAWDATA = srcdir("00_RawData/")
REF = srcdir("01_Reference/")
CONTAINER = srcdir("02_Container/")
SCRIPTDIR = srcdir("03_Script/")
ENVDIR = srcdir("04_Workflow/")
OUTPUTDIR = srcdir("05_Output/")
SCHEMAS = srcdir("06_Schemas/")
REPORT = srcdir("07_Report/")

# ----------------------------------------------
# Target rules
# ----------------------------------------------

rule all:
  input:
    X_train = OUTPUTDIR + "00_preprocessing/X_train.txt",
    y_train = OUTPUTDIR + "00_preprocessing/y_train.npy",
    decision_boundaries = OUTPUTDIR + "01_svn/decision_boundaries.pdf",

# ----------------------------------------------
# Setup report
# ----------------------------------------------

report: "07_Report/workflow.rst"

# ----------------------------------------------
# Load rules 
# ----------------------------------------------

include: ENVDIR + "ml_data_analysis.smk"
