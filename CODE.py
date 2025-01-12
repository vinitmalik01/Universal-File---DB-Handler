import mysql.connector
import pickle
import csv

def main():
    print("WELCOME TO THIS MULTIFUNCTIONALITY PROGRAM")
    print("Features:")
    print("1. File Handling: Binary, CSV, and Text files")
    print("2. Database Operations: MySQL command execution and table operations")
    print("Enter your choice to proceed.")

    while True:
        user_choice = input("Choose an option (binary/csv/txt/mysql/exit): ").strip().lower()
        if user_choice == "binary":
            handle_binary_file()
        elif user_choice == "csv":
            handle_csv_file()
        elif user_choice == "txt":
            handle_text_file()
        elif user_choice == "mysql":
            handle_mysql_operations()
        elif user_choice == "exit":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def get_filename():
    return input("Enter the file name: ").strip()

def get_data():
    return input("Enter the data to write: ").strip()

def handle_binary_file():
    filename = get_filename()
    found = False
    action = input("Choose an action (read/write/search/update/append): ").strip().lower()

    try:
        if action == "read":
            with open(filename, "rb") as file:
                print("File contents:")
                print('-' * 20)
                while True:
                    try:
                        record = pickle.load(file)
                        print(record)
                    except EOFError:
                        print('-' * 20)
                        print("End of file.")
                        break

        elif action in {"write", "append"}:
            with open(filename, "ab") as file:
                while True:
                    record={}
                    n=int(input("Enter the number of keys: "))
                    for i in range(n):
                        key=input("Enter the key: ")
                        value=input("Enter the value: ")
                        record[key]=value
                    pickle.dump(record, file)
                    more_data = input("Add more records? (y/n): ").strip().lower()
                    if more_data == "n":
                        break
                

        elif action=="search":
            search_term = input("Enter the term to search: ")
            
            with open(filename, "rb") as file:
                while True:
                    try:
                        record = pickle.load(file)
                        if search_term in record:
                            found = True
                            print(f"Found: {record}")
                    except EOFError:
                        break
                
            if not found:
                print(f"'{search_term}' not found in the file.")
        elif action=="update":
            search_term = input("Enter the key to search: ").strip()
            value = input("Enter the present value of the key: ").strip()
            
            if value.isdigit():
                value = int(value)

            found = False 
            with open(filename, "rb+") as file:
                while True:
                    pos = file.tell() 
                    try:
                        record = pickle.load(file) 
                        if search_term in record and record[search_term] == value:
                            print(f"Found: {record}")
                            updated_value = input(f"Enter the updated value for {search_term}: ").strip()
                            
                            if updated_value.isdigit():
                                updated_value = int(updated_value)

                            # Update the record
                            record[search_term] = updated_value
                            file.seek(pos)  # Reposition the pointer to the start of the current record
                            pickle.dump(record, file)  # Overwrite the record in the file
                            print(f"Updated '{search_term}' successfully.")
                            found = True
                            break
                    except EOFError:
                        break  # Exit the loop when the end of the file is reached

            if not found:
                print(f"Key '{search_term}' with value '{value}' not found.")
        else:
            print("Invalid action for binary file handling.")

    except FileNotFoundError:
        print("File not found. Please ensure the file exists.")
    except Exception as e:
        print(f"An error occurred: {e}")
def handle_csv_file():
    filename = get_filename()
    action = input("Choose an action (read/write/search/update/append): ").strip().lower()

    try:
        if action == "read":
            with open(filename, "r") as file:
                reader = csv.reader(file)
                print("File contents:")
                print('-' * 20)
                for row in reader:
                    print(row)
                print('-' * 20)

        elif action == "write":
            with open(filename, "w", newline='') as file:
                writer = csv.writer(file)
                headers = input("Enter headers (comma-separated): ").split(',')
                writer.writerow(headers)
                while True:
                    row_data = input("Enter row data (comma-separated): ").split(',')
                    writer.writerow(row_data)
                    more_data = input("Add more rows? (y/n): ").strip().lower()
                    if more_data == "n":
                        break

        elif action in {"search", "update"}:
            search_term = input("Enter the term to search: ")
            rows = []
            with open(filename, "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    rows.append(row)

            found = False
            for row in rows:
                if search_term in row:
                    found = True
                    print(f"Found: {row}")
                    if action == "update":
                        updated_value = input("Enter the updated value: ")
                        row[row.index(search_term)] = updated_value

            if found and action == "update":
                with open(filename, "w", newline='') as file:
                    writer = csv.writer(file)
                    writer.writerows(rows)
                print(f"Updated '{search_term}' successfully.")
            elif not found:
                print(f"'{search_term}' not found in the file.")

        elif action == "append":
            with open(filename, "a", newline='') as file:
                writer = csv.writer(file)
                while True:
                    row_data = input("Enter row data (comma-separated): ").split(',')
                    writer.writerow(row_data)
                    more_data = input("Add more rows? (y/n): ").strip().lower()
                    if more_data == "n":
                        break

        else:
            print("Invalid action for CSV file handling.")

    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def handle_text_file():
    filename = get_filename()
    action = input("Choose an action (read/write/search/update/append): ").strip().lower()

    try:
        if action == "read":
            with open(filename, "r") as file:
                print("File contents:")
                print('-' * 20)
                print(file.read())
                print('-' * 20)

        elif action == "write":
            with open(filename, "w") as file:
                while True:
                    line = get_data()
                    file.write(line + "\n")
                    more_data = input("Add more lines? (y/n): ").strip().lower()
                    if more_data == "n":
                        break

        elif action in {"search", "update"}:
            search_term = input("Enter the term to search: ")
            lines = []
            with open(filename, "r") as file:
                lines = file.readlines()

            found = False
            for i, line in enumerate(lines):
                if search_term in line:
                    found = True
                    print(f"Found: {line.strip()}")
                    if action == "update":
                        updated_line = input("Enter the updated line: ")
                        lines[i] = updated_line + "\n"

            if found and action == "update":
                with open(filename, "w") as file:
                    file.writelines(lines)
                print(f"Updated '{search_term}' successfully.")
            elif not found:
                print(f"'{search_term}' not found in the file.")

        elif action == "append":
            with open(filename, "a") as file:
                while True:
                    line = get_data()
                    file.write(line + "\n")
                    more_data = input("Add more lines? (y/n): ").strip().lower()
                    if more_data == "n":
                        break

        else:
            print("Invalid action for text file handling.")

    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def handle_mysql_operations():
    try:
        host = input("Enter the host: ").strip()
        username = input("Enter the username: ").strip()
        password = input("Enter the password: ").strip()
        database = input("Enter the database name: ").strip()

        connection = mysql.connector.connect(
            host=host,
            user=username,
            password=password,
            database=database
        )
        cursor = connection.cursor()
        print("Connected to the database.")

        while True:
            query = input("Enter an SQL query (or type 'exit' to quit): ").strip()
            if query.lower() == "exit":
                break

            try:
                cursor.execute(query)
                if query.strip().lower().startswith("select"):
                    results = cursor.fetchall()
                    for row in results:
                        print(row)
                else:
                    connection.commit()
                    print("Query executed successfully.")

            except mysql.connector.Error as err:
                print(f"Error: {err}")

        cursor.close()
        connection.close()
        print("Disconnected from the database.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
