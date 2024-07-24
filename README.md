# portfolio_flask_app

use of gitglore
how the directories look like
states redux states



Understanding APIs and Frameworks:

API Overview:

    REST API:
        REST APIs are stateless, meaning they do not store session data (like cookies) from previous requests.
        They are lightweight and resolve issues efficiently by adhering to REST principles.

Frameworks:

    Flask:
        Usage: Often used for small systems where you can define your own file structure.
        Nature: Synchronous, meaning it processes one request at a time.
        Flexibility: Does not enforce a specific structure, making it easy to start but harder to scale for complex applications.
        Database: Commonly uses SQLAlchemy for database operations, drawing table schemas.
        Flask-RESTful: An extension for Flask that adds support for quickly building REST APIs. It carries the logic of the API routes.

    Django:
        Usage: Suitable for building complex systems.
        Nature: Supports both synchronous and asynchronous operations.
        Structure: Comes with a built-in structure and many pre-configured components, often referred to as "batteries included."

    FastAPI:
        Usage: Ideal for handling large datasets, machine learning, and data analysis due to its asynchronous I/O capabilities.
        Nature: Asynchronous, allowing it to handle multiple tasks concurrently.

Async vs. Sync:

    Asynchronous (Async): Can execute multiple tasks simultaneously, such as loading two pages at once.
    Synchronous (Sync): Executes one task at a time, such as loading one page before moving to the next.

Front-End Integration:

    JavaScript: Commonly used for front-end development.
    Dash: A front-end framework for visualization, often used with Flask for creating interactive web applications.

Building a CRUD Application with Flask:

    CRUD Operations:
        Create: Handled by POST requests.
        Read: Handled by GET requests.
        Update: Handled by PUT requests.
        Delete: Handled by DELETE requests.

    Route Definition:
        Each route in Flask corresponds to a method (GET, POST, PUT, DELETE) and a URL.

    Jinja2 Templating:
        Jinja2 allows mixing HTML with Python code, helping to render dynamic content in HTML templates. This is useful for displaying data from a database in the front-end.


Jinja2 and REST APIs serve different purposes in web development, and understanding their roles can help you use them effectively in your applications.
Jinja2 Templating:

Purpose:

    Jinja2 is a templating engine for Python. It allows you to mix HTML with Python code to create dynamic web pages.
    It's primarily used to render HTML pages with dynamic data on the server side before sending them to the client.

How It Works:

    You create HTML templates with placeholders for dynamic content.
    In your Flask route, you pass data to these templates using render_template.
    Jinja2 processes the templates, replacing placeholders with actual data, and generates the final HTML.
Summary:

    Jinja2 Templating: Used for rendering HTML with dynamic data on the server side. The output is a fully formed HTML page that gets sent to the client.
    REST API: Used for exposing your application’s data and functionality over HTTP. The output is typically JSON or XML data that clients can use to build their own interfaces.

When to Use:

    Jinja2: Use when you need to render HTML pages on the server with dynamic content, such as in a traditional web application.
    REST API: Use when you need to provide data and functionality to different types of clients (web, mobile, etc.) and allow them to interact with your application programmatically.