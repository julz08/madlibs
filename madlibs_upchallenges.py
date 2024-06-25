import datetime
from datetime import date
from datetime import datetime

today = date.today()
# Textual month, day and year	
d1 = today.strftime("%B %d, %Y")
# mm/dd/y
d2 = today.strftime("%m/%d/%y")

# datetime object containing current date and time
now = datetime.now()
# current time in hours(%H), minutes(%M) (optional: seconds(%S))
current_time = now.strftime("%H:%M")

