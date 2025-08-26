# 🌍 TravelEase – Online Travel Booking System ✈️🚆🚌

Live Demo 👉 [https://travelease-p0ov.onrender.com](https://travelease-p0ov.onrender.com)

**TravelEase** is a full-stack **Django-based travel booking application** built with **PostgreSQL** and styled with **Bootstrap**.  
It allows users to browse travel options (Flights, Trains, Buses), make bookings, manage their profile, and view/cancel their tickets.

---

## ✨ Features

✅ User Registration, Login & Profile Management  
✅ Browse Travel Options (Flight / Train / Bus)  
✅ Book Tickets & Manage Bookings  
✅ Cancel Bookings Anytime  
✅ Responsive UI with **Bootstrap**  
✅ Configurable via `.env` file  
✅ PostgreSQL Database Integration  
✅ Deployed on **Render**

---

## 🛠️ Tech Stack

- **Backend:** Django (Python)
- **Frontend:** Django Templates + Bootstrap
- **Database:** PostgreSQL
- **Deployment:** Render
- **Config:** `.env` file for secure credentials

---

## 📂 Project Structure

travelease/
├── TravelEase/ # Core project
│ ├── init.py
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
├── bookings/ # Bookings app
│ ├── migrations/
│ ├── init.py
│ ├── admin.py
│ ├── apps.py
│ ├── forms.py
│ ├── models.py
│ ├── tests.py
│ ├── urls.py
│ └── views.py
├── users/ # Users app
│ ├── migrations/
│ ├── init.py
│ ├── admin.py
│ ├── apps.py
│ ├── forms.py
│ ├── models.py
│ ├── tests.py
│ ├── urls.py
│ └── views.py
├── templates/ # HTML templates
│ ├── base.html
│ ├── registration/
│ │ ├── login.html
│ │ ├── register.html
│ │ └── profile.html
│ └── bookings/
│ ├── travel_list.html
│ ├── booking_form.html
│ ├── booking_list.html
│ └── booking_detail.html
├── static/ # Static assets
│ ├── css/style.css
│ └── images/
├── .env # Environment variables
├── .gitignore
├── requirements.txt
├── manage.py
└── README.md

yaml
Copy
Edit

---

## 🔑 Environment Variables

`.env` file example:

```env
PROJECT_NAME=TravelEase
DEBUG=True
SECRET_KEY=your-secret-key-here-change-in-production

# Database Config (PostgreSQL)
DB_NAME=travelease_db
DB_USER=your_db_user
DB_PASSWORD=yourpassword
DB_HOST=localhost
DB_PORT=5432

# Deployment
ALLOWED_HOSTS=127.0.0.1,localhost,travelease-p0ov.onrender.com
⚡ Setup Instructions
1️⃣ Clone Repository
bash
Copy
Edit
git clone https://github.com/mdwarish7867/TravelLykkeAssignment.git
cd TravelLykkeAssignment
2️⃣ Create Virtual Environment
bash
Copy
Edit
python -m venv venv
venv\Scripts\activate   # Windows
# OR
source venv/bin/activate   # Linux/Mac
3️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4️⃣ Configure .env
Update database credentials and project name as per your setup.

5️⃣ Run Migrations
bash
Copy
Edit
python manage.py makemigrations
python manage.py migrate
6️⃣ Create Superuser
bash
Copy
Edit
python manage.py createsuperuser
7️⃣ Start Server
bash
Copy
Edit
python manage.py runserver
Now visit 👉 http://127.0.0.1:8000/

🚀 Deployment
This project is deployed on Render with PostgreSQL.

Live URL 👉 https://travelease-p0ov.onrender.com

📖 Future Improvements
🔹 Add Payment Gateway (Stripe / Razorpay)
🔹 Email Notifications for Bookings
🔹 Advanced Filtering with Pagination
🔹 REST API using Django REST Framework

👨‍💻 Developer
Developed by Mohammad Warish Ansari 💻
🎯 Internship Assignment for Travel Lykke
```
