Mabati Web Application
Overview
The Mabati Web Application is an e-commerce platform designed to streamline the purchasing process for roofing sheets, gutters, accessories, and other related products. This application enables users to browse products, view detailed descriptions, and manage their shopping carts, while providing administrators with a robust dashboard to manage inventory, orders, and customer interactions.

Features
For Customers
Product Browsing: View products by categories such as Roofing Sheets, Gutters, and Accessories.
Product Details: View detailed descriptions of products, including specifications and images.
Shopping Cart: Add items to the cart, update quantities, remove items, and view total cost.
User Dashboard: Access order history, saved items, account settings, and manage personal information.
For Administrators
Admin Dashboard: Manage products, categories, orders, and customer messages.
Quick Stats: View real-time data on total products, orders, registered users, and inquiries.
Product Upload: Dynamically upload new products with images and categories.
Order Management: Process and track customer orders efficiently.
Technologies Used
Backend: Django (Python)
Frontend: HTML, CSS, Bootstrap, JavaScript
Database: MySQL
Deployment: Apache
Installation
Prerequisites
Python 3.8+
MySQL database
Virtual environment tool (venv or virtualenv)
Django
Steps
Clone the Repository

bash
Copy code
git clone https://github.com/yourusername/mabati-web-application.git  
cd mabati-web-application  
Set Up a Virtual Environment

bash
Copy code
python -m venv env  
source env/bin/activate  # For Linux/Mac  
env\Scripts\activate     # For Windows  
Install Dependencies

bash
Copy code
pip install -r requirements.txt  
Set Up the Database

Create a MySQL database (e.g., mabati).
Update settings.py with your database credentials.
Run Migrations

bash
Copy code
python manage.py makemigrations  
python manage.py migrate  
Create Superuser

bash
Copy code
python manage.py createsuperuser  
Start the Server

bash
Copy code
python manage.py runserver  
Usage
Customer Actions
Navigate to the homepage to browse products.
Add desired items to the cart and proceed to checkout.
Log in or register to track orders and access personal settings.
Admin Actions
Log in to the Admin Dashboard.
Manage inventory by uploading, editing, or removing products.
View customer inquiries and process orders.
Directory Structure
plaintext
Copy code
mabati-web-application/  
├── mabatiapp/         # Main Django app  
│   ├── templates/     # HTML templates  
│   ├── static/        # CSS, JS, images  
│   ├── models.py      # Database models  
│   ├── views.py       # Business logic  
│   ├── urls.py        # URL configurations  
├── manage.py          # Django management script  
├── requirements.txt   # Python dependencies  
└── README.md          # Project documentation  
Contribution
Contributions are welcome! Please fork the repository and submit a pull request with your changes.

License
This project is licensed under the MIT License.

Author
LinkedIn:[]
X(Twitter):[]
Email:[mikemanuu273@gmail.com]











