# SOLID Principles: Notification & Alert Dispatch Framework

A modular Python notification framework demonstrating clean object-oriented design and all five SOLID principles.

## Overview

This project provides an extensible notification dispatch engine supporting four channels:

- Email
- SMS
- Slack
- WhatsApp

The architecture uses a common notification interface and dependency injection, allowing new channels to be added without modifying the core notification service.

## Architecture

```text
                 main.py
                    |
                    v
          NotificationService
                    |
             NotificationChannel
              /    |    |    \
             v     v    v     v
          Email   SMS  Slack WhatsApp
```

## SOLID Principles

- **S — Single Responsibility Principle:** Each class has a focused responsibility.
- **O — Open/Closed Principle:** New channel implementations can be added without changing the core service.
- **L — Liskov Substitution Principle:** Every channel implementation follows the common interface contract.
- **I — Interface Segregation Principle:** The channel interface contains only the essential `send()` operation.
- **D — Dependency Inversion Principle:** The notification service depends on the `NotificationChannel` abstraction rather than concrete channel classes.

## Project Structure

```text
Notification-Alert-Dispatch-Framework/
├── main.py
├── README.md
├── .gitignore
├── src/
│   ├── __init__.py
│   ├── interfaces.py
│   ├── channels.py
│   ├── notification_service.py
│   └── exceptions.py
├── tests/
│   └── test_notifications.py
└── docs/
```

## Requirements

- Python 3.10 or later
- No external dependencies required

## Run the Demo

```bash
python main.py
```

## Run Tests

```bash
python -m unittest discover -s tests -v
```

## Current Features

- Four notification channel implementations
- Dependency injection
- Case-insensitive channel selection
- Unsupported-channel validation
- Automated unit tests
- Extensible, interface-based architecture

## Important Note

Email, SMS, Slack, and WhatsApp currently use simulated senders that print messages to the terminal. No real notifications are delivered. Production integrations would require the appropriate APIs, credentials, and delivery-error handling.

## Future Improvements

- Real provider integrations
- Retry and failure-handling policies
- Structured logging
- Configuration-based channel registration
- Delivery status tracking

## License

This project is available for educational and portfolio use.


## Architecture

The framework uses a common notification interface and dependency injection
to dispatch notifications through independent channel implementations.

```mermaid
flowchart TD
    A[main.py] --> B[NotificationService]
    B --> C[NotificationChannel Interface]
    C --> D[EmailChannel]
    C --> E[SMSChannel]
    C --> F[SlackChannel]
    C --> G[WhatsAppChannel]
    H[Unit Tests] -.-> B