import pandas as pd
Data ={
    "Name":["Uday","Ashish","Vishal","Sachin","Harsh"],
    "Age" :[20,16,11,18,20],
    "Department":["B.tech","B.tech","B.tech","B.tech","B.tech"],
    "Salary":["25lacs","45laccs","10k","1cr","2cr"]
}
df = pd.DataFrame(Data)
print(df.head(3))
print()
df.rename(columns={"Salary":"Income"},inplace=True)
print("After Renaming Salary to Income :")
print(df)