import json

def file_reformater(target):
    """
    input: str
        file route to file meant to be converted to json
        ****FILE NAME CANNOT HAVE SPECIAL CHARACTERS****

    output: .json object
    """

    #Read file
    with open(f"./temp_files/raw/{target}", "r") as file:
        lines = file.readlines()
        
        #Add curly brackets to the beginning and end of target file contents
        lines[0] = "{"+lines[0]
        lines[-1] = lines[-1]+"}"

    #Splits file name at
    json_file = target.split(".")[0]+".json"

    #Exports .json file to temp folder/formatted
    with open(f"./temp_files/formatted/{json_file}", "w") as file_j:
        file_j.writelines(lines)