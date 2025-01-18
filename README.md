# Gas Utility Services

## Overview
Gas Utility Services is a Django-based web application designed to streamline customer service operations for gas utility companies. The application allows customers to:

- Submit service requests online.
- Track the status of their service requests.
- View their account information.

It also provides customer support representatives with tools to manage requests and offer support efficiently.

## Features
### Customer-Facing Features
- **Service Request Submission:**
  - Customers can select the type of service request.
  - Provide details about their request.
  - Attach relevant files.

- **Request Tracking:**
  - Customers can view the status of their requests.
  - See submission and resolution dates.

- **Account Management:**
  - Secure login and signup functionalities.
  - Access to personal account details.

### Admin/Support Features
- **Support Dashboard:**
  - View and manage all service requests.
  - Update request statuses.
  - Automatically record resolution timestamps.

- **User Management:**
  - Admins can manage user accounts via the Django admin interface.

## Installation
### Prerequisites
- Python 3.8+
- PostgreSQL
- pip
- Virtual Environment (optional but recommended)

### Steps
1. Clone the repository:
   ```bash
   git clone <repository_url>
   
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the database:
   - Update `DATABASES` in `consumer_services/settings.py` with your PostgreSQL configuration.
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': '<database_name>',
           'USER': '<username>',
           'PASSWORD': '<password>',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
   ```

5. Run migrations:
   ```bash
   python manage.py migrate
   ```

6. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

7. Start the development server:
   ```bash
   python manage.py runserver
   ```

8. Access the application:
   - Customer portal: `http://127.0.0.1:8000`
   - Admin dashboard: `http://127.0.0.1:8000/admin`

## Usage
### For Customers
1. Register an account or log in.
2. Submit a service request via the "Submit Request" page.
3. Track your requests in the "Track Requests" section.

### For Support/Admin Users
1. Log in using superuser credentials.
2. Navigate to the "Support" section to view and manage all customer requests.
3. Update request statuses as needed.

## Project Structure
```project_root/
│
├── consumer_services/
│   ├── settings.py        # Project settings
│   ├── urls.py            # Root URL configurations
│   ├── wsgi.py            # WSGI entry point
│   ├── asgi.py            # ASGI entry point
│   └── __init__.py
│
├── accounts/              # User authentication and profile management
│   ├── models.py
│   ├── views.py   
│   ├── urls.py
│   ├── templates/         # User-related templates
│   └── forms.py
│
├── service_requests/      # Feature for handling service requests
│   ├── models.py          # Request-related database models
│   ├── views.py           # Handles customer-facing views
│   ├── urls.py            # App-specific URLs
│   ├── templates/         # Service request-related templates
│   └── forms.py           # Django forms for requests
│
├── support/               # Admin/customer support module
│   ├── models.py          # Support-specific data, if any
│   ├── views.py           # Handles support-facing views
│   ├── urls.py            # URLs for the support module
│   └── templates/         # Templates for support functionality
│
│
├── manage.py              # Django management script
│
└── requirements.txt       # Project dependencies

```

## Dependencies
Key dependencies for this project include:
- Django
- djangorestframework
- psycopg2
- Bootstrap (for frontend styling)

## Contribution
Contributions are welcome! Follow these steps:
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature/your-feature-name
   ```
5. Create a pull request.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact
For queries or support, reach out to the project maintainer at ayush.michael03@gmail.com.

