# Python-Newsletter-Automation

# 📧 Bulk Newsletter Sender

This project is a Python-based email automation script designed to send bulk HTML newsletters to a list of subscribers. It fetches subscriber data from a remote PHP script and sends customized emails via an SMTP server.

---

## 🚀 Features

- ✅ Fetches recipients from a remote PHP endpoint
- ✅ Sends bulk emails using GoDaddy SMTP
- ✅ Uses a rich HTML template for formatting
- ✅ Includes batching and delays to avoid spam filters
- ✅ Logs sent emails with timestamps

---

## 📁 Files

```bash
.
├── newsletter_script.py      # Main script to send emails
├── email_log.txt             # Log file for sent emails
└── README.md                 # This file
```

---

## 🛠️ Requirements

- Python 3.x
- Internet connection
- SMTP credentials
- Install required package:

```bash
pip install requests
```

*Other libraries used (`smtplib`, `time`, `email`, `re`) are part of Python's standard library.*

---

## ⚙️ SMTP Configuration

The script uses the following SMTP setup (already configured inside `newsletter_script.py`):

```python
SMTP_SERVER = "sg2plzcpnl505626.prod.sin2.secureserver.net"
SMTP_PORT = 25
SENDER_EMAIL = "newsletter@ibeeanalytics.com"
SENDER_NAME = "iBee Analytics"
SENDER_PASSWORD = "your_password_here"
```

> 🔐 **Important:** Replace `"your_password_here"` with your actual email password or load it securely using `.env` or environment variables in production.

---

## 📥 Fetching Subscribers

The subscriber list is fetched using a `GET` request from:

```
https://ibeeanalytics.com/newsletter/testing.php
```

The response should contain email addresses separated by commas.

---

## 📧 Email Template

The script includes a detailed and responsive HTML email template, featuring:

- iBee logo and intro
- Market updates and highlights
- Featured tools and images
- Footer with disclaimer and contact info

You can customize the HTML section inside `newsletter_script.py`.

---

## ▶️ How to Run

1. Clone this repository or download the files.
2. Update SMTP Configuration in the script.
3. Run the script:

```bash
python newsletter_script.py
```

4. Check `email_log.txt` for the status of sent emails.

---

## 🧠 Notes

- Batching is set to 10 emails per batch with a 5-second delay.
- You can increase or decrease this by editing these lines:

```python
emails_per_batch = 10
sleep_time_between_batches = 5
```

---

## 📜 License

This project is open-sourced under the MIT License.

---

## 📩 Created by sriram
