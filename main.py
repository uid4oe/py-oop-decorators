from AdditionOperations import AdditionOperations as addition
from ReportOperations import ReportOperations as report
import mock_data

report_menu = str("--Report Menu--\n"
                  "1)Details of all staff\n"
                  "2)Details of all animals\n"
                  "3)Details of all foods\n"
                  "4)Feeding details of a given animal between specified dates\n"
                  "5)Observation details of a given animal between specified dates\n"
                  "6)Staff who have observed a given animal\n"
                  "7)Foods that have been fed to a given animal\n")

addition_menu = str("--Addition Menu--\n"
                    "1)Add staff\n"
                    "2)Add animal\n"
                    "3)Add food\n"
                    "4)Add feeding details of a given animal\n"
                    "5)Add observation details of a given animal\n")

main_menu = str("--Main Menu--\n"
                "1)Addition Operations\n"
                "2)Report Operations\n"
                "3)Exit")

while True:
    try:
        print(main_menu)
        choice = input("Enter Choice[1-3]:")
        if choice == "3":
            break
        elif choice == "1":
            print(addition_menu)
            choice = input("Enter Choice[1-5]:")
            if choice == "1":
                addition.add_staff()
            elif choice == "2":
                addition.add_animal()
            elif choice == "3":
                addition.add_food()
            elif choice == "4":
                addition.add_feeding_record_given_animal()
            elif choice == "5":
                addition.add_observation_record_given_animal()
        elif choice == "2":
            print(report_menu)
            choice = input("Enter Choice[1-7]:")
            if choice == "1":
                report.details_of_all_staff()
            elif choice == "2":
                report.details_of_all_animals()
            elif choice == "3":
                report.details_of_all_foods()
            elif choice == "4":
                report.feeding_details_of_a_given_animal_between_specified_dates()
            elif choice == "5":
                report.observation_details_of_a_given_animal_between_specified_dates()
            elif choice == "6":
                report.staff_who_have_observed_a_given_animal()
            elif choice == "7":
                report.foods_that_have_been_fed_to_a_given_animal()
    except Exception as e:
        print(f"Error: {e}")