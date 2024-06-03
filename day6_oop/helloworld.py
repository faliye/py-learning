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



