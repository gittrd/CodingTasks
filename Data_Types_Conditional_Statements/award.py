'''
Prompt the user to input the time it has taken to complete:
1) Swimming
2) Cycling
3) Running
Then calculate and display the total time that it has taken to complete the triathlon.

Then use an if elif else to determine to award someone receives based on the following criteria:
1) Within the qualifying time, 0-100 minutes, award is "Provincial colours"
2) Witin five minutes of the qualifying time, 101-105 minutes, award is "Provincial half colours"
3) Within ten minutes of the qualifying time, 106-110 minutes, award is "Provincial scroll"
4) More than ten minutes off from the qualifying time, 111+ minutes, award is "No award"
'''

# prompting the user to add the qualifying time for the three events; Swimming, Cycling and Running
swimming = input("What is your time for Swimming? " )
cycling = input("What is your time for cycling? ")
running = input("What is your time for running? ")

# computing the total time for all the events
total_time = int(swimming) + int(cycling) + int(running)
print(total_time)

# if, elif, else
if total_time <= 100:
    print("The award is Provincial Colours")
elif total_time == 101 or total_time <= 105:
    print("The award is Provincial Half Colours")
elif total_time == 106 or total_time <= 110:
    print("The award is Provincial Scroll")
else:
    print("No award")
