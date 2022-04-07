"""
Name: {วาศิฏฐี ธีรภาพสถาพร}
SID: {364211760016}
Group: {MIT211}
"""

"""
Question 5:
เขียนโปรแกรมเพื่อคำนวณค่า Body Mass Index (BMI) โดยรับ input เป็นน้ำหนักตัวและส่วนสูง
จากนั้นแสดงผล BMI ทาง output ตามสมการต่อไปนี้
"""

w = int(input("น้ำหนัก(kg):"))
h = int(input("ส่วนสูง(cm):"))/100
bmi=w/h**2
print("ดัชนีมวลกายของคุณ เท่ากับ",bmi)

if bmi<30 and bmi>29.9:
  print("โรคอ้วน มีความเสี่ยง")
elif bmi<29.9 and bmi> 24.9:
  print("โรคอ้วน")
elif bmi<24.9 and bmi>22.9:
  print("น้ำหนักเกิน")
elif bmi<22.9 and bmi>18.5:
  print("สมส่วน")
else:
  print("ผอม")