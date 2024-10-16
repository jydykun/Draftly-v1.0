# Draftly
A minimal blog engine built with Flask, styled with Tailwind CSS, and powered by TinyMCE. Work in progress...

## Overview
Draftly is a beginner-friendly blog engine designed for simplicity. It allows users to create and manage posts with categories (no tags) through a dashboard. The project uses Flask on the backend, with a focus on delivering clean designs using Tailwind CSS and dynamic post editing with TinyMCE.

## Features
- Post Management: Create, update, and delete posts with category support.
- Dashboard Interface: Manage your content easily from an admin dashboard.
- TinyMCE Editor: Rich text editor for creating engaging blog posts.
- Tailwind CSS Styling: Responsive design with minimal custom CSS.
- Blueprints in Flask: Clean structure with modular routes and views.
- SQLite Database: Simple, lightweight database for managing content.
- Still Under Construction: Some features are being finalized!

## Project Structure
```bash
    /Draftly
    │
    ├── /app              # Contains the core Flask app (blueprints, models, routes)
    │   ├── __init__.py   # App factory function (create_app)
    │   ├── models.py     # Database models
    │   ├── routes.py     # Application routes (post & dashboard logic)
    │
    ├── /instance         # Configuration files (e.g., SQLite database)
    │   └── draftly.db    # SQLite database (auto-generated after migration)
    │
    ├── /venv             # Virtual environment (not tracked by Git)
    ├── .gitignore        # Files and folders to ignore in Git
    ├── cli.py            # Custom CLI commands for managing the app
    ├── config.py         # App configuration (environment variables loaded here)
    ├── tailwind.config.js # Tailwind CSS configuration
    ├── wsgi.py           # WSGI entry point for deployment
    └── requirements.txt  # Python dependencies


## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)
- [Acknowledgments](#acknowledgments)

## Installation
To install this project, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/username/my-awesome-project.git
sfdfsd