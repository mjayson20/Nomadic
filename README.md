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

Create a MySQL database and update the connection details in `main.py`:

```python
mycon = mys.connect(
    host='localhost',
    user='your_db_user',
    passwd='your_db_password',
    database='nomadic'
)
```

> Tip: Use environment variables or a config file to avoid committing credentials.

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

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m "feat: add your feature"`
4. Push and open a Pull Request

---

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
