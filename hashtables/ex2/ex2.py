#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):


    cache = {}
    for ticket in tickets:
        cache[ticket.source] = ticket.destination

        # Your code here
    route = []
    start = cache["NONE"]

    while start != "NONE":
        route.append(start)
        start = cache[start]

    route.append("NONE")

    return route
