def count_banknotes(amount):
    
    banknotes = [50, 20, 10, 5, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]
    needed_banknotes = {50: 0, 
                    20: 0,
                    10: 0,
                    5: 0,
                    1: 0,
                    0.5: 0,
                    0.2: 0,
                    0.1: 0,
                    0.05: 0,
                    0.02: 0,
                    0.01: 0}

    for banknote in banknotes:
        needed_banknotes[banknote] = amount // banknote
        amount = round(amount % banknote, 2)

    return needed_banknotes


pounds = {50: "£50",
          20: "£20",
          10: "£10",
          5: "£5",
          1: "£1",
          0.5: "50p",
          0.2: "20p",
          0.1: "10p",
          0.05: "5p",
          0.02: "2p",
          0.01: "1p"}

banknotes = count_banknotes(74.5)

for banknote, amount in banknotes.items():
    if amount != 0:
        print(pounds[banknote] + ':', int(amount))
