# 🎫 Support Ticket Automation API

A REST API that simulates a real-world technical support pipeline — automatically classifying incoming tickets, defining the next best action, and logging interactions. Built to demonstrate skills in backend automation, webhook handling, and support engineering workflows.

## 🧩 The Problem
Support teams often receive hundreds of messages daily. Without an automated triage system, tickets are manually read, categorized, and routed, which leads to slow response times and workflow bottlenecks.

## ✅ The Solution
This API receives a support message via webhook, automatically classifies it into a specific category (e.g., Billing, Technical), determines the appropriate action, and stores the event for tracking.

## ⚙️ Tech Stack
- **Python / Flask** — Core logic and REST API framework
- **JSON** — Data payload formatting
- **File Logging** — Persistent ticket tracking

## 📬 API Endpoint Example

**POST** `/webhook`

**Request:**
```json
{
  "message": "I was charged twice for my subscription this month"
}
```

**Response:**
```json
{
  "message": "I was charged twice for my subscription this month",
  "category": "Billing Issue",
  "action": "Escalate to billing team",
  "status": "processed"
}
```

## 🚀 How to Run Locally
1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run the application: `python main.py`
4. Send a POST request to `http://localhost:5000/webhook`

## 💼 Skills Demonstrated
- REST API design and webhook handling
- Automated classification logic
- Real-world support engineering simulation
