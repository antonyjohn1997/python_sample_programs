import os

path = "D:/sample projects/"

files_list = []

# Walk through the directory tree rooted at 'path'
for root, d_names, f_names in os.walk(path):
    print("Root:", root)
    print("Directories:", d_names)
    print("Files:", f_names)
    
    # Collect file paths into a list
    for f in f_names:
        files_list.append(os.path.join(root, f))

print("All files found:", files_list)
