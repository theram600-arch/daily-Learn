# file = open("data.txt", "r")
# contest=file.read()
# print(contest)
# file.close()


# file=open("data.txt", "w")
# file.write("\nlearomg i/o files")
# file.close()

# inp=input("enter whtaq you wanna write: ")
# with open("data.txt", "a") as file:
#     file.write(inp +"\n")
    

# with open("data.txt","r") as file:                          
#     cont=file.read()                                                  if we wanna read character , just split it into string and print
#     print(len(cont))


# with open("data.txt","r") as file:
#     cont=file.readlines()
#     print(len(cont))

#                                                                         find longest word
# with open("data.txt","r") as file:
#     cont=file.read().split()
# longest=""
# for word in cont:
#     if len(word)>len(longest):
#         longest=word
# print(longest)




# while True:
#     print("\n1. Add Note")
#     print("2. View Notes")
#     print("3. Exit")

#     choice = input("Choose option: ")

#     if choice == "1":
#         note = input("Write your note: ")

#         with open("dat.txt", "a") as file:
#             file.write(note + "\n")

#         print("Note saved!")

#     elif choice == "2":
#         with open("data.txt", "r") as file:
#             print("\nYour Notes:")
#             print(file.read())

#     elif choice == "3":
#         break




# print("1. Register")
# print("2. Login")

# choice = input("Choose: ")

# if choice == "1":
#     username = input("Enter username: ")
#     password = input("Enter password: ")

#     with open("dat.txt", "a") as file:
#         file.write(username + "," + password + "\n")

#     print("User registered!")

# elif choice == "2":
#     username = input("Enter username: ")
#     password = input("Enter password: ")

#     with open("data.txt", "r") as file:
#         users = file.readlines()

#     for user in users:
#         u, p = user.strip().split(",")

#         if u == username and p == password:
#             print("Login successful!")
#             break
#     else:
#         print("Invalid credentials")


















