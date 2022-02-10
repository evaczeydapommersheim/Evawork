# Why does expression cause an error: 
# message = "I have eaten " + 99 + "burritos."
# print(message)

# ANSWER: CAUSES AN ERROR AS 99 IS CONSIDERED AN INTEGER AND NOT A STRING. ARTING CANNOT BE ADDED TO AN INT AND VICE VERSA.

# Author: Eva Czeyda-Pommersheim

message = "I have eaten " + "99" + " burritos."
print(message)