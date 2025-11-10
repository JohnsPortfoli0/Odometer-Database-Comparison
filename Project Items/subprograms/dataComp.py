def dataComp(comparison, rta_min, zonar_min):
    
    # check to see which assets match in each database
    common_assets = set(rta_min["Asset ID"]).intersection(set(zonar_min["Asset ID"]))
    common_count = len(common_assets) # returns how many common assets there are

    Zonar_mismatch = comparison[comparison["_merge"] == "left_only"] # which assets were not found in Zonar
    RTA_mismatch = comparison[comparison["_merge"] == "right_only"] # which assets were not found in RTA

####################################################################################################################
    # THIS BLOCKED SECTION IS FOR DEBUGGING PURPOSES ONLY
    # I do not need to see this when made an .exe but it is nice to have when checking the .csv to the terminal

    #print("\nNumber of matching assets: ", common_count, "\n") 

    # checks if data frame is empty
    #if Zonar_mismatch.empty:
        #print("No Assets found in Zonar that are not in RTA\n")
    #else:
        #print("Assets found in RTA but not in Zonar:")
        #Zonar_mismatch = comparison[comparison["_merge"] == "left_only"] # which assets were not found in Zonar

    # For debugging purposes
    # checks if data frame is empty
    #if RTA_mismatch.empty:
        #print("No Assets found in RTA that are not in Zonar\n")
    #else:
        #print("Assets found in Zonar but not in RTA:")
        #RTA_mismatch = comparison[comparison["_merge"] == "right_only"] # which assets were not found in RTA

    # For debugging purposes
    #print(comparison[["Asset ID", "RTA Odometer", "Zonar Odometer", "Mileage Difference"]].to_string(index=False))
    #print("\n")
####################################################################################################################

    return comparison, RTA_mismatch, Zonar_mismatch, common_count