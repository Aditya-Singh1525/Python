#_________________________________________________________________________________________________________________#
class Stu_Details:
    stu_id = int(input("Please enter your six digit ID:"))
    converting_string = str(stu_id)
    no_of_digits = len(converting_string)
#_________________________________________________________________________________________________________________#
    if no_of_digits > 6:
        print('Invalid ID! Please give correct ID')
    else:    
        stu_name = input('Please enter your Full Name:')
        stu_rollno = int(input('Please enter your Rollno:'))
        stu_attempt = int(input('Please enter your Exam Attempt:'))
#_________________________________________________________________________________________________________________#
        print(f'''\nCheck your details:
Your ID:{stu_id}
Your Name:{stu_name}
Your Roll.no:{stu_rollno}
Your Attempt:{stu_attempt}
If any thing wrong please give the details again!\n''')
#_________________________________________________________________________________________________________________#
        if stu_attempt <= 5:
            print('Congrats! You came in top fifty and your details will be given to AIIMS Delhi or Madaras:)')
        else:
            print('Sorry! you have to give the exam again to get AIIMS Delhi or Madaras:(\n')
            print('You will get AIIMS Kolkata or AIIMS Mumbai.')
#_________________________________________________________________________________________________________________#
