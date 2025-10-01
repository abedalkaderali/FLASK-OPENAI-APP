# Flask OpenAI Application

This project is a Flask-based web application that integrates with OpenAI's API for chat completions and image generation. It is containerized using Docker and includes unit tests for all API endpoints.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
- [Testing](#testing)
- [Postman Collection](#postman-collection)
- [Swagger Documentation](#swagger-documentation)

## Prerequisites
- Python 3.7 or higher
- Docker
- OpenAI API Key (request from ITXI)

## Installation
1. Clone the repository:
   ```
   git clone <repository-url>
   cd flask-openai-app
   ```

2. Install the required Python packages:
   ```
   pip install -r requirements.txt
   ```

## Running the Application
To build and run the Docker container, use the following commands:

1. Build the Docker image:
   ```
   docker build -t flask-openai-app .
   ```

2. Run the Docker container:
   ```
   docker run -p 5000:5000 -e OPENAI_API_KEY=<your_openai_api_key> flask-openai-app
   ```

The application will be accessible at `http://localhost:5000`.

## API Endpoints

### GET /
Returns a simple "Hello, World!" message.

**Request:**
```
GET / HTTP/1.1
x-api-key: <your_api_key>
```

**Response:**
```json
{
  "response": "Hello, World!"
}
```

### POST /chat
Accepts a user message and returns a response from OpenAI's chat completion API.

**Request:**
```
POST /chat HTTP/1.1
x-api-key: <your_api_key>
Content-Type: application/json

{
  "content": "what is the capital of Lebanon"
}
```

**Response:**
```json
{
  "response": "what is the capital of Lebanon",
  "version": "0.1.0"
}
```

### POST /generateImage
Accepts a user message and returns an image or base64 JSON response based on the response-type header.

**Request:**
```
POST /generateImage HTTP/1.1
x-api-key: <your_api_key>
response-type: base64
Content-Type: application/json

{
  "content": "A red elephant"
}
```

**Response (base64):**
```json
{
  "base64": "4AAQSkZJRgABAQAAAQABAAD/2wCEAAUFBQoHC...",
  "version": "0.1.0"
}
```

**Response (image):**
```
Image file: image-20240816-123214.png
```

## Testing
Unit tests are provided for all API endpoints. To run the tests, use:
```
pytest tests/
```

## Postman Collection
A Postman collection is included in the `postman_collection.json` file for easy testing of the API endpoints.

## Swagger Documentation
Swagger documentation is available in the `src/swagger/swagger.yaml` file, detailing the request and response formats for each endpoint.