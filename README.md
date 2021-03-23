# NNIA Assignment



## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Prerequisites

A working python environment should be installed on the machine used for this task. (Preferably latest version) 


### Data Preprocessing

The data required for preprocessing should be in .conll format. Samples can be seen in [Example_files](https://github.com/Kaikei1/NN_Project/tree/main/example%20files)

For later development purposes we need .tsv format files and the given datasets had the .conll format.
preprocessing.py takes a .conll and extracts three features (3 columns) and returns a new dataset only containing those 3 features. Here we are interested in position of a word (first column), the word itself (second column), POS tag (third column). In addition, this program creates a .info file containing some notable statistics. If a folder called 'output' doesn't already exist in the same directory as preprocessing.py, it is created. This is where the .tsv file and the .info file are saved.

How to use: 

Input: .conll data (Error will be returned if it is the wrong datatype) and desired output name of the file. (E.g. you have nyt.conll and you want it to be named nyt_processed.tsv and nyt_processed.info after processing the data.)

Given that you processed the data into a tsv file using the preprocessor.py, you can use the loading_script.py to load your data into a fitting format for run_ner.py to train your BERT model. (NOTE: The names in loading_script.py are predefined and take no input. You might want to change the data you want to process, therefore you should change the path in the code.)
The loading script reads the tsv files and processes them into a dataframe, generating a .csv output.

## Deployment


Try running the run_pos.sh in [Example_files](https://github.com/Kaikei1/NN_Project/tree/main/example%20files). You might have to change the bash script, if you want to use different embeddings or accessing different directory's.
This one is built to run POS task using the pretrained bert-base-cased model on a single epoch.
run_pos.sh executes run_ner.py and automatically passes the required arguments to run the training and evaluation.

## Built With

Python using the huggingface/transformers library.




## Authors

Kaikei1 & Unkei1

## License

