🚀 MIS Performance Analysis System

A simple Flask-based web application that helps manage company financial data and analyze performance using calculated MIS scores.

📌 Project Description

This project allows users to enter financial details of a company like R&D, Admin, Marketing, and Profit.
Based on this data, the system automatically calculates:

Total Expenses
Revenue
Profit Percentage
MIS Score

Finally, it classifies the company into:

High Performer
Stable Growth
Under Observation

This makes it easy to understand a company’s financial health in a simple and smart way.

✨ Features
Add company financial data
Automatic calculations (Revenue, Expenses, Profit %)
MIS Score generation
Performance classification
API support (/api/data)
Delete company records
🛠️ Technologies Used
Python (Flask)
SQLite Database
HTML Templates
🧠 MIS Logic (Simple)

The system calculates score using:

Score = (profit_percent × 1.5) + ((100 - expense_ratio) × 0.8)

Higher score = better performance ✅

🎓 What I Learned (Coursera Integration)

This project is built using concepts learned from Coursera courses.

💻 From DevOps & Software Engineering:
How to build web apps using Flask
Git & GitHub for project management
Writing clean and structured code
Understanding real-world development process
🤖 From AI & Generative AI:
Basics of Artificial Intelligence
Data analysis and logic building
Thinking in a data-driven way
📊 From Data Science:
Working with data
Performing calculations
Understanding performance metrics

👉 I applied all these learnings to build this real-world project.

⚙️ How to Run
python app.py

Open in browser:

http://localhost:5095
📡 API
GET /api/data

Returns all company performance data in JSON format.

📂 Project Structure
app.py
mis.db
requirements.txt
templates/
👩‍💻 Author

Priyanshi Tiwari
