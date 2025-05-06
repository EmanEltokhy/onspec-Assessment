# OnSpec API

A Django REST API for managing candidate information. It allows users to create or update candidate information.

## Features

- Create or update candidate information
- Repository pattern for database abstraction
- Service layer for business logic
- Comprehensive unit tests
- Clean, modular architecture

## Installation

## Setup

1. Clone the repository
2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Run migrations:
   ```
   python manage.py migrate
   ```
5. Start the development server:
   ```
   python manage.py runserver
   ```

## API Endpoints

### Candidates

- `POST /api/candidates/` - Create or update a candidate

## Running Tests

```
python manage.py test
```

## Project Structure

```
onspec_api/
├── candidates/                   # Candidate management app
│   ├── migrations/               # Database migrations
│   ├── admin.py                  # Django admin configuration
│   ├── apps.py                   # App configuration
│   ├── models.py                 # Data models
│   ├── repository.py             # Data access layer
│   ├── serializers.py            # API serializers
│   ├── services.py               # Business logic
│   ├── tests.py                  # Unit tests
│   ├── urls.py                   # URL routing
│   └── views.py                  # API views
├── onspec_api/                   # Project configuration
│   ├── asgi.py                   # ASGI configuration
│   ├── settings.py               # Django settings
│   ├── urls.py                   # Project URL routing
│   └── wsgi.py                   # WSGI configuration
├── manage.py                     # Django management script
└── README.md                     # Project documentation
```

## Assumptions

- Email is the unique identifier for candidates
- First name, last name, and email are required fields
- Other fields are optional

## Time Spent

- Planning and setup: 30 minutes
- Core implementation: 2 hours
- Testing: 30 minutes
- Documentation: 30 minutes
- Total: 3 hours 30 minutes

## Future Improvements

- Implement authentication (JWT or Session-based)
- Implement filtering and searching capabilities
- Implement functionality to fetch all candidates or a specific candidate by ID
- Add caching for frequently accessed candidates
- Enhance error handling and validation
- Implement rate limiting
- Add monitoring and logging