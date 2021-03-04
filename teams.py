# Data to serve with our API
TEAMS = {
    "0": {
        "first_name": "Development Team",
        "last_name": 1,
    },
    "1": {
        "first_name": "Operations Team",
        "last_name": 3,
    }
}

# Create a handler for our read (GET) teams
def read():
    """
    This function responds to a request for /api/teams
    with the complete lists of teams

    :return:        sorted list of teams
    """
    # Create the list of people from our data
    return [TEAMS[key] for key in sorted(TEAMS.keys())]