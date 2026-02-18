```
# FlaskMasterBlog

![Flask](https://img.shields.io/badge/Framework-Flask-blue)
![Python](https://img.shields.io/badge/Python-3.10+-green)
![License](https://img.shields.io/badge/License-MIT-orange)
![Status](https://img.shields.io/badge/Status-Production-ready-brightgreen)

## Overview

**FlaskMasterBlog** یک وبلاگ حرفه‌ای و مدرن است که با Flask طراحی شده و شامل سیستم مدیریت کاربران، مقالات، دیدگاه‌ها و تولید PDF می‌باشد. مناسب برای وبلاگ شخصی یا آموزشی با قابلیت‌های پیشرفته و توسعه‌پذیر.

## Key Features

- ورود کاربران با **رمز عبور یا OTP ایمیلی**  
- پروفایل کاربری با تصویر اختصاصی  
- ایجاد، ویرایش و حذف مقالات  
- مدیریت دیدگاه‌ها و پاسخ‌ها  
- سیستم صفحه‌بندی (Pagination) برای لیست مقالات  
- تولید PDF از محتوا مقالات و ارائه به کاربران  
- امنیت فرم‌ها با **Google reCAPTCHA**  

## Project Structure

```
FlaskMasterBlog/
├── run.py
├── config.py
├── requirements.txt
└── app/
    ├── __init__.py
    ├── models.py
    ├── forms.py
    ├── routes.py
    ├── utils.py
    ├── static/
    │   └── generated_pdfs/
    └── templates/
        ├── base.html
        ├── home.html
        ├── register.html
        ├── login.html
        ├── verify.html
        ├── create_post.html
        ├── post.html
        └── edit_post.html
```

## Technologies Used

- **Python 3.10+**  
- **Flask 3.x**  
- **Flask-Login, Flask-Mail, Flask-WTF**  
- **SQLAlchemy**  
- **FPDF** برای تولید PDF  
- **Jinja2** برای قالب‌بندی HTML  

## Contribution

این پروژه باز و قابل توسعه است. برای مشارکت:  
1. Fork کنید  
2. Branch جدید بسازید  
3. تغییرات را Commit و Push کنید  
4. Pull request بسازید  

## License

این پروژه تحت **MIT License** منتشر شده است.
```
