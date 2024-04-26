# Python Project - Test Swagger Petstore API

- Petstore API is run locally using docker.
- A utility class is used to handle api calls.
- Fixtures are used to make the single initial api call for each test class

### Project Set Up in Docker:
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
pytest
```
Run all tests using marker - inventory
```
pytest -m inventory
```
Generate a report:
_View the report in the browser using the file path
C:\Users\theho\projects\APItestingProject\report.html_
```
pytest --html=report.html
```
