file_path = 'data.txt'  # Replace with your file's path

try:
    with open(file_path, 'r') as file:
        file_contents = file.read()
        # You can process the file_contents here
        # For example, print it or store it in another variable
        processed_data = file_contents.split('\n')  # Split content into lines
        print(processed_data)
except FileNotFoundError:
    print(f"File '{file_path}' not found.")
