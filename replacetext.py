import logging
def replace_Text_fun():
    logging.info("File Execution started")
    #This is orginal text
    orginal_Text= "placement"
    #This is test to be replaced
    replace_Text = "screening"

    try:
        #To open the file
        f = open("Example.txt", "r+")
    except:
        logging.error("Error occured while opening Example.txt File")
        print("Can't open the File")

    #To read the file
    lines_in_files = f.readlines()
    logging.info("Extracted lines from the files")
    #c = 0
    for i in lines_in_files:
        if orginal_Text in i:
            #To replace the orginal text with replace test
            Replacement = i.replace(orginal_Text,replace_Text)
            lines_in_files = Replacement
            logging.info("replacement done")
       # c += 1
    
    #It will delete all file contents
    f.truncate(0)
    logging.info("Deleted the contents of files")
    
    #It will go to start of file contents
    f.seek(0)

    try:
        logging.info("Writing replaced contents into the file")
        # It will write in the files
        f.writelines(lines_in_files)
    except:
        logging.error("Error occured while writing into the file")
        print("Cant writ into the files")
    finally:
        #To close the file.
        f.close()
        logging.info("File closed sucessfully")
logging.basicConfig(filename = "replacetextlog.log" ,level = logging.INFO, format ='%(asctime)s %(levelname)s %(message)s')
replace_Text_fun()
