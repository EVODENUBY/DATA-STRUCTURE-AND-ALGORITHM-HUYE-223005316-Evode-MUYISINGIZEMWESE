from collections import deque

bookings_stack = []
lesson_queue = deque()

# List to manage available tutors
tutors_list = ['TUTOR ADOLPHE', 'Tutor BERNARD', 'Tutor MANI', 'Tutor PATRICK','Tutor EVODE']


def print_tutors():
    print("\nAvailable Tutors:\n")
    for tutor in tutors_list:
          print(tutor)
 
def add_booking(session_info):
    bookings_stack.append(session_info)
    print(f"\nBooking added: {session_info}")

def undo_booking():
    if bookings_stack:
        removed_booking = bookings_stack.pop()
        print(f"\nBooking removed: {removed_booking}")
    else:
        print("\nNo bookings to undo.")

def print_bookings(): # Display all booked sessions
    if bookings_stack:

        print("\nCurrent Bookings:")
        for bookings in bookings_stack:
           print(bookings)  
       
    else:
        print("\n Sorry!!, No bookings available.")

def schedule_lesson(lesson_info):
    lesson_queue.append(lesson_info)
    print(f"\nLesson scheduled: {lesson_info}")


def print_scheduled_lessons(): #Display all scheduled lessons
    if lesson_queue:
        print("\nScheduled Lessons:")
        for lessons in lesson_queue:
             print(lessons)
       
    else:
        print("\nNo lessons scheduled.")

def main():
    while True:
        print("\n ONLINE TUTORING SYSTEM")
        print("\n------------------------\n")
        print("1. View Available Tutors")
        print("2. Book a Session")
        print("3. Undo Last Booking")
        print("4. View Current Bookings")
        print("5. Schedule a Lesson")
        print("6. View Scheduled Lessons")
        print("7. Exit")

        choice = input("\nEnter your choice: ")

        if choice == '1':
            print_tutors()

        elif choice == '2':
            session_info = input("Enter booking details (e.g., 'ECONOMICS with Tutor EV0DE'): ")
            add_booking(session_info)

        elif choice == '3':
            undo_booking()

        elif choice == '4':
            print_bookings()

        elif choice == '5':
            lesson_info = input("Enter lesson details (e.g., 'ECONOMICS Lesson at 10:00AM'): ")
            schedule_lesson(lesson_info)

        elif choice == '6':
            print_scheduled_lessons()

        elif choice == '7':
            print("Exiting the system...")
            break

        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
