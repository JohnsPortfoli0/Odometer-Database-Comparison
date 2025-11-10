# LIBRARIES
import time
from subprograms import getFacility, fileSelect, colParser, dataManip, dataComp

# Message for users upon use
print("Welcome to the Mileage Comparator Application.")

#####################################################################################################################
# FUNCTION DECLARATION SECTION

# FUNCTION: helpMenu.py
# DESCRIPTION: Gives user a list of options to help them find where to download the reports and what results mean.
## NEED TO CREATE STILL

# FUNCTION: getFacility.py
# DESCRIPTION: Asks user for their facility and uses result to name the saved file at the end
facility_name = getFacility.getFacility()

# FUNCTION: fileSelect.py
# DESCRIPTION: Asks user to select the files that they want to compare
rta, zonar = fileSelect.fileSelect()

# FUNCTION: parse.py
# DESCRIPTION: Breaks the CSVs down so we only look at the Asset (Vehicle) and its odometer
rta_min, zonar_min = colParser.colParser(rta, zonar)
time.sleep(2)
print("\nComparison report is now running...")
time.sleep(2)

# FUNCTION: dataManip.py
# DESCRIPTION: Changes the entered data in the CSVs to make it work with each other. 
#              Assets are casted to strings, odometers are casted to floats
comparison = dataManip.dataManip(rta_min, zonar_min)
print("\nComparison is now complete!")
time.sleep(2)

# FUNCTION: dataComp
# DESCRIPTION: Compares the data in both CSVs and then saves to a new file
comparison, RTA_mismatch, Zonar_mismatch, common_count = dataComp.dataComp(comparison, rta_min, zonar_min)
#####################################################################################################################
# OUTPUTTING DATA TO A NEW CSV

from tkinter import filedialog

# Ask user where to save the file
save_path = filedialog.asksaveasfilename(
    title="Save Mileage Comparison Report As",
    defaultextension=".csv",
    filetypes=[("CSV files", "*.csv")],
    initialfile=f"Mileage Comparison Sheet - {facility_name}.csv"
)

# Only save if user didn’t cancel
if save_path:
    
    with open(save_path, "a", newline="") as f:

        # saves the comparison sheet first
        comparison.drop(columns=["_merge"]).to_csv(save_path, index=False)

        # Append summary info + mismatched assets
        f.write("\n")  # blank line for separation
        f.write(f"Vehicles matched, {common_count}\n")
        f.write(f"Missing in Zonar (in RTA only), {len(Zonar_mismatch)}\n")
        f.write(f"Missing in RTA (in Zonar only), {len(RTA_mismatch)}\n")

        # write Asset IDs under headers only if the lists aren’t empty
        if not Zonar_mismatch.empty:
            f.write("\nAssets in RTA but not in Zonar\n")
            Zonar_mismatch[["Asset ID"]].to_csv(f, index=False)

        if not RTA_mismatch.empty:
            f.write("\nAssets in Zonar but not in RTA\n")
            RTA_mismatch[["Asset ID"]].to_csv(f, index=False)
    
        print(f"\nFile saved successfully at:\n{save_path}")
        time.sleep(2)
else:
    print("Save cancelled by user.")


