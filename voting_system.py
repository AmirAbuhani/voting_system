# Amir Abu Hani
# this variable will be given for each voter for checking validation
receipt_vote = 1
# this dictionary will include every voter and his receipt_vote number as key:value
validate_votes = {}
# This dictionary will include the candidate as key and id as value. as we know for each vote there is the name and
# it's symbol(unique)
votes = {}
# This dictionary will include the total of votes for each candidate
votes_for_candidates = {}
# This dictionary will include all the candidates and their applying for position. in my code
# I assumed that there is a manager that registered each candidate
candidates_database = {}
# This list will include all the applying for position for each candidate
positions = []
# This dictionary will be the database for all the voters. In reality when voter come to vote, his details
# are exists and just to look for his details.
voters_database = {"yosi": {"age": "26", "address": "tel aviv 4"},
                   "avi": {"age": "30", "address": "bear sheva2"},
                   "amir": {"age": "28", "address": "rahat2"},
                   "ahmad": {"age": "33", "address": "haifa1"},
                   "moshe": {"age": "47", "address": "jerusalem8"},
                   "samar": {"age": "20", "address": "lod19"},
                   "nazar": {"age": "56", "address": "ramla71"}
                   }


# This function takes the  candidates_database dictionary and for each candidate, the manager has to insert
# id for the candidate to show for the voter the details when he comes to vote
def vote():
    for item in candidates_database:
        id = input(f"Insert id for {item} candidate: ")
        votes[item] = id


# The voter function asking for the voter to insert his details(name, age and address)
def voter():
    global receipt_vote
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    addr = input("Enter your address: ")
    for item in voters_database:
        # if the voter details exists in the voters database, the system allows him to vote.
        if name == item and age == voters_database[item]["age"] and addr == voters_database[item]["address"]:
            print("you can vote. Please vote from the list below")
            print(votes)
            # Here the voter choose his candidate and the id candidate. both(candidate and the id) defining a vote
            voter_candidate = input("choose the candidate name ")
            voter_candidate_id = input("choose candidate id: ")
            for vo in votes:
                # if the voter choose one of the item in the votes dictionary, that's mean a valid vote
                if voter_candidate == vo and voter_candidate_id == votes[vo]:
                    print(f"your vote is registered. your receipt number is {receipt_vote}. thank you")
                    # the voter gets unique receipt vote number for validation if necessary
                    validate_votes[item] = receipt_vote
                    # way to validate that a vote was made by a specific voter, if we need it.
                    check_validate_vote()
                    # the candidate who gets the voter vote, his total votes increase by 1
                    votes_for_candidates[vo] += 1
            # the next voter gets the next receipt vote number
            receipt_vote += 1
            # delete the voter from the  voters_database dictionary to ensure that ths voter will not vote again
            del voters_database[item]
            break
        # if the voter details not exist, he can not vote
        else:
            print("you can't vote!, your details is not exist in the system")


# This function registering candidates in the system. so voters can see the candidates name and their id and choice
# candidate in accordance
def condidate():
    while True:
        candidate_register = input("Are there candidates to register? yes or no ")
        if candidate_register == "yes":
            candidate_name = input("Enter candidate name:")
            while True:
                yes_no = input("Are you want to enter a position? yes or no ")
                if yes_no == "yes":
                    position = input("Enter the position you are applying for: ")
                    positions.append(position)
                else:
                    candidates_database[candidate_name] = positions
                    break
        else:
            break


def check_validate_vote():
    your_name = input("Insert your name to check validation: ")
    receipt_vote_number = int(input("insert your receipt vote number: "))
    if your_name in validate_votes and validate_votes[your_name] == receipt_vote_number:
        print("There are details matching ")
    else:
        print("The input details does not match the registering details")


# The main function
def voting_system():
    print("This is for the manager system")
    print("Registering candidates ...")
    condidate()
    print("\n")
    print("For each candidate, insert the id for him: ")
    vote()
    print("\n")
    print("Voters can vote now")
    # here, for each candidate initialize his total votes to 0
    for con in candidates_database:
        votes_for_candidates[con] = 0
    while True:
        voter_vote = input("Are there voters? yes or no ")
        if voter_vote == "yes":
            voter()
        else:
            break
    print("Here is the results:")
    print(votes_for_candidates)


voting_system()
