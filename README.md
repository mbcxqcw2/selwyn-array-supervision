# Selwyn College Cambridge
## Coding Supervision
## Python array manipulation for astronomical processing

___

## Introduction

Welcome to this Selwyn College coding supervision. This supervision is a practical tutorial in array manipulation using the Python programming language.

During this tutorial, we will introduce the concept of Python arrays. We will learn how to create, access, edit, and display arrays of increasing complexity. We will then use what we have learned to process some simulated astronomical data, developing practical experience in *radio frequency interference (RFI) mitigation*, which is a commonly employed early processing step in many transient radio astronomy data analysis pipelines.

___
___

## Resources

You can access the workbook for this tutorial in one of two ways:

### Option 1: Using Google Colab

Click [here](INSERT LINK) to access a Google Colab notebook containing the learning material. Once you have been granted access to this notebook, please save a copy of it to your drive. *Please and only modify your copy of the file.* If you modify the original file, other students will lose access to the original learning material.

The Google Colab notebook works you through the supervision, leaving gaps for you to input your own code where required. Please attempt the blank sections by yourself best of your ability first. If you get stuck, another workbook complete with answers can be found below.

### Option 2: Running the workbook locally on your laptop

If you wish to run through this notebook locally on your laptop instead of online using Google Colab, you will need access to Jupyter notebooks and various python packages on your machine. Click below to see these dependencies:

<details>
<summary>Dependencies for running local version</summary>

- python=3.8
- numpy
- matplotlib
- astropy
- scipy
- jupyter
- ipython
- pip
- imageio

</details>

If you have access to your machine's command line, miniconda and github, then you can easily set up this environment with the following steps:

<details>
<summary>Steps for running a local version</summary>

- Open your command line and navigate to the directory you will use as your base directory using `cd`
- Within your base directory, git clone this repository: `>git clone https://github.com/mbcxqcw2/selwyn-array-supervision.git`
- Within your base directory, navigate to the repository's miniconda subdirectory: `>cd /selwyn-array-supervision/miniconda/`
- Create an environment: `>conda env create -f selwyn_computing_env.yml`
- Activate the environment as instructed by miniconda
- From within the `/miniconda/ directory, navigate back to the subdirectory containing the workbooks: `>cd ../notebooks/`
- Within your `/notebooks/` directory, run: `>jupyter notebook` in your command line and open the url which is displayed
- Open `Workbook.ipynb`

</details>

### Workbook answers

<details>

<summary>Accessing workbook answers</summary>

- Option 1: [Click here](INSERT LINK) to access a Google Colab notebook containing the complete workbook. DO NOT MODIFY ANY OF THE CODE IN THIS WORKBOOK! It should serve as a reference for your personal workbook only. Save a copy of this worked example into your drive before you run anything.

- Alternatively, if you are running a local version of this tutorial, you can find a completed workbook in the `/notebooks/` directory. This completed workbook is called `Workbook_Answers.ipynb`.

</details>

## Developers

- Walker, C.R.H. (University of Cambridge, Trevelyan Research Associate, Selwyn College, Cambridge)
