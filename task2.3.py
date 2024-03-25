def update_voter_info(voter_id, name, voting_district, has_voted, voter_database):
   
    if voter_id in voter_database:
        voter_database[voter_id]["name"] = name
        voter_database[voter_id]["voting_district"] = voting_district
        if not voter_database[voter_id]["has_voted"]:
            voter_database[voter_id]["has_voted"] = has_voted
            print(f"Voter {voter_id} has voted.")
        else:
            print(f"Voter {voter_id} has already voted.")
    else:
        voter_database[voter_id] = {"name": name, "voting_district": voting_district, "has_voted": has_voted}
        print(f"New voter {voter_id} added to the database.")
    
    return voter_database

if __name__ == "__main__":
    voter_database = {
        1: {"name": "John Doe", "voting_district": "District A", "has_voted": False},
        2: {"name": "Jane Smith", "voting_district": "District B", "has_voted": True}
    }
    
    updated_database = update_voter_info(3, "Alice Johnson", "District C", False, voter_database)
    updated_database = update_voter_info(2, "Jane Smith", "District B", False, updated_database)
