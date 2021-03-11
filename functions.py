import pandas as pd
def logins():
 file_path = "logins.csv"
 df = pd.read_csv(file_path, delimiter=";")
 username_list = df["username"].tolist()
 password_list = df["password"].tolist()
 #print(username_list)
 #print(password_list)
 dictionary = dict(zip(username_list, password_list))
 print(dictionary)
 return dictionary
