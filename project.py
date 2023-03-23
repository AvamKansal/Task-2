import datetime
print("\tWELCOME TO LIBRARY")
print(f"Current Date: {datetime.date.today()}")
Name= input("enter Your name - ")
Roll_Num = input("Enter your roll NUmber - ")
print("""
        1.Issue book[1]
        2.Return book[2]""")
print("What would you like to do:")
action=input()
maths=["College  mathematics","THe Universal history of Numbers","THe man who counted","The triumph by numbers"]
physics=["7 brief lessons in physics","feynman lectures on physics","the elegant universe","a brief history of time"]
program=["A python crash course","Learn python the hard way","Python in 30 days","Automate boring stuff with python"]
if action=="1":
    print("\nPlease state the subject of the book you would like to issue:")
    print("""
    \t1.Maths[m]
    \t2.Physics[p]
    \t3.Programming[pr]
    """)
    subject=input("\nSubject: ")
    
    if subject=="m":

        print("""
        1.College  mathematics[1]
        2.The Universal history of Numbers[2]
        3.The man who counted[3]
        4.The triumph by numbers[4]
        """)
        title=input("Book Name: ")
        print(f"""
        BOOK SUCCESSFULLY ISSUED by - """, Name)
        print("        Roll Number - ", Roll_Num)
        print(f"""
        BOOK NAME:{maths[int(title)-1].title()}
        DATE ISSUED:{datetime.date.today()}
        RETURN BY: {datetime.date.today()+datetime.timedelta(days=7)}""")
    if subject=="p":

        print("""
        1.7 brief lessons in physics[1]
        2.feynman lectures on physics[2]
        3.the elegant universe[3]
        4.a brief history of time[4]
        """)
        title=input("Book Name: ")
        print(f"""
        BOOK SUCCESSFULLY ISSUED by - """, Name)
        print("        Roll Number - ", Roll_Num)
        print(f"""
        BOOK NAME:{physics[int(title)-1].title()}
        DATE ISSUED:{datetime.date.today()}
        RETURN BY: {datetime.date.today()+datetime.timedelta(days=7)}""")
    if subject=="pr":

        print("""
        1.A python crash course[1]
        2.Learn python the hard way[2]
        3.Python in 30 days[3]
        4.Automate boring stuff with python[4]
        """)
        title=input("Book Name: ")
        print(f"""
        BOOK SUCCESSFULLY ISSUED by - """, Name)
        print("        Roll Number - ", Roll_Num)
        print(f"""
        BOOK NAME:{program[int(title)-1].title()}
        DATE ISSUED:{datetime.date.today()}
        RETURN BY: {datetime.date.today()+datetime.timedelta(days=7)}""")
if action=="2":
    #returns

    print("""
            MATHS[m]
            1.College  mathematics[1]
            2.The Universal history of Numbers[2]
            3.The man who counted[3]
            4.The triumph by numbers[4]
            """)
    print("""
           PHYSICS[p]
           1.7 brief lessons in physics[1]
           2.feynman lectures on physics[2]
           3.the elegant universe[3]
           4.a brief history of time[4]
           """)
    print("""
            PROGRAMMING[pr]
            1.A python crash course[1]
            2.Learn python the hard way[2]
            3.Python in 30 days[3]
            4.Automate boring stuff with python[4]
            """)
    book_name=[i for i in input("Please enter book subject and name code:  ").split()]
    date1=input("Issue date[YYYY-MM-DD]:")
    date=datetime.datetime.strptime(date1,"%Y-%m-%d")
    difference = (datetime.date.today() - datetime.timedelta(days=7) - date.date()).days
    fine = difference * 5
    if book_name[0]=="m":
        if date.date()<datetime.date.today()-datetime.timedelta(days=7):
            print(f"You failed to return '{maths[int(book_name[1])-1].title()}' on time.You have to pay a fine of {fine}.")
