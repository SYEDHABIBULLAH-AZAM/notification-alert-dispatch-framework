import unittest

from src.exceptions import ChannelNotFoundError
from src.channels import (
    EmailChannel,
    SMSChannel,
    SlackChannel,
    WhatsAppChannel,
)
from src.notification_service import NotificationService


class TestNotificationService(unittest.TestCase):

    def setUp(self):
        channels = {
            "email": EmailChannel(),
            "sms": SMSChannel(),
            "slack": SlackChannel(),
            "whatsapp": WhatsAppChannel(),
        }
        self.service = NotificationService(channels)

    def test_email_notification(self):
        self.assertTrue(
            self.service.send_notification(
                "email", "habib@example.com", "Test email"
            )
        )

    def test_sms_notification(self):
        self.assertTrue(
            self.service.send_notification(
                "sms", "+911234567890", "Test SMS"
            )
        )

    def test_slack_notification(self):
        self.assertTrue(
            self.service.send_notification("slack", "#alerts", "Test alert")
        )

    def test_whatsapp_notification(self):
        self.assertTrue(
            self.service.send_notification(
                "whatsapp", "+911234567890", "Test WhatsApp"
            )
        )

    def test_unknown_channel(self):
        with self.assertRaises(ChannelNotFoundError):
            self.service.send_notification("telegram", "user", "Test")

    def test_case_insensitive_channel(self):
        self.assertTrue(
            self.service.send_notification(
                "EMAIL", "habib@example.com", "Hello"
            )
        )


if __name__ == "__main__":
    unittest.main()