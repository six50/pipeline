# SixFifty Pipeline Requirements

Follow these steps to get your system setup to run this pipeline:

1. If you're not comfortable with configuring a Python environment on your system (i.e. working with virtualenvs and pip in Python 3) then it is strongly recommended that you download the [Anaconda Python 3.6 installer](https://www.continuum.io/downloads).
2. When this is installed you should be able to open your system shell (Terminal on macOS, or search for "Anaconda Prompt" from Windows Start menu) and type `conda list` to see installed and available Python packages. You may wish to [read a little more about what Anaconda is](https://docs.continuum.io/anaconda/) at this stage if you are new to it.
3. Currently [over 450 packages are available to install](https://docs.continuum.io/anaconda/pkg-docs) for Python 3.6 via Anaconda's `conda install package-name` command. Other packages can be installed from the open source [Python Package Index](https://pypi.python.org/pypi) (a.k.a PyPI) using `pip install package-name`. The only difference is that packages installed using `conda` will be downloaded from the Anaconda repository, which has had some level of vetting by the company Continuum Analytics (provider of Anaconda) around security/reliability for use within enterprise.
4. The following packages you can `conda install` (many will already be installed):
```
conda install boto
conda install cython
conda install numpy==1.11.3
conda install pandas==0.19.2
conda install python-dateutil==2.6.0
conda install pyyaml==3.12
conda install requests==2.12.4
conda install xlrd==1.0.0
```
5. The following packages you will have to `pip install`:
```
pip install awscli==1.11.82
pip install feather-format==0.3.1
```
6. At this point you should be able to change into the repo root (`cd pipeline`) and run `python data/generate_data.py` to populate this repo with the various datasets.
7. If you want to also be able to push files to S3, you will need to do a couple more steps:
  - You will need to ask John for permissions to write into the SixFifty S3 bucket. He will set up an IAM user account and provide you with an AWS Access Key ID and a Secret Access Key.
  - Run `aws configure` from your CLI and enter the provided tokens plus `eu-west-1` for the default region. [Documentation for this step can be found here](http://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html).
  - You should now be able to run `python data/push_to_s3.py`

### TODO
Steps 4 and 5 above can be made a lot easier if we use [conda environments to manage package dependencies](https://conda.io/docs/using/envs.html#export-the-environment-file) split by conda vs pip. These are well documented and can be easily created by running `conda env export > environment.yml`, and activated from the file using `activate environment_name` (Windows) or `source activate environment_name` (macOS, Linux).

However, for this project to remain easily accessible to people using either Anaconda OR pip+virtualenv to manage their dependencies, we would need to maintain both an `environment.yml` and `requirements.txt`, unless someone can figure out a way to get `pip` to use `environment.yml`, or we autogenerate `requirements.txt` from `environment.yml`. For now, this is pretty low down my priority list, the instructions above should suffice for now.
