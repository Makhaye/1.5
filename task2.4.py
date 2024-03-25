parties = [
    "ANC", "DA", "EFF", "IFP",  "ACDP", "UDM", "COPE", "NFP", "ATM",
    "GOOD", "AIC", "PAC", "ALJAMA", "ATM", "BLF", "CRA", "COPE", "EFF", 
    "GA", "GRN",  "IFP",   "UBUNTU", "UDM", "VF+"
]

party_memberships = {
    "ANC": 5000,
    "DA": 3000,
    "EFF": 1500,
    "IFP": 800,
    "ACDP": 700,
    "UDM": 600,
    "COPE": 950,
    "NFP": 300,
    "ATM": 200,
    "AIC": 500,
    "PAC": 400,
    "ALJAMA": 350,
    "BLF": 100,
    "SRWP": 200,
    "UBUNTU": 400
}

selected_parties = [party for party in filter(lambda x: party_memberships[x] >= 1000, parties)]

print(selected_parties)
