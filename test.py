import datetime
from datetime import datetime, timedelta
rah_day = 9
for _ in range(10):
   
    day_first = datetime.now() - timedelta(days=rah_day)
    day_to_day = day_first.strftime("%d.%m.%Y")
    
    rah_day = rah_day - 1
   
