from tkinter import Tk, filedialog
import sys
import time

def fileSelect():
    while True: # continously runs until a satisfactory input is given

        fileImport = input("Would you like to proceed in doing an odometer " \
        "comparison? (Y/N): ").strip().upper() # converts all to upper case

        if fileImport == "Y": # user wants to import their CSVs
            # FILE SELECTION
            Tk().withdraw()  # hide root Tk window

            print("\nSelect the RTA mileage file...")
            rta = filedialog.askopenfilename(title="Select RTA CSV", filetypes=[("CSV files", "*.csv")])
            print(rta)

            print("\nSelect the Zonar mileage file...")
            zonar = filedialog.askopenfilename(title="Select Zonar CSV", filetypes=[("CSV files", "*.csv")])
            print(zonar)

            # File loading check
            if not rta or not zonar:
                print("You must select both files.")
                sys.exit()  # stop program

            # Return the selected paths to your main program
            return rta, zonar

        elif fileImport == "N":
            print("\nUser chose not to do comparison.")
            time.sleep(1.5)
            print("\nApplication is now closing.")
            time.sleep(3)
            sys.exit()

        else:
            print("Invalid entry. Please enter Y or N.\n")
