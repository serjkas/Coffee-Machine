class User:
    # create the class here
    users = []
    n_active = 0  # number of fish in the aquarium

    def __init__(self,active, user_name):
        self.user_name = user_name
        self.active = active
