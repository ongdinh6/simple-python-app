# simple-python-app

A simple FastAPI application.

## Requirements

- Python 3.12+
- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)

## Installation

1. Clone this repository.
2. Install dependencies:

   ```sh
   pip install -r requirements.txt
   ```

## Running the Application
Start the server with:

```sh
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```
*Note: This makes the API accessible not just to localhost (127.0.0.1) but to any machine that can reach the VM.*


The API will be available at [http://127.0.0.1:8000](http://127.0.0.1:8000).

## API Endpoints

- **GET /greet?name=YourName**  
  Returns a greeting message.

- **GET /health**  
  Returns the health status of the application.

## Example

```sh
curl "http://127.0.0.1:8000/greet?name=Alice"
# Response: {"message":"Hello, Alice!"}
```

## Docker

You can also run this application using Docker.

### Build the Docker image

```sh
docker build -t simple-python-app .
```

### Run the Docker container locally

```sh
docker run -d -p 8000:8000 --name simple-python-app simple-python-app
```

The API will be available at [http://127.0.0.1:8000](http://127.0.0.1:8000).

## FastAPI Documentation

Once the server is running, FastAPI automatically generates interactive API documentation:

- **Swagger UI:**  
    [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

- **ReDoc:**  
    [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

These interfaces allow you to explore and test the API endpoints directly from your browser.

## Bonus: Setting Up Python on Windows with Ubuntu (WSL)

To use Ubuntu and Python 3 on Windows, follow these steps:

1. **Install Windows Subsystem for Linux (WSL) and Ubuntu:**

    Open PowerShell as Administrator and run:

    ```sh
    wsl --install
    ```

    This installs WSL and Ubuntu by default. Restart your computer if prompted.

2. **Set up Ubuntu and install Python 3:**

    Open Ubuntu from the Start menu, then run:

    ```sh
    sudo apt update
    sudo apt install python3 python3-pip
    ```

3. **Verify Python installation:**

    ```sh
    python3 --version
    pip3 --version
    ```

Now you can proceed with the installation steps above inside your Ubuntu terminal.