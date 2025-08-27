# CloudFit API Documentation

## Overview
CloudFit is a real-time fitness activity monitoring application that provides a REST API for tracking fitness activities. This API is built using Flask and serves as the backend for the CloudFit platform.

## Setup Instructions

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Installation
1. Clone the repository:
   ```
   git clone https://github.com/yourusername/cloudfit-devops.git
   cd cloudfit-devops/api
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running the Application
To run the Flask application, execute the following command:
```
python src/app.py
```
The application will start on `http://localhost:5000`.

## API Endpoints

### GET /status
- **Description**: Returns the status of the API.
- **Response**:
  ```json
  {
    "status": "ok"
  }
  ```

## Testing
To run tests, ensure you have a testing framework set up (e.g., pytest) and execute:
```
pytest
```

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.