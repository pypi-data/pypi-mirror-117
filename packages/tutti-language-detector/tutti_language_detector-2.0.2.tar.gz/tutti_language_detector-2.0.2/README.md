# tutti language detector

This repository contains a Python package with pretrained language model for German, Italian and French that allows us to identify the language of a tutti.ch ad from its subject and body text.

## Installation prerequisites
Tutti language detector requires [Vowpal Wabbit](https://github.com/VowpalWabbit/vowpal_wabbit/wiki/Getting-started) executable `vw` which can be installed on Ubuntu with `sudo apt-get install vowpal-wabbit`. **Do not use the PyPI version** since it only installs the Python package but not the `vw` binary that the language detector uses.

## Installation
`pip install tutti-language-detector`

## Development
To ensure reproducibility, try to develop in a virtual environment. The directory `venv` is in gitignore. To setup a virtual environment, run `python3 -m venv --copies venv`, then activate the environment `source venv/bin/activate` and upgrade pip `pip install pip --ugprade`.

To develop the package, first install AWS command-line tool and [DVC](https://dvc.org). These are needed to pull in the models from S3. Installation steps: 
1. `pip install awscli`
2. `aws configure`
3. `pip install dvc`
 
Then get the code:
 
1. `git clone git@gitlab.com:tutti-ch/team-data/tutti-language-detector-package.git language-detector`
2. `cd language-detector`
3. `dvc pull`
4. `pip3 install -e .` 
 
## Releases
Production released are git-tagged and then uploaded to `https://pypi.org/project/tutti-language-detector`.

## Training
In the `develop-new-model` directory there are scripts used for training and generating a new language classification model, configured into a DVC pipeline that ingests a CSV dataset, outputs VW formatted data files for the train/test split, uses these files for training models and doing an automatized parallel random search for model hyperparameters, and once it finds the best model it trains it on the full dataset.

Be aware that training a new model is a highly manual procedure and that due to the random nature of 1) train-test splits (although the random seed allows us to stabilize these) and 2) random search of hyperparameters, the results may not be reproducible (so a same dataset can yield different end models using the automated DVC pipeline). In order to get the exact same results, the exact same dataset and hyperparameters need to be used, which is not implemented into the pipeline and as such deemed as 'manual work'. What's more, the concepts of overfitting, precision and recall, cross entropy, confusion matrices..., give information about the performance of a model, and this manual testing step is somewhat skipped in the pipeline by comparing models exclusively by cross entropy (log-loss). For a better understanding of the strenghts and weaknesses of the trained models more 'manual work' is required.

## Publish new version to PyPI
1. Commit and push your code modifications to the repository.
2. Update `__init__.py` to bump the version (if there are possible breaking changes, bump the major version).
3. Create a git tag for marking the release in the repository, e.g.: 
`git tag -a 3.2.1 -m "Release 3.2.1"`, and push it to the remote: `git push origin 3.2.1`.
3. Use the `setup.py` script to generate a source distribution and build the package: `python3 setup.py sdist bdist_wheel`. 
You will possibly need to install the `wheel` package: `pip3 install --user wheel`. 
4. Publish the package generated in the `dist/` directory to PyPI. You can use the `twine` package to do so. See 
[the documentation](https://twine.readthedocs.io/en/latest/) to configure it. An example command is for pushing version
3.2.1 would be `twine upload --repository pypi dist/*3.2.1*`.
