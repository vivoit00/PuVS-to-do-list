# Todo Application Setup Guide

## Overview

Application with a Thymeleaf Frontend, Django Backend and PostgreSQL Database




## Steps to Run

1. Clone the repository:

    ```sh
    git clone https://github.com/vivoit00/PuVS-to-do-list 
    
    cd PuVS-to-do-list/sample/otel-in-action
    ```

2. Build and run the containers:

    ```sh
    docker-compose up --build
    ```

3. Access the services:
    - Django Backend: `http://localhost:8080`
    - Thymeleaf Frontend: `http://localhost:8090`

## Endpoints


### Get All Todos

- **URL:** `/todos/`
- **Method:** GET
- **Response:** List of todo items in plain text

### Add a Todo

- **URL:** `/todos/{toDo}`
- **Method:** POST
- **Path Parameter:**
  - `toDo`: The name of the todo item to be added
- **Response:** The added todo item in plain text

### Delete a Todo

- **URL:** `/todos/{toDo}`
- **Method:** DELETE
- **Path Parameter:**
  - `toDo`: The name of the todo item to be deleted
- **Response:** 204 No Content if successful

### Example Usage

#### Get all Todos
```sh
curl http://localhost:8080/todos/
```

#### Add a Todo
```sh
curl -X POST http://localhost:8080/todos/NewItem
```
## Configuration
The `docker-compose.yaml` file contains all the needed configurations for frontend, backend <br> 
and database

