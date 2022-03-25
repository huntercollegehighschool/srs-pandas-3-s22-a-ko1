# 1. Import pandas
import pandas as pd

# 2. Read the "metacritic2.csv" file, and save the data in a dataframe variable. Print the data
x = pd.read_csv('metacritic2.csv')



# 3. Create a new dataframe with only Mario Games. Save that in a new dataframe variable and print that data (this will involve Boolean indexing)
y = x[x.Game.str.contains('Mario')]

# 4. Sort the Mario data by release year in descending order. (a .sort_values() function exists)
j = y.sort_values('Release Year', axis=0, ascending=False)

# 5. Last time we used a loop to find individual data on different platforms, years, etc. There is a .groupby() function that exists as well. Let's start by grouping by Release Year. Run the following code:
# <var> = <dataframe>.groupby("Release Year").count()
# What does it seems like count presents?

# presents how many games were released in each year
q = x.groupby("Release Year").count()



# 6. Use groupby again, but this time on Platform. Afterwards, run .count(), .mean(), and .median(). Which platform looks like it has the best games?

#3DS
z = x.groupby("Platform").count()
o = x.groupby("Platform").mean()
g = x.groupby("Platform").median()

# 7. Create a new dataframe from the HunterAMC.csv file.
davis = pd.read_csv('HunterAMC.csv', sep = '\t')

# 8. In that csv, contest 0 is the AMC 10, and contest 2 is the AMC 12. Create two separate dataframes containing data from the two different contests.
amc_10 = davis[davis["contest"] == 0]
amc_12 = davis[davis["contest"] == 2]


# 9. Find the average scores for each contest.



# 10. For each column, count how often each answer choice was selected.
