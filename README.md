
# Automobile Service Management System

![developer](https://img.shields.io/badge/Developed%20By%3A-Kartik%20Gupta-blue)

---

## Overview

The **Automobile Service Management System** is a comprehensive software solution designed to simplify and automate the management of automobile service centers. It provides robust features for managing customer interactions, service scheduling, technician allocation, inventory tracking, billing, and analytics. This system is user-friendly, secure, and highly customizable to meet the unique requirements of service centers.

---

## Key Features

### **Customer Management**

- Maintain a detailed database of customers, including contact details, vehicle information, and service history.
- Enable personalized customer experiences with streamlined access to customer information.

### **Service Requests**

- Handle service requests with detailed inputs like vehicle number, model, problem description, and preferred appointment times.
- Track the status of requests (Pending, Approved, Repairing, Completed, Released).

### **Technician Management**

- Manage a roster of technicians with details on skills, availability, and workload.
- Efficiently assign service requests to technicians based on their expertise and availability.

### **Inventory Management**

- Track spare parts, tools, and other items with real-time inventory monitoring.
- Automate stock reordering and generate purchase orders as needed.

### **Billing and Invoicing**

- Generate professional invoices with detailed breakdowns of services and costs.
- Simplify billing processes and minimize errors.

### **Reports and Analytics**

- Analyze service efficiency, customer satisfaction, and inventory usage through visualized reports.
- Make informed decisions to improve business operations.

### **User Roles and Permissions**

- Implement role-based access control for administrators, technicians, and customers.
- Enhance security and maintain data integrity.

---

## Technologies Used

- **Programming Languages**: Python, Java
- **Frameworks**: Django, Spring Boot
- **Database**: PostgreSQL, MySQL
- **Frontend**: HTML, CSS, JavaScript
- **Version Control**: Git
- **Hosting**: Localhost or server deployment via Django

---

## Screenshots

### Home Page

![Home Page](https://github.com/kartikgupta1503/vehicleservicemanagement/blob/master/static/screenshots/home.png?raw=true)

### Admin Dashboard (Dark Theme)

![Admin Dashboard Dark](https://github.com/kartikgupta1503/vehicleservicemanagement/blob/master/static/screenshots/admin_dark.png?raw=true)

### Admin Dashboard (Light Theme)

![Admin Dashboard Light](https://github.com/kartikgupta1503/vehicleservicemanagement/blob/master/static/screenshots/admin_light.png?raw=true)

### Mechanic Dashboard

![Mechanic Dashboard](https://github.com/kartikgupta1503/vehicleservicemanagement/blob/master/static/screenshots/mechanic_dashboard.png?raw=true)

### Customer Dashboard

![Customer Dashboard](https://github.com/kartikgupta1503/vehicleservicemanagement/blob/master/static/screenshots/customer_dashboard.png?raw=true)

---

## Usage Instructions

### Setting Up the Project

1. Install **Python 3.7.6** or later (ensure to check "Add to PATH" during installation).
2. Clone or download the project repository.
3. Navigate to the project folder in the terminal.
4. Install required packages:
   ```bash
   pip install django==3.0.5
   pip install django-widget-tweaks
   ```

### Running the Project

1. Perform database migrations:
   ```bash
   py manage.py makemigrations
   py manage.py migrate
   ```
2. Start the development server:
   ```bash
   py manage.py runserver
   ```
3. Open the following URL in your browser:
   ```
   http://127.0.0.1:8000/
   ```

### Creating an Admin User

1. Run the following command:
   ```bash
   py manage.py createsuperuser
   ```
2. Provide username, email, and password when prompted.

### Email Configuration for Contact Us Page

- Update the following lines in `settings.py` with your email credentials:
  ```python
  EMAIL_HOST_USER = 'youremail@gmail.com'
  EMAIL_HOST_PASSWORD = 'your-email-password'
  EMAIL_RECEIVING_USER = 'youremail@gmail.com'
  ```
- Enable less secure app access for Gmail:  
   [Enable Less Secure Apps](https://myaccount.google.com/lesssecureapps)

---

## Limitations

- User profile updates require a re-login due to username/password updates.

---

## License

This project is released under the [MIT License](https://opensource.org/licenses/MIT). Please refer to the LICENSE file for more details.

---

## Acknowledgments

Special thanks to the contributors and developers for their support and insights during the development of this project.

---

## Feedback

Suggestions and feedback are always welcome!  
You can connect with me via:

- [GitHub Profile](https://github.com/kartik2629)
- [LinkedIn Profile](https://www.linkedin.com/in/kartik-gupta-2b7b8a/)

---

Let me know if you want further adjustments! 🚀
