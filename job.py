import pandas as pd

# Read CSV file
df = pd.read_csv("jobs.csv")

# Ask user for a skill to search
skill = input("Enter a skill to search for (e.g. Python): ")

# Count jobs that require this skill
count = df["Skills"].str.contains(skill, case=False).sum()

# Show result
print(f"Number of jobs requiring '{skill}': {count}")
