# Nomadic — Travel Companion Desktop App

Nomadic is a PyQt5 desktop application for travellers. It supports two user roles — **User** and **Nomadic** (power user) — each with their own dashboard and feature set.

---

## Features

| Screen | Description |
|---|---|
| Login | Role-based login (User / Nomadic) with password masking |
| Sign Up | New user registration |
| User Dashboard | Central hub with navigation to all user features |
| Nomadic Dashboard | Extended dashboard with an additional Credentials page |
| Discover | Browse cities, restaurants, hotels, and tourist spots |
| Trending | View trending travel destinations |
| Your Travels | Personal travel history |
| Account | User account management |
| Credentials | Nomadic-only credentials page |

---

## Tech Stack

- Python 3.x
- PyQt5 — UI framework
- Qt Designer `.ui` files — layout definitions
- PyQt5 Resource Compiler (`pyrcc5`) — image assets compiled into `.py` resource modules
- MySQL — backend database (via `mysql-connector-python`)

---

## Project Structure

```
Nomadic/
├── main.py              # Application entry point — all screens and navigation
├── db.py                # DB connection helper + table initialisation
├── .env.example         # Environment variable template (copy to .env)
├── *.ui                 # Qt Designer UI layout files
│   ├── front.ui         # Login screen
│   ├── signup.ui        # Sign-up screen
│   ├── userdash.ui      # User dashboard
│   ├── nomaddash.ui     # Nomadic dashboard
│   ├── discover.ui      # Discover page
│   ├── trending.ui      # Trending page
│   ├── travelhistory.ui # Your Travels page
│   ├── account.ui       # Account page
│   └── creds.ui         # Credentials page (Nomadic only)
├── *.qrc                # Qt resource definition files (image assets)
│   ├── source.qrc       # Navigation icons
│   ├── source02.qrc     # Dashboard icons
│   ├── discover.qrc     # Discover page images
│   └── trending.qrc     # Trending page images
├── requirements.txt     # Python dependencies
└── README.md
```

> The compiled resource files (`source.py`, `source02.py`, `discover.py`, `trending.py`) are auto-generated from the `.qrc` files and are excluded from version control. See setup instructions below to regenerate them.

---

## Getting Started

### Prerequisites

- Python 3.8+
- PyQt5
- MySQL server
- `bcrypt` (installed via requirements)
- Qt Designer (optional, for editing `.ui` files)
- `pyrcc5` (bundled with PyQt5 tools)

### Installation

```bash
# Clone the repository
git clone https://github.com/your-username/nomadic.git
cd nomadic

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Compile Resource Files

The image assets must be compiled from the `.qrc` files before running the app:

```bash
pyrcc5 source.qrc   -o source.py
pyrcc5 source02.qrc -o source02.py
pyrcc5 discover.qrc -o discover.py
pyrcc5 trending.qrc -o trending.py
```

### Database Setup

Create a MySQL database, then copy `.env.example` to `.env` and fill in your credentials:

```bash
cp .env.example .env
```

```env
DB_HOST=localhost
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_NAME=nomadic
```

The app reads these at startup via `db.py` and automatically creates the `users` table if it doesn't exist. Passwords are stored as **bcrypt hashes** — never plaintext.

### Run the App

```bash
python main.py
```

---

## Navigation Overview

```
Login (front.ui)
├── Sign Up → back to Login
├── User Login  → User Dashboard (userdash.ui)
│   ├── Discover
│   ├── Trending
│   ├── Your Travels
│   ├── Account
│   └── Logout → Login
└── Nomadic Login → Nomadic Dashboard (nomaddash.ui)
    ├── Discover
    ├── Trending
    ├── Your Travels
    ├── Account
    ├── Credentials
    └── Logout → Login
```

## Security Notes

- Passwords are hashed with **bcrypt** — plaintext passwords are never stored
- DB credentials are read from **environment variables** via a `.env` file — never hardcoded
- A `Session` class tracks the logged-in user and role at runtime, so all back-buttons and navigation resolve to the correct dashboard automatically

---

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m "feat: add your feature"`
4. Push and open a Pull Request

---

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
