# 🌍 TravelEase – Online Travel Booking System ✈️🚆🚌

**Live Demo** 👉 [https://travelease-p0ov.onrender.com](https://travelease-p0ov.onrender.com)

TravelEase is a **Django-based travel booking system** that allows users to search for **flights, trains, and buses**, book tickets, and manage their bookings online.
It was built as part of the **Travel Lykke Internship Assignment** and deployed on **Render with PostgreSQL**.

---

## ✨ Features

- 🔑 **User Authentication** – Register, Login, Profile Management
- 🌍 **Browse Travel Options** – Filter by travel type, source, destination, and date
- 🎟️ **Booking System** – Book tickets, manage active bookings, cancel anytime
- 📅 **Travel Scheduling** – Travel options with departure/arrival times
- 📱 **Responsive UI** – Built with Bootstrap for mobile & desktop
- 🔒 **Secure Configuration** – All secrets managed via `.env` file
- 🗄️ **Database** – PostgreSQL (production) & SQLite (development fallback)

---

## 🛠 Tech Stack

- **Backend:** Django (Python)
- **Frontend:** Django Templates + Bootstrap
- **Database:** PostgreSQL (Render) / SQLite (local dev)
- **Deployment:** Render
- **Environment Management:** `.env` file

---

## 📂 Project Structure

```
travelease/
├── TravelEase/              # Core project settings
├── bookings/                # Bookings & Travel Options
├── users/                   # User authentication & profiles
├── templates/               # HTML templates
├── static/                  # CSS, JS, Images
├── .env                     # Environment configs
├── manage.py
└── requirements.txt
```

---

## ⚡ Setup Guide (For Testers / Developers)

### 1️⃣ Clone & Setup

```bash
git clone https://github.com/mdwarish7867/TravelLykkeAssignment.git
cd TravelLykkeAssignment
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate  # Linux/Mac
pip install -r requirements.txt
```

### 2️⃣ Configure Environment

Create a `.env` file in project root:

```env
PROJECT_NAME=TravelEase
DEBUG=True
SECRET_KEY=your-secret-key

# Database (PostgreSQL / SQLite fallback)
DB_NAME=travelease_db
DB_USER=your_user
DB_PASSWORD=your_password
DB_HOST=your-host
DB_PORT=5432

ALLOWED_HOSTS=127.0.0.1,localhost,travelease-p0ov.onrender.com
```

---

### 3️⃣ Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 4️⃣ Create Superuser (Admin Access)

```bash
python manage.py createsuperuser
```

👉 Use this superuser account to log in at:
`http://127.0.0.1:8000/admin/`

From here, the **tester can:**

- Add **Travel Options** (Flight, Train, Bus)
- Manage **Users & Bookings**
- Update or delete records

---

### 5️⃣ Add Travel Options

1. Log in to the **Django Admin Panel** (`/admin/`) with your superuser account.
2. Go to **Bookings → Travel Options**.
3. Click **Add Travel Option** and fill in:

   - Travel ID (e.g., FL123)
   - Travel Type (Flight / Train / Bus)
   - Source & Destination
   - Departure & Arrival Time
   - Price & Available Seats

4. Save – the travel option is now visible to users on the website.

---

### 6️⃣ Test Booking Flow

1. Register as a new user from the website.
2. Log in and browse available travel options.
3. Select a travel option and book seats.
4. View bookings under **My Bookings**.
5. Cancel a booking to test cancellation flow.

---

## 🚀 Deployment (Render)

- Collect static files:

  ```bash
  python manage.py collectstatic
  ```

- Configure environment variables in **Render Dashboard**.
- Apply migrations on the server.
- Connect repository → Deploy.

Live URL 👉 [https://travelease-p0ov.onrender.com](https://travelease-p0ov.onrender.com)

---

## 📖 Future Enhancements

- 💳 Payment Gateway (Stripe / Razorpay)
- 📩 Email Notifications (Booking Confirmations)
- 🔍 Advanced Search + Pagination
- 📱 REST API with Django REST Framework

---

## 👩‍💻 How Testers/Admins Can Manage

- **Superuser/Admin:**

  - Add/Edit/Delete travel options
  - Manage bookings (approve/cancel)
  - View registered users

- **Normal Users:**

  - Register/Login
  - Search travel options
  - Book & cancel tickets

---

## 🤝 Contribution

1. Fork repo
2. Create feature branch
3. Commit & push
4. Open PR 🎉

---

## 📜 License

Licensed under the **MIT License**.

---

### 👨‍💻 Developed by [Md Warish Ansari](https://github.com/mdwarish7867)

🎯 Internship Selection Project for **Travel Lykke**
