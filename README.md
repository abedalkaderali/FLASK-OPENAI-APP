# Flask OpenAI Application

This project is a Flask-based web application that integrates with OpenAI's API for chat completions and image generation. It is containerized using Docker and includes unit tests for all API endpoints.

# Running the Application
To run the application, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/abedalkader/flask-openai-app.git
   ```
2. Navigate to the project directory:
   ```bash
   cd flask-openai-app
   ```
3. create .env file and add your API_KEY AND X_API_KEY
   ```bash
   touch .env
   ```
4. Build the Docker image:
   ```bash
   docker compose up --build



## Postman Collection
A Postman collection is included in the `postman_collection.json` file for easy testing of the API endpoints.

## Swagger Documentation
Swagger documentation is available in the `src/swagger/swagger.yaml` file, detailing the request and response formats for each endpoint.
