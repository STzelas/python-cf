# Constants
# Δεν υπάρχουν σταθερές στην python, by convention εχουμε SCREAMING_CASE
SECONDS_IN_A_MINUTE = 60
SECONDS_IN_AN_HOUR = 3600
SECONDS_IN_A_DAY = 86400

# prompt
total_seconds = int(input("Enter the number of seconds: "))

# calculations

days = total_seconds // SECONDS_IN_A_DAY  # επιστρέφει int το //, ενώ το / float
remaining_seconds = total_seconds % SECONDS_IN_A_DAY

hours = remaining_seconds // SECONDS_IN_AN_HOUR
remaining_seconds %= SECONDS_IN_AN_HOUR

minutes = remaining_seconds // SECONDS_IN_A_MINUTE
remaining_seconds %= SECONDS_IN_A_MINUTE

seconds = remaining_seconds

print(f"{total_seconds} seconds is equal to")
print(f"{days} days, {hours} hours, {minutes} minutes, {seconds} seconds")

# result
# 105310 seconds is equal to
# 1 days, 5 hours, 15 minutes, 10 seconds