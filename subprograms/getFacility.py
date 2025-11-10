# Program that allows user to select their working facility

def getFacility():
    while True:
        facility = input("\nPlease enter your facility number: ").strip()

        match facility:
            case "1":
                return "Facility 1"
            case "2":
                return "Facility 2"
            case "3":
                return "Facility 3"
            case "4":
                return "Facility 4"
            case "5":
                return "Facility 5"
            case "6":
                return "Facility 6"
            case "7":
                return "Facility 7"
            case "8":
                return "Facility 8"
            case "9":
                return "Facility 9"
            case "10":
                return "Facility 10"
            case "14":
                return "Facility 14"
            case _:
                print("Invalid entry. Please re-enter the number.\n")
