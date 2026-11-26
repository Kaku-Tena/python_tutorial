file = None
try:
    file = open("data.txt", "r")
    print("--- Reading from data.txt ---")
    for line in file:
        print(line.strip())
    print("--- Finished Reading ---")
except FileNotFoundError:
    print("Error: The file 'data.txt' was not found.")
except Exception as e:
    print(f"An unexpected error occured: {e}")
finally:
    if file is not None and not file.closed:
        file.close()
        print("File has been closed")



file = open("output.txt", "w")
file.write("Hello, World!\n")
file.write("This is a second line.!\n")
file.close()

file = open("output.txt", "a")
file.write("This line was appended to the end.\n")
file.close()

           

