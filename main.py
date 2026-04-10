from flask import Flask, request, jsonify

app = Flask(__name__)

def classify_ticket(message):
    message = message.lower()

    if "payment" in message or "charged" in message or "refund" in message:
        return "Billing Issue"
    elif "error" in message or "bug" in message or "crash" in message:
        return "Technical Issue"
    elif "login" in message or "password" in message:
        return "Account Issue"
    elif "how" in message or "help" in message:
        return "General Question"
    else:
        return "Other"


def decide_action(category):
    if category == "Billing Issue":
        return "Escalate to billing team"
    elif category == "Technical Issue":
        return "Create bug report and collect logs"
    elif category == "Account Issue":
        return "Send password reset instructions"
    elif category == "General Question":
        return "Send help article"
    else:
        return "Manual review"


def log_ticket(message, category, action):
    with open("tickets.log", "a") as file:
        file.write(f"Message: {message}\n")
        file.write(f"Category: {category}\n")
        file.write(f"Action: {action}\n")
        file.write("-" * 40 + "\n")


@app.route("/webhook", methods=["POST"])
def receive_ticket():
    data = request.get_json()

    if not data or "message" not in data:
        return jsonify({"error": "No message provided"}), 400

    message = data["message"]
    category = classify_ticket(message)
    action = decide_action(category)

    log_ticket(message, category, action)

    return jsonify({
        "message": message,
        "category": category,
        "action": action,
        "status": "processed"
    })


if __name__ == "__main__":
    print("Support Ticket API running on http://127.0.0.1:5000")
    app.run(debug=True)
