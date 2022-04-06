import os

#Creating a list of all available .txt files
files = os.listdir("./temp_folder")

def reformater(target):
    """
    input: str
        file route to file meant to be converted to json
        ****FILE NAME CANNOT HAVE SPECIAL CHARACTERS****

    output: .json object
    """

    #Read file
    with open(f"./temp_folder/{target}", "r") as file:
        lines = file.readlines()
        
        #Add curly brackets to the beginning and end of target file contents
        lines[0] = "{"+lines[0]
        lines[-1] = lines[-1]+"}"

    #Splits file name at
    json_file = target.split(".")[0]+".json"

    #Exports .json file to temp folder
    with open(f"./temp_folder/{json_file}", "w") as file_j:
        file_j.writelines(lines)

#Iterating over the entire folder
[reformater(file) for file in files]

#Removing original files from temp folder
[os.remove(f"./temp_folder/{file}") for file in files]