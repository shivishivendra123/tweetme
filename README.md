# TweetMe

**TweetMe** is a Django-based web application that allows users to create and share blog posts with images. The application leverages Django's built-in authentication system for secure user registration and login, with OTP-based signup to ensure user security. The application is built with a simple and intuitive UI using Bootstrap, and utilizes SQLite as the database with Django ORM for data management.

## Features

- **User Authentication:** 
  - Users can sign up using OTP-based verification, ensuring secure registration.
  - Django's authentication system handles user login and logout.

- **Blog Posting:**
  - Users can write and publish blog posts.
  - Each blog post can include text and image uploads.

- **Responsive UI:**
  - Built with **Bootstrap** for a modern, responsive design.
  
- **Database Management:**
  - Uses **SQLite** for database management, with Django ORM for easy querying and interaction.

## Tech Stack

- **Backend:** Django (Python)
- **Database:** SQLite
- **Frontend:** HTML, CSS, Bootstrap
- **Authentication:** Django Authentication, OTP-based signup
- **ORM:** Django ORM for database interaction

## Installation

### Prerequisites

Ensure you have the following installed:
- Python 3.x
- pip (Python package manager)
- SQLite (comes pre-installed with Python)

### Clone the Repository

```bash
git clone https://github.com/shivishivendra123/tweetme.git
cd tweetme

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver

```

Usage

Sign Up / Login: Users can sign up using OTP or log in with their credentials.

Post Blogs: After logging in, users can write, edit, and publish their blogs.

Upload Images: Users can upload images along with their posts to enhance content.

Contributing
Fork the repository.
Create your feature branch (git checkout -b feature/YourFeature).
Commit your changes (git commit -am 'Add new feature').
Push to the branch (git push origin feature/YourFeature).
Open a pull request.
