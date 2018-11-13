# Backend service

The service stores and supplies search engine for loads. 
It keeps business logic related to loadboards
Sends requests to Elasticsearch server to get store and get data. 
Written in Django.



## Codebase

The project folders description:

- deployment: this is where deployment related stuff is stored.
- loadboard: this is where the main code is stored
    - api: this is where all the API is stored
    - domain: this is where all domain business logic stored
    - contrib: this is where util functions/classes are stored
    - models: this is where framework models are stored
    - settings: well, settings
- tests: this is where the tests are stored.
- requirements: required packages list


## Getting Started

As it is a microservice.



## Tests

Pytest is used for writing and running the tests. 
As the project is running inside a docker container, tests should be run from the container:

```bash
docker-compose exec loadboard pytest
```
