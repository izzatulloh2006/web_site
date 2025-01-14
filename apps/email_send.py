import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(subject, message, to_email):
    # SMTP sozlamalari
    smtp_server = "smtp.example.com"  # SMTP serveringiz manzili
    smtp_port = 587  # SMTP porti (masalan, Gmail uchun 587)
    smtp_user = "fayzullaxojaevi@gmail.com"  # Elektron pochta manzilingiz
    smtp_password = "wnxzsnvulsuuhdms"  # Pochta parolingiz

    # Xabarni yaratish
    msg = MIMEMultipart()
    msg['From'] = smtp_user
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    # SMTP orqali xabarni yuborish
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_user, smtp_password)
        server.sendmail(smtp_user, to_email, msg.as_string())
        server.quit()
        return "Xabar muvaffaqiyatli yuborildi!"
    except Exception as e:
        return str(e)
