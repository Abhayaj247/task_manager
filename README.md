﻿# Task Management App

Setup and Deployment Guide

## Prerequisites
- Python 3.9+
- pip
- virtualenv (recommended)
- Google Cloud account for OAuth

## Project Setup

### 1. Clone the Repository
```bash
git clone https://github.com/Abhayaj247/task_manager.git
cd task_manager
```

### 2. Create and Activate Virtual Environment
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Create Environment Configuration

#### 3.1 Create .env File
Create a file named `.env` in the project root with the following structure:

```env
# Django Settings
DJANGO_SECRET_KEY=your_very_long_random_secret_key
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1

# Google OAuth Credentials
GOOGLE_CLIENT_ID=your_google_client_id
GOOGLE_CLIENT_SECRET=your_google_client_secret

# Email Settings (Optional)
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_email_app_password
EMAIL_USE_TLS=True
```

#### 3.2 Generate a Secret Key
```bash
python -c "import secrets; print(secrets.token_urlsafe(50))"
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Git Configuration for Sensitive Information

#### 5.1 Create .gitignore
Create or update `.gitignore` in the project root:

```gitignore
# Python
__pycache__/
*.py[cod]
*$py.class
*.so

# Virtual Environment
venv/
env/
.env/
.venv/

# Django
*.log
local_settings.py
db.sqlite3
db.sqlite3-journal

# Sensitive Files
.env
*.env
!.env.example

# IDE and Editor Files
.vscode/
.idea/
*.swp
*.swo
*~

# OS Generated Files
.DS_Store
Thumbs.db
```

#### 5.2 Create .env.example
Create a template `.env.example` with dummy/placeholder values:

```env
# Django Settings
DJANGO_SECRET_KEY=change_this_to_your_secret_key
DJANGO_DEBUG=False
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1

# Google OAuth Credentials
GOOGLE_CLIENT_ID=your_google_client_id
GOOGLE_CLIENT_SECRET=your_google_client_secret

# Email Settings
EMAIL_HOST=smtp.example.com
EMAIL_PORT=587
EMAIL_HOST_USER=example@gmail.com
EMAIL_HOST_PASSWORD=your_email_app_password
EMAIL_USE_TLS=True
```

### 6. Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Create Superuser
```bash
python manage.py createsuperuser
```

### 8. Set Up Google OAuth

1. Go to Google Cloud Console (https://console.cloud.google.com/)
2. Create a new project
3. Navigate to "Credentials"
4. Click "Create Credentials" > "OAuth client ID"
5. Select "Web application"
6. Add authorized JavaScript origins and redirect URIs:
   - http://localhost:8000
   - http://localhost:8000/accounts/google/login/callback/

### 9. Configure Django Admin for Site and Social App

1. Run the server: `python manage.py runserver`
2. Go to admin panel (http://localhost:8000/admin/)
3. Add a Site:
   - Domain name: localhost:8000
   - Display name: Local Development
4. Add a Social Application:
   - Provider: Google
   - Name: Google OAuth
   - Client ID: [from Google Cloud Console]
   - Secret Key: [from Google Cloud Console]
   - Chosen sites: Select your local site

### 10. Running the Application
```bash
python manage.py runserver
```

## Deployment Considerations

### Production Checklist
1. Set `DEBUG=False` in production
2. Use a production-grade database (PostgreSQL recommended)
3. Use environment-specific settings
4. Set strong, unique `SECRET_KEY`
5. Configure proper logging
6. Use HTTPS
7. Set up proper email backend

### Recommended Production Dependencies
```bash
pip install gunicorn psycopg2-binary dj-database-url
```

## Troubleshooting

### Common Issues
- Verify all dependencies are installed
- Check environment variables
- Ensure correct Python and Django versions
- Verify Google OAuth configuration

### Logging
- Check Django debug logs
- Use `python manage.py check --deploy` for deployment checks

## Security Best Practices
- Regularly update dependencies
- Rotate secret keys
- Use strong, unique passwords
- Enable two-factor authentication
- Limit admin access

## Contributing
1. Fork the repository
2. Create a feature branch
3. Commit changes
4. Push to the branch
5. Create a Pull Request

## License
[Specify your project license]
```
