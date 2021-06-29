
[![Python application test with Github Actions](https://github.com/fengxiakira/BostonHousingPricePrediction/actions/workflows/python-app.yml/badge.svg)](https://github.com/fengxiakira/BostonHousingPricePrediction/actions/workflows/python-app.yml)
# Overview

BostonHousingPricePrediction is a web app that hosted on Azure App Service to predict the housing price at Boston.

## Project Plan


* [A link to a Trello board for the project](https://trello.com/b/f0h9Nuuu/az2-build-ci-cd-pipeline-5-29)


* [A link to a spreadsheet that includes the original and final project plan](https://docs.google.com/spreadsheets/d/1dWaVzakvCpGNrWAXU-JxqgsjDw-sZNddCc69C8quTYc/edit#gid=596363533)

## Instructions

<TODO:  
* Architectural Diagram (Shows how key parts of the system work)>

<TODO:  Instructions for running the Python project.  How could a user with no context run this project without asking you for any help.  Include screenshots with explicit steps to create that work. Be sure to at least include the following screenshots:

* Project running on Azure App Service
![APP SERVICE](/app_service.png)

* Project cloned into Azure Cloud Shell
![clone](/cloneproject.png)

* Passing tests that are displayed after running the `make all` command from the `Makefile`
![all](/make.png)

* Output of a test run
![test](/passing_tests.png)

* Successful deploy of the project in Azure Pipelines.  [Note the official documentation should be referred to and double checked as you setup CI/CD](https://docs.microsoft.com/en-us/azure/devops/pipelines/ecosystems/python-webapp?view=azure-devops).
![deploy](/successful_deployment.png)

* Running Azure App Service from Azure Pipelines automatic deployment

![azurepiplines](./azpipeline-result.png)

* Successful prediction from deployed flask app in Azure Cloud Shell.  [Use this file as a template for the deployed prediction](https://github.com/udacity/nd082-Azure-Cloud-DevOps-Starter-Code/blob/master/C2-AgileDevelopmentwithAzure/project/starter_files/flask-sklearn/make_predict_azure_app.sh).
The output should look similar to this:

![prediction](./successful_prediction.png)
* Output of streamed log files from deployed application
![logtail](./log-tail.png)
> 

## Enhancements

<TODO: A short description of how to improve the project in the future>
To be continued

## Demo 

<TODO: Add link Screencast on YouTube>


