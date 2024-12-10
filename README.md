# Fresh Shop  
An E-Commerce web application built using Django where users can **register**, **log in**, view products (with pagination), add products to the **cart**, and proceed to **checkout**.  

---

## Features  
- **User Authentication**:  
   - Registration  
   - Login  
   - Session management  

- **Product Viewing**:  
   - View a list of products  
   - Pagination support for easy browsing  

- **Shopping Cart**:  
   - Add products to the cart  
   - View items in the cart  
   - Update or remove items  

- **Checkout**:  
   - View the final cart summary  
   - Proceed to checkout (without payment integration)  

---

## Technologies Used  
- **Backend**: Django (Python)  
- **Database**: MySQL
- **Frontend**: HTML, CSS, Bootstrap  
- **Tools**: Git, GitHub  

---

## Setup Instructions  

Follow these steps to set up the project locally:

### 1. Clone the Repository  
```bash
git clone https://github.com/Ashil7/FreshShop.git
cd FreshShop
```
### 2. Create virtual environment
```bash
python -m venv venv
```
### 3. Activate virtual environment
### For Windows:
```bash
venv\Scripts\activate
```
### 4. Configure MySQL Database
### 1. Create Database
```sql
CREATE DATABASE freshshop;
```
### 2. Update setting.py
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'freshshop',       # Your database name
        'USER': 'root',            # Your MySQL username
        'PASSWORD': 'yourpassword',# Your MySQL password
        'HOST': 'localhost',       # Database host
        'PORT': '3306',            # Default MySQL port
    }
}

```
### 5. Install Dependencies
```bash
pip install -r requirements.txt
```
### 6. Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```
### 7. Run the Development Server
```bash
python manage.py runserver
```
Visit http://127.0.0.1:8000/ in your browser to access the application.
