# Odometer-Database-Comparison
A Python-based tool for comparing odometer readings between RTA and Zonar vehicle mileage reports.  
Disclaimer: Functionality still being added!

## Steps for Running the Program  
Please download the `Mileage_Difference_Calculator.py` and the 'subprograms' folder file under “Project Items.”
Additionally, download the sample .csv files that are labeled 'Zonar' and 'RTA' (these are necessary).

1. **Run the program**  
   - Open a terminal or command prompt in the same directory as the script.  
   - Execute:  
     ```bash
     python Mileage_Difference_Calculator.py
     ```  
     or run the compiled `.exe` file.  

2. **Enter the facility number** when prompted.
   
   Valid Facility ID Numbers (actual facility names removed for privacy): 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 14
    
3. **Select your CSV files** when the file dialogs appear:  
   - First select the **RTA** mileage file.  
   - Then select the **Zonar** mileage file.  
4. The program automatically performs the comparison and opens a **Save As** dialog for the output file.  
5. Choose a save location. The output file will be named: "Mileage Comparison Sheet - Facility X"

## Script Explanation and Flow  

### 1. Facility Selection (`getFacility.py`)  
- Prompts the user to enter a facility number.  
- Maps the number to the corresponding facility name (e.g., `3 → Facility 3`).  
- Used to label the output file automatically.  

### 2. File Selection (`fileSelect.py`)  
- Opens a GUI dialog (via `tkinter`) for easy file browsing.  
- Ensures both RTA and Zonar reports are selected before proceeding.  

### 3. Column Parsing (`colParser.py`)  
- Extracts only the relevant columns from each CSV:  
- RTA → *Vehicle*, *Primary Meter*  
- Zonar → *Asset*, *Odometer*  
- Renames columns for consistent formatting.  

### 4. Data Manipulation (`dataManip.py`)  
- Normalizes data for reliable comparison:  
- Converts *Asset IDs* to uppercase strings.  
- Removes commas from odometer values.  
- Converts odometer fields to floats.  
- Merges both dataframes by *Asset ID* to create a combined comparison table.  

### 5. Data Comparison (`dataComp.py`)  
- Calculates mileage difference as `RTA Odometer - Zonar Odometer`.  
- Identifies:  
- **Matching assets** (present in both files)  
- **Assets missing in Zonar** (in RTA only)  
- **Assets missing in RTA** (in Zonar only)  
- Returns summary counts for reporting and saves them to the CSV.  

## Output Explanation  
The generated file contains the aligned data and mileage differences:  

| Asset ID | RTA Odometer | Zonar Odometer | Mileage Difference |
|-----------|---------------|----------------|--------------------|
| 0571    | 2333          | 2300           | 33                 |
| 1154    | 2917          | 3000           | -83                |

At the bottom of the CSV, a summary is included:

## Key Features  

**Automated Comparison**  
- Aligns and analyzes mileage data without manual entry.  

**File Dialog Interface**  
- No path editing required — select files through a graphical window.  

**Data Cleaning**  
- Automatically formats IDs and numeric fields for consistency.  

**Summary Reporting**  
- Includes total vehicle matches and missing assets for quick review.  

**Facility-Specific Output**  
- Names the file automatically based on the facility number entered.  

## Requirements  
- **Python 3.10+** (tested with 3.14)  
- **Libraries:**  
  - `pandas`  
  - `tkinter` (included with Python)  
  - `sys`, `time`, `os`  

To install dependencies:  
```bash
pip install pandas



