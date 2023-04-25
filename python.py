# Write a function called check-season, it takes a month parameter
#  and returns the season: Autumn, Winter, Spring or Summer.
# def check_season(season):
#     for i in season:
#         if season===

# function which takes a string parameter month. If month is assigned a valid month name, then the function returns the corresponding season (as a string). Otherwise the function returns the string "Undefined - invalid month".
 
# wrute a function showing the seasons and their corresponding months.
def get_season(month):
    message1 = "Spring"
    message2= "Summer"
    message3= "Autumn"
    message4= "Winter"
    message5= "Undefined - invalid month"
    msg= ""
     
    if month == "September" or "October" or "November":
        msg= message1
    elif month == "December" or "January" or "February":
        msg= message2
    elif month == "March" or "April" or "May":
        msg = message3
    elif month == "June" or "July" or "May":
        msg = message4
    else:
        msg = message5
         
    return msg

# Write a functions which checks if all items are unique in the list.
def unique(item):
    item=["apples","pineapple","mango","avocado"]
    for i in item:
        if i>1:
            print ("i")
        else:
            print ("all unique ")   


# Declare a function named remove_item. It takes a list and an 
# item parameters. It returns a list with the item removed from it.
def remove_item(items):
    items=["soda","bags","chairs","soda","pen"]

