# Monaco Racing 2018 Report

This README provides an overview of the Monaco Racing 2018 Report application and its key components.

## Tools Used

- **Flask REST API:**

- **SQLite3:** 

- **PyPI:** 

- **Flasgger (Swagger):**

- **functools:**

- **Peewee:**

- **Pytest/Unittest:**

## API Endpoints

Monaco Racing 2018 Report exposes the following API endpoints:

- **Top Racing Results (Asc Order):**
  - Endpoint: `http://127.0.0.1:5000/api/v1/report/`
  - Description: This API endpoint provides the top racing results in ascending order.

- **Driver Information:**
  - Endpoint: `http://127.0.0.1:5000/api/v1/drivers/`
  - Description: This API endpoint offers information about the drivers participating in the Monaco Racing 2018.

- **Personal Driver Information (by Driver ID):**
  - Endpoint: `http://127.0.0.1:5000/api/v1/drivers/{driver_id}`
  - Description: Use this API to retrieve personal information about a specific driver by providing their unique driver ID.

## Swagger Documentation

To explore and interact with the API endpoints, you can use the Swagger documentation:

- **Swagger Documentation:** `http://127.0.0.1:5000/apidocs/`

## Supported Formats

Monaco Racing 2018 Report supports the following response formats:

- **JSON:** Response data can be retrieved in JSON format.
- **XML:** Response data can be retrieved in XML format.

You can specify the desired format using request headers or parameters as documented in the Swagger API.

## Monaco Logic Package

The Monaco Logic package provides several essential functionalities for working with the application's data. You can install it using the following command:

```shell
pip install -i https://test.pypi.org/simple/ monaco-logic
```
OR
```shell
https://test.pypi.org/project/monaco-logic/
```

### Key Functions in Monaco Logic Package (Created by Me)

- **`get_data_start`:** Converts data to a tuple format like `[{key: value}]`.

- **`get_sort_start`:** Sorts the data efficiently.

- **`racers_start_sorted`:** A global variable used for specific purposes.

- **`build_report`:** Builds the top racing report.

### Testing

We use Pytest to test the functionality and format of the API. 
Additionally, Unittest is employed to test the data models defined in `models.py`.

