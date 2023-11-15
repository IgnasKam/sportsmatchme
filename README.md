# SportsMatchMe


### Project Overview: 
SportsMatchMe is a Django-based web application designed for organizing and participating in sports events. Users can host events, join games, and manage their participation in various sports activities. The platform supports features like user registration and authentication, event creation and management, and court rentals.

### Main Features
• User registration and login.
• Event creation and listing.
• Court management for hosting events.
• Profile management for users.

## Getting Started
### Prerequisites
• Python 3.8 or higher.
• Django 4.2.7.
• PostgreSQL (or other database systems like SQLite for development).

### Installation
1. Clone the Repository
git clone https://github.com/your-username/sportsmatchme.git
cd sportsmatchme

2. Set Up a Virtual Environment (Optional but Recommended)
python -m venv venv
venv\Scripts\activate

3. Install Dependencies
pip install -r requirements.txt

4. Configure Database
Update settings.py with your database connection details:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',  # Or 'django.db.backends.sqlite3', etc.
        'NAME': 'your-database-name',
        'USER': 'your-database-user',
        'PASSWORD': 'your-database-password',
        'HOST': 'your-database-host',
        'PORT': 'your-database-port',  # Default is 5432 for PostgreSQL
    }
}

5. Run Migrations
python manage.py makemigrations
python manage.py migrate

6. Start the Development Server
python manage.py runserver
Navigate to http://127.0.0.1:8000/ in your browser to view the application.

## Usage
After starting the server, you can:
• Register as a new user.
• Create and manage sports events.
• View and join events created by other users.
• Manage personal profiles.


## Contributing
Contributions to the SportsMatchMe project are welcome. Please follow the standard fork and pull request workflow.
