import read_write as rw


#gets a list from a  txt file inside of a directory


#opens a list and asks the user to rate eache topic, returning the rating necessary to the next sterps
def get_list(p1_list):
    rate_list_1 = []
    for x in p1_list:
        idea, question = x.split(",")
        print()
        print(question +"\n")
        rate = input("Por favor qualifique o nível de identificação de 1 a 5 do seu incômoco como a o pensamneto acima sugerido \n")
        new_line = idea, question.replace("\n", ",") + rate
        rate_list_1.append(new_line)
    return rate_list_1


rate_list_1 = get_list(p1_list = rw.data("D:\\MAIN DRIVE\\RUN DRIVE\\PYTHON\\Projects\\ThoughtsProject\\Selection\\p1\\p1.txt"))

    
    
for x in rate_list_1:
    print(x)