

desired_avg   = 6.5
desired_stdev = 1.0

options = {
    -3: 'Way worse',
    -2: 'Definitely worse',
    -1: 'Maybe worse',
    0: 'Idk',
    1: 'Definitely better',
    2: 'Maybe better',
    3: 'Way better'
}

class CompareEvent(object):
    def __init__(id1, id2, score):
        self.id1 = id1
        self.id2 = id2
        self.score = score

def compute_ratings_from_events(ids, events):
    ratings = []
    idmap = {}
    index = 0

    setup()

    # Variance is the expected value of the squared deviation from the mean
    # Standard deviation is the square root of the expected value of the squared deviation from the mean

    # If i did one pass thru all the items, what would the stdev be?
    # change_per_event = x

    # Sum of squared change_per_event MUST equal n * sd * sd

    # Raw su

    n = len(events)
    v = desired_stdev * desired_stdev
    y = 0.0

    for event in events:
        y += event.score * event.score
    
    a = (n*v)/(y)

    for event in events:
        event.score = event.score * sqrt(a)
        ratings[event.id1] += event.score
        ratings[event.id2] -= event.score






    def setup():
        for id in ids:
            idmap[id] = index
            index += 1
            ratings.append(desired_avg)
        
        for event in events:
            event.id1 = idmap[event.id1]
            event.id2 = idmap[event.id2]

def rate_of_change_matrix(ratings):
    rates = []
    for slice in ratings[-1]:
        total_diff = 0.0
        for i in range(0,len(ratings[slice])):
            before = ratings[slice][i]
            after = ratings[slice+1][i]
            diff = abs(after - before)
            total_diff = diff
        rates.append(total_diff)
    return rates

def recent_rate_of_change(ratings, num_most_recent_events):
    total_rate = 0.0

    rates = rate_of_change_matrix(ratings)
    rates = rates.reverse()

    for i in (0,num_most_recent_events):
        rate = rates[i]
        total_rate += rate
    
    avg_rate = total_rate / num_most_recent_events

    return avg_rate

def rate_items(dfrateditems):
    df = dfrateditems.sample(frac=1).reset_index(drop=True)
    events = []
    ratings = []

def show_scale():
    print(options)

def create_event(name1, name2):
    message = '{} vs {}'.format(name1, name2)
    terminal.prompt_user(message)

def save_events(location):

def load_events(location):

def normalize_ratings(rateditems):
