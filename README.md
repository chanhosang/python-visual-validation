# Python Visual Validation

- [Python Visual Validation](#python-visual-validation)
- [Overview](#overview)
  - [Setup Chrome Driver](#setup-chrome-driver)
  - [Setup Virtual Environment](#setup-virtual-environment)
  - [Setup Image Tester](#setup-image-tester)
  - [Run Test](#run-test)
    - [Organizing Tests in Test Suite](#organizing-tests-in-test-suite)
    - [Visual Validation - PDF](#visual-validation---pdf)

# Overview

This project was modified from the source code provided by [Automated Visual Testing with Python](https://testautomationu.applitools.com/visual-testing-python) in [Test Automation University](https://testautomationu.applitools.com/).


## Setup Chrome Driver

Selenium WebDriver by itself is just a programming package and it needs different WebDriver to work with different browsers:
* ChromeDriver - Chrome
* GeckoDriver - Firefox
  
Always make sure to stay on top of updates, and make sure your driver versions match your browser versions. 

In this example project, I am using **Chrome browser**. 

Hence, you will need to download ChromeDriver from [here](https://chromedriver.chromium.org/) to your preferable directory and include the directory as PATH environment variable.

Then, check the version of the chrome driver by the following terminal command:
```
chromedriver --version
```

## Setup Virtual Environment
To install pipenv on your Python installation, run the following terminal command:
```
 pip install pipenv
 ```

To initialize an empty virtual environment (virtualenv) and activate the environment, run the following terminal command:
 ```
 pipenv --three
 pipenv shell
```
To install [pytest](https://pypi.org/project/pytest/), run the following terminal command:
 ```
 pipenv install pytest
 ```
To install [eyes-selenium](https://chromedriver.chromium.org/) module, run the following terminal command:
 ```
 pipenv install eyes-selenium
 ```
To install [pytest-html](https://pypi.org/project/pytest-html/) module, run the following terminal command:
```
pipenv install pytest-html
```
## Setup Image Tester

In this sample project, I will be integrating the pytest with [ImageTester](https://help.applitools.com/hc/en-us/articles/360007188551-Image-Tester-Stand-alone-tool-for-images-comparison).

Download the ImageTester Version 1.4.5.2 binary jar file from [here](https://bintray.com/applitoolseyes/generic/ImageTester/1.4.5.2#files) to 'libs' folder in this project directory.

**Note:** If you choose to use a different version of the toool, please update the **IMAGE_TESTER_PATH** in *core/eyes_manager.py*.

## Run Test
### Organizing Tests in Test Suite

There are two tests in 'organizing_test_suite' module, which click on the first name and the last name header and then take a screenshot to compare against the baseline.

Instead of creating different test suites for each of the individual cases, there will ONLY be a single test suite with the name that was provided and the two cases nicely organized.

To run tests, run the following command from the project's root directory:
```
python -m pytest -m organize tests/organizing_test_suite --html=report.html 
```

If you want to filter test by marker (e.g. organize), just use the -m option and specify the desired marker name as follow:
```
python -m pytest -m organize tests/organizing_test_suite --html=report.html 
```
*Note: Markers are basically tags for test cases. Any test can have any number of markers. pytest has a few standard markers, but you can add your own custom markers too.*

### Visual Validation - PDF

In 'visual_validation_pdf' module, here is the test scenario being automated:
* Log on to https://app.invoicesimple.com/
* Generate an Invoice in PDF
* Download and copy the PDF to the *resources* folder of this project directory.
* Execute ImageTester to performance visual tests on the PDF files found in the *resources* folder.
  
To run tests, run the following command from the project's root directory:
```
python -m pytest tests/visual_validation_pdf --html=report.html 
```
Once the test is completed, the comparison result will be published to [Applitools Website](https://eyes.applitools.com/app/test-results).