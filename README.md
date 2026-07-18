# Library Management System in Python

A comprehensive Python-based Command Line Interface (CLI) application designed to efficiently manage library resources. This project demonstrates core software engineering concepts, modular programming, error handling, and version control using Git.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Screenshots](#screenshots)
- [Tech Stack](#tech-stack)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [API Endpoints](#api-endpoints)
- [Database Schema](#database-schema)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## 📖 Overview

The Library Management System in Python is a robust backend solution for managing library operations. It provides an intuitive interface for librarians and administrators to manage books, patrons, and transactions efficiently. The system is built with scalability and maintainability in mind, following Python best practices and software engineering principles.

## ✨ Features

### Book Management
- ✅ Add new books to the library database
- ✅ Edit existing book information (title, author, ISBN, etc.)
- ✅ Delete books from the system
- ✅ Track book availability and status
- ✅ Manage multiple copies of the same book

### Patron Management
- ✅ Register and maintain patron records
- ✅ Update patron contact information
- ✅ Track patron borrowing history
- ✅ Manage patron account status

### Book Operations
- ✅ Issue books to patrons
- ✅ Process book returns
- ✅ Track due dates and overdue notifications
- ✅ Calculate late fees (if applicable)

### Search and Retrieval
- ✅ Search books by title
- ✅ Search books by author
- ✅ Search books by ISBN
- ✅ Filter books by availability status
- ✅ Advanced search with multiple criteria

### Additional Features
- ✅ Error handling and validation
- ✅ Data persistence using SQLite
- ✅ User-friendly command-line interface
- ✅ Comprehensive logging and reporting

## 📸 Screenshots

### Main Dashboard
![Dashboard](https://github.com/user-attachments/assets/07b7f937-6844-4d97-8987-fd2d01cc9394)

### Book Management Interface
![Book Management](https://github.com/user-attachments/assets/50a5fa82-5cfa-45f0-906f-0456311539cc)

### Transaction History
![Transactions](https://github.com/user-attachments/assets/73ad672c-2d71-40fc-a54d-3122933e995f)

## 🛠 Tech Stack

- **Language**: Python 3.7+
- **Database**: SQLite3
- **Architecture**: Modular CLI Application
- **Key Libraries**:
  - `sqlite3` - Database management
  - `datetime` - Date and time operations
  - `argparse` - Command-line argument parsing
  - Additional dependencies listed in `requirements.txt`

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.7 or higher
- pip (Python package manager)
- Git
- SQLite3 (usually included with Python)

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/gihangreshan1/library-management-system-in-python.git
cd library-management-system-in-python
```

### 2. Create a Virtual Environment (Recommended)

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS and Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Database Setup

#### Option A: Using Provided Schema (Recommended)

```bash
# The application will automatically create the database on first run
python main.py
```

#### Option B: Manual Setup

1. Create a SQLite database using the provided schema:
```bash
sqlite3 library.db < database_schema.sql
```

2. Update the database connection settings in `config.py`:
```python
DATABASE_URL = "sqlite:///library.db"
```

## ⚙️ Configuration

Update the `config.py` file to customize settings:

```python
# Database Configuration
DATABASE_NAME = "library.db"
DATABASE_PATH = "./data/"

# Application Settings
MAX_BOOKS_PER_PATRON = 5
LOAN_PERIOD_DAYS = 14
FINE_PER_DAY = 0.50

# Logging
LOG_LEVEL = "INFO"
LOG_FILE = "./logs/app.log"
```

## 💻 Usage

### Starting the Application

```bash
python main.py
```

### Main Menu Options

Upon running the application, you'll see the main menu with the following options:

```
========================================
  Library Management System
========================================
1. Book Management
2. Patron Management
3. Book Transactions
4. Search
5. Reports
6. Exit
========================================
```

### Common Operations

#### Adding a Book

```
Select Option: 1
Select Sub-option: 1 (Add Book)
Enter Book Title: Python Programming
Enter Author Name: Guido van Rossum
Enter ISBN: 978-0-13-110362-7
Enter Publication Year: 2020
Enter Number of Copies: 3
```

#### Registering a Patron

```
Select Option: 2
Select Sub-option: 1 (Register Patron)
Enter Patron Name: John Doe
Enter Email: john@example.com
Enter Phone: +1-555-0123
```

#### Issuing a Book

```
Select Option: 3
Select Sub-option: 1 (Issue Book)
Enter Book ID: 1
Enter Patron ID: 1
Enter Due Date (YYYY-MM-DD): 2024-12-31
```

#### Returning a Book

```
Select Option: 3
Select Sub-option: 2 (Return Book)
Enter Transaction ID: 1
```

## 📁 Project Structure

```
library-management-system-in-python/
├── main.py                      # Application entry point
├── config.py                    # Configuration settings
├── requirements.txt             # Python dependencies
├── database_schema.sql          # Database schema
├── README.md                    # This file
├── LICENSE                      # MIT License
│
├── src/
│   ├── __init__.py
│   ├── database.py              # Database connection and operations
│   ├── models.py                # Data models (Book, Patron, Transaction)
│   ├── services/
│   │   ├── book_service.py      # Book management logic
│   │   ├── patron_service.py    # Patron management logic
│   │   └── transaction_service.py # Transaction management logic
│   └── utils/
│       ├── validators.py        # Input validation functions
│       ├── logger.py            # Logging configuration
│       └── helpers.py           # Helper functions
│
├── data/
│   └── library.db               # SQLite database (created on first run)
│
├── logs/
│   └── app.log                  # Application logs
│
└── tests/
    ├── test_book_service.py
    ├── test_patron_service.py
    └── test_transaction_service.py
```

## 🔌 API Endpoints

The application supports the following operations through the CLI interface:

### Books
- `GET /books` - List all books
- `GET /books/<id>` - Get book details
- `POST /books` - Add a new book
- `PUT /books/<id>` - Update book information
- `DELETE /books/<id>` - Delete a book

### Patrons
- `GET /patrons` - List all patrons
- `GET /patrons/<id>` - Get patron details
- `POST /patrons` - Register a new patron
- `PUT /patrons/<id>` - Update patron information
- `DELETE /patrons/<id>` - Delete a patron

### Transactions
- `GET /transactions` - List all transactions
- `POST /transactions/issue` - Issue a book
- `POST /transactions/return` - Return a book
- `GET /transactions/patron/<id>` - Get patron's transaction history

### Search
- `GET /search/books?title=<keyword>` - Search by title
- `GET /search/books?author=<keyword>` - Search by author
- `GET /search/books?isbn=<keyword>` - Search by ISBN

## 🗄️ Database Schema

### Books Table
```sql
CREATE TABLE books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    isbn TEXT UNIQUE,
    publication_year INTEGER,
    total_copies INTEGER DEFAULT 1,
    available_copies INTEGER DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Patrons Table
```sql
CREATE TABLE patrons (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE,
    phone TEXT,
    membership_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status TEXT DEFAULT 'active'
);
```

### Transactions Table
```sql
CREATE TABLE transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    book_id INTEGER NOT NULL,
    patron_id INTEGER NOT NULL,
    issue_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    return_date TIMESTAMP,
    due_date TIMESTAMP,
    status TEXT DEFAULT 'borrowed',
    FOREIGN KEY (book_id) REFERENCES books(id),
    FOREIGN KEY (patron_id) REFERENCES patrons(id)
);
```

## 🤝 Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

### Steps to Contribute

1. **Fork the repository**
   ```bash
   Click the 'Fork' button on the repository page
   ```

2. **Clone your fork**
   ```bash
   git clone https://github.com/YOUR_USERNAME/library-management-system-in-python.git
   cd library-management-system-in-python
   ```

3. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

4. **Make your changes**
   - Ensure code follows PEP 8 standards
   - Add comments and docstrings
   - Write tests for new features

5. **Commit your changes**
   ```bash
   git commit -am 'Add new feature: description of your changes'
   ```

6. **Push to your branch**
   ```bash
   git push origin feature/your-feature-name
   ```

7. **Create a Pull Request**
   - Go to the repository page
   - Click 'New Pull Request'
   - Provide a clear description of your changes

### Contribution Guidelines

- Ensure your code adheres to [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guidelines
- Add comprehensive docstrings to all functions and classes
- Write unit tests for new features (minimum 80% coverage)
- Update documentation if adding new features
- For major changes, open an issue first to discuss proposed changes
- Keep commits atomic and well-documented

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

### MIT License Summary
- ✅ You can use this code for personal, commercial, and private purposes
- ✅ You can modify, distribute, and sublicense the code
- ❌ You cannot hold the author liable for any claims
- ✅ You must include a copy of the license and copyright notice

## 📧 Contact

For any inquiries, feedback, or suggestions, please reach out:

- **Author**: Gihan Greshan
- **Email**: [gihangreshan@gmail.com](mailto:gihangreshan@gmail.com)
- **GitHub**: [@gihangreshan1](https://github.com/gihangreshan1)
- **Repository**: [Library Management System](https://github.com/gihangreshan1/Library-Management-System-in-Python)

## 🚀 Future Enhancements

- [ ] Web-based interface using Flask/Django
- [ ] REST API with FastAPI
- [ ] User authentication and role-based access control
- [ ] Advanced reporting and analytics
- [ ] Email notifications for due dates and overdue books
- [ ] Mobile app integration
- [ ] Integration with barcode/QR code scanning

---

**Last Updated**: July 18, 2026

Made with ❤️ by Gihan Greshan
