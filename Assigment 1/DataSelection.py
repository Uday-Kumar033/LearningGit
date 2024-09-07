import pandas as pd
Data ={
    "Name":["Uday","Ashish","Vishal","Sachin","Harsh"],
    "Age" :[20,16,31,18,40],
    "Department":["IT","B.tech","B.tech","IT","B.tech"],
    "Salary":[100000,50001,6000,250000,50000]
}
df = pd.DataFrame(Data)
age_g2_5000 = df[df["Salary"]>50000]
print("The salary of person greater than 5000")
print(age_g2_5000)
print()
select = age_g2_5000[["Salary","Name"]]
print("The name and salary columns :")
print(select)
print()
filter_data = df[(df["Department"]=="IT")& (df["Salary"]>50000)]
print("Filtered Data where department is it and salary is greater than 50000 :")
print(filter_data)