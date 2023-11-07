# course-recommender-system
The Course Recommender System aims to assist computer science students in making informed decisions during their course enrollments. The system leverages a rule-based algorithm to ensure students receive tailored recommendations based on their academic performance and program requirements.

## Dataset Description:

Student Performance and Grades Dataset:

Contains information on students' academic performance, including student ID, semester, courses taken, corresponding units, and grades received.
Computer Chart Dataset:

Provides details on computer science courses, including course names, units, prerequisites, and their respective categories.
Recommendation Algorithm:
The system employs a rule-based algorithm to generate course recommendations. This approach ensures that the recommendations adhere to specific conditions and constraints defined for each student.

## Recommendation Conditions:

The course must not have been previously passed by the student.
All prerequisites for the recommended course must be successfully completed.
A course and its prerequisites cannot be recommended simultaneously.
The maximum number of recommended units is determined based on the student's GPA.
Only one "اسلامی" course is allowed in each recommendation.
