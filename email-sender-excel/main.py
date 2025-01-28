import pandas as pd
import smtplib
import os
import time
import traceback
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Configuration à modifier par l'utilisateur
CONFIG = {
    "EXCEL_PATH": "path/to/excel_file.xlsx",
    "EMAIL_COLUMN": "Email",
    "SMTP_SERVER": "smtp.mail.me.com",
    "SMTP_PORT": 587,
    "SENDER_EMAIL": "your_email@icloud.com",
    "APP_PASSWORD": "your_app_specific_password",
    "ATTACHMENT_PATH": "path/to/attachment.pdf",
    "EMAIL_SUBJECT": "Candidature professionnelle",
    "THROTTLE_DELAY": 5  # Secondes entre les envois
}

def load_recipients():
    """Charge la liste des destinataires depuis le fichier Excel"""
    df = pd.read_excel(CONFIG["EXCEL_PATH"])
    return df[CONFIG["EMAIL_COLUMN"]].dropna().unique().tolist()

def create_email(destinataire):
    """Crée le message email avec pièce jointe"""
    msg = MIMEMultipart()
    msg['From'] = CONFIG["SENDER_EMAIL"]
    msg['To'] = destinataire
    msg['Subject'] = CONFIG["EMAIL_SUBJECT"]
    
    message = """Madame, Monsieur,
    
    [Votre message personnalisé ici]
    
    Cordialement,
    [Votre Nom]"""
    
    msg.attach(MIMEText(message, 'plain'))
    
    if os.path.exists(CONFIG["ATTACHMENT_PATH"]):
        with open(CONFIG["ATTACHMENT_PATH"], "rb") as f:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(f.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 
                      f'attachment; filename="{os.path.basename(CONFIG["ATTACHMENT_PATH"])}"')
        msg.attach(part)
    
    return msg

def send_emails():
    """Lance le processus d'envoi des emails"""
    try:
        recipients = load_recipients()
        
        with smtplib.SMTP(CONFIG["SMTP_SERVER"], CONFIG["SMTP_PORT"]) as server:
            server.starttls()
            server.login(CONFIG["SENDER_EMAIL"], CONFIG["APP_PASSWORD"])
            
            for index, recipient in enumerate(recipients, 1):
                try:
                    msg = create_email(recipient)
                    server.sendmail(CONFIG["SENDER_EMAIL"], recipient, msg.as_string())
                    print(f"{index}/{len(recipients)} - Envoyé à {recipient}")
                    
                    if index % 5 == 0:
                        time.sleep(CONFIG["THROTTLE_DELAY"])
                        
                except Exception as e:
                    print(f"Erreur pour {recipient}: {str(e)}")
                    continue
                    
    except Exception as e:
        print(f"ERREUR GLOBALE : {str(e)}")
        print(traceback.format_exc())

if __name__ == "__main__":
    send_emails()