import csv

# 0 indexed
NAME_COLUMN = 1
STUDENT_NUMBER_COLUMN = 6
COURSE_COLUMN = 9
INTERNATIONAL_COLUMN = 8
GRADUATE_COLUMN = 10
AGE_COLUMN = 7

membership_list = input("Enter the qpay membership list csv file: \n")
with open(membership_list, 'r') as membership_csv:
    csvreader = csv.reader(membership_csv)
    new_csv_dict = {"First Name": [], "Last Name": [], "Student Number": [], 
                "UniMelb Course": [], "International Student?(Yes/No)": [], 
                "Graduate Student?(Yes/No)": [], "Over 18?(Yes/No)": []}
    next(membership_csv)
    for row in csvreader:

        # middle names go into first name
        first = " ".join(row[NAME_COLUMN].split()[:-1])
        last = row[NAME_COLUMN].split()[-1]
        new_csv_dict["First Name"].append(first)
        new_csv_dict["Last Name"].append(last)

        # If left blank will fill in NA for student number
        if row[STUDENT_NUMBER_COLUMN] == "":
            new_csv_dict["Student Number"].append("NA")
        else:
            new_csv_dict["Student Number"].append(row[STUDENT_NUMBER_COLUMN])

        new_csv_dict["UniMelb Course"].append(row[COURSE_COLUMN])

        new_csv_dict["International Student?(Yes/No)"].append(row[INTERNATIONAL_COLUMN])

        new_csv_dict["Graduate Student?(Yes/No)"].append(row[GRADUATE_COLUMN])

        new_csv_dict["Over 18?(Yes/No)"].append(row[AGE_COLUMN])

with open("new_membership_list.csv", 'w', newline='') as new_membership_csv:
    csvwriter = csv.writer(new_membership_csv)
    csvwriter.writerow(new_csv_dict.keys())
    csvwriter.writerows(zip(*new_csv_dict.values()))