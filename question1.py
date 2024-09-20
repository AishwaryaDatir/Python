marks= int(input("Enter the marks in percentage"))
if marks <= 100:
    print("You got",marks)

if marks >=100:
    raise Exception("InvalidMarksException:Marks must be from 0 to 100")


