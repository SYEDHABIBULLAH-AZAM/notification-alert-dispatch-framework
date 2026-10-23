from src.interfaces import NotificationChannel


class EmailChannel(NotificationChannel):
    def send(self, recipient: str, message: str) -> bool:
        print(f"[EMAIL] To: {recipient} | Message: {message}")
        return True


class SMSChannel(NotificationChannel):
    def send(self, recipient: str, message: str) -> bool:
        print(f"[SMS] To: {recipient} | Message: {message}")
        return True


class SlackChannel(NotificationChannel):
    def send(self, recipient: str, message: str) -> bool:
        print(f"[SLACK] Channel: {recipient} | Message: {message}")
        return True


class WhatsAppChannel(NotificationChannel):
    def send(self, recipient: str, message: str) -> bool:
        print(f"[WHATSAPP] To: {recipient} | Message: {message}")
        return True