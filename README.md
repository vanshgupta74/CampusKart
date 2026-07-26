# 🛒 CampusKart

A full-stack e-commerce web application designed for college students to **buy and sell products within campus** — like a mini OLX, but only for your college!

🔗 **Live Demo:** [campuskart-n2yl.onrender.com](https://campuskart-n2yl.onrender.com)

---

## 📌 About The Project

CampusKart solves a common campus problem — final year students leaving college often have furniture, books, electronics, and other items they no longer need. Instead of throwing them away, they can **list them for sale** on CampusKart and help junior students get things at affordable prices.

---

## ✨ Features

- 🔐 **User Authentication** — Register, Login, Logout
- 📦 **Product Listings** — Add, view, and manage products
- 🖼️ **Image Upload** — Upload product photos
- 🗂️ **Categories** — Browse by category (Books, Furniture, Electronics, etc.)
- 🔍 **Search & Filter** — Find products easily
- 📱 **Responsive Design** — Works on mobile and desktop

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| **Backend** | Python, Django 6.0 |
| **Frontend** | HTML, CSS, Bootstrap, JavaScript |
| **Database** | PostgreSQL (Supabase) |
| **Deployment** | Render |
| **Media Storage** | Cloudinary / Local |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- pip
- PostgreSQL (or Supabase account)

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/vanshgupta74/CampusKart.git
cd CampusKart

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Create .env file and add your credentials
cp .env.example .env

# 5. Run migrations
python manage.py migrate

# 6. Create superuser (for admin access)
python manage.py createsuperuser

# 7. Run the server
python manage.py runserver
```

---

## ⚙️ Environment Variables

Create a `.env` file in the root directory:

```env
SECRET_KEY=your_django_secret_key
DEBUG=False
DATABASE_URL=your_supabase_postgresql_url
ALLOWED_HOSTS=your_domain.onrender.com
```

---

## 📁 Project Structure

```
CampusKart/
├── campus_marketplace/     # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── marketplace/            # Main app
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
├── static/                 # CSS, JS, Images
├── media/                  # Uploaded product images
├── requirements.txt
├── manage.py
└── README.md
```

---

## 👨‍💻 Author

**Vansh Gupta**
- GitHub: [@vanshgupta74](https://github.com/vanshgupta74)
- B.Tech CSE | IET Lucknow

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

⭐ **If you found this project helpful, please give it a star!**
