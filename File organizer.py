import os
import shutil
path = input("Enter path: ")
files = os.listdir(path)
for file in files:
    filename, extension = os.path.splitext(file)
    extension1 = extension[1:]
    extension = extension1.upper()
    destination = os.path.join(path, extension)
    # Destination variable for where the file will go
    if os.path.exists(destination):
        pass
    else:
        os.makedirs(destination)

    file_source = os.path.join(path, file)
    # file_source variable for where the file is from

    shutil.move(file_source, os.path.join(destination, file))
    # move function = file source , file destination
