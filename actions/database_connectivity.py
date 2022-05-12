# import mysql.connector
# def DataUpdate(FirstName,LastName,Feedback): 
#             mydb = mysql.connector.connect( host="localhost", user="root",  
#             passwd="8506", database="rasa_feedback") 
#             mycursor = mydb.cursor() 
#             #sql = "CREATE TABLE FeedBack_rasa (firstName VARCHAR(255),lastName VARCHAR(255), feedback VARCHAR(255))"
#             sql='INSERT INTO FeedBack_rasa (firstName, lastName, feedback) VALUES ("{0}","{1}", "{2}");'.format(FirstName,LastName,Feedback) 
#             mycursor.execute(sql) 
#             mydb.commit()