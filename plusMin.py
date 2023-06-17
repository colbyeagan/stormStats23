import csv
import json
import time

class GameFile:
    csv_file_path: str = str()
    target_value: str = str()
    playersList: list = list()

    # Specify the CSV file path
    def __init__(self, csv_file_path1: str, target_value1: str, listOfNumbers: list):
        global csv_file_path
        global target_value
        global playersList
        playersList = listOfNumbers
        csv_file_path = csv_file_path1
        target_value = target_value1

    def allStatsListCombo(self, comboNum: int):
        #comboNum = int(input("How many players in the combo? "))
        comboDict= dict()
        if comboNum == 1:
            # Open the CSV file
            with open(csv_file_path, 'r') as file:
                csv_reader = csv.DictReader(file)
                # Iterate through each row in the CSV file
                for row in csv_reader:
                    for i in range(len(playersList)):
                        if row[playersList[i]] == target_value:
                            if playersList[i] in comboDict:
                                comboDict[playersList[i]]["Plus"] += int(row['Plus'])
                                comboDict[playersList[i]]["Minus"] += int(row['Minus'])
                                comboDict[playersList[i]]["Plus/Minus"] += int(row['Plus/Minus'])
                            else:
                                comboDict[playersList[i]] = {"Plus": 0, "Minus": 0, "Plus/Minus": 0}
                                comboDict[playersList[i]]["Plus"] += int(row['Plus'])
                                comboDict[playersList[i]]["Minus"] += int(row['Minus'])
                                comboDict[playersList[i]]["Plus/Minus"] += int(row['Plus/Minus'])
        if comboNum == 2:
            # Open the CSV file
            with open(csv_file_path, 'r') as file:
                csv_reader = csv.DictReader(file)
                # Iterate through each row in the CSV file
                for row in csv_reader:
                    for i in range(len(playersList) - 1):
                        for j in range(i + 1, len(playersList)):
                            if row[playersList[i]] == target_value and row[playersList[j]] == target_value:
                                if(f"{playersList[i]},{playersList[j]}") in comboDict:
                                    comboDict[f"{playersList[i]},{playersList[j]}"]["Plus"] += int(row['Plus'])
                                    comboDict[f"{playersList[i]},{playersList[j]}"]["Minus"] += int(row['Minus'])
                                    comboDict[f"{playersList[i]},{playersList[j]}"]["Plus/Minus"] += int(row['Plus/Minus'])
                                else:
                                    comboDict[f"{playersList[i]},{playersList[j]}"] = {"Plus": 0, "Minus": 0, "Plus/Minus": 0}
                                    comboDict[f"{playersList[i]},{playersList[j]}"]["Plus"] += int(row['Plus'])
                                    comboDict[f"{playersList[i]},{playersList[j]}"]["Minus"] += int(row['Minus'])
                                    comboDict[f"{playersList[i]},{playersList[j]}"]["Plus/Minus"] += int(row['Plus/Minus'])
        if comboNum == 3:
            # Open the CSV file
            with open(csv_file_path, 'r') as file:
                csv_reader = csv.DictReader(file)
                # Iterate through each row in the CSV file
                for row in csv_reader:
                    for i in range(len(playersList) - 2):
                        for j in range(i + 1, len(playersList) - 1):
                            for k in range(j + 1, len(playersList)):
                                if row[playersList[i]] == target_value and row[playersList[j]] == target_value and row[playersList[k]] == target_value:
                                    if(f"{playersList[i]},{playersList[j]},{playersList[k]}") in comboDict:
                                        comboDict[f"{playersList[i]},{playersList[j]},{playersList[k]}"]["Plus"] += int(row['Plus'])
                                        comboDict[f"{playersList[i]},{playersList[j]},{playersList[k]}"]["Minus"] += int(row['Minus'])
                                        comboDict[f"{playersList[i]},{playersList[j]},{playersList[k]}"]["Plus/Minus"] += int(row['Plus/Minus'])
                                    else:
                                        comboDict[f"{playersList[i]},{playersList[j]},{playersList[k]}"] = {"Plus": 0, "Minus": 0, "Plus/Minus": 0}
                                        comboDict[f"{playersList[i]},{playersList[j]},{playersList[k]}"]["Plus"] += int(row['Plus'])
                                        comboDict[f"{playersList[i]},{playersList[j]},{playersList[k]}"]["Minus"] += int(row['Minus'])
                                        comboDict[f"{playersList[i]},{playersList[j]},{playersList[k]}"]["Plus/Minus"] += int(row['Plus/Minus'])
    #sortedPlusMinus = sorted(comboDict.items(), key=lambda x:x[1], reverse=True)
        from tqdm import tqdm
        for i in tqdm(range(len(comboDict))):
            time.sleep(.005)
            pass
        for item in comboDict:
            print(f"{item} --- {comboDict[item]}")

    def plusStatsListCombo(self, comboNum: int, sortKey: bool):
        
        comboDict= dict()
        if comboNum == 1:
            # Open the CSV file
            with open(csv_file_path, 'r') as file:
                csv_reader = csv.DictReader(file)
                # Iterate through each row in the CSV file
                for row in csv_reader:
                    for i in range(len(playersList)):
                        if row[playersList[i]] == target_value:
                            if playersList[i] in comboDict:
                                comboDict[playersList[i]]["Plus"] += int(row['Plus'])
                                comboDict[playersList[i]]["Plus/Pos"] += int(row['Plus'])
                                comboDict[playersList[i]]["Possessions"] += int(row['# Possessions'])
                            else:
                                comboDict[playersList[i]] = {"Plus": 0, "Plus/Pos": 0, "Possessions": 0}
                                comboDict[playersList[i]]["Plus"] += int(row['Plus'])
                                comboDict[playersList[i]]["Plus/Pos"] += int(row['Plus'])
                                comboDict[playersList[i]]["Possessions"] += int(row['# Possessions'])
        if comboNum == 2:
            # Open the CSV file
            with open(csv_file_path, 'r') as file:
                csv_reader = csv.DictReader(file)
                # Iterate through each row in the CSV file
                for row in csv_reader:
                    for i in range(len(playersList) - 1):
                        for j in range(i + 1, len(playersList)):
                            if row[playersList[i]] == target_value and row[playersList[j]] == target_value:
                                if(f"{playersList[i]},{playersList[j]}") in comboDict:
                                    comboDict[f"{playersList[i]},{playersList[j]}"]["Plus"] += int(row['Plus'])
                                    comboDict[f"{playersList[i]},{playersList[j]}"]["Plus/Pos"] += int(row['Plus'])
                                    comboDict[f"{playersList[i]},{playersList[j]}"]["Possessions"] += int(row['# Possessions'])
                                else:
                                    comboDict[f"{playersList[i]},{playersList[j]}"] = {"Plus": 0, "Plus/Pos": 0, "Possessions": 0}
                                    comboDict[f"{playersList[i]},{playersList[j]}"]["Plus"] += int(row['Plus'])
                                    comboDict[f"{playersList[i]},{playersList[j]}"]["Plus/Pos"] += int(row['Plus'])
                                    comboDict[f"{playersList[i]},{playersList[j]}"]["Possessions"] += int(row['# Possessions'])
        if comboNum == 3:
            # Open the CSV file
            with open(csv_file_path, 'r') as file:
                csv_reader = csv.DictReader(file)
                # Iterate through each row in the CSV file
                for row in csv_reader:
                    for i in range(len(playersList) - 2):
                        for j in range(i + 1, len(playersList) - 1):
                            for k in range(j + 1, len(playersList)):
                                if row[playersList[i]] == target_value and row[playersList[j]] == target_value and row[playersList[k]] == target_value:
                                    if(f"{playersList[i]},{playersList[j]},{playersList[k]}") in comboDict:
                                        comboDict[f"{playersList[i]},{playersList[j]},{playersList[k]}"]["Plus"] += int(row['Plus'])
                                        comboDict[f"{playersList[i]},{playersList[j]},{playersList[k]}"]["Plus/Pos"] += int(row['Plus'])
                                        comboDict[f"{playersList[i]},{playersList[j]},{playersList[k]}"]["Possessions"] += int(row['# Possessions'])
                                    else:
                                        comboDict[f"{playersList[i]},{playersList[j]},{playersList[k]}"] = {"Plus": 0, "Plus/Pos": 0, "Possessions": 0}
                                        comboDict[f"{playersList[i]},{playersList[j]},{playersList[k]}"]["Plus"] += int(row['Plus'])
                                        comboDict[f"{playersList[i]},{playersList[j]},{playersList[k]}"]["Plus/Pos"] += int(row['Plus'])
                                        comboDict[f"{playersList[i]},{playersList[j]},{playersList[k]}"]["Possessions"] += int(row['# Possessions'])
        for row in comboDict:
            comboDict[row]['Plus/Pos'] = (comboDict[row]['Plus/Pos'] / comboDict[row]['Possessions'])
    
        from tqdm import tqdm
        for i in tqdm(range(len(comboDict))):
            time.sleep(.005)
            pass
        if sortKey:
            sorted_data = sorted(comboDict.items(), key=lambda x: x[1]['Plus/Pos'])
            i = 0
            for item in sorted_data:
                print(item)
                i += 1
            print(f"{i} total combinations")
        else:
            i = 0
            for item in comboDict:
                print(f"{item}:{comboDict[item]}")
                i += 1
            print(f"{i} total combinations")

    def minusStatsListCombo(self, comboNum: int, sortKey: bool):
        #comboNum = int(input("How many players in the combo? "))
        playersList = ['0', '1', '3', '4', '5','10', '12', '20', '21', '22', '23', '25', '33', '34']
        comboDict= dict()
        if comboNum == 1:
            # Open the CSV file
            with open(csv_file_path, 'r') as file:
                csv_reader = csv.DictReader(file)
                # Iterate through each row in the CSV file
                for row in csv_reader:
                    for i in range(len(playersList)):
                        if row[playersList[i]] == target_value:
                            if playersList[i] in comboDict:
                                comboDict[playersList[i]]["Minus"] += int(row['Minus'])
                                comboDict[playersList[i]]["Minus/Pos"] += int(row['Minus'])
                                comboDict[playersList[i]]["Possessions"] += int(row['# Possessions'])
                            else:
                                comboDict[playersList[i]] = {"Minus": 0, "Minus/Pos": 0, "Possessions": 0}
                                comboDict[playersList[i]]["Minus"] += int(row['Minus'])
                                comboDict[playersList[i]]["Minus/Pos"] += int(row['Minus'])
                                comboDict[playersList[i]]["Possessions"] += int(row['# Possessions'])
        if comboNum == 2:
            # Open the CSV file
            with open(csv_file_path, 'r') as file:
                csv_reader = csv.DictReader(file)
                # Iterate through each row in the CSV file
                for row in csv_reader:
                    for i in range(len(playersList) - 1):
                        for j in range(i + 1, len(playersList)):
                            if row[playersList[i]] == target_value and row[playersList[j]] == target_value:
                                if(f"{playersList[i]},{playersList[j]}") in comboDict:
                                    comboDict[f"{playersList[i]},{playersList[j]}"]["Minus"] += int(row['Minus'])
                                    comboDict[f"{playersList[i]},{playersList[j]}"]["Minus/Pos"] += int(row['Minus'])
                                    comboDict[f"{playersList[i]},{playersList[j]}"]["Possessions"] += int(row['# Possessions'])
                                else:
                                    comboDict[f"{playersList[i]},{playersList[j]}"] = {"Minus": 0, "Minus/Pos": 0, "Possessions": 0}
                                    comboDict[f"{playersList[i]},{playersList[j]}"]["Minus"] += int(row['Minus'])
                                    comboDict[f"{playersList[i]},{playersList[j]}"]["Minus/Pos"] += int(row['Minus'])
                                    comboDict[f"{playersList[i]},{playersList[j]}"]["Possessions"] += int(row['# Possessions'])
        if comboNum == 3:
            # Open the CSV file
            with open(csv_file_path, 'r') as file:
                csv_reader = csv.DictReader(file)
                # Iterate through each row in the CSV file
                for row in csv_reader:
                    for i in range(len(playersList) - 2):
                        for j in range(i + 1, len(playersList) - 1):
                            for k in range(j + 1, len(playersList)):
                                if row[playersList[i]] == target_value and row[playersList[j]] == target_value and row[playersList[k]] == target_value:
                                    if(f"{playersList[i]},{playersList[j]},{playersList[k]}") in comboDict:
                                        comboDict[f"{playersList[i]},{playersList[j]},{playersList[k]}"]["Minus"] += int(row['Minus'])
                                        comboDict[f"{playersList[i]},{playersList[j]},{playersList[k]}"]["Minus/Pos"] += int(row['Minus'])
                                        comboDict[f"{playersList[i]},{playersList[j]},{playersList[k]}"]["Possessions"] += int(row['# Possessions'])
                                    else:
                                        comboDict[f"{playersList[i]},{playersList[j]},{playersList[k]}"] = {"Minus": 0, "Minus/Pos": 0, "Possessions": 0}
                                        comboDict[f"{playersList[i]},{playersList[j]},{playersList[k]}"]["Minus"] += int(row['Minus'])
                                        comboDict[f"{playersList[i]},{playersList[j]},{playersList[k]}"]["Minus/Pos"] += int(row['Minus'])
                                        comboDict[f"{playersList[i]},{playersList[j]},{playersList[k]}"]["Possessions"] += int(row['# Possessions'])
        for row in comboDict:
            comboDict[row]['Minus/Pos'] = (comboDict[row]['Minus/Pos'] / comboDict[row]['Possessions'])
    #sortedPlusMinus = sorted(comboDict.items(), key=lambda x:x[1], reverse=True)
        from tqdm import tqdm
        for i in tqdm(range(len(comboDict))):
            time.sleep(.005)
            pass
        if sortKey:
            sorted_data = sorted(comboDict.items(), key=lambda x: x[1]['Minus/Pos'])
            i = 0
            for item in sorted_data:
                print(item)
                i += 1
            print(f"{i} total combinations")
        else:
            i = 0
            for item in comboDict:
                print(f"{item}:{comboDict[item]}")
                i += 1
            print(f"{i} total combinations")

    def plusMinusStatsListCombo(self, comboNum: int, sortKey: bool):
        #comboNum = int(input("How many players in the combo? "))
        playersList = ['0', '1', '3', '4', '5','10', '12', '20', '21', '22', '23', '25', '33', '34']
        comboDict= dict()
        if comboNum == 1:
            # Open the CSV file
            with open(csv_file_path, 'r') as file:
                csv_reader = csv.DictReader(file)
                # Iterate through each row in the CSV file
                for row in csv_reader:
                    for i in range(len(playersList)):
                        if row[playersList[i]] == target_value:
                            if playersList[i] in comboDict:
                                comboDict[playersList[i]]["Plus/Minus"] += int(row['Plus/Minus'])
                                comboDict[playersList[i]]["Plus/Minus/Pos"] += int(row['Plus/Minus'])
                                comboDict[playersList[i]]["Possessions"] += int(row['# Possessions'])
                            else:
                                comboDict[playersList[i]] = {"Plus/Minus": 0, "Plus/Minus/Pos": 0, "Possessions": 0}
                                comboDict[playersList[i]]["Plus/Minus"] += int(row['Plus/Minus'])
                                comboDict[playersList[i]]["Plus/Minus/Pos"] += int(row['Plus/Minus'])
                                comboDict[playersList[i]]["Possessions"] += int(row['# Possessions'])
        if comboNum == 2:
            # Open the CSV file
            with open(csv_file_path, 'r') as file:
                csv_reader = csv.DictReader(file)
                # Iterate through each row in the CSV file
                for row in csv_reader:
                    for i in range(len(playersList) - 1):
                        for j in range(i + 1, len(playersList)):
                            if row[playersList[i]] == target_value and row[playersList[j]] == target_value:
                                if(f"{playersList[i]},{playersList[j]}") in comboDict:
                                    comboDict[f"{playersList[i]},{playersList[j]}"]["Plus/Minus"] += int(row['Plus/Minus'])
                                    comboDict[f"{playersList[i]},{playersList[j]}"]["Plus/Minus/Pos"] += int(row['Plus/Minus'])
                                    comboDict[f"{playersList[i]},{playersList[j]}"]["Possessions"] += int(row['# Possessions'])
                                else:
                                    comboDict[f"{playersList[i]},{playersList[j]}"] = {"Plus/Minus": 0, "Plus/Minus/Pos": 0, "Possessions": 0}
                                    comboDict[f"{playersList[i]},{playersList[j]}"]["Plus/Minus"] += int(row['Plus/Minus'])
                                    comboDict[f"{playersList[i]},{playersList[j]}"]["Plus/Minus/Pos"] += int(row['Plus/Minus'])
                                    comboDict[f"{playersList[i]},{playersList[j]}"]["Possessions"] += int(row['# Possessions'])
        if comboNum == 3:
            # Open the CSV file
            with open(csv_file_path, 'r') as file:
                csv_reader = csv.DictReader(file)
                # Iterate through each row in the CSV file
                for row in csv_reader:
                    for i in range(len(playersList) - 2):
                        for j in range(i + 1, len(playersList) - 1):
                            for k in range(j + 1, len(playersList)):
                                if row[playersList[i]] == target_value and row[playersList[j]] == target_value and row[playersList[k]] == target_value:
                                    if(f"{playersList[i]},{playersList[j]},{playersList[k]}") in comboDict:
                                        comboDict[f"{playersList[i]},{playersList[j]},{playersList[k]}"]["Plus/Minus"] += int(row['Plus/Minus'])
                                        comboDict[f"{playersList[i]},{playersList[j]},{playersList[k]}"]["Plus/Minus/Pos"] += int(row['Plus/Minus'])
                                        comboDict[f"{playersList[i]},{playersList[j]},{playersList[k]}"]["Possessions"] += int(row['# Possessions'])
                                    else:
                                        comboDict[f"{playersList[i]},{playersList[j]},{playersList[k]}"] = {"Plus/Minus": 0, "Plus/Minus/Pos": 0, "Possessions": 0}
                                        comboDict[f"{playersList[i]},{playersList[j]},{playersList[k]}"]["Plus/Minus"] += int(row['Plus/Minus'])
                                        comboDict[f"{playersList[i]},{playersList[j]},{playersList[k]}"]["Plus/Minus/Pos"] += int(row['Plus/Minus'])
                                        comboDict[f"{playersList[i]},{playersList[j]},{playersList[k]}"]["Possessions"] += int(row['# Possessions'])
        for row in comboDict:
            comboDict[row]['Plus/Minus/Pos'] = (comboDict[row]['Plus/Minus/Pos'] / comboDict[row]['Possessions'])
    #sortedPlusMinus = sorted(comboDict.items(), key=lambda x:x[1], reverse=True)
        from tqdm import tqdm
        for i in tqdm(range(len(comboDict))):
            time.sleep(.005)
            pass
        if sortKey:
            sorted_data = sorted(comboDict.items(), key=lambda x: x[1]['Plus/Minus/Pos'])
            i = 0
            for item in sorted_data:
                print(item)
                i += 1
            print(f"{i} total combinations")
        else:
            i = 0
            for item in comboDict:
                print(f"{item}:{comboDict[item]}")
                i += 1
            print(f"{i} total combinations")