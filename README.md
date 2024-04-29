# Python Project - Test Swagger Petstore API

- Petstore API is run locally using docker.
- A utility class is used to handle api calls.
- Fixtures are used to make the single initial api call for each test class
- The file structure in the tests folder is based on the pathways used in the api; _store_, _pet_ and _user_
- The tests in the _store_ pathway, replicate a java structure where models are used (similar to POJO's) to process the retrieved json data
- The tests in the _pet_ pathway have a more pythonic structure, directly accessing the json data

Clone repo and install dependencies
```
pip install -r requirements.txt
```

### Use Docker to run API:
Download Docker

Pull *swaggerapi/petstore3:unstable* Image:
```
docker pull swaggerapi/petstore3:unstable
```
Run the Docker container:
```
docker run --name petrehomingservice -d -p 8080:8080 swaggerapi/petstore3:unstable
```
Verify Installation:
Open a web browser and navigate to http://localhost:8080/ to access the Swagger Petstore running locally on your machine.

### Run tests using Pytest
Run all tests
```
python -m pytest
```
Run all tests using marker - inventory
```
python -m pytest -m inventory
```
Generate a report:
_View the report in the browser using the file path
C:\Users\theho\projects\APItestingProject\report.html_
```
python -m pytest --html=report.html
```
