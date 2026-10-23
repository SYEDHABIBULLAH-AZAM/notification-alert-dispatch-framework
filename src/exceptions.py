class NotificationError(Exception):
    """Base exception for notification framework errors."""


class ChannelNotFoundError(NotificationError):
    """Raised when a requested channel is unavailable."""


class NotificationDeliveryError(NotificationError):
    """Raised when notification delivery fails."""