# Let's build a social network. 

# In this social network, each user has friends.

# A chain of friends between two users, user A and user B, is a sequence of users starting with A and ending with B, such that for each user in the chain, ua, the subsequent user, ua + 1, are friends.

# Given a social network and two users, user A and user B, please write a function that computes the length of the shortest chain of friends between A and B.


def shortest_chain_length(network, A, B):
    assert A in network and B in network
    assert A != B

    visited = set()
    queue = [(A, 0)]

    while queue:
        user, length = queue.pop(0)
        visited.add(user)

        for friend in network[user]:
            if friend == B:
                return length
            elif friend not in visited:
                queue.append((friend, length + 1))

    return -1


if __name__ == "__main__":
    # network1 = {
    #     "Andrei": {"Bogdan"},
    #     "Bogdan": {"Andrei"},
    # }

    # Test case 1: A function call with users not in the network - to cover the previously discussed caveat;

    # print(shortest_chain_length(network1, "Cristian", "Daniel")) 

    # Test case 2: A function call where users A and B are the same user - to make sure that the function doesn't search a path from a user to itself in an impossible situation;
    # print(shortest_chain_length(network1, "Andrei", "Andrei"))


    network2 = {
        "Andrei": {"Bogdan"},
        "Bogdan": {"Andrei"}
    }

    # Test case 3: A social network with two users that are friends of each other - to test the easiest case possible;
    print("3: The length of the shortest chain of friends is:", shortest_chain_length(network2, "Andrei", "Bogdan"))


    network3 = {
        "Andrei": {"Bogdan"},
        "Bogdan": {"Andrei", "Cristian", "Daniel"},
        "Cristian": {"Bogdan", "Daniel"},
        "Daniel": {"Bogdan", "Cristian"}
    }

    # Test case 4: A social network with two users A and B that have multiple chains of friends inbetween each other - to make sure that the function will return the length of the shortest chain;
    print("4: The length of the shortest chain of friends is:", shortest_chain_length(network3, "Andrei", "Daniel"))


    network4 = {
        "Andrei": {"Bogdan"},
        "Bogdan": {"Andrei"},
        "Cristian": {"Daniel"},
        "Daniel": {"Cristian"},
    }

    # Test case 5: A social network that contains certain users that ultimately aren't friends with each other - to assure that the function is able to distinguish certain cases that do not have solutions;
    print("5: The length of the shortest chain of friends is:", shortest_chain_length(network4, "Andrei", "Daniel"))


    network5 = {
    'Andrei': {'Bogdan', 'Cristian'},
    'Bogdan': {'Andrei', 'Emma'},
    'Cristian': {'Andrei', 'Daniel'},
    'Daniel': {'Cristian', 'Emma', 'Florin'},
    'Emma': {'Bogdan', 'Daniel'},
    'Florin': {'Daniel', 'Georgiana'},
    'Georgiana': {'Florin'}
    }

    # Test case 6: A vast social network that also includes some of the cases discussed previously - to ensure that the function is behaving properly; here I also tested if a function call that started the search from user A and ended with user B produced the same result as a function call that started the search from user B and ended with user A.
    print("6: The length of the shortest chain of friends is:", shortest_chain_length(network5, "Andrei", "Georgiana"))
    print("6(reverse): The length of the shortest chain of friends is:", shortest_chain_length(network5, "Georgiana", "Andrei"))