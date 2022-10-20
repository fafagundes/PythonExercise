"""

we want to write a script that generates a report of which users are logged in
to which machines at that time.

# Input
List of events - Each event is an instance of the event class
Event Class - Contains the date when the event happened, the name of the machine where it happened,
the user involved, and the event type
*we care about the "login" and "logout" type.

Attributes - Date, user, machine, type

# Output

Machine name
User name
Date


"""

class Event:
    def __init__(self, event_date, event_type, machine_name, user):
        self.date = event_date
        self.type = event_type
        self.machine = machine_name
        self.user = user

# - Get the event date to use in a fuction
def get_event_date(event):
    return event.date


def current_users(events):
    events.sort(key=get_event_date)  # - sorted by date all events
    machines = {}  # - dictionary to storage the users and names machine
    for event in events:
        if event.machine not in machines:  # - create a new
            machines[event.machine] = set()
        if event.type == "login":
            machines[event.machine].add(event.user)
        elif event.type == "logout":
            machines[event.machine].remove(event.user)
    return machines

def generate_report(machines):
    for machine, users in machines.items():
        if len(users) > 0:
            user_list = ", ".join(users)
            print(f"{machine}: {user_list}")

events = [
    Event('2020-02-21 12:45:56', 'login', 'myworkstation.local', 'jordan'),
    Event('2020-02-22 15:53:42', 'logout', 'webserver.local', 'jordan'),
    Event('2020-02-21 18:53:21', 'login', 'webserver.local', 'lane'),
    Event('2020-02-22 10:25:34', 'logout', 'myworkstation.local', 'jordan'),
    Event('2020-02-21 08:20:01', 'login', 'webserver.local', 'jordan'),
    Event('2020-02-23 11:24:35', 'login', 'mailserver.local', 'chris'),
]

users = current_users(events)
print(users)

generate_report(users)
