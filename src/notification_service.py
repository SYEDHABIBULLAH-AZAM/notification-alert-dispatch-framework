
from src.interfaces import NotificationChannel
from src.exceptions import (
    ChannelNotFoundError,
    NotificationDeliveryError,
)


class NotificationService:
    """Dispatch notifications through injected channels."""

    def __init__(self, channels: dict[str, NotificationChannel]):
        self._channels = {
            name.lower(): channel for name, channel in channels.items()
        }

    def send_notification(
        self, channel_name: str, recipient: str, message: str
    ) -> bool:
        channel = self._channels.get(channel_name.lower())

        if channel is None:
            raise ChannelNotFoundError(
                f"Unsupported notification channel: {channel_name}"
            )

        try:
            success = channel.send(recipient, message)
        except Exception as error:
            raise NotificationDeliveryError(
                f"Delivery failed via {channel_name}: {error}"
            ) from error

        if not success:
            raise NotificationDeliveryError(
                f"Channel {channel_name} reported delivery failure."
            )

        return True
