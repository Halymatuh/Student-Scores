import csv

filename = "student_scores.csv"

# Write student names and scores to a CSV file

with open(filename, "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Name", "Score"])

    while True:
        name = input("Enter student name: ")

        score = float(input("Enter student score: "))

        writer.writerow([name, score])

        choice = input("Do you want to add another student? (yes/no): ")

        if choice.lower() != "yes":
            break


# Read the CSV file

total_score = 0
student_count = 0
top_score = -1
top_student = ""

with open(filename, "r") as file:

    reader = csv.reader(file)

    next(reader)

    for row in reader:

        name = row[0]
        score = float(row[1])

        total_score += score
        student_count += 1

        if score > top_score:
            top_score = score
            top_student = name


if student_count > 0:

    average = total_score / student_count

    print("\nClass Average:", average)
    print("Top Performer:", top_student)
    print("Highest Score:", top_score)

else:
    print("No student records found.")
