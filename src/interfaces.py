from abc import ABC, abstractmethod


class NotificationChannel(ABC):
    """Common interface for all notification channels."""

    @abstractmethod
    def send(self, recipient: str, message: str) -> bool:
        """Send a notification to a recipient."""
        pass