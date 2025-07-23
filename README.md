# 🚀 KPA Backend API (FastAPI + PostgreSQL)

This is a backend assignment project that implements two production-style APIs based on the KPA Form Data Swagger Spec. It uses **FastAPI** and **PostgreSQL**, following clean code and modular architecture practices.

---

## 📌 Implemented Endpoints

| Method | Endpoint                                      | Description                          |
|--------|-----------------------------------------------|--------------------------------------|
| POST   | `/api/forms/wheel-specifications`             | Submit a wheel specification form    |
| GET    | `/api/forms/wheel-specifications`             | Get filtered wheel specification records |
| POST   | `/api/forms/bogie-checksheet`                 | Submit a bogie checksheet form       |

---

## 📦 Tech Stack

- **Framework:** FastAPI  
- **Database:** PostgreSQL (Neon.tech compatible)  
- **ORM:** SQLAlchemy  
- **Validation:** Pydantic  
- **Environment Config:** python-dotenv  
- **API Testing:** Swagger UI, Postman  

---

## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/Kusuma-GM/kpa_backend-main.git
cd kpa_backend-main

3. Create Virtual Environment & Install Dependencies
python -m venv venv
# Activate environment
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

4. Run the Application
uvicorn app.main:app --reload

API Documentation
Swagger UI: http://localhost:8000/docs

ReDoc: http://localhost:8000/redoc

🧪 Sample API Payloads
➕ POST /api/forms/wheel-specifications
{
  "formNumber": "WHEEL-2025-001",
  "submittedBy": "user_id_123",
  "submittedDate": "2025-07-03",
  "fields": {
    "treadDiameterNew": "915 (900-1000)",
    "wheelGauge": "1600 (+2,-1)"
  }
}

🔍 GET /api/forms/wheel-specifications
Query Parameters:
formNumber=...&submittedBy=...&submittedDate=...

➕ POST /api/forms/bogie-checksheet
{
  "formNumber": "BOGIE-2025-001",
  "inspectionBy": "user_id_456",
  "inspectionDate": "2025-07-03",
  "bogieDetails": {
    "bogieNo": "BG1234",
    "makerYearBuilt": "RDSO/2018"
  },
  "bogieChecksheet": {
    "bolster": "Good",
    "lowerSpringSeat": "Good"
  },
  "bmbcChecksheet": {
    "cylinderBody": "WORN OUT",
    "plungerSpring": "GOOD"
  }
}

🧾 Notes
Tables are automatically created on app startup.

Compatible with Neon.tech, Railway, and other PostgreSQL cloud providers.

Strong validation with Pydantic for nested JSON objects and required fields.

📬 Submission Checklist
 Source code (GitHub repo or ZIP)

✅ Updated Postman Collection

✅ README with complete setup and usage instructions

✅  Recorded video walkthrough of the app

👨‍💻 Author
Made with ❤️ by Kusuma GM for the KPA Backend API development assignment.

