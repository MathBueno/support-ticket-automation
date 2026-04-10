# Support Ticket Automation API

This project simulates a real-world technical support system using a simple API.

It receives customer messages, classifies the issue, decides the appropriate action, and logs the interaction.

---

## 🚀 Features

- Ticket classification (Billing, Technical, Account, General)
- Automated decision-making
- Log storage for support tracking
- REST API with webhook endpoint
- JSON request/response handling

---

## 🧠 What this project demonstrates

- API development with Flask
- Handling HTTP requests (POST)
- Working with JSON data
- Basic automation logic
- Logging and traceability
- Error handling

---

## 🔧 Tech Stack

- Python
- Flask
- JSON
- File logging

---

## 📡 API Endpoint

POST /webhook

### Example request:

{
  "message": "I was charged twice"
}

### Example response:

{
  "message": "I was charged twice",
  "category": "Billing Issue",
  "action": "Escalate to billing team",
  "status": "processed"
}

---

## ⚙️ How to run locally

pip install flask  
python main.py  

---

## 📌 Notes

This project is part of my transition into the tech industry, focusing on technical support, automation, and system integration.

---

## 👤 Author

Matheus Bueno

- LinkedIn: https://www.linkedin.com/in/eng-matheusbueno/
