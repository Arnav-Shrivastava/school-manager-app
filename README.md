# 🏫 School Management App [CLASS 12 PROJECT]

Welcome to Transcend, your all-in-one solution for school management! This Python Tkinter app simplifies tasks like adding faculty or students and scheduling timetables.

![tmain](https://github.com/user-attachments/assets/34c8dd74-37d7-4628-991b-9c1e4a367664)

## ✨ Features

- **Manage Faculty:** Easily add, edit, or remove faculty members.
- **Student Management:** Keep track of students, their information, and enrollment details.
- **Timetable Scheduler:** Plan and organize school timetables efficiently.
- **Intuitive GUI:** User-friendly interface designed with Tkinter for a smooth experience.
- **Admin Page:** An admin page to access all the features
- **Export as CSV TEXT BINARY:** Export Details as a CSV, binary or text file.

## 🛠️ Getting Started

### Prerequisites

- Ensure you have Python installed. If not, download it from [python.org](https://www.python.org/downloads/).
- Ensure you have MySql installed. If not, download it from [MySql](https://www.mysql.com/).

### 🚀 Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/transcend-app.git
    ```

2. Navigate to the project directory:

    ```bash
    cd transcend-app
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Create The Database:

   Create a table called timetable in MySQL and create the following tables

   FACULTY
   ```bash
   CREATE TABLE FACULTY(
    FID int PRIMARY KEY,
    PASSWORD varchar(50),
    NAME varchar(50),
    INITIAL varchar(50),
    EMAIL varchar (50),
    SUBCODE1 varchar (50),
    SUBCODE2 varchar (50));
   ```
   SCHEDULE
   ```bash
   CREATE TABLE SCHEDULE(
    ID varchar(5) PRIMARY KEY,
    DAYID int,
    PERIODID int,
    SUBCODE varchar(50),
    SECTION varchar(50),
    INITIAL varchar(50));
   ```
   STUDENT
   ```bash
   CREATE TABLE STUDENT(
    ADMISSION_ID int PRIMARY KEY,
    PASSWORD varchar(50),
    NAME varchar(50),
    ROLL int,
    SECTION varchar(50));
   ```
   SUBJECT
   ```bash
    CREATE TABLE SUBJECT(
    SUBCODE varchar(50) PRIMARY KEY,
    SUBNAME varchar(50),
    SUBTYPE varchar(50));
   ```

### 🎮 Usage

Run the app using:

```bash
python main.py
```

Exported files are saved in:
```bash
Export Folder
```
Login Details:
```bash
Student: username=ADMISSION_ID
         password=INTEGER VALUE

Faculty: username=FID
         password=INTEGER VALUE

Admin: username=admin
       password=admin
```

Working Project:

![tmain](https://github.com/user-attachments/assets/34c8dd74-37d7-4628-991b-9c1e4a367664)
![44](https://github.com/user-attachments/assets/b8201c1f-6899-4de4-8455-0f12af1f0a22)
![22](https://github.com/user-attachments/assets/fd1abb39-746a-4f18-af50-f80fb39b2b0b)
![33](https://github.com/user-attachments/assets/12b71cd4-8ae8-4983-b4ed-6c9b8358ae09)
![11](https://github.com/user-attachments/assets/06133aa9-2f0f-42c3-96c7-10954ef3f3f0)



