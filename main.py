import openai
import smtplib
from email.mime.text import MIMEText

# إعداد OpenAI
openai.api_key = "YOUR_OPENAI_API_KEY"

def get_motivation():
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "Give me a short motivational quote."}]
    )
    return response.choices[0].message.content.strip()

def send_email(message):
    msg = MIMEText(message)
    msg["Subject"] = "🌟 Daily Motivation"
    msg["From"] = "YOUR_EMAIL@gmail.com"
    msg["To"] = "YOUR_EMAIL@gmail.com"

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login("YOUR_EMAIL@gmail.com", "YOUR_APP_PASSWORD")
        server.send_message(msg)

if __name__ == "__main__":
    quote = get_motivation()
    send_email(quote)
