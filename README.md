<div id="top">

<!-- HEADER STYLE: CLASSIC -->
<div align="left">


# BACKEND_SISTEMA_RESTAURANTE

<em>Transforming restaurant operations with seamless innovation</em>

<!-- BADGES -->
<img src="https://img.shields.io/github/last-commit/Erik-egam/backend_sistema_restaurante?style=flat&logo=git&logoColor=white&color=0080ff" alt="last-commit">
<img src="https://img.shields.io/github/languages/top/Erik-egam/backend_sistema_restaurante?style=flat&color=0080ff" alt="repo-top-language">
<img src="https://img.shields.io/github/languages/count/Erik-egam/backend_sistema_restaurante?style=flat&color=0080ff" alt="repo-language-count">

<em>Built with the tools and technologies:</em>

<img src="https://img.shields.io/badge/Markdown-000000.svg?style=flat&logo=Markdown&logoColor=white" alt="Markdown">
<img src="https://img.shields.io/badge/FastAPI-009688.svg?style=flat&logo=FastAPI&logoColor=white" alt="FastAPI">
<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white" alt="Python">

</div>
<br>

---

## Table of Contents

- [Overview](#overview)
- [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
    - [Usage](#usage)
    - [Testing](#testing)
- [Project Structure](#project-structure)
    - [Project Index](#project-index)

---

## Overview

backend_sistema_restaurante is a comprehensive backend solution built with FastAPI, designed to streamline restaurant operations through modular, scalable services. It integrates core functionalities such as user authentication, order management, and kitchen workflows, all supported by a secure and efficient MySQL database connection.

**Why backend_sistema_restaurante?**

This project aims to provide a robust foundation for restaurant management systems. The core features include:

- 🛠️ **Modular Architecture:** Supports scalable and maintainable development with clearly separated modules.
- 🔑 **Secure Authentication:** Implements JWT-based login and user validation for protected access.
- 🍽️ **Order & Kitchen Workflows:** Facilitates real-time order creation, status updates, and kitchen order management.
- 🧱 **Data Models:** Defines consistent schemas for users, dishes, and orders to ensure data integrity.
- 🌐 **Environment Configuration:** Uses environment variables for secure secrets and flexible deployment.
- ⚙️ **Database Pooling:** Ensures efficient, reliable database interactions with centralized connection management.

---

## Project Structure

```sh
└── backend_sistema_restaurante/
    ├── README.md
    ├── config
    │   ├── constants.py
    │   └── dbconfig.py
    ├── logic
    │   ├── inserts.sql
    │   ├── logica_cocina.py
    │   ├── logica_mesero.py
    │   └── logica_usuario.py
    ├── main.py
    ├── models
    │   ├── orden.py
    │   ├── plato.py
    │   └── usuario.py
    ├── requirements.txt
    └── routes
        ├── cocina.py
        ├── jwt_auth_users.py
        └── mesero.py
```

---

### Project Index

<details open>
	<summary><b><code>BACKEND_SISTEMA_RESTAURANTE/</code></b></summary>
	<!-- __root__ Submodule -->
	<details>
		<summary><b>__root__</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ __root__</b></code>
			<table style='width: 100%; border-collapse: collapse;'>
			<thead>
				<tr style='background-color: #f8f9fa;'>
					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
					<th style='text-align: left; padding: 8px;'>Summary</th>
				</tr>
			</thead>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Erik-egam/backend_sistema_restaurante/blob/master/README.md'>README.md</a></b></td>
					<td style='padding: 8px;'>- Provides an overview of the project’s architecture and core components, illustrating how different modules interact to deliver the applications primary functionalities<br>- Serves as a guide for understanding the overall structure, enabling developers to navigate, extend, and maintain the system effectively within the broader codebase.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Erik-egam/backend_sistema_restaurante/blob/master/main.py'>main.py</a></b></td>
					<td style='padding: 8px;'>- Establishes the core FastAPI application, integrating essential route modules for user authentication, waiter, and kitchen functionalities<br>- Configures CORS middleware to enable cross-origin requests, facilitating seamless communication between frontend clients and backend services<br>- Serves as the central entry point that orchestrates routing and middleware setup, supporting the overall architecture of a modular, scalable restaurant management system.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Erik-egam/backend_sistema_restaurante/blob/master/requirements.txt'>requirements.txt</a></b></td>
					<td style='padding: 8px;'>- Defines project dependencies essential for building a secure, scalable FastAPI application with MySQL integration<br>- Ensures the environment includes web framework capabilities, database connectivity, environment variable management, cryptographic functions, and password hashing, supporting robust API development and secure user authentication within the overall architecture.</td>
				</tr>
			</table>
		</blockquote>
	</details>
	<!-- logic Submodule -->
	<details>
		<summary><b>logic</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ logic</b></code>
			<table style='width: 100%; border-collapse: collapse;'>
			<thead>
				<tr style='background-color: #f8f9fa;'>
					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
					<th style='text-align: left; padding: 8px;'>Summary</th>
				</tr>
			</thead>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Erik-egam/backend_sistema_restaurante/blob/master/logic/logica_cocina.py'>logica_cocina.py</a></b></td>
					<td style='padding: 8px;'>- Manages kitchen order workflows by updating order statuses to prepared and retrieving pending orders with their associated dishes for a specific location<br>- Facilitates real-time kitchen operations, ensuring accurate order tracking and efficient preparation within the overall system architecture.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Erik-egam/backend_sistema_restaurante/blob/master/logic/logica_mesero.py'>logica_mesero.py</a></b></td>
					<td style='padding: 8px;'>- Facilitates the creation of new orders within the restaurant system by associating session data with ordered dishes, ensuring accurate order recording and status management<br>- Integrates seamlessly into the overall architecture to support real-time order processing, session handling, and kitchen preparation workflows, thereby enabling efficient restaurant operations and customer service.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Erik-egam/backend_sistema_restaurante/blob/master/logic/inserts.sql'>inserts.sql</a></b></td>
					<td style='padding: 8px;'>- Establishes initial data for a restaurant management system, including roles, locations, users, sessions, menu items, and orders<br>- Facilitates testing and development by providing sample entries that support core functionalities such as user management, menu operations, and order processing within the overall architecture<br>- Ensures a consistent baseline for database interactions and application workflows.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Erik-egam/backend_sistema_restaurante/blob/master/logic/logica_usuario.py'>logica_usuario.py</a></b></td>
					<td style='padding: 8px;'>- Provides core logic for retrieving user information from the database based on identification number, integrating role data<br>- Facilitates user data access within the overall system architecture, supporting authentication, authorization, and user management functionalities<br>- Ensures seamless data retrieval while handling errors and resource management, contributing to the applications user-related operations.</td>
				</tr>
			</table>
		</blockquote>
	</details>
	<!-- config Submodule -->
	<details>
		<summary><b>config</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ config</b></code>
			<table style='width: 100%; border-collapse: collapse;'>
			<thead>
				<tr style='background-color: #f8f9fa;'>
					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
					<th style='text-align: left; padding: 8px;'>Summary</th>
				</tr>
			</thead>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Erik-egam/backend_sistema_restaurante/blob/master/config/dbconfig.py'>dbconfig.py</a></b></td>
					<td style='padding: 8px;'>- Establishes a centralized database connection pool for the application, enabling efficient and scalable access to the MySQL database<br>- Facilitates resource management and connection reuse across the codebase, supporting reliable data operations within the restaurant management system<br>- This configuration ensures consistent database connectivity, optimizing performance and simplifying connection handling throughout the project.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Erik-egam/backend_sistema_restaurante/blob/master/config/constants.py'>constants.py</a></b></td>
					<td style='padding: 8px;'>- Defines essential configuration constants by loading environment variables, including security secrets, token expiration durations, and cryptographic algorithms<br>- These constants serve as foundational parameters for authentication and security mechanisms across the application, ensuring consistent and secure handling of sensitive information throughout the codebase.</td>
				</tr>
			</table>
		</blockquote>
	</details>
	<!-- models Submodule -->
	<details>
		<summary><b>models</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ models</b></code>
			<table style='width: 100%; border-collapse: collapse;'>
			<thead>
				<tr style='background-color: #f8f9fa;'>
					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
					<th style='text-align: left; padding: 8px;'>Summary</th>
				</tr>
			</thead>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Erik-egam/backend_sistema_restaurante/blob/master/models/plato.py'>plato.py</a></b></td>
					<td style='padding: 8px;'>- Defines the data model for a menu item within the application, encapsulating essential attributes such as identifier, name, description, image, and price<br>- Serves as a foundational schema for validating and managing dish data across the system, supporting consistent data handling and integration within the broader architecture of the project.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Erik-egam/backend_sistema_restaurante/blob/master/models/usuario.py'>usuario.py</a></b></td>
					<td style='padding: 8px;'>- Defines user data models for the application, facilitating structured representation of user information and database interactions<br>- The models ensure data validation and consistency across the system, supporting user management functionalities such as registration, authentication, and role assignment within the overall architecture.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Erik-egam/backend_sistema_restaurante/blob/master/models/orden.py'>orden.py</a></b></td>
					<td style='padding: 8px;'>- Defines data models for restaurant order management, encapsulating order details and associated dishes<br>- Facilitates structured data validation and serialization within the application, supporting seamless handling of order creation, updates, and processing workflows in the overall system architecture<br>- Ensures consistent data representation for orders and their components across different modules.</td>
				</tr>
			</table>
		</blockquote>
	</details>
	<!-- routes Submodule -->
	<details>
		<summary><b>routes</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ routes</b></code>
			<table style='width: 100%; border-collapse: collapse;'>
			<thead>
				<tr style='background-color: #f8f9fa;'>
					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
					<th style='text-align: left; padding: 8px;'>Summary</th>
				</tr>
			</thead>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Erik-egam/backend_sistema_restaurante/blob/master/routes/mesero.py'>mesero.py</a></b></td>
					<td style='padding: 8px;'>- Facilitates order creation for waiters within the system, ensuring proper authorization and input validation<br>- Integrates with backend logic to record new orders associated with specific locations, supporting the overall architecture of order management and role-based access control in the application<br>- Enhances operational workflows by streamlining order submission processes for authorized personnel.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Erik-egam/backend_sistema_restaurante/blob/master/routes/cocina.py'>cocina.py</a></b></td>
					<td style='padding: 8px;'>- Defines API endpoints for kitchen staff to manage and update order statuses within the application<br>- Facilitates marking orders as prepared and retrieving pending orders for specific locations, ensuring only authorized kitchen personnel can perform these actions<br>- Integrates with core logic to maintain order workflow and supports seamless communication between the user interface and backend processes.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Erik-egam/backend_sistema_restaurante/blob/master/routes/jwt_auth_users.py'>jwt_auth_users.py</a></b></td>
					<td style='padding: 8px;'>- Implements JWT-based authentication endpoints to manage user login, token issuance, and user validation within the application<br>- Facilitates secure access control by verifying user credentials, generating access tokens, and retrieving authenticated user details, thereby supporting the overall security architecture of the system.</td>
				</tr>
			</table>
		</blockquote>
	</details>
</details>

---

## Getting Started

### Prerequisites

This project requires the following dependencies:

- **Programming Language:** Python
- **Package Manager:** Pip

### Installation

Build backend_sistema_restaurante from the source and install dependencies:

1. **Clone the repository:**

    ```sh
    ❯ git clone https://github.com/Erik-egam/backend_sistema_restaurante
    ```

2. **Navigate to the project directory:**

    ```sh
    ❯ cd backend_sistema_restaurante
    ```

3. **Install the dependencies:**

**Using [pip](https://pypi.org/project/pip/):**

```sh
❯ pip install -r requirements.txt
```

### Usage

Run the project with:

**Using [pip](https://pypi.org/project/pip/):**

```sh
python {entrypoint}
```

### Testing

Backend_sistema_restaurante uses the {__test_framework__} test framework. Run the test suite with:

**Using [pip](https://pypi.org/project/pip/):**

```sh
pytest
```

---

<div align="left"><a href="#top">⬆ Return</a></div>

---
