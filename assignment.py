from datetime import datetime
class remainder:
    def remember_event():
        date_event ={}
        flag =True
        while flag:
            choice =input('Do you want to remember something:')
            if choice.lower()=='yes':
                date=input('Enter the important date:')
                event=input('Enter the event for the date:')
                date_event[date]=event
            if choice.lower()=='no':
                flag=False
        return date_event
    def check_event(date_event):
        current_datetime=datetime.now()
        current_date=str(current_datetime.date())
        keys=list(date_event.keys())
        values=list(date_event.values())
        for value in keys:
            if current_date==value:
                print(date_event[value])

rem=remainder
date_and_event=rem.remember_event()
print(date_and_event)
rem.check_event(date_and_event)