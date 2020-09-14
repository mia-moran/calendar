import json
import datetime

class Calendar_:
    def __init__(self):
        self.activities = self.load_()
    def load_(self):
        activities = []
        with open('./activities.json') as file:
            data = json.load(file)
            for activity in data['Activities']:
                activities.append(Activity_(activity['area'], activity['title'], activity['init'], activity['end'], activity['day'], activity['color']))
        return activities
class Activity_:
    def __init__(self, area_, title_, init_, end_, day_, color_, desc_):
        self.area = area_
        self.title = title_
        self.init = init_
        self.end = end_
        self.day = day_
        self.color = color_
        self.desc = desc_

class Day_:
    def __init__(self, date_):
        self.date = date_

class Week_:
    def __init__(self, today_):
        self.week = self.get_week(today_)
    def get_week(self, today_):
        today = today_.split('/')
        today = datetime.datetime(int(today[2]), int(today[1]), int(today[0]))
        week_day = today.weekday()
        while(week_day != 0):
            yesterday = today - datetime.timedelta(days=1)
            week_day = yesterday.weekday()
            today = yesterday
        week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        week_days = []
        for d in week:
            week_days.append(today)
            today = today + datetime.timedelta(days=1)
        return week_days


week = Week_('14/09/2020')
calendar = Calendar_()
for a in calendar.activities:
    
print(week.week)

