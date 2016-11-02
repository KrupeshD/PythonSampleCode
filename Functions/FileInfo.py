def list_file_info(size=False, create_date=False, mod_date=False):
    """Returns requested infromation about the given file"""

    file_info={}
    if size:
        ##Code to get size information goes here
        file_info['size']="PASS"
        if create_date:
            ##Code to get created date goes here
            file_info['create_date']="PASS"
            if mod_date:
                #Code to get last modify date goes here
                file_info['mod_date']="PASS"



    return file_info

print(list_file_info(size=True,create_date=True,mod_date=True))