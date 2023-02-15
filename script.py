# Libraries requried
from mdutils.mdutils import MdUtils as mdu
import csv


def data_to_md():
    # Read the data
    with open('CS Courses Information - Database.csv', newline='') as f:
        reader = csv.reader(f, delimiter=',')
        rows = list(reader)
    
    # Use the data
    for i in range(1, len(rows)):
        row = rows[i]

        # Create markdown file
        fname = str(row[0])
        mdFile = mdu(file_name=fname, title="")

        # Add body info
        course = "Course: " + str(row[0])
        mdFile.new_paragraph(course)

        name = "Name: " + str(row[1])
        mdFile.new_paragraph(name)

        if "(" in row[2]:
            # Fix such files manually
            pass
        elif "or" in row[2]:
            prereq1 = row[2].split(" or ")[0]
            prereq2 = row[2].split(" or ")[1]
            prereq = "Prerequisite(s): [[" + prereq1 + "]] or [[" + prereq2 + "]]"
            mdFile.new_paragraph(prereq)
        elif "and" in row[2]:
            prereq1 = row[2].split(" and ")[0]
            prereq2 = row[2].split(" and ")[1]
            prereq = "Prerequisite(s): [[" + prereq1 + "]] and [[" + prereq2 + "]]"
            mdFile.new_paragraph(prereq)
        elif row[2] == "__":
            prereq = "Prerequisite(s): none"
            mdFile.new_paragraph(prereq)
        else:
            prereq = "Prerequisite(s): [[" + str(row[2]) + "]]"
            mdFile.new_paragraph(prereq)

		# Final command for creating .md files
        mdFile.create_md_file()


def main():
    data_to_md()
    print("done")


if __name__ == "__main__":
    main()