import os
import subprocess


# symbol = ":;<=>?@!\"#$%&'()*+,-./\n"
# symbol = "\n"

def check_dir():
    # Go to [export] in current folder, if it wasn't exist,then create it.
    try:
        os.chdir("export")
    except:
        os.mkdir("export")
    else:
        os.chdir("..")

# def opt_funcion(usrinput):
#     while True:
#         if usrinput == 1:
#             # Convert input string
#             convert(ori_string, shift_value)
#         elif usrinput == 2:
#             # Input Text file
#         elif usrinput == 3:
#             # input multiple files
#             pass
#         else:
#             continue

def im_port():
    # An input loop until the path is correct.
    while True:
        print("Drag the file here or keyin the pathname.")
        file_path = input(">>> ")
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

# def multi_im_port():
#     data_list = []
#     data_name_list = []
#     file_path_list = []
#     while True:
#         print("Drag the file here or keyin the pathname.")
#         print("Keyin 'q' to finish the input.")
#         file_path = input(">>> ")
#         if file_path in ["q","Q"]:
#             for file_path in file_path_list:

#                 try:
#                     with open(file_path, "r") as file:
#                         # read the file assign to the data
#                         data = file.read()
#                         data_list.append(data)
#                         data_name_list.append(file_path.split("/")[-1])
#                 except Exception as Error_info:
#                     # Print Error informaiton..
#                     print(Error_info)

#             if len(data_list) > 0:
#                 return data_list,data_name_list
#             else:
#                 file_path_list = []

#         else:
#             file_path_list.append(file_path)

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

    print(new_string)
    return new_string

    # def convert(ori_string,shift_value):

    # new_string = ""
    # for character in ori_string:
    #     if character not in symbol:
    #         character = chr(ord(character)+shift_value)
    #     if character != "\n":
    #         new_string += character

    # print(new_string)
    # return new_string

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
            while True:
                print("Input shift value:")
                try:
                    shift_value = int(input(">>> "))
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
            ori_string = im_port()

            print("Input shift value:")
            shift_value = int(input())

            data = convert(ori_string[0],shift_value)
            ex_port(data,ori_string[1])
            #Reveal in Finder
            subprocess.call(["open","export"])
            subprocess.call(["open","export/test_convert.txt"])

        # elif function_option == "3":
        #     ori_string = multi_im_port()[1]
        #     print(ori_string)
        #     #Reveal in Finder
        #     subprocess.Popen("open export",shell=True)

        elif function_option == "w":
            subprocess.call(["pwd"])

        elif function_option in ["q","Q","Quit","QUIT"]:
            terminate_info = "\n\t+"+"-"*33+"+"+"\n\t|  Function has been terminated!  |\n\t"+"+"+"-"*33+"+"
            print("\n"*20)
            exit(terminate_info)
        else:
            print("\n----Error Input!----\n")

if __name__ == "__main__":
    main()
