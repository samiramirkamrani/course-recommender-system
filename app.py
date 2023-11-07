import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import *
import os

students = pd.read_excel(r'C:\Users\acer\Desktop\myrepo\data\students-performance.xlsx')
courses = pd.read_excel(r'C:\Users\acer\Desktop\myrepo\data\computer-chart.xlsx')

def get_passed_courses(student_id):
    passed_courses = students[(students['شماره دانشجویی'] == student_id) & (students['نمره'] >= 10)]['دروس']
    return passed_courses.tolist()

def get_passed_units(student_id):
    passed_courses = students[(students['شماره دانشجویی'] == student_id) & (students['نمره'] >= 10)]
    passed_units = passed_courses['واحد'].sum()
    return passed_units

def calculate_gpa(student_id):
    # Assuming 'students' is your DataFrame
    passed_courses = students[(students['شماره دانشجویی'] == student_id) & (students['نمره'] >= 10)]
    
    total_passed_units = passed_courses['واحد'].sum()
    total_weighted_grade = (passed_courses['واحد'] * passed_courses['نمره']).sum()
    
    if total_passed_units == 0:
         gpa = 0  # or any other default value you prefer
    else:
         gpa = total_weighted_grade / total_passed_units
        
    return gpa

def recommend_courses(student_id):
    passed_courses = get_passed_courses (student_id )
    gpa = calculate_gpa(student_id)
    recommended_courses = []
    num_eslami_courses = 0
    total_units = 0
    
    
    # Define unit limits based on GPA
    if gpa < 12:
        max_units = 14
        print("gpa < 12 ")
    elif 12 <= gpa < 17:
        max_units = 20
        print("12 <= gpa < 17 ")
    else:
        max_units = 24
        print("gpa >= 17 ")
        

    for _, course_row in courses.iterrows():
        course_name = course_row['نام درس']
        units = course_row['واحد']
        course_prerequisites = course_row['پیشنیاز'].split('-') if isinstance(course_row['پیشنیاز'], str) else []
        course_kind = course_row['نوع']

      # Condition 1: Course has not been passed
        if course_name not in passed_courses:
            # Condition 2: Student has passed the recommended course prerequisites
            if all(prereq in passed_courses for prereq in course_prerequisites):
                # Condition 3: Course and its prerequisites can't be recommended at the same time
                if not any(prereq in recommended_courses for prereq in course_prerequisites):
                    # Condition 4: Total units of recommended courses should not exceed 24
                    if total_units + units <= max_units:
                        # condition 5: there can be just one of "اسلامی" courses on each recommendation
                        if course_kind != "اسلامی" or num_eslami_courses == 0:
                            recommended_courses.append(course_name)
                            total_units += units
                            if course_kind == "اسلامی":
                                num_eslami_courses += 1

                        
    return recommended_courses


student_id = input("Enter the student ID: ")
student_id = int(student_id)
recommended_courses = recommend_courses(student_id)
print(f"Recommended courses for student {student_id}: {recommended_courses}")
