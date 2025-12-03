#..............................wedding manager....................................................
# Scenario: You are managing a guest list for a high-profile wedding. You have two lists: one for the confirmed guests and another for the waitlisted guests. The couple wants a simple wedding with close friends and family in attendance so there is room for only 10 guests. Follow the instructions to manage the guest lists accordingly. Write the program in a file `wedding_guest_manager.py`.
# 1. Currently, Alice, Charlie, Eve, Bob, Frank, Grace, David, Hannah, Liam and Mia have accepted invitations to the wedding and are on the confirmed_guests list. The confirmed_guests list is full. New guests who accept the invitation will be waitlisted.

# Stage 1
confirmed_guests = ["Alice", "Charlie", "Eve", "Bob", "Frank", "Grace", "David", "Hannah", "Liam", "Mia"] 
waitlist = []
print("\n\nStage 1")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)

# 2. Three siblings Ken, Jack and Ivy accept the invitation but are put on the waitlist.
# Stage 2
waitlist.extend(["Ken", "Jack", "Ivy"])
print("\n\nStage 2")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)

# 3. Noah, the groom’s ex-classmate in the university and Oliver who lives next door to the bride have accepted the invitation. Put them on the waitlist.
# Stage 3
waitlist.append("Noah")
waitlist.append("Oliver")
print("\n\nStage 3")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)
# 4. Alice has a family emergency and won’t be able to attend the wedding, She cancels her attendance. Remove Alice from the confirmed guest list and add the first person from the waitlist to the confirmed list. 

# Stage 4
# confirmed_guests = ["Alice", "Charlie", "Eve", "Bob", "Frank", "Grace", "David", "Hannah", "Liam", "Mia"] 
confirmed_guests.remove("Alice")
confirmed_guests.append(waitlist[0])
waitlist.remove("Ken")
print("\n\nStage 4")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)
# 5. Charlie is the godfather of the groom and he is the one funding the wedding. Therefore he is a VIP guest and the couple has asked you to make sure he is on the guestlist. Check whether or not Charlie is on the guestlist.
is_in_the_guest_list = True
name = "Charlie"
print("\n\nStage 5")
print("Confirmed guests: ", confirmed_guests)
# print("Waitlist: ", waitlist)
print(f"it is {is_in_the_guest_list} that {name} is in the guest List")

# 6. David and Eve have decided they no longer want to attend the wedding and therefore cancel their attendance. Remove them from the confirmed_guests list. 
confirmed_guests.remove("David")
confirmed_guests.remove("Eve")
print("\n\nStage 6")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)

# 7. Move the first 2 people on the waitlist into the guestlist to fill up the newly freed slots.
confirmed_guests.extend(waitlist[0:2])
waitlist.remove(waitlist[0])
waitlist.remove(waitlist[0])
print("\n\nStage 7")
print("Confirmed guests: ", confirmed_guests)
print("waitlist", waitlist)

# 8. Oliver just realized the day of the wedding is the same day he has to take his pet to see the vet and he cancels his attendance. Remove him from the waitlist.
waitlist.remove("Oliver")
print("\n\nStage 8")
print("waitlist: ", waitlist)


# 9. The event planner has asked you for the names of the last 3 guests on the guest list because she needs to make additional arrangements for them. Get her this information.
last_three_confirmed_guest = confirmed_guests[-3:]
print("\n\nStage 9")
print("confirmed_guests:",confirmed_guests)
print("waitlist:", waitlist)
print("last_three_confirmed_guest:", last_three_confirmed_guest)

# 10. The bride and groom have decided that they want to allow room for 5 more people to attend their wedding. Move waitlisted guest (Noah)into the confirmed_guests list.
confirmed_guests.append(waitlist.pop(0))
waitlist.clear()
print("\n\nStage 10")
print("confirmed_guests:",confirmed_guests)
print("waitlist:", waitlist)


# 11. The event planner wants a report on the number of people who will be attending the wedding. Give her this information.

number_of_people = len(confirmed_guests)
print("\n\nStage 11")
print("confirmed_guests:", confirmed_guests)
print("waitlist:", waitlist)
print("number_of_people:", number_of_people)


# 12.	The event planner has also requested that you give her a list of all the names of the confirmed_guests. The guests would be seated alphabetically at the venue and so she wants the names in alphabetical order.
confirmed_guests.sort()
print("\n\nStage 12")
print("confirmed_guests:", confirmed_guests)
print(waitlist)

# 13. A new guest called Collins who is the son of Grace and Noah would be attending on their behalf, Replace Grace and Noah on the confirmed_guests list with Collins. Make sure you re-sort the list.
confirmed_guests.pop(-1)
confirmed_guests.pop(-7)
confirmed_guests.append("Collins")
confirmed_guests.sort()
print("\n\n Stage 13")
print("confirmed_guests", confirmed_guests)

# 14. The caterer has also requested for the confirmed_guests list so she can provide the guests with customized bags containing their food with their names on it. Give her a copy of the confirmed_guests list titled guests_list_for_caterer`.
import copy
guests_list_for_caterer = confirmed_guests.copy()
print("\n\n Stage 14")
print("confirmed_guests:", confirmed_guests)
print("guests_list_for_caterer:", guests_list_for_caterer)

# 15. The deadline for accepting the invitations sent has now passed. There is no more need for the waitlist. 	Clear the waitlist.
waitlist.clear()
print("\n\n Stage 15")
print("confirmed_guests", confirmed_guests)
print("waitlist", waitlist)


# At every stage from numbers 1 to 15, print out the following like so:
# print(“\n\nStage X”)
# print(“Confirmed guests: ”, confirmed_guests)
# print(“Waitlist: ”, waitlist)
# X means the current stage i.e. 1, 2, etc. If the question requests for some particular info apart from the content of confirmed_guests and waitlist such as numbers 5, 9 and 11, print it under the three lines above.

