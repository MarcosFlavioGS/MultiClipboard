import sys
import clipboard
import json
# Comentário mais para me lembrar que quando o erro  : AttributeError: partially initialized module 'MODULE_NAME' has no attribute... 
# É prq dei o mesmo no do modulo para o arquivo. Causando uma "circular reference"

SAVED_DATA = "clipboard.json"

def save_data(filepath, data):
    with open(filepath, "w", encoding = "utf-8") as f:
        json.dump(data, f)        

def load_data(filepath):
    try:
        with open(filepath, "r", encoding = "utf-8") as f:
            data = json.load(f)
            return data
    except:
        return {}        


if len(sys.argv) ==2:
    command = sys.argv[1]
    data = load_data(SAVED_DATA)
    
    if command == "save":
        key = input("Enter a key ")
        data[key] = clipboard.paste()
        save_data(SAVED_DATA, data)
        print("Key saved.")
    elif command == "load":
        key = input("Enter a key ")
        if key in data:
            clipboard.copy(data[key])
            print("data copied to clipboard.")
        else:
            print("Key does not exist.")    

    elif command == "list":
        print(data)
    else:
        print("unknown command")  
else:
    print("Please pass exactly one command")                