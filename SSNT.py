import os
import subprocess

def check_dir():
    # Go to [export] in current folder, if it wasn't exist,then create it.
    try:
        os.chdir("export")
    except:
        os.mkdir("export")
    else:
        os.chdir("..")

def im_port():
    # An input loop until the path is correct.
    while True:
        print("Drag the file here or keyin the pathname.")
        file_path = input(">>> ")
        print()
        try:
            # try to open the file
            with open(file_path, "r") as file:
                # If the file is readable, assign it to data
                data = file.read()
                # Get the file' name by split method
                name = file_path.split("/")[-1]
            return data,name
        except:
            # If it went wrong, go back and loop again.
            continue
            file_path_list.append(file_path)

def ex_port(data,name):
    check_dir()

    file_name = name.split(".")[0]
    file_extention = name.split(".")[1]
    os.chdir("export")
    with open(file_name+"_convert."+file_extention,"w") as file:
        file.write(data)
    os.chdir("..")

def convert(ori_string,shift_value):

    new_string = ""
    for character in ori_string:
        character = chr(ord(character)+shift_value)
        new_string += character

    print("-"*20+"Start line"+"-"*20)
    print(new_string)
    print("-"*21+"End line"+"-"*21)
    print()
    return new_string

def main():
    while True:
        print("\nWhat would you like to do?")
        print("\t- 1. Convert a string.")
        print("\t- 2. Convert a text file.")
        print("\t- w. Get current working directory.")
        print("\t- q. Exit.")
        function_option = input(">>> ")
        print()

        if function_option == "1":
            # Convert a string
            print("Input anying:")
            ori_string = input(">>> ")
            print()
            while True:
                print("Input shift value:")
                try:
                    shift_value = int(input(">>> "))
                    print()
                except:
                    print("Invalid input!")
                    continue
                else:
                    if shift_value < 1000000:
                        # limit is 0x110000 which is 1114112
                        convert(ori_string,shift_value)
                        break
                    else:
                        print("Input a number under 1,000,000!")
                        continue

        elif function_option == "2":
            # Convert a Text
            ori_string = im_port()

            print("Input shift value:")
            shift_value = int(input(">>> "))
            print()

            data = convert(ori_string[0],shift_value)
            ex_port(data,ori_string[1])
            #Reveal in Finder
            subprocess.call(["open","export"])

        elif function_option == "w":
            # Show Current working directory
            subprocess.call(["pwd"])

        elif function_option in ["q","Q","Quit","QUIT"]:
            # Terminate the fuctiion
            terminate_info = "\n\t+"+"-"*33+"+"+"\n\t|  Function has been terminated!  |\n\t"+"+"+"-"*33+"+"
            print("\n"*20)
            exit(terminate_info)
        else:
            # Show Invalid Input!
            print("\n----Invalid Input!----\n")

if __name__ == "__main__":
    main()
