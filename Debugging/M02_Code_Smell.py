uncleSam = 1.08
paytheserver = 1.15
foodstuff = input("How much was your meal? ")
corporate_cut = uncleSam * int(foodstuff)
pocket_book_pain = corporate_cut * paytheserver
print("You need to leave " + str(pocket_book_pain) + " on the table to cover tax and tip.")
