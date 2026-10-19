# Hotel Management System

A simple Python CLI application for managing hotel rooms, bookings, checkouts, and revenue reporting.

## Description
This project demonstrates Object-Oriented Programming (OOP) principles in Python:
- Encapsulation: Room status is protected and controlled via methods.
- Inheritance: Standard Room (PhongThuong) and VIP Room (PhongVIP) inherit from base Room (Phong).
- Polymorphism: Different price calculation for standard and VIP rooms.
- File Handling: Data persistence using JSON format.
- Exception Handling: Preventing runtime crashes on invalid user input or missing files.

## Project Structure
- models.py: Contains data models (Phong, PhongThuong, PhongVIP, KhachHang, PhieuThue).
- services.py: Contains business logic and management class (QuanLyKhachSan).
- file_handler.py: Handles reading from and writing to khachsan_data.json.
- main.py: CLI menu and user interaction with error handling.

## Requirements
- Python 3.x

## How to Run
Run the main script:
```bash
python main.py
```
