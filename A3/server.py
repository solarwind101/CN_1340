import socket
import sys

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 60134
server_socket.bind((host, port))
server_socket.listen(10)

# Questions
Questions = ["1. What is the total number of CS credits required to complete the 4-year BSc Hons degree in Computer Sciences",
             "2. Could you provide the breakdown of CS credits?",
             "3. What is the list of CS core course?",
             "4. What are the foundation courses? Why should I even do them given that I wish to pursue a major in computer science?"
             "5. Can you please provide the list the foundation courses?",
             "6. What are the open credits? Can I take a course from CS department under open credits?",
             "7. What are the non academic credits",
             "8. What is the example path that I need to follow to obtain 4 Year BSc Computer Science?",
             "9. What is Capstone Project? When can I do it?",
             "10. What are the prerequsite for Each CS Course?"
             ]

#Q3
core_courses = {
    "Categary 1: Basic Science and Maths": [
        "P&S",
        "Linear Algebra",
        "Calculus",
        "Physics",
        "Biology"
    ],
    "Categary 2: Computational thinking": [
        "Introduction to Computer Science",
        "Discrete Mathematics",
        "Data Structures and Algorithms",
        "Introduction to Machine Learning",
        "Data Science and Management",
        "Theory of Computation",
        "Design and Analysis of Algorithms",
        "Programming Languages and Translation",
        "Information Security"
    ],
    "Categary 3: Systems and Software": [
        "Computer Organisation and Systems",
        "Design Practices in CS",
        "Computer Networks",
        "Embedded Systems",
        "Capstone Project"
    ]
}

#Q4
why_FC = "Good Question! The Foundation Courses are a must for you, no matter what your major is. They offer a diverse perspective and a well-rounded understanding of human knowledge, ensuring you're well-prepared for your future, both academically and in all aspects of life. We wish to prepare better human being, not just an educated person."

#Q5
foundation_courses = [
    "Economy, Politics and Society",
    "Environmental Studies",
    "Great Books",
    "Indian Civilizations",
    "Literature and the World",
    "Mind and Behaviour",
    "Principles of Science",
    "Quantitative Reasoning and Mathematical Thinking"
    "Introduction to Critical Thinking"
]

#Q2
CS_credits = ["A minimum of 86 credits from the Computer Science Department, divided as follows:",
    "1. The student must complete 74 credits of CS core courses",
    "2. Additionally, a student can take a minimum of 12 credits in CS elective courses.",
    "3. Students need to achieve a minimum grade of “B” in both Introduction to Computer Science and Discrete Mathematics courses."
]


#Q6
Open_credits= "A student can take courses worth of 22 credits under open credit category. These 22 academic credits can be earned by taking courses from any department within the university, including the Computer Science Department"



#Q7
NONacad_Credits = ["To gradute with a 4 Year BSc Computer Science, a student has to complete a minimum of 6 non-academic credits apart from other requirements. They includes", 
                   "-4 credits designated for co-curricular courses",
                   "-2 credits allocated for internship experience"]

#Q1
credit_requirements = {"Academic Credits": 
                       ["FC Credits : 36 ",
                        "CS Credits : 86",
                        "Open Credits : 22"],

                       "Non-academic Credits": 
                        ["Co-curricular Credits : 4",
                         "Internship Credits : 2"]
}

#Q8
course_path = {
    "1st Semester": ["Calculus"],
    "2nd Semester": ["Introduction to Computer Science", "Discrete Mathematics"],
    "3rd Semester": ["Probability and Statistics", "Linear Algebra", "Data Structures and Algorithms"],
    "4th Semester": ["Theory of Computation", "Computer Organisation and Systems"],
    "5th Semester": ["Design Practices in CS", "Introduction to Machine Learning", "Computer Networks", "Information Security (2 credits)"],
    "6th Semester": ["Design and Analysis of Algorithms", "Data Science and Management", "Embedded Systems"],
    "7th Semester": ["Capstone Project", "Programming Languages and Translation"],
    "8th Semester": []
}

#Q9
capstone_project = "Capstone Project is a research project that you undertake under the guidance of a faculty member in the department, and you can earn credit for it. It essentially involves the integration of theoretical knowledge with practical application of that knowledge and skill. You can complete a Capstone Project in your 7th and/or 8th semester during your 4-Year BSc program."

#Q10
course_prereq = { "P&S" : ["Mathematics in Grades XI and XII OR Quantitative Reasoning and Math-ematical Thinking + Calculus Enabler"],
                 "Linear Algebra": ["NA"],
                 "Calculus" : ["NA"],
                 "Physics": ['NA'],
                 "Biology" : ['NA'],
                "Introduction to Computer Science": ["Mathematics in Grades XI and XII OR a minimum of B grade in both Quantitative Reasoning and Mathematical Thinking and Calculus"],
                "Discrete Mathemetics" : ["Mathematics in Grades XI and XII OR a minimum of B grade in both Quantitative Reasoning and Mathematical Thinking and Calculus"],
                "Data Structures and Algorithms":  ["Introduction to Computer Science", "Discrete Mathematics"],
                "Theory of Computation" :  ["Data Structures and Algorithms"],
                "Computer Organisation and Systems" : ["Introduction to Computer Science"],
                "Introduction to Machine Learning" : ["Probability and Statistics", "Linear Algebra", "Data Structures and Algorithms"],
                "Design Practices in CS" : ["Data Structures and Algorithms", "Computer Organisation and Systems"],
                "Computer Networks" : ["Introduction to Computer Science",  "Data Structures and Algorithms"],
                "Information Security":  ["Data Structures and Algorithms", "Probability and Statistics"],
                "Design and Analysis of Algorithms" : ["Data Structure and Algorithms", "Linear Algebra"],
                "Data Science and Management": ["Data Structures and Algorithms" , "Introduction to Machine Learning"],
                "Programming Languages and Translations":  ["Data Structures and Algorithms" , "Theory of Computation"],
                "Embedded Systems": ["Computer Organisation and Systems"]                                     
}



####################### SERVER UP ##############################
print('SERVER UP.....\n')
################################################################

############## DRIVE FUNCTION STARTS ###########################
def query_response(client_socket):

    print("Client Connected!\n\n")
    welcome_message = "Hi there! Welcome to the Department of Computer Science at Ashoka University. How can we assist you today?\n\n"
    welcome_message += "Here are some frequently asked questions about majoring in computer science. Please select a question number to get the answer:\n"
    welcome_message += "\n".join(Questions)

    client_socket.send(welcome_message.encode())

    while True:
        Qno = client_socket.recv(1024).decode()
        if int(Qno)==1:
            message = "The 4-year BSc Hons degree in Computer Science mandates a minimum of 150 credits for completion, ensuring a well-rounded education encompassing both core computer science knowledge and broader academic experiences.\nThese credits are classified into two categories:\n"
            for key, value in credit_requirements.items():
                message += f"{key}:\n"
                for item in value:
                    message += f"{item}\n"
                message +="\n"

            client_socket.send(message.encode())
            client_socket.send("Do you want to ask another Question Y/N".encode())
            response = client_socket.recv(1024).decode()
            if response.lower()!='y':
                break

        elif int(Qno)==2:
            message = ""
            for item in CS_credits:
                message += f"{item}\n"

            client_socket.send(message.encode())

            client_socket.send("Do you want to ask another Question Y/N".encode())
            response = client_socket.recv(1024).decode()
            if response.lower()!='y':
                break

        elif int(Qno) == 3:
            message = "Following are the CS core courses boardly divided into three categaries:\n"
            for key, value in core_courses.items():
                message +=f"{key}:\n"
                for item in value:
                    message += f"{item}\n"    
                message +="\n"      
            client_socket.send(message.encode())

            client_socket.send("Do you want to ask another Question Y/N".encode())
            response = client_socket.recv(1024).decode()
            if response.lower()!='y':
                break

        elif int(Qno)==4:
            client_socket.send(why_FC.encode())

            client_socket.send("Do you want to ask another Question Y/N".encode())
            response = client_socket.recv(1024).decode()
            if response.lower()!='y':
                break


        elif int(Qno) == 5:
            message = ''
            for course in foundation_courses:
                message += f"{course}\n"
            client_socket.send(message.encode())

            client_socket.send("Do you want to ask another Question Y/N".encode())
            response = client_socket.recv(1024).decode()
            if response.lower()!='y':
                break

        elif int(Qno) == 6:
            client_socket.send(f"{Open_credits}\n".encode())

            client_socket.send("Do you want to ask another Question Y/N".encode())
            response = client_socket.recv(1024).decode()
            if response.lower()!='y':
                break

        elif int(Qno)==7:
            message = ''
            for item in NONacad_Credits:
                message += f"{item}\n"
            client_socket.send(message.encode())

            client_socket.send("Do you want to ask another Question Y/N".encode())
            response = client_socket.recv(1024).decode()
            if response.lower()!='y':
                break

        elif int(Qno)==8:
            message = ""
            for key, value in course_path.items():
                message += f"{key}:\n"
                for i in value:
                    message += f"{i}\n"
                message +="\n"
                
            client_socket.send(message.encode())

            client_socket.send("Do you want to ask another Question Y/N".encode())
            response = client_socket.recv(1024).decode()
            if response.lower()!='y':
                break

        elif int(Qno)==9:
            client_socket.send(f"{capstone_project}\n".encode())

            client_socket.send("Do you want to ask another Question Y/N".encode())
            response = client_socket.recv(1024).decode()
            if response.lower()!='y':
                break

        elif int(Qno)==10:
            message = ''
            for key, value in course_prereq.items():
                message += f"{key}:\n"
                for i in value:
                    message += f"{i}\n"
                message += "\n"
            client_socket.send(message.encode())

            client_socket.send("Do you want to ask another Question Y/N".encode())
            response = client_socket.recv(1024).decode()
            if response.lower()!='y':
                break

        else:
            client_socket.send("Invalid Input! Please enter a valid question number:".encode())

############## DRIVE FUNCTION ENDS ###########################
        
while True:
    print("Server is waiting for a connection....")
 
    (client_socket, address) = server_socket.accept()
    print(f"Connection from: {address}")

    query_response(client_socket)

    client_socket.close()

# Closing the server...
server_socket.close()
############## THE END ###########################
