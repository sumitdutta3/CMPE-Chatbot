# CMPE Department Chatbot
Transition to the graduate environment leaves students with many unanswered questions. International students strive hard finding the Point of Contact to many department related queries. Hence, this chatbot has been created that handles all the queries a student might have regarding the CMPE graduate course.
This chatbot is capable of handing several utterances including multi-turn conversations. The API functionality has been tested and the chatbot succeeded in pulling the weather & population details. At the end, the chatbot requests for a feedback on a scale from 0 to 10, and stores the value in a database (MySQL here).


## Purpose
Generally a high influx of students have similar queries upon beginning graduate studies, ranging from what their core subjects are, which areas of specialization they are allowed to take etc.
Hence it is prudent to save time and resources spent on these tasks by having a system that automates such tasks. Further, students would also have 24X7 access to it so they do not have to wait for a real person to get their queries answered.


## Contents
This chatbot is capable of understanding more than 20 user utterances/queries (~32 utterances here).
It has few set of rules and multi-turn interactive conversations. It also has few stories that focus on small talk (e.g., hi, how are you, etc.).

Future implementations can expand the chatbot's ability to answer a diverse range of topics. It can be done by having more intents and data/stories. However, the current implementation fulfills the scope and goal of the project. A future scope would be each department in the University incorporating such a bot thereby enabling many students avail benefits from it.

## Capabilities
This bot can provide the user with the following information when prompted:

1. Assist students with all the major CMPE department related queries.

2. The chatbot is trained well through several utterances and can handle multi-turn conversations.

3. This chatbot has the ability to make 2 API calls (weather and population) and can pull relevant details.

4. This chatbot collects and store a user's feedback post the conversation in a database MYSQL.

5. This chatbot has been integrated with Slack.

## Implemented Conversation Flows

#### Example 1:
```python
User ->  hi
Bot -> Hey! How are you? How may I assist you?
User ->  What are the mandatory core courses for the MS CMPE program?
Bot -> To be eligible for a MS CMPE degree, you need to complete following mandatory core courses:
          (1) CMPE 200 - Computer Architecture
          (2) CMPE 220 - System Software
          (3) CMPE 240 - Advance Computer Design
User ->  What are the conditions required for advancement to graduation candidacy?
Bot -> For advancement to graduate candidacy, following conditions should be met:
          (1) Pre requisites should be completed
          (2) GWAR should be completed
          (3) Minimum GPA of 3.0 should be maintained
          (4) Core courses should be completed
```

#### Example 2 (Multi-turn conversation):
```python
User -> What are the areas of specialization that MS CMPE program allow?
Bot -> MS CMPE program offers below areas of specialization:
          (1) System Software Architecture
          (2) Network System
          (3) Embedded Systems
          (4) Cyber Security
          (5) Machine Learning Engineering
		  
User -> I am interested in Machine Learning
Bot -> To specialize in Machine Learning, you need to complete three courses from the following:
          (1) CMPE 252 - Artificial Intelligence & Data Engg 
          (2) CMPE 255 - Data Mining
          (3) CMPE 256 - Advance Data Mining
          (4) CMPE 257 - Machine Learning
          (5) CMPE 258 - Deep Learning
          (6) CMPE 260 - Reinforcement Learning
		  
Multi-turn conversation-2
User -> Who is my point of contact for fees related issues
Bot -> Bursars office is your point of contact for any fees related issues. Please feel free to contact them at https://www.sjsu.edu/bursar/
User -> Can I pay fees in installments?
Bot -> Yes, you are allowed to pay fees in installments. Please contact Bursars office at https://www.sjsu.edu/bursar/ for any further information.
```

#### Example 3 (API's- weather/population):
```python
User ->  hi
Bot -> Hey! How are you? How may I assist you?
User ->  Can I know the weather?
Bot -> Which city do you want to check the weather for?
User ->  San Jose
Bot -> Todays temperature is 12 degree Celcius.

	API-2(population)
User ->  hi
Bot -> Hey! How are you? How may I assist you?
User ->  Can I know the population?
Bot -> Which state do you want to check the population for?
User ->  Arizona
Bot -> The population is 7278717.
```

#### Example 4 (Storing data into a database- MySQL):
```python
User -> How many credits are required for MS CMPE?
Bot -> You are required to complete 33 units + set of pre requisites (if you have any)
User -> thanks
Bot -> I am glad to be of your help. If you are satisfied by my service today, would you mind taking a survey to help me further improve?
User ->  sure
Bot -> On a scale of 0 to 10 with 0 being the lowest and 10 being the highest, how would you rate my service today?
User ->  10
Bot -> Thank you, I appreciate your valuable feedback!
```
These examples illustrate the  conversations flows implemented in this chatbot.

## Notes
In order to run this program, install all the packages in the requirements.txt which will ensure correct versions being installed. Additionally, it is crucial to note that the chatbot is applicable for CMPE dept. grad students.
Rasa version: 3.0.0
MySQL version: 8.0