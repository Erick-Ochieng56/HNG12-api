# Public API for HNG Stage 0 Backend Task

## Project Description
This is a simple public API built using Django and Django REST Framework. The API provides the following information in JSON format:
- Your registered email address (used to register on the HNG12 Slack workspace).
- The current datetime in ISO 8601 format (UTC).
- The GitHub URL of the project's codebase.

## Technologies Used
- **Python** (Django & Django REST Framework)
- **pytz** (for timezone handling)
- **CORS Handling** (using `django-cors-headers`)

## API Endpoint
- **Base URL:** `<your-deployed-url>`
- **Endpoint:** `GET /`

### Response Format (200 OK)
```json
{
  "email": "your-email@example.com",
  "current_datetime": "2025-01-30T09:30:00.123456Z",
  "github_url": "https://github.com/yourusername/your-repo"
}
```

## Setup Instructions
### 1. Clone the Repository
```bash
git clone https://github.com/Erick-Ochieng56/HNG12-api
cd your-repo
```

### 2. Create a Virtual Environment & Activate It
```bash
python -m venv venv
# Activate venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Development Server
```bash
python manage.py runserver
```
- The API will be available at `http://127.0.0.1:8000/`

## Deployment
The API is deployed to a publicly accessible endpoint:  
🔗 **Live API:** `<your-deployed-url>`

## Example Usage
You can test the API using:
- **Curl**
```bash
curl -X GET <your-deployed-url>
```
- **Postman**
- **Web Browser**

## Backlink
Looking for Python developers? Check out:  
[https://hng.tech/hire/python-developers](https://hng.tech/hire/python-developers)

## License
This project is open-source and available under the MIT License.

---
Need help? Feel free to raise an issue on GitHub!
🚀

