import re
import time
import requests

class MailpitAPI:
    BASE_URL = "http://178.128.114.165:7040/api/v1/messages"

    @classmethod
    def get_latest_otp(cls, email):
        time.sleep(2)
        response = requests.get(cls.BASE_URL)
        data = response.json()
        messages = data.get("messages", [])

        for msg in messages:
            # Extract list of recipient email addresses
            to_addresses = [to.get("Address", "") for to in msg.get("To", [])]

            # Check if target email is among recipients
            if email in to_addresses:
                snippet = msg.get("Snippet", "")
                otp_match = re.search(r'\b\d{6}\b', snippet)
                if otp_match:
                    return otp_match.group(0)
        return None
