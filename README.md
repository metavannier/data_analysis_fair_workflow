# Introduction to biological data analysis

## Author

Thomas Vannier (@metavannier), https://centuri-livingsystems.org/t-vannier/

## About

A workflow to understand how to analyze this data follow the FAIR data principles (findable, accessible, interoperable, reusable).

## Usage

### Step 1: Install workflow

You can use this workflow by downloading and extracting the latest release. If you intend to modify and further extend this workflow or want to work under version control, you can fork this repository.

We would be pleased if you use this workflow and participate in its improvement. If you use it in a paper, don't forget to give credits to the author by citing the URL of this repository and, if available, its DOI (see above).

### Step 2: Configure workflow

Configure the workflow according to your needs via editing the files and repositories:
- 00_RawData need the iris table (iris.txt).

- [config.yaml](/config.yaml) indicating the parameters to use.

### Step 3: Execute workflow

#### In local

- You need [Singularity v3.5.3](https://github.com/hpcng/singularity/blob/master/INSTALL.md#install-golang) installed on your computer or cluster.

- Load snakemake from a docker container and run the workflow from the root by using these commands:

`singularity run docker://snakemake/snakemake:v6.3.0`

- Then execute the workflow locally via

`snakemake  --use-conda --use-singularity --cores 10`

#### On a cluster

- Adapt the batch scripts run_slurm.sh and cluster_config.json file to run your snakemake from the working directory

It will install snakemake with pip and run the workflow in the HPC:

`sbatch run_slurm.sh`

### Step 4: Investigate results 

After successful execution, you can create a self-contained interactive HTML report with all results via:

`snakemake --report report.html`
