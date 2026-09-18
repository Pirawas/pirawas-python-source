try:
    Num1 = int(input("Enter first Number: "))
    Num2 = int(input("Enter second Number: "))
    signal = input(("Enter signal (+, - ,* , /): "))
    result = 0

    if signal == "+":
        result = Num1 + Num2
    elif signal == "-":
        result = Num1 - Num2
    elif signal == "*":
        result = Num1 * Num2
    elif signal == "/":
        result = Num1 / Num2
    else:
        raise ValueError("Enter Only signal + - * /")
    
    print(f"{Num1} {signal} {Num2} = {result}")

except ValueError: #กรณีผู้ใช้ไม่พิมพ์ตัวเลข
    print("Enter Only Number please")

except ZeroDivisionError: #กรณีผู้ใช้หารตัวเป็น 0 
    print("Can not Division by Zero")
except Exception: #กรณีอื่นๆ
    print("Something is Error but not sure")
else: #จะทำที่นี้ก็ต่อเมื่อไม่มีException
    print("Calculation Successful")
finally: #ทำเสมอไม่ว่าจะมี Exception เกิดขึ้นก็ตาม
    print("End")

