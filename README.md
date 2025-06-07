# CSV Data Entry Pipeline 📝➡️📁

This project is a basic data pipeline built in Python that collects structured input from users and saves it to a CSV file using `pandas`.

## 🚀 What It Does

- Accepts user input for student details (name, roll number, age, address, phone, etc.)
- Organizes the data using a Python class and nested dictionaries
- Flattens complex nested data (like address)
- Saves everything to a clean, structured CSV file

## 🔧 Technologies Used

- Python
- Pandas
- json_normalize (for flattening)
- Basic OOP (Object-Oriented Programming)

## 📂 Example Fields Collected

- Roll number
- Name
- Age
- Address (house, street, city, pincode, state)
- Phone number

## 📈 Future Improvements

- Load CSV into MySQL (ETL: Load step)
- Add validation (for phone, pincode, etc.)
- Fetch data from APIs
- Automate daily/weekly runs
