import pandas as pd

data = {
    "Name": ["Aman", "Riya", "Sohan", "Priya", "Karan"],
    "Age": [21, 22, 20, 23, 21],
    "Marks": [85, 90, 78, 92, 88]
}

df = pd.DataFrame(data)

print("\n First 3 rows:\n", df.head(3))
print("\n Last 3 rows:\n", df.tail(3))

# Average age
avg = df["Age"].mean()
print("\n Average Age:", avg)

# Top student
top_student = df.loc[df["Marks"].idxmax(), "Name"]
print("\n Top Student:", top_student)

# Lowest student
low_student = df.loc[df["Marks"].idxmin(), "Name"]
print("\n Lowest Student:", low_student)

# Above average students
above_avg = df[df["Marks"] > df["Marks"].mean()]
print("\n Students above average:", len(above_avg))

# Add bonus
df["Marks"] = df["Marks"] + 5

# Add new row
new_row = {"Name": "Rahul", "Age": 24, "Marks": 80}
df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

# Sorting
print("\n Sorted Data:\n", df.sort_values("Marks", ascending=False))

# Pass/Fail
df["Status"] = df["Marks"].apply(lambda x: "Pass" if x > 80 else "Fail")

print("\n Final Data:\n", df)
