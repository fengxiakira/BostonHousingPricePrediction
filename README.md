
[![Python application test with Github Actions](https://github.com/fengxiakira/BostonHousingPricePrediction/actions/workflows/python-app.yml/badge.svg)](https://github.com/fengxiakira/BostonHousingPricePrediction/actions/workflows/python-app.yml)
# Overview

BostonHousingPricePrediction is a web app that hosted on Azure App Service to predict the housing price at Boston.

## Project Plan

* [A link to a Trello board for the project](https://trello.com/b/f0h9Nuuu/az2-build-ci-cd-pipeline-5-29)


* [A link to a spreadsheet that includes the original and final project plan](https://docs.google.com/spreadsheets/d/1dWaVzakvCpGNrWAXU-JxqgsjDw-sZNddCc69C8quTYc/edit#gid=596363533)

## Instructions

<TODO:  
* Architectural Diagram (Shows how key parts of the system work)>

![diagram](./pics/diagram.png)

* Project running on Azure App Service
![APP SERVICE](./pics/app_service.png)

* Project cloned into Azure Cloud Shell
![clone](./pics/cloneproject.png)

* Passing tests that are displayed after running the `make all` command from the `Makefile`
![all](./pics/make.png)

* Output of a test run
![test](./pics/passing_tests.png)

* Successful deploy of the project in Azure Pipelines.  [Note the official documentation should be referred to and double checked as you setup CI/CD](https://docs.microsoft.com/en-us/azure/devops/pipelines/ecosystems/python-webapp?view=azure-devops).
![deploy](./pics/successful_deployment.png)

* Running Azure App Service from Azure Pipelines automatic deployment

![azurepiplines](./pics/azpipeline-result.png)

* Successful prediction from deployed flask app in Azure Cloud Shell.  [Use this file as a template for the deployed prediction](https://github.com/udacity/nd082-Azure-Cloud-DevOps-Starter-Code/blob/master/C2-AgileDevelopmentwithAzure/project/starter_files/flask-sklearn/make_predict_azure_app.sh).
The output should look similar to this:

![prediction](./pics/successful_prediction.png)
* Output of streamed log files from deployed application
![logtail](./pics/log-tail.png)

* Locust: load test output
![locust](./pics/locust.png)
> 

## Enhancements


Plan : May add a friendly user interface to it.


## Demo 

https://youtu.be/57mUqMczNWY


