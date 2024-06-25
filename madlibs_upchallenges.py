import datetime
from datetime import date
from datetime import datetime

today = date.today()
# Textual month, day and year	
# d2 = today.strftime("%B %d, %Y")
# mm/dd/y
d1 = today.strftime("%m/%d/%y")

# datetime object containing current date and time
now = datetime.now()
# current time in 12 hr cycle (%l), military hours(%H), minutes(%M) (optional: seconds(%S))
current_time = now.strftime("%l:%M")

#script variables
place = input("give me a place: ")
nouns1 = input("give me a plural noun: ")
verb1 = input("give me a verb ending in -ing: ")
verb2 = input("give me another verb ending in -ing: ")
nouns2 = input("give me a plural noun: ")
adverb = input("give me an adverb: ")
verb3 = input("give me a verb ending in -ing: ")
emotion = input("give me a emotion ending in -er or -ier: ")
verb4 = input("give me a verb ending in -ing: ")

print(f"Today is {d1} and it's {current_time}.")
print(f"I should be at CodeNext right now,")
print(f"but tell me why I'm at the {place}...")
print(f"All around me I see {nouns1} {verb1} and {verb2}")
print("Another thing to mention is that these")
print(f"{nouns2} keep {adverb} staring at me.")
print("I should be coding and programming right now,")
print(f"but I find myself {verb3} with the {nouns1}.")
print("And the weird thing is...")
print(f"I feel {emotion} than I did before.")
print(f"The {nouns2}, that were staring at me,")
print(f"are now {verb4} along with me.")
print("I don't know if I can go home!")


