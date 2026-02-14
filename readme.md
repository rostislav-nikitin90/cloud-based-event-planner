# Overview

This Event Planner project is a backend‑only Django application integrated with **Firebase Authentication** and **Cloud Firestore**. It demonstrates secure **CRUD operations** (Create, Read, Update, Delete) for events, guests, and RSVPs. The program is designed to be used entirely from the command line with **curl commands**. Each curl request interacts with Django API endpoints, and the results can be observed directly in the Firestore console. For convenience, I have included a **`rundemo.txt`** file in the project folder. This file contains step‑by‑step instructions to run this program and all the curl commands needed to reproduce the CRUD demonstration. To set up the environment, a **`requirements.txt`** file is also included. This file lists all the Python dependencies required to run the project.  

The purpose of writing this software was to strengthen my skills as a software engineer by:  
- Learning how to connect Django to a cloud database.  
- Implementing middleware for authentication.  
- Practicing API design and CRUD workflows without relying on a frontend.  
- Demonstrating reproducible backend operations in a clear, beginner‑friendly way. 

# Quick Start

Follow these steps to run the project locally:

1. **Clone the repository from GitHub**  
   ```bash
   git clone https://github.com/rostislav-nikitin90/cloud-based-event-planner.git
   cd cloud-based-event-planner
   ```
2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate   # On Windows
   source venv/bin/activate   # On macOS/Linux
   ```
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the Django development server**
   ```bash
   python manage.py runserver
   ```
5. Open **`rundemo.txt`**
Follow the instructions inside **`rundemo.txt`** to run curl commands that demonstrate CRUD operations (unauthorized request, login, add/update/retrieve/delete event).

# Cloud Database

This project uses **Google Cloud Firestore** as its database. Firestore is a NoSQL document database that stores data in collections and documents.  

## Database Structure
- **events** collection  
  - Each document represents an event with fields: `event_id`, `name`, `date`, `location`.  
- **guests** collection  
  - Each document represents a guest with fields: `guest_id`, `name`, `email`.  
- **rsvps** collection  
  - Each document represents a guest’s RSVP with fields: `event_id`, `guest_id`, `status`.  

This structure allows events to be created, guests to be added, and RSVPs to be tracked in a flexible, scalable way.

# Development Environment

**Tools used:**  
- Django (Python web framework) for API endpoints.  
- Django REST Framework (DRF) for serializers and response handling.  
- Firebase Admin SDK for verifying ID tokens and enforcing authentication.  
- Cloud Firestore for storing event, guest, and RSVP data.  

**Programming language:**  
- Python 3.x  

**Libraries:**  
- `django`  
- `djangorestframework`  
- `firebase-admin`  
- `requests` 

# Useful Websites

- [Django REST Framework Documentation](https://www.django-rest-framework.org/)  
- [Firebase Admin SDK Setup](https://firebase.google.com/docs/admin/setup)  
- [Firestore Data Model Guide](https://firebase.google.com/docs/firestore/data-model)  
- [Django Middleware Documentation](https://docs.djangoproject.com/en/stable/topics/http/middleware/)  
- [Curl Command Manual](https://curl.se/docs/manual.html) 

# Future Work

- Expand database structure to include event details like description, organizer, and capacity.
- Implement refresh token handling for longer authentication sessions. 
- Build a simple frontend dashboard to visualize events and RSVPs.