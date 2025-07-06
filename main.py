import os
import smtplib
import requests
from email.mime.text import MIMEText

def get_gold_price():
    api_key = os.getenv("METALS_API_KEY")
    url = f"https://metals-api.com/api/latest?access_key={api_key}&base=USD&symbols=XAU"
    
    response = requests.get(url)
    data = response.json()

    if "rates" in data and "XAU" in data["rates"]:
        gold_price = data["rates"]["XAU"]
        return round(gold_price, 2)
    else:
        raise Exception("لم نتمكن من جلب سعر الذهب.")

def send_email(price):
    sender = os.getenv("EMAIL_USER")
    password = os.getenv("EMAIL_PASS")
    receiver = os.getenv("RECEIVER_EMAIL")

    subject = "📈 تحديث سعر الذهب اليومي"
    body = f"سعر الذهب اليوم هو: {price} دولار أمريكي للأونصة (XAU)."

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = receiver

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender, password)
        server.send_message(msg)

if __name__ == "__main__":
    try:
        price = get_gold_price()
        send_email(price)
        print("✅ تم إرسال سعر الذهب على الإيميل.")
    except Exception as e:
        print("حدث خطأ:", e)
