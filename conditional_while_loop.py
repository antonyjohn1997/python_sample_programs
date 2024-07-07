release_date=28
current_date=18
# Create a condition where current_date is less than or equal to the release_date

while current_date <= release_date:
     # Increment current_date by one

     current_date+=1
     
     ##Check if current_date is less than 21 and, if so, print "Purchase before the 21st for early access"
     if current_date<21:
         print("Purchase b4 21st for early access")
     # Check if the date is less than or equal to the 25th
     elif current_date <= 25:
         print("Coming soon")
     else:
         print("Available now!")    
