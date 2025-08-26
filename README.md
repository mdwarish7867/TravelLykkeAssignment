# 🌍 TravelEase – Online Travel Booking System ✈️🚆🚌

Live Demo 👉 [https://travelease-p0ov.onrender.com](https://travelease-p0ov.onrender.com)

Welcome to **TravelEase**, a simple and efficient **online travel booking system** built with **Django, PostgreSQL, and Bootstrap**.  
This project was created as part of the **Travel Lykke Internship Assignment**.

Users can register, browse travel options (flights, trains, buses), make bookings, manage their profile, and cancel tickets.  
The app is fully configurable via `.env` file and deployed on **Render with PostgreSQL**. 🚀

---

## ✨ Features

✅ User Registration, Login & Profile Management  
✅ Browse Travel Options (Flight / Train / Bus)  
✅ Book Tickets & Manage Bookings  
✅ Cancel Bookings Anytime  
✅ Responsive UI with **Bootstrap**  
✅ Secure Configs via **.env File**  
✅ PostgreSQL Database Integration  
✅ Filters & Search Options for Travel Plans  
✅ Deployable on **Render**

---

## 🛠️ Tech Stack

- **Backend:** Django (Python)
- **Frontend:** Django Templates + Bootstrap
- **Database:** PostgreSQL
- **Deployment:** Render
- **Environment:** `.env` file for secure configs

---

## 📂 Project Structure

```

travelease/
├── TravelEase/              # Core project settings
│   ├── **init**.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── bookings/                # Bookings app
│   ├── models.py            # Booking & TravelOption models
│   ├── views.py             # Booking logic
│   ├── forms.py             # Booking forms
│   ├── urls.py
│   └── admin.py
├── users/                   # Users app
│   ├── models.py            # Extended User Profile
│   ├── views.py             # Auth & Profile logic
│   ├── forms.py             # User forms
│   ├── urls.py
│   └── admin.py
├── templates/               # Frontend templates
│   ├── base.html
│   ├── registration/
│   │   ├── login.html
│   │   ├── register.html
│   │   └── profile.html
│   └── bookings/
│       ├── booking\_list.html
│       ├── travel\_list.html
│       ├── booking\_form.html
│       └── booking\_detail.html
├── static/                  # Static files (CSS, JS, images)
│   ├── css/style.css
│   └── images/
├── .env                     # Environment variables
├── .gitignore
├── requirements.txt
├── manage.py
└── README.md

```

---

## 🔑 Environment Variables

Create a `.env` file in the project root:

```env
PROJECT_NAME=TravelEase
DEBUG=True
SECRET_KEY=your-secret-key-here-change-in-production

# Database Config (PostgreSQL)
DB_NAME=travelease_db
DB_USER=your_db_user
DB_PASSWORD=yourpassword
DB_HOST=your-db-host.render.com
DB_PORT=5432

# Deployment
ALLOWED_HOSTS=127.0.0.1,localhost,travelease-p0ov.onrender.com
```

---

## ⚡ Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone https://github.com/mdwarish7867/TravelLykkeAssignment.git
cd TravelLykkeAssignment
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # For Linux/Mac
venv\Scripts\activate      # For Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure `.env` File

Update `.env` with your PostgreSQL credentials, project name, and secret key.

### 5️⃣ Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6️⃣ Create Superuser

```bash
python manage.py createsuperuser
```

### 7️⃣ Start Development Server

```bash
python manage.py runserver
```

Now visit 👉 `http://127.0.0.1:8000/`

---

## 🚀 Deployment

This project is deployed on **Render with PostgreSQL**.

Live URL 👉 [https://travelease-p0ov.onrender.com](https://travelease-p0ov.onrender.com)

- Collect static files:

```bash
python manage.py collectstatic
```

- Configure **ALLOWED_HOSTS** in `.env`
- Push code to GitHub and connect to Render
- Apply migrations on the server

---

## 📖 Future Improvements

🔹 Add Payment Gateway (Stripe / Razorpay)
🔹 Email Notifications for Bookings
🔹 Advanced Filtering with Pagination
🔹 REST API using Django REST Framework

---

## 🤝 Contribution

Contributions are welcome! 🎉

1. Fork the repo
2. Create a new branch (`feature/your-feature`)
3. Commit changes
4. Push & create PR

---

## 📜 License

This project is licensed under the **MIT License**.

---

### 👨‍💻 Developed by [Mohammad Warish Ansari](https://github.com/mdwarish7867)

🎯 Internship Assignment for **Travel Lykke**
