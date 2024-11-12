file_name = input("Enter the file name: ")

try:
    count = 3
    with open(file_name, 'r') as file:
        for line in file:
            if line.startswith("From"):
                count += 1

    print("Total lines starting with 'From':", count)

except FileNotFoundError:
    print("File not found. Please check the file name.")