
from collections import deque

bookings_stack = []
lesson_queue = deque()


Available_lectures = ['1.TEACHER ADOLPHE', '2.TEACHER BERNARD', '3.TEACHER MARY', '4.TEACHER PATRICK','5.TEACHER EVODE']
Available_lessons = ['1.SYSTEM ENGINEERING','2.DSA','3.BUSINESS FUNCTION','4.ESP','5.DATABASE TECHNOLOGY']

def print_tutors():
    print("\nAvailable Tutors:\n")
    for tutor in Available_lectures:
          print(f'\t{tutor}')
 
def add_booking(session_info):
    bookings_stack.append(session_info)

def undo_booking():
    if bookings_stack:
        removed_booking = bookings_stack.pop()
        print(f"\n\t The undoing booking of session for {removed_booking} is successful.")
    else:
        print("\n\t No bookings available to undo!.")

def print_bookings():
    if bookings_stack:

        print("\nCurrent Bookings:")
        for bookings in bookings_stack:
           print(f'\tbookings')  
       
    else:
        print("\n\t Sorry!!, No bookings available.")

def schedule_lesson(lesson_info):
    lesson_queue.append(lesson_info)

def undo_scheduled_lesson():
    if lesson_queue:
        removed_schedule = lesson_queue.popleft()
        print(f'The schedule for lesson {removed_schedule} is successfully cancelled.')
    else:
        print(f'\nSorry!!, no schedules available to undo!!')
        

def print_scheduled_lessons():
    if lesson_queue:
        print("\nScheduled Lessons:")
        for lessons in lesson_queue:
             print(lessons)
        else:
         print("\nNo lessons scheduled.")

def ONLINE_TUTORING_SYSTEM():
    while True:
        print("\n\tWELCOME TO ONLINE TUTORING SYSTEM")
        print("\t ----------------------------------\n")
        print("\t1. View Available Tutors")
        print("\t2. Booking a Session")
        print("\t3. Undo Last Booked session")
        print("\t4. View Current Bookings")
        print("\t5. Schedule a Lesson")
        print("\t6. Undo last Scheduled Lesson")
        print("\t7. View Scheduled Lessons")
        print("\t8. Exiting the system")

        choice = int(input("\nEnter your choice: "))
        if choice == 1:
            print_tutors()

        elif choice == 2:
            print('AVAILABLE LESSONS\n')
            for courses in Available_lessons:
                print(f'\t{courses}')
            name =input('Enter your Name: ')
            session_info = input("Enter The name of lesson (Select only lesson on the list): ").upper()
            if session_info == 'SYSTEM ENGINEERING':
               print(f'{name} Booked {session_info} To be tought by TEACHER ADOLPHE')
            elif session_info == 'DSA':
                print(f'{name} Booked {session_info} To be tought by TEACHER BERNARD')
            
            elif session_info == 'BUSINESS FUNCTION':
                print(f'{name} Booked {session_info} To be tought by TEACHER MARY')
            
            elif session_info == 'ESP':
                print(f'{name} Booked {session_info} To be tought by TEACHER PATRICK')
            
            elif session_info == 'DATABASE TECHNOLOGY':
                print(f'{name} Booked {session_info} To be tought by TEACHER EVODE')
            else:
                print(f'\n\tIncorect choice, please try Again\n')
            
            add_booking(session_info)

        elif choice == 3:
            undo_booking()

        elif choice == 4:
            print_bookings()

        elif choice == 5:
            schedules=['SYSTEM ENGINEERING AT 8:00AM-10:00AM','DSA AT 10:00AM-12:00AM','BUSINESS FUNCTION 12:30PM-2:00PM','ESP AT 2:30PM-3:30PM',
                       'DATABASAE TECHNOLOGY AT 4:00PM-5:00PM']
            print(f'\nLESSON SCHEDULES:')
            for schedule in schedules:
                print(f'\t {schedule}')
            lesson_info = input('Enter the lesson schedule as indicated: ').upper()
            if lesson_info in schedules:
                print(f'\n\t Your schedule for {lesson_info} is successful!!')
            else:
                print(f'\n\tPlease, Try Again')
            schedule_lesson(lesson_info)
            
        elif choice == 6:
            undo_scheduled_lesson()
            
        elif choice == 7:
             print_scheduled_lessons()

        elif choice == 8:
            print("\n\tThank you for using ONLINE TUTORING SYSTEM\n")
            break
        else:
            print("Invalid choice, please try again.")
ONLINE_TUTORING_SYSTEM()
