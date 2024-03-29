import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from datetime import datetime
import requests
from email_credentials import email, password

smtp_port = 587
smtp_server = "smtp.gmail.com"

email_from = email
email_list = [ email]
pswd = password

subject = "New email is sent from the system"

def get_public_ip():
    try:
        response = requests.get('https://api64.ipify.org?format=json')
        public_ip_data = response.json()
        return public_ip_data.get('ip')
    except Exception as e:
        print(f"Error getting public IP address: {e}")
        return None

def get_location_from_ip(ip_address):
    try:
        response = requests.get(f'https://ipinfo.io/{ip_address}/json')
        location_data = response.json()

        city = location_data.get('city')
        region = location_data.get('region')
        country = location_data.get('country')

        if city and region and country:
            return f"Location based on IP: {city}, {region}, {country}"

    except Exception as e:
        print(f"Error getting location from IP: {e}")

    return None

def send_emails(email_list):
    for person in email_list:
        body = f"""
        The person tried to access your database {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}:
        """

        public_ip = get_public_ip()

        if public_ip:
            location_from_ip = get_location_from_ip(public_ip)

            if location_from_ip:
                body += f"\n\nIP Address: {public_ip}"
                body += f"\nLocation: {location_from_ip}"
            else:
                body += "\nNo location information available based on public IP."

        else:
            body += "\nError getting public IP address."

        picture_folder = "pictures of unauthorized persons"
        picture_files = [f for f in os.listdir(picture_folder) if f.endswith('.png')]

        latest_picture = max(picture_files, key=lambda x: os.path.getmtime(os.path.join(picture_folder, x)))

        msg = MIMEMultipart()
        msg["From"] = email_from
        msg["To"] = person
        msg["Subject"] = subject

        msg.attach(MIMEText(body, "plain"))

        file_path = os.path.join(picture_folder, latest_picture)
        attachment = open(file_path, 'rb')
        attachment_package = MIMEBase("application", 'octet-stream')
        attachment_package.set_payload(attachment.read())
        encoders.encode_base64(attachment_package)
        attachment_package.add_header('Content-Disposition', f"attachment; filename={latest_picture}")
        msg.attach(attachment_package)

        text = msg.as_string()

        print("Connecting with the server...")
        TIE_server = smtplib.SMTP(smtp_server, smtp_port)
        TIE_server.starttls()
        TIE_server.login(email_from, pswd)
        print("Successfully connected to the server")
        print()

        print(f"Sending email to: {person}....")
        TIE_server.sendmail(email_from, person, text)
        print(f"Email sent to: {person}")
        print()

        TIE_server.quit()

if __name__ == "__main__":
    send_emails(email_list)
