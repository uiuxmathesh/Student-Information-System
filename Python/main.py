from model import *


def main():


    while True:
        option = int(
            input(
    """
    ======MAIN MENU======
    1. Student Menu
    2. Course Menu
    3. Teacher's Menu
    4. Enrollments Menu
    5. Payments Menu
    6. Exit
    =====================
    Please select a option to continue.... """))

        if option == 1:
            Student.studentMenu()
        elif option == 2:
            Course.courseMenu()
        elif option == 3:
            Teacher.teacherMenu()
        elif option == 4:
            Enrollment.enrollmentMenu()
        elif option == 5:
            Payment.paymentMenu()
        elif option == 6:
            break
        else:
            print("Not yet")


if __name__ == "__main__":
    main()

