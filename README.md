# Novatide Labs CMS Backend

Welcome to the CMS backend repository for **Novatide Labs**. This platform is designed to serve as a dynamic content administrator for our static websites. It provides a robust, scalable, and maintainable backend leveraging modern best practices in Python, Flask, and PostgreSQL.

## Overview

The CMS Backend handles:

- User and admin account management
- Session and authentication (for admins)
- Content creation and editing (articles, images, tags, categories)
- Association of content with multiple static websites
- Management of subscribers and related website entities

By separating the backend (business logic, data access, and API endpoints) from the static frontend, we enable flexible content delivery to multiple web properties, ensuring a consistent and secure interface to our data.

## Key Features

- **Clean Architecture**:

  - **Models**: SQLAlchemy-based models represent database tables, split into dedicated files for maintainability.
  - **Services**: Encapsulate business logic and database operations separately from route handlers.
  - **Routes**: Flask Blueprints provide a clear separation of API endpoints by domain.

- **Database & Migrations**:

  - **PostgreSQL** as the relational database for robust and scalable data storage.
  - **Alembic** for schema migrations, enabling smooth database evolution over time.

- **Security & Authentication**:

  - Secure password hashing and role-based admin management.
  - Session handling and token-based API authentication for secure endpoint access.

- **Modularity & Extensibility**:
  - Pythonic best practices and PEP8 style conventions.
  - Environment-based configuration ensures seamless deployment across development, staging, and production environments.

## Technology Stack

- **Language**: Python 3.11+
- **Framework**: Flask
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy
- **Migrations**: Alembic
- **Environment Management**: `python-dotenv`
- **Dependency Management**: `requirements.txt` (pip)

## License

This project is proprietary to Novatide Labs. All rights reserved. For internal use only.

The Novatide Labs CMS Backend ensures a centralized, secure, and efficient platform to manage and deliver content to all of our static websites, adhering to industry-leading backend best practices.
