# Mabati Web Application
## Overview
The Mabati Web Application is an e-commerce platform designed to streamline the purchasing process for roofing sheets, gutters, accessories, and other related products. This application enables users to browse products, view detailed descriptions, and manage their shopping carts, while providing administrators with a robust dashboard to manage inventory, orders, and customer interactions.

## Features
### For Customers
- **Product Browsing:** View products by categories such as Roofing Sheets, Gutters, and Accessories.
- **Product Details:** View detailed descriptions of products, including specifications and images.
- **Shopping Cart:** Add items to the cart, update quantities, remove items, and view total cost.
- **User Dashboard:** Access order history, saved items, account settings, and manage personal information.
### For Administrators
- **Admin Dashboard:** Manage products, categories, orders, and customer messages.
- **Quick Stats:** View real-time data on total products, orders, registered users, and inquiries.
- **Product Upload:** Dynamically upload new products with images and categories.
- **Order Management:** Process and track customer orders efficiently.
## Technologies Used
- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, Bootstrap, JavaScript
- **Database:** MySQL
- **Deployment:** Apache
## Installation
### Prerequisites
- Python 3.8+
- MySQL database
- Virtual environment tool (venv or virtualenv)
- Django
### Steps
1. **Clone the Repository**
```
git clone https://github.com/mikemanuu/MabatiWebApp.git  
cd MabatiWebApp
``` 
2. **Set Up a Virtual Environment**
```
python -m venv env  
source env/bin/activate  # For Linux/Mac  
env\Scripts\activate     # For Windows  
```

3. **Install Dependencies**
```
pip install -r 
requirements.txt  
```
4. **Set Up the Database**
- Create a MySQL database (e.g., mabati).
- Update settings.py with your database credentials.
- 
5. **Run Migrations**
```
python manage.py makemigrations  
python manage.py migrate  
```
6. **Create Superuser**
```
python manage.py createsuperuser 
``` 
7. **Start the Server**
```
python manage.py runserver  
```
## Usage
### Customer Actions
- Navigate to the homepage to browse products.
- Add desired items to the cart and proceed to checkout.
- Log in or register to track orders and access personal settings.
### Admin Actions
- Log in to the Admin Dashboard.
- Manage inventory by uploading, editing, or removing products.
- View customer inquiries and process orders.
## Directory Structure
```
MabatiWebApp/  
├── mabatiapp/          
│   ├── models.py        
│   ├── views.py      
│   ├── urls.py         
├── templates/     
├── static/        
├── media/        
├── manage.py         
├── requirements.txt    
└── README.md          
```
## Contribution
Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License
This project is licensed under the MIT License.

## Author
This project was developed by:
**[Emmanuel Rotich]**
- **LinkedIn**:[Connect with me on LinkedIn](https://www.linkedin.com/in/rotich-emmanuel-14ba25188)
- **X(Twitter)**:[Follow me on X(Twitter)](https://www.x.com/mikemanuu)
- **GitHub**:[Visit my GitHub profile](https://github.com/mikemanuu)
- **Email**:[Email Me](mailto:mikemanuu273@gmail.com)]










