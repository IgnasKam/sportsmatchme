# SportsMatchMe


### Project Overview: 
SportsMatchMe is a Django-based web application designed for organizing and participating in sports events. Users can host events, join games, and manage their participation in various sports activities. The platform supports features like user registration and authentication, event creation and management, and court rentals.

### Main Features
• User registration and login.<br>
• Event creation and listing.<br>
• Court management for hosting events.<br>
• Profile management for users.<br>

## Getting Started
### Prerequisites
• Python 3.8 or higher.<br>
• Django 4.2.7.<br>
• PostgreSQL (or other database systems like SQLite for development).

### Installation
1. Clone the Repository<br>
git clone https://github.com/your-username/sportsmatchme.git<br>
</code></pre>cd sportsmatchme</code></pre>

2. Set Up a Virtual Environment (Optional but Recommended)<br>
</code></pre>python -m venv venv
venv\Scripts\activate</code></pre>

3. Install Dependencies<br>
</code></pre> pip install -r requirements.txt
</code></pre>

4. Configure Database<br>
Update settings.py with your database connection details:

<pre><code>DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',  <!-- Or 'django.db.backends.sqlite3', etc. -->
        'NAME': 'your-database-name',
        'USER': 'your-database-user',
        'PASSWORD': 'your-database-password',
        'HOST': 'your-database-host',
        'PORT': 'your-database-port',  <!-- Default is 5432 for PostgreSQL -->
    }
}
</code></pre>

5. Run Migrations
<pre><code>python manage.py makemigrations<br>
python manage.py migrate </code></pre>

6. Start the Development Server
</code></pre>python manage.py runserver
<br>
Navigate to http://127.0.0.1:8000/ in your browser to view the application.<br>

## Usage
After starting the server, you can:<br>
• Register as a new user.<br>
• Create and manage sports events.<br>
• View and join events created by other users.<br>
• Manage personal profiles.<br>


## Contributing
Contributions to the SportsMatchMe project are welcome. Please follow the standard fork and pull request workflow.
