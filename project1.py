print("________________________________________________________________________________")
print("\t ***** WELCOME TO STUDENT MANGEMENT SYSTEM *****")
l=['sonam','shanti','ashish']

def view_list():
    for i in range(len(l)):
        print(l[i])

def add_data():
    x=input("\n enter the name:")
    l.append(x)
    print("name add successful......")

def remove_data():
    name=input("enter the remove name:")
    if name in l:
        l.remove(name)
        print("record deleted successfull.....")
    else:
        print("record  not found")

def search_data():
    name=input("enter the search name:")
    if name in l:
        print(name)
    else:
        print("not found..")

while True:
    print("________________________________________________________________________________")
    print("please choose any one option: \n")
    print("1. To view a list:")
    print("2. To add a data:")
    print("3. To remove a data :")
    print("4. To search a data:")
    print("5. exit()")

    ch=int(input("Enter your choice: "))

    if ch==1:
        view_list()
    elif ch==2:
        add_data()
    elif ch==3:
        remove_data()
    elif ch==4:
        search_data()
    elif ch==5:
        exit()
    else:
        print("wrong input")

    g=input("do you continue(y/n):")
    print("_______")

    if g=="y":
        continue
    else:
        break





