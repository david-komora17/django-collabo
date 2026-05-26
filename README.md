# Local Event & Ticket Booking System 

A robust, backend-heavy Django web application designed for communities, schools, or local neighborhoods to host events, manage registrations, and track ticket bookings seamlessly. 

---

##  Project Overview

This system allows regular users to browse local happenings, register accounts, and instantly book tickets to their favorite events. Simultaneously, it empowers event organizers and administrators with an intuitive dashboard to manage event listings and track attendance analytics without drowning in spreadsheets.

### Key Highlights
*  **Secure Workflows:** Robust user registration, authentication, and session handling.
*  **Relational Architecture:** Strongly mapped database relationships using Django ORM.
*  **Organizer Analytics:** Custom dashboards to monitor attendee lists and revenue.
*  **Media Handling:** Structured pipeline for dynamic event poster uploads.

---

##  Tech Stack

* **Backend Framework:** Django 5.x (Python 3.11+)
* **Database:** SQLite (Development) / PostgreSQL (Production ready)
* **Frontend:** HTML5, CSS3, Bootstrap 5
* **Image Processing:** Pillow

---

##  Project Architecture & Apps Structure

The project emphasizes a strict **separation of concerns** by dividing features into dedicated, modular Django applications:

```text
local_events_project/
│
├── core/                  # Project configuration & global settings
│
├── authentication/        # User registration, login, logout, and profiles
│   ├── models.py          # UserProfile model extensions
│   └── views.py           # Authentication and profile rendering logic
│
├── events/                # Event creation and discovery
│   ├── models.py          # Event details schema (Venue, Price, Images)
│   └── views.py           # Event feed and full CRUD operations
│
├── bookings/              # Ticket transaction and management engine
│   ├── models.py          # Booking relational schema (User <-> Event)
│   └── views.py           # Ticket purchase processing and history
│
├── static/                # Global assets (Compiled Bootstrap, custom CSS)
└── templates/             # Global base templates and shared layouts
```

---

##  Team & Responsibilities Split

To prevent the classic "one person carries the team" group dynamic, responsibilities are cleanly divided into isolated deliverables:

* **Person 1 (Authentication Specialist):** Handles registration, login modules, security restrictions, and profile management.
* **Person 2 (Frontend & UI Engineer):** Standardizes templates, configures Bootstrap, and ensures look-and-feel consistency.
* **Person 3 (Data Architect):** Owns the `Event` model, database constraints, dynamic media uploads, and Event CRUD.
* **Person 4 (Logic & Transaction Engineer):** Implements `Booking` relationships, reservation views, and "My Tickets" filtering.
* **Person 5 (Dashboard & QA Panelist):** Designs the metrics dashboard, configures Django Admin overrides, and conducts system integration tests.

---

##  Getting Started & Installation

Follow these steps to set up the project locally on your machine:

### 1. Clone the Repository
```bash
git clone https://github.com
cd local-events-system
```

### 2. Set Up a Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
*(Ensure `Django` and `Pillow` are present in your requirements file).*

### 4. Run Migrations & Initialize Database
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create an Admin Account (Organizer Account)
```bash
python manage.py createsuperuser
```

### 6. Launch the Local Development Server
```bash
python manage.py runserver
```
Navigate to `http://127.0.0` in your browser to view the system!

---

##  System Map & URL Routes


| Page Endpoint | Accessible By | Purpose |
| :--- | :--- | :--- |
| `/` | Anyone | Home Page: Feed of upcoming events |
| `/auth/register/` | Anonymous | Account creation form |
| `/auth/login/` | Anonymous | User authentication portal |
| `/events/all/` | Anyone | Directory of all available events |
| `/events/<int:id>/` | Anyone | Detailed view with description and pricing |
| `/bookings/book/<int:id>/` | Logged-in Users | Backend routing to process a ticket reservation |
| `/auth/profile/` | Logged-in Users | Dashboard displaying user's active tickets |
| `/dashboard/organizer/` | Admins/Organizers | Analytics page featuring attendee lists and totals |

---

##  Git Workflow Rules

To keep our repository organized and clean, all members must adhere to this workflow:
1. **Never commit directly to `main`.**
2. Branch out from `main` using your feature name: `git checkout -b feature/your-feature-name`.
3. Push your branch to GitHub and open a **Pull Request (PR)**.
4. Request a review from at least one teammate. Once approved, merge it into `main`.
