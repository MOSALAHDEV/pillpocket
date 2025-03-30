# 💊 PillPocket – Medication Management API

PillPocket is a backend-focused portfolio project for ALX that simplifies prescription tracking and order management. It's built using Flask, MySQL, and RESTful principles, with a modular codebase and solid database design.

---

## 🚀 Live App
Coming soon…

---

## 🧪 Example API Endpoints

| Method | Endpoint              | Description       |
|--------|-----------------------|-------------------|
| GET    | `/api/v1/users`       | List all users    |
| POST   | `/api/v1/users`       | Create new user   |
| GET    | `/api/v1/medications` | List medications  |
| POST   | `/api/v1/orders`      | Place order       |

> Use Postman or `curl` to interact with the API. Swagger docs can be enabled via Flasgger.

---

## 📁 Project Structure

```bash
pillpocket/
├── api/
│   └── v1/
│       ├── views/
│       └── app.py
├── models/
│   ├── engine/
│   ├── base_model.py
│   ├── medication.py
│   ├── order.py
│   └── user.py
├── tests/
├── app.py
├── console.py
├── insert_data.py
├── file.json
└── README.md
```

---

## 👥 Team

| Name          | GitHub                                       | LinkedIn                                                   | Twitter   |
|---------------|----------------------------------------------|-------------------------------------------------------------|-----------|
| Mohamed Salah | [MOSALAHDEV](https://github.com/MOSALAHDEV) | [linkedin.com/in/mohamed-salah-3a09572a0](https://linkedin.com/in/mohamed-salah-3a09572a0) | [@Mo10salah100](https://twitter.com/Mo10salah100) |

---

## 🛠 Installation & Setup

```bash
# Clone the repo
git clone https://github.com/MOSALAHDEV/pillpocket.git
cd pillpocket

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Setup MySQL DB (adjust credentials)
mysql -u root -p < setup_mysql_dev.sql

# Start the Flask server
python3 app.py
```

---

## 🤝 Contributing

Contributions are welcome! Here's how:

```bash
# Fork the repo
# Create your feature branch
git checkout -b feature/awesome-feature

# Make changes and commit
git commit -m 'feat: add awesome feature'

# Push and open a PR
git push origin feature/awesome-feature
```

---

## 🖼 Screenshots

Add your screenshots inside a `screenshots/` folder and reference them here:

```markdown
![Landing Page](screenshots/landing-page.png)
![API Swagger](screenshots/swagger-docs.png)
```

---

## 🧭 Project Inspiration

This project was inspired by the need to simplify medical order and prescription management — especially in underserved areas where tech access is limited. **PillPocket** offers a minimal backend that can be integrated into full-stack systems, and it helped us solidify REST design, Flask, and ORM skills.

We focused on building scalable APIs, maintaining a clean structure, and writing maintainable code.

---

## 📘 License

This project is licensed under the **MIT License**. See [LICENSE](./LICENSE) for details.

---

## 📎 Useful Links

- [GitHub Repository](https://github.com/MOSALAHDEV/pillpocket)
- [DigitalOcean Python Commenting Standards](https://www.digitalocean.com/community/tutorials/how-to-write-comments-in-python-3)

---

## 🔮 Next Steps

- Add frontend (React/Vue)
- Email/SMS integration for order tracking
- Role-based access (admin/patient/pharmacy)
- Improve API documentation with Swagger/OpenAPI

---

> 👨‍💻 Built with 💙 by Mohamed Salah
