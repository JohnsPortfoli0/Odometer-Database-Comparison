import pandas as pd

def colParser(rta, zonar):

    # Read the data in the file
    rta = pd.read_csv(rta) # header = 1 specifies that we want to begin looking at the second row of the csv
    zonar = pd.read_csv(zonar)
    print("\nFiles loaded successfully.")

    # I only care about the asset number and mileage of the asset
    rta_min = rta[["Vehicle", "Primary Meter"]]
    zonar_min = zonar[["Asset", "Odometer with Offset"]]

    # rename columns from the Zonar report and RTA report so they share the same name when doing comparions
    rta_min = rta_min.rename(columns={"Vehicle":"Asset ID", 
                                    "Primary Meter":"RTA Odometer"})

    zonar_min = zonar_min.rename(columns={"Asset":"Asset ID", 
                                      "Odometer with Offset":"Zonar Odometer"})
    
    return rta_min, zonar_min