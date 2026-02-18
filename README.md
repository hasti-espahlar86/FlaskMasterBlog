# FlaskMasterBlog 🚀

![Flask](https://img.shields.io/badge/Framework-Flask-blue)
![Python](https://img.shields.io/badge/Python-3.10+-green)
![License](https://img.shields.io/badge/License-MIT-orange)
![Status](https://img.shields.io/badge/Status-Production-ready-brightgreen)

## Overview 🌟

**FlaskMasterBlog** is a modern and professional blog built with **Flask**, featuring user management, posts, comments, and PDF generation. It is suitable for personal or educational blogs with advanced features and high scalability.

## Key Features ✨

- User login with **password or email OTP**  
- User profiles with avatar support  
- Create, edit, and delete posts  
- Manage comments and replies  
- Pagination for post listings  
- Generate PDFs from post content and provide them to users  
- Form security with **Google reCAPTCHA**  

## Project Structure 📂

FlaskMasterBlog/
- run.py  
- config.py  
- requirements.txt  
- app/  
  - __init__.py  
  - models.py  
  - forms.py  
  - routes.py  
  - utils.py  
  - static/  
    - generated_pdfs/  
  - templates/  
    - base.html  
    - home.html  
    - register.html  
    - login.html  
    - verify.html  
    - create_post.html  
    - post.html  
    - edit_post.html  

## Technologies Used 🛠️

- **Python 3.10+**  
- **Flask 3.x**  
- **Flask-Login, Flask-Mail, Flask-WTF**  
- **SQLAlchemy**  
- **FPDF** for PDF generation  
- **Jinja2** for HTML templating  

## Contribution 🤝

This project is open and extensible. To contribute:  
1. Fork the repository  
2. Create a new branch  
3. Commit and push your changes  
4. Open a Pull Request  

## License 📜

This project is licensed under the **MIT License**.
