class Attendee:
    'Common base class for all attendees'

    def __init__(self, name, tickets):
        self.name = name
        self.tickets = tickets

    def displayAttendee(self):
        print('Name : {}, Tickets: {}'.format(self.name, self.tickets))

    def addTicket(self):
        self.tickets += 1
        print('{} tickets increased to {}'.format(self.name, self.tickets))


attendee1 = Attendee('Ahmed', 2)
attendee2 = Attendee('Yousef', 1)
attendee1.displayAttendee()
attendee2.displayAttendee()
attendee2.addTicket()
attendee2.addTicket()
