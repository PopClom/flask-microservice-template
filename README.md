# Flask Microservice Template with Layered Architecture

This project is a Flask microservice template that follows a layered architecture design pattern.
- It provides examples of the Controller, Service, Repository, and Client layers, along with a Model class. 
- The application is built using default Flask modules without any extensions. 
- All methods are defined using Python type hints for better readability and maintainability.
- Additionally, the project includes unit tests for each class to ensure proper functionality.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/popclom/flask-microservice-template.git
cd flask-microservice-template
```

2. Set up the virtual environment and install dependencies:

```bash
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

### Run the App

To start the Flask microservice, run the following command:

```bash
python run.py
```

The service will be accessible at `http://localhost:5000`.

### Run Unit Tests

To execute all unit tests for the application, use the following command:

```bash
python -m unittest discover -s tests
```

## Endpoints

### Get Users

Retrieve all users:

```bash
curl http://localhost:5000/users
```

### Get User by ID

Retrieve a specific user by ID (replace `<user_id>` with the actual ID):

```bash
curl http://localhost:5000/users/<user_id>
```

### Create User

Create a new user:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"name": "John Doe", "email": "john@example.com"}' http://localhost:5000/users
```

### Update User

Update an existing user by ID (replace `<user_id>` with the actual ID):

```bash
curl -X PUT -H "Content-Type: application/json" -d '{"name": "Updated Name", "email": "updated@example.com"}' http://localhost:5000/users/<user_id>
```

### Delete User

Delete a user by ID (replace `<user_id>` with the actual ID):

```bash
curl -X DELETE http://localhost:5000/users/<user_id>
```

## Contributing

Contributions are welcome! If you find any issues or want to add new features, please feel free to open a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
