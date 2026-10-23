from src.channels import (
    EmailChannel,
    SMSChannel,
    SlackChannel,
    WhatsAppChannel,
)
from src.notification_service import NotificationService


def main():
    channels = {
        "email": EmailChannel(),
        "sms": SMSChannel(),
        "slack": SlackChannel(),
        "whatsapp": WhatsAppChannel(),
    }

    notification_service = NotificationService(channels)

    print("=" * 55)
    print("   NOTIFICATION & ALERT DISPATCH FRAMEWORK")
    print("=" * 55)

    notifications = [
        ("email", "habib@example.com", "Welcome to our platform!"),
        ("sms", "+911234567890", "Your OTP is 123456."),
        ("slack", "#security-alerts", "New security alert detected."),
        ("whatsapp", "+911234567890", "Your notification is ready."),
    ]

    for channel, recipient, message in notifications:
        try:
            notification_service.send_notification(
                channel, recipient, message
            )
            print(f"Status: SUCCESS | Channel: {channel.upper()}\n")
        except Exception as error:
            print(f"Status: FAILED | Error: {error}\n")

    print("=" * 55)
    print("Demo completed. No real messages were sent.")
    print("=" * 55)


if __name__ == "__main__":
    main()