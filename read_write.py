



#reads a txt file and returns a list

def data(string):
    read_list = []
    with open(string, mode="r", encoding="utf-8") as file:
        r = file.readlines()
        for line in r:
            read_list.append(line)
        return read_list
    
    
#writes data into a txt file