from loader import load_all_zipcode_data

repo = load_all_zipcode_data()

records = repo.find("1000001")
for r in records:
    print(r)

records = repo.find("0608554")
for r in records:
    print(r)
