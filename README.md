                                                      WORKFLOWS PROJECT DESCRIPTION 

Project overview: 

This is a simple Django project which is hosted on GitHub. In this project we create a simple User Registration forms method in Django. 

User is registered using template Register.html. After registered successfully it will redirect to thanks. Html 
They were located in workflows/setupworkflow/templates directory. 
In this project we are using Django, Git, GitHub, Python. 

Activating Virtual environment:

  run on terminal:
    venv/scripts/activate

Steps to Run Project: 

  Install all Dependencies mentioned in the requirements.txt 

  Configure Database in settings.py

  Make migrations as follows:
    py manage.py makemigrations                # for creating all required tables for the models in the database	
    py manage.py migrate	                     # for creating neccessary tables inthe database
    py manage.py sqlmigrate app1 0001          # for saving models in the database

  Create super user:
    py manage.py create superuser 
  
  Run server:
    py manage.py runserver

Testing The project:

  in this project we are using Unit Test framework for testing our project. We are using coverage to get the test report for our project.
  
  Steps to Testing our project:
  
    For Testing:
      py manage.py test
  
    Test by using coverage:
      coverage run manage.py test
      
    Getting coverage report in the folder:
      coverage html     # this will create htmlcov directory in workflows/htmlcov/ directory and get coverage reports in html format
      
 Testing Code Quality:
  For testing our code quality we are using flake8.
  
  Steps:
    run on terminal:
      flake8
        # this will test our code quality
    if we want to exclude any code such as venv, migrations we create a setup.cfg file inside we mention what we want to exclude
  
 Work flows:
    For this project we are using GitHub Actions forl Continuous Integration
    GitHub provide different kind of workflows for Deveopers to Deploy and run their projects. In this project we are usimg two workflows
    they are,
        1.Django workflow
        2.Deploy to IBM Cloud Kubernetes Service
      
     Steps to workflows in GitHub Actions:
     
      Steps for Django workflow:
      
        1.go to GitHub and then go to Actions and choose Django workflow
          # This will create a folder .github inside this a sub folder named workflows. inside workflows directiory 
          they autometically generate a file djangotesting.yml. they located in workflows/.github/workflows/
        2. This will helps to run our server on linux environment Ubuntu
        3. If we want to modify we can modify based on our requirements
        4. Click on this file and run. It will run our application on ubuntu and test it if anything is not working or something done wrong
         it will fail otherwise it will become success
         
     Steps to Deploy to IBM Cloud Kubernetes Service:
     
        1.go to GitHub and then go to Actions and choose IBM Cloud Kubernetes Service
        2. this will create a file ibm.yml inside .github/workflows
        3. Click on run it will deploy our project Build a docker container, publish it to IBM Cloud Container Registry, and deploy to IBM Cloud Kubernetes Service.
