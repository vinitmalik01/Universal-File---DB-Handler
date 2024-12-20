import mysql.connector
import pickle
import csv

def main():
    print("WELCOME TO THIS MULTIFUNCTIONALITY PROGRAM WHICH SERVES ")
    print("FILE HANDLING OF BINARY, CSV, TXT")
    print("THIS PROGRAM ALSO PROVIDES FUNCTIONALITY TO YOU TO BE ABLE TO GIVE NORMAL COMMANDS AND INTERPRET THEM AND PERFORM FUNCTIONS IN DATABASE")
    print("ENTER WHAT YOU WANT TO DO")
    
    while True:
        choice = input("Enter your choice (binary/csv/txt/mysql/exit): ").lower()
        if "binary" in choice:
            binaryfilehandling()
        elif "csv" in choice:
            csvfilehandling()
        elif "txt" in choice:
            txtfilehandling()
        elif "mysql" in choice:
            mysqlconnection()
        elif "exit" in choice:
            print("EXITING PROGRAM.")
            break
        else:
            print("Invalid choice. Please try again.")

def askfilename():
    file = input("Enter file name: ")
    return file

def askdata():
    data = input("Enter the data you want to write: ")
    return data

def binaryfilehandling():
    file = askfilename()
    datan = []
    choice = input("What to do? (read/write/search/update/Append more data): ").lower()
    
    if "read" in choice:
        try:
            with open(file, "rb") as f:
                print("GIVING FILE'S DATA")
                print('-'*20)
                while True:
                    try:
                        data = pickle.load(f)
                        print(data)
                    except EOFError:
                        print('-'*20)
                        print("Successfully printed data.")
                        break
        except FileNotFoundError:
            print("File not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

    elif "write" in choice:
        with open(file, "ab") as f:
            while True:
                data = askdata()
                pickle.dump(data, f)
                ask = input("More data (Y/N)? ").lower()
                if "n" in ask:
                    break
    elif "Append more data".lower() in choice:
        with open(file,"ab")as f:
            while True:
                data = askdata()
                pickle.dump(data,f)
                ask = input("More data (Y/N)? ").lower()
                if "n" in ask:
                    break

    elif "search" in choice or "update" in choice:
        try:
            with open(file, "rb") as f:
                word = input("Enter the word to search: ")
                while True:
                    try:
                        dat = pickle.load(f)
                        datan.append(dat)
                    except EOFError:
                        break
                for i in datan:
                    if word in i:
                        print(f"Found {word} in {file}")
                        new_word = input("Enter new data to update: ")
                        index = datan.index(i)
                        datan[index] = new_word
            with open(file, "wb") as f:
                for i in datan:
                    pickle.dump(i, f)
                print(f"Updated {word} to {new_word}")
        except FileNotFoundError:
            print("File not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

def csvfilehandling():
    file = askfilename()
    choice = input("What to do? (read/write/search/update/Append more data): ").lower()

    if "read" in choice:
        try:
            with open(file, "r") as f:
                reader = csv.reader(f)
                print("GIVING FILE'S DATA")
                print('-'*20)
                for row in reader:
                    print(row)
                print('-'*20)
                print("Successfully printed data.")
        except FileNotFoundError:
            print("File not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

    elif "write" in choice:
        with open(file, "w", newline='') as f:
            writer = csv.writer(f)
            header = input("Enter header (comma-separated): ").split(',')
            writer.writerow(header)
            while True:
                data = askdata().split(',')
                writer.writerow(data)
                ask = input("More data (Y/N)? ").lower()
                if "n" in ask:
                    break

    elif "search" in choice or "update" in choice:
        datan = []
        try:
            with open(file, "r") as f:
                word = input("Enter the word to search: ")
                reader = csv.reader(f)
                for row in reader:
                    datan.append(row)
                for i in datan:
                    if word in i:
                        print(f"Found {word} in {file}")
                        new_word = input("Enter new data to update: ")
                        index = i.index(word)
                        i[index] = new_word
            with open(file, "w", newline='') as f:
                writer = csv.writer(f)
                writer.writerows(datan)
            print("Updated successfully.")
        except FileNotFoundError:
            print("File not found.")
        except Exception as e:
            print(f"An error occurred: {e}")
    elif "Append more data".lower() in choice:
        with open(file,"a")as f:
            writer = csv.writer(f)
            while True:
                data = askdata().split(',')
                writer.writerow(data)
                ask = input("More data (Y/N)? ").lower()
                if "n" in ask:
                    break

def txtfilehandling():
    file = askfilename()
    choice = input("What to do? (read/write/search/update/Append more data): ").lower()

    if "read" in choice:
        try:
            with open(file, "r") as f:
                
                print("GIVING FILE'S DATA")
                print('-'*20)
                lines = f.readlines()
                for line in lines:
                    print(line, end="")
                print('-'*20)
                print("Successfully printed data.")
        except FileNotFoundError:
            print("File not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

    elif "write" in choice:
        with open(file, "a") as f:
            while True:
                data = askdata()
                f.write(data + '\n')
                ask = input("More data (Y/N)? ").lower()
                if "n".lower() in ask:
                    break

    elif "search" in choice or "update" in choice:
        datan = []
        try:
            with open(file, "r") as f:
                word = input("Enter the word to search: ")
                lines = f.readlines()
                for line in lines:
                    datan.append(line.strip())
                for i in datan:
                    if word in i:
                        print(f"Found {word} in {file}")
                        new_word = input("Enter new data to update: ")
                        index = datan.index(i)
                        datan[index] = new_word
            with open(file, "w") as f:
                for line in datan:
                    f.write(line + '\n')
            print("Updated successfully.")
        except FileNotFoundError:
            print("File not found.")
        except Exception as e:
            print(f"An error occurred: {e}")
    elif "Append more data".lower() in choice:
        with open(file,"a")as f:
            while True:

                data = askdata()
                f.write(data+'\n')
                ask = input("More data (Y/N)? ").lower()
                if "N".lower() in ask:
                    break


def mysqlconnection():
    try:
        # Get MySQL connection details from the user
        host = input("Enter host to connect to: ")
        userr = input("Enter user name: ")
        your_password = input("Enter password: ")
        your_database = input("Enter database name to connect to: ")

        # Establish the connection to MySQL database
        connection = mysql.connector.connect(
            host=host,
            user=userr,
            password=your_password,
            database=your_database
        )
        cursor = connection.cursor()
        print("Connected to MySQL database.")

        # Show all tables in the selected database
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()
        print("These are the tables present in", your_database)
        print('-'*15)
        for table in tables:
            print(table[0])
        print('-'*15)

        # Get table name from user
        table = input("Choose one table: ")

        # Check if table exists
        cursor.execute("SHOW TABLES LIKE %s", (table,))
        if cursor.fetchone() is None:
            print(f"Table {table} does not exist.")
            return

        # Show all records in the selected table
        cursor.execute(f"SELECT * FROM {table}")
        records = cursor.fetchall()
        print("These records are present in the table:")
        print('-'*15)
        for record in records:
            print(record)
        print('-'*15)

        # Show table structure
        cursor.execute(f"DESC {table}")
        structure = cursor.fetchall()
        print("Following structure is followed in the table:")
        print('-'*15)
        for column in structure:
            print(column)
        print('-'*15)

        # Menu for table operations
        while True:
            print("What to do in the table now?")
            choice = input("UPDATE / INSERT / DELETE / ADD COLUMN / REMOVE COLUMN / DROP TABLE / EXIT: ").lower()

            if "update" in choice:
                # Update operation
                column = input("Which column to update? ")
                condition = input("Extra condition? (y/n): ").lower()
                internal_choice = input("What operation? (increase, decrease, multiply, divide, set default): ").lower()

                if "increase" in internal_choice:
                    increase = input("Increase by? ")
                    query = f"UPDATE {table} SET {column} = {column} + %s"
                    cursor.execute(query, (increase,))
                    connection.commit()
                    print("Column updated.")

                elif "decrease" in internal_choice:
                    decrease = input("Decrease by? ")
                    query = f"UPDATE {table} SET {column} = {column} - %s"
                    cursor.execute(query, (decrease,))
                    connection.commit()
                    print("Column updated.")

                elif "multiply" in internal_choice:
                    multiply = input("Multiply by? ")
                    query = f"UPDATE {table} SET {column} = {column} * %s"
                    cursor.execute(query, (multiply,))
                    connection.commit()
                    print("Column updated.")

                elif "divide" in internal_choice:
                    divide = input("Divide by? ")
                    query = f"UPDATE {table} SET {column} = {column} / %s"
                    cursor.execute(query, (divide,))
                    connection.commit()
                    print("Column updated.")

                elif "set" in internal_choice:
                    value = input("Set value to: ")
                    query = f"UPDATE {table} SET {column} = %s"
                    cursor.execute(query, (value,))
                    connection.commit()
                    print("Column updated.")

                # Conditional update
                if "y" in condition:
                    cond = input("Provide condition after WHERE clause: ")
                    query = f"UPDATE {table} SET {column} = %s WHERE {cond}"
                    cursor.execute(query, (value,))
                    connection.commit()
                    print("Column updated with condition.")

            elif "insert" in choice:
                # Insert operation
                d = {}
                while True:
                    col = input("Enter column name: ")
                    val = input("Enter value: ")
                    d[col] = val
                    ask = input("More data (Y/N)? ").lower()
                    if "n" in ask:
                        break
                columns = list(d.keys())
                values = list(d.values())
                placeholders = ', '.join(['%s'] * len(values))
                query = f"INSERT INTO {table} ({', '.join(columns)}) VALUES ({placeholders})"
                cursor.execute(query, values)
                connection.commit()
                print("Inserted record successfully.")

            elif "delete" in choice:
                # Delete operation
                cnd = input("Enter condition after WHERE clause: ")
                query = f"DELETE FROM {table} WHERE {cnd}"
                cursor.execute(query)
                connection.commit()
                print("Deleted record successfully.")

            elif "alter" in choice:
                # Alter table operation (add/drop column)
                action = input("Modify / Add / Drop the column? ").lower()
                if action == "add":
                    column = input("Enter column name to add: ")
                    datatype = input("Enter datatype (e.g., INT, VARCHAR): ")
                    query = f"ALTER TABLE {table} ADD COLUMN {column} {datatype}"
                    cursor.execute(query)
                    connection.commit()
                    print(f"Column {column} added.")
                elif action == "drop":
                    column = input("Enter column name to drop: ")
                    query = f"ALTER TABLE {table} DROP COLUMN {column}"
                    cursor.execute(query)
                    connection.commit()
                    print(f"Column {column} dropped.")

            elif "drop" in choice:
                # Drop table operation
                query = f"DROP TABLE {table}"
                cursor.execute(query)
                connection.commit()
                print(f"Table {table} dropped.")

            elif "exit" in choice:
                print("Exiting Program....")
                cursor.close()
                connection.close()
                break

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
