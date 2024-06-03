# class Student:
    
#     def study(self,course_name):
#         print(f"学习{course_name}")
        
#     def play():
#         print(f"学习学个*")
        
# s1 =  Student()
# s2 = Student()

# print(s1, s2)


# import time

# class Clock:
#     def __init__(self, hours = 23, mins = 59, second = 59):
#         self.hours = hours
#         self.mins =  mins
#         self.second = second
        
#     def run(self):
#         time.sleep(1)
#         self.second+=1
#         if(self.second>=60):
#             self.second = 0
#             self.mins+=1
#             if(self.mins>=60):
#                 self.mins =0
#                 self.hours+=1
#                 if(self.hours>=24):
#                     self.hours =0
        
#     def show(self):
#         print(f"{str(self.hours).rjust(2, '0')}: {str(self.mins).rjust(2, '0')}: {str(self.second).rjust(2, '0')}")
#         self.run()
        
# clk = Clock()
# while True:
#     clk.show()


import operator
from typing import List
import pandas as pd

# def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
#     return  pd.DataFrame(student_data, columns=['student_id, age'])

# def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
#     arr = []
#     for stu in student_data:
#         arr += stu

#     return  pd.DataFrame(data={"student_id":arr[0::2], "age": arr[1::2]})

# def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
#     arr = sum(student_data, [])

#     return  pd.DataFrame(data={"student_id":arr[0::2], "age": arr[1::2]})

# def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
#     arr = [i for arr in student_data for i in arr]

#     return  pd.DataFrame(data={"student_id":arr[0::2], "age": arr[1::2]})

import functools 

student_data =[[1,15],[2,11],[3,11],[4,20]]

print(functools.reduce(operator.add,student_data))