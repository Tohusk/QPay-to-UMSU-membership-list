import csv

### NEW COLUMN INDICES
# 0 indexed
NAME_COLUMN = 1
STUDENT_NUMBER_COLUMN = 6
COURSE_COLUMN = 10
INTERNATIONAL_COLUMN = 11
GRADUATE_COLUMN = 9
AGE_COLUMN = 7
UNIMELB_COLUMN = 8

### OLD COLUMN INDICES
OLD_INTERNATIONAL = 12
OLD_GRAD = 13

### COLUMN NAMES
FIRST_NAME = "First Name"
LAST_NAME = "Last Name"
STUDENT_NUMBER_NAME = "Student Number"
UNIMELB_COURSE_NAME = "UniMelb Course"
INTERNATIONAL_NAME = "International Student?(Yes/No)"
GRADUATE_NAME = "Graduate Student?(Yes/No)"
OVER_EIGHTEEN_NAME = "Over 18?(Yes/No)"




#TODO add try excepts

membership_list = input("Enter the qpay membership list csv file: \n")
with open(membership_list, 'r') as membership_csv:
    csvreader = csv.reader(membership_csv)
    new_csv_dict = {FIRST_NAME: [], LAST_NAME: [], STUDENT_NUMBER_NAME: [], 
                UNIMELB_COURSE_NAME: [], INTERNATIONAL_NAME: [], 
                GRADUATE_NAME: [], OVER_EIGHTEEN_NAME: []}
    next(membership_csv)
    for row in csvreader:

        if row[OLD_INTERNATIONAL] == "":
            # middle names go into first name
            first = " ".join(row[NAME_COLUMN].split()[:-1])
            last = row[NAME_COLUMN].split()[-1]
            new_csv_dict[FIRST_NAME].append(first)
            new_csv_dict[LAST_NAME].append(last)

            # unimelb student
            if row[UNIMELB_COLUMN] == "Yes":
                new_csv_dict[STUDENT_NUMBER_NAME].append(row[STUDENT_NUMBER_COLUMN])
                new_csv_dict[UNIMELB_COURSE_NAME].append(row[COURSE_COLUMN])
                new_csv_dict[INTERNATIONAL_NAME].append(row[INTERNATIONAL_COLUMN])
                new_csv_dict[GRADUATE_NAME].append(row[GRADUATE_COLUMN])
                new_csv_dict[OVER_EIGHTEEN_NAME].append(row[AGE_COLUMN])


            # non unimelb student
            else:
                new_csv_dict[STUDENT_NUMBER_NAME].append("NA")
                new_csv_dict[UNIMELB_COURSE_NAME].append("NA")
                new_csv_dict[INTERNATIONAL_NAME].append("NA")
                new_csv_dict[GRADUATE_NAME].append("NA")
                new_csv_dict[OVER_EIGHTEEN_NAME].append(row[AGE_COLUMN])
        else:
            # middle names go into first name
            first = " ".join(row[NAME_COLUMN].split()[:-1])
            last = row[NAME_COLUMN].split()[-1]
            new_csv_dict[FIRST_NAME].append(first)
            new_csv_dict[LAST_NAME].append(last)

            # If not numeric, then input NA
            if not row[STUDENT_NUMBER_COLUMN].isnumeric():
                new_csv_dict[STUDENT_NUMBER_NAME].append("NA")
            else:
                new_csv_dict[STUDENT_NUMBER_NAME].append(row[STUDENT_NUMBER_COLUMN])

            new_csv_dict[UNIMELB_COURSE_NAME].append(row[COURSE_COLUMN])

            new_csv_dict[INTERNATIONAL_NAME].append(row[OLD_INTERNATIONAL])

            new_csv_dict[GRADUATE_NAME].append(row[OLD_GRAD])

            new_csv_dict[OVER_EIGHTEEN_NAME].append(row[AGE_COLUMN])



with open("\\".join(membership_list.split("\\")[:-1]) + "\\new_membership_list.csv", 'w', newline='') as new_membership_csv:
    csvwriter = csv.writer(new_membership_csv)
    csvwriter.writerow(new_csv_dict.keys())
    csvwriter.writerows(zip(*new_csv_dict.values()))