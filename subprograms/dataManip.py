import pandas as pd

# DATA MANIPULATION
def dataManip(rta_min, zonar_min):
    
    # Normalize IDs on BOTH sides: make them strings, strip spaces, uppercase
    rta_min["Asset ID"] = rta_min["Asset ID"].astype(str).str.strip().str.upper()
    zonar_min["Asset ID"] = zonar_min["Asset ID"].astype(str).str.strip().str.upper()

    # convert to data to numeric values: remove any discrepancies such as "," or spaces
    rta_min["RTA Odometer"] = rta_min["RTA Odometer"].astype(str).str.replace(",", "", regex = False).astype(float)
    zonar_min["Zonar Odometer"] = zonar_min["Zonar Odometer"].astype(str).str.replace(",", "", regex=False).astype(float)

    # alternatively we can convert both numbers in a more simplified way by doing:
    #zonar_min["zonar_odometer"] = pd.to_numeric(zonar_min["zonar_odometer"], errors="coerce")
 
    # merge on the shared column (Asset ID)
    # use "inner" if you only want vehicles present in BOTH (this will ignore vehicles that aren't common)
    # use "left" if you want vehicles found in the left list and not in the right (this will flag vehicles not in Zonar)
    # use "right" if you want vehicles found in the right list and not in the left (this will flag vehicles not in RTA)
    comparison = pd.merge(rta_min, zonar_min, on="Asset ID", how="left", indicator=True)

    # now they line up Asset to Asset
    comparison["Mileage Difference"] = comparison["RTA Odometer"] - comparison["Zonar Odometer"]

    return comparison