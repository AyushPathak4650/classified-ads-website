# Classified Ads Website

A secure and interactive classified ads platform built with Django, inspired by real-world online marketplaces. This project was built as part of the Django for Everybody (DJ4E) course.

## Features

- **User Authentication** - Registration, login, and logout
- **Ad Management** - Create, edit, delete, and browse ads
- **Image Uploads** - Safe image handling for ad photos
- **Commenting System** - Discussion on ads
- **Favorites** - Save interesting ads for later
- **Search with Tags** - Quick discovery of ads
- **Ownership Rules** - Users can only manage their own content
- **REST API Support** - Built with Django REST Framework
- **Tagging System** - Organize ads with tags

## Requirements

- Python 3.10+
- Django 4.2+

## Installation

```bash
pip install -r requirements.txt
```

## Setup

1. Run migrations:
   ```bash
   python manage.py migrate
   ```

2. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

3. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Tech Stack

- **Backend**: Django, Python
- **Frontend**: HTML, CSS
- **Database**: SQLite (default)
- **APIs**: Django REST Framework
- **Authentication**: Built-in Django auth

## Acknowledgments

Built as part of the [Django for Everybody](https://www.dj4e.com/) course by Dr. Charles Severance.

## License

MIT License - see LICENSE file for details.
