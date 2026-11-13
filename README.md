🎓 Grade Manager
A simple Streamlit-based Grade Manager application that allows users to add student names and marks, automatically assign grades, and view class statistics.
Features
- Add student records with a student name and mark.
- Validate that the student name is not empty.
- Automatically calculate a grade based on the mark.
- Display all student records.
- Show class statistics:
  - Average mark
  - Highest mark
  - Lowest mark
- Clear all student records with one button.
- Store records in Streamlit session state while the app session is active.
Grade Criteria
Mark Range	Grade
90–100	A
80–89	B
70–79	C
60–69	D
0–59	F


Requirements
- Python 3.8 or later
- Streamlit
Installation
1. Make sure Python is installed.
2. Open a terminal in the project folder.
3. (Optional) Create and activate a virtual environment.
   Windows:
   python -m venv venv
   venv\Scripts\activate
   macOS / Linux:
   python3 -m venv venv
   source venv/bin/activate
4. Install Streamlit:
   pip install streamlit
Run the Application
Save the Python code in a file named app.py, then run:
streamlit run app.py
Streamlit will provide a local URL in the terminal (usually http://localhost:8501). Open that URL in your web browser.
How to Use
1. Open the Grade Manager application.
2. Enter a student's name.
3. Enter a mark between 0 and 100.
4. Click Add Student.
5. The student record and automatically assigned grade will appear.
6. Add more students to update the class statistics.
7. Click Clear All Students to remove all records from the current session.
Project Structure
grade-manager/
├── app.py
└── README.md
How It Works
- Session state: st.session_state.students stores the student records while the Streamlit session is active.
- Grade calculation: The get_grade(mark) function returns a grade based on the ranges listed above.
- Statistics: The app calculates the average, highest, and lowest marks from the students currently stored in session state.
- Clear records: The Clear All Students button empties the list and reruns the app.
Data Storage Note
This application stores student records in Streamlit session state only. Records are not saved to a database or file, so they may be lost when the session ends or the app is restarted.
Possible Improvements
- Save student records to CSV or a database.
- Add options to edit or delete individual student records.
- Prevent duplicate student entries.
- Add charts to visualize grade distribution.
- Add student search and filtering.
License
This project is provided for learning and demonstration purposes. Add a license if you plan to distribute or reuse it publicly.
