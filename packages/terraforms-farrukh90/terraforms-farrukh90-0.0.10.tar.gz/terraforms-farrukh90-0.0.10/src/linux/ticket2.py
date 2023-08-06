import os 

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 


def filestructure():
    FILETOWORK="/tmp/fruits"
    fruits = ["apple", "pear", "peach", "grape", "banana"]
    try:
        # Checks if /tmp/fruits is created
        if os.path.getsize(FILETOWORK) <= 0:
            print(bcolors.FAIL + FILETOWORK + " " + "seems to be empty" + bcolors.ENDC  )
        else:
            with open(FILETOWORK) as file_content:
                contents = file_content.read()
                for x in contents.splitlines():
                    if fruits[0] in x and fruits[1] in x and fruits[2] in x and fruits[3] in x and fruits[4] in x: 
                        print(bcolors.OKGREEN + FILETOWORK + " has a proper content"+ bcolors.ENDC)
                    else: 
                        print(bcolors.FAIL + FILETOWORK + " does not have a proper content"+ bcolors.ENDC)
    except FileNotFoundError:
        print(bcolors.FAIL +  FILETOWORK + " is not created"+ bcolors.ENDC)



    try:
        FILETOWORK="/tmp/services"
        # Checks if /tmp/services is created
        if os.path.getsize(FILETOWORK) <= 0:
            print(bcolors.FAIL + FILETOWORK + " seems to be empty" + bcolors.ENDC  )
        elif os.path.isfile(FILETOWORK):
            print(bcolors.OKGREEN + FILETOWORK + " has been created"+ bcolors.ENDC)
        else:
            print(bcolors.FAIL +  "Something went wrong please try again" + bcolors.ENDC)
    except FileNotFoundError:
        print(bcolors.FAIL +  FILETOWORK + " is not created"+ bcolors.ENDC)

    try:
        FILETOWORK="/tmp/top10"
        num_lines = sum(1 for line in open(FILETOWORK))
        # Checks if /tmp/top10 is created
        if os.path.getsize(FILETOWORK) <= 0:
            print(bcolors.FAIL + FILETOWORK + " seems to be empty" + bcolors.ENDC  )
        elif os.path.isfile(FILETOWORK) and num_lines == 10:
            print(bcolors.OKGREEN + FILETOWORK + " has been created and has %d lines" % num_lines + bcolors.ENDC)
        else:
            print(bcolors.FAIL +  FILETOWORK + " has not been created or has %d lines" % num_lines + bcolors.ENDC)
    except FileNotFoundError:
        print(bcolors.FAIL +  FILETOWORK + " is not created"+ bcolors.ENDC)

    try:
        FILETOWORK="/tmp/bottom10"
        num_lines = sum(1 for line in open(FILETOWORK))
        # Checks if /tmp/bottom10 is created
        if os.path.getsize(FILETOWORK) <= 0:
            print(bcolors.FAIL + FILETOWORK + " seems to be empty" + bcolors.ENDC  )
        elif os.path.isfile(FILETOWORK) and num_lines == 10:
            print(bcolors.OKGREEN + FILETOWORK + " has been created and has %d lines" % num_lines + bcolors.ENDC)
        else:
            print(bcolors.FAIL +  FILETOWORK + " has not been created or has %d lines" % num_lines + bcolors.ENDC)
    except FileNotFoundError:
        print(bcolors.FAIL +  FILETOWORK + " is not created"+ bcolors.ENDC)

    try:
        FILETOWORK="/tmp/sorted_fruits"
        # Checks if /tmp/sorted_fruits is created
        if os.path.getsize(FILETOWORK) <= 0:
            print(bcolors.FAIL + FILETOWORK + " seems to be empty" + bcolors.ENDC  )
        elif os.path.isfile(FILETOWORK):
            print(bcolors.OKGREEN + FILETOWORK + " has been created"+ bcolors.ENDC)
        else:
            print(bcolors.FAIL +  "Something went wrong please try again" + bcolors.ENDC)
    except FileNotFoundError:
        print(bcolors.FAIL +  FILETOWORK + " is not created"+ bcolors.ENDC)

    try:
        FILETOWORK="/tmp/counted_services"
        # Checks if /tmp/counted_services is created
        if os.path.getsize(FILETOWORK) <= 0:
            print(bcolors.FAIL + FILETOWORK + " seems to be empty" + bcolors.ENDC  )
        elif os.path.isfile(FILETOWORK):
            print(bcolors.OKGREEN + FILETOWORK + " has been created"+ bcolors.ENDC)
        else:
            print(bcolors.FAIL +  "Something went wrong please try again" + bcolors.ENDC)
    except FileNotFoundError:
        print(bcolors.FAIL +  FILETOWORK + " is not created"+ bcolors.ENDC)
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
 
 

 
 