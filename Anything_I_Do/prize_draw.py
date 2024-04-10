import random

# List of crypto wallet addresses
wallets = [
    "bitsong10vm5cufzctcsvfel7e785nc00sthxt8zgejhut",
    "bitsong12q567kam3tclejefg8jggkxfxues5xlhsycwp5",
    "bitsong13xknrd2t5d28w3rnkly2dx3yxdwr97vhqr4z5w",
    "bitsong17q9x8lda8g2020rnhn9uqdtfsfhdh37vp9tny6",
    "bitsong192ceynhn99lfyqfga2rvr4duxrfvyvjww23f64",
    "bitsong1akhswynqs07zj5p2k25r6s4ur45qyjnraxurk2",
    "bitsong1gqd76semntxx3y0wuauv8sll00zuy39035qmgp",
    "bitsong1gwjpdja2pqu4xkavehkef7n64zrhwf6kp63zq3",
    "bitsong1gwq9m0uc2a4m5xfcr6jurq3pyutam32z5e04yp",
    "bitsong1kr9phxmf5efd7z0mf3nmr6k8qt7u8pwvlcxvg5",
    "bitsong1l9qn4d8a6lesk4syna5r2asxnz88adqudus5lt",
    "bitsong1r6anwk2jmf4040hd8jj3pky97lur0am9zmjmj7",
    "bitsong1w7vcwqg59n3gket07p5f3cy0tx7q8m5nvy5j6u",
    "bitsong1waatekychq80g0w2497g3nlt4gvmjv06zm5xsl",
    "bitsong1x2slrjfmgxq7qx3xwmsjue73t5ynmwy7nvaym7",
    "bitsong1x8gaxd59h38epy20agxmkywl3a9txyy5cwaj9w",
    "bitsong1ym8ffeyjkevwafnyemdu3edrlgqpg3qvpqxcea",
    "bitsong1yrqsvdvxjsmj6r23lat6tm0zh7yrhhrez9d5af",
    "bitsong1zmkncxu7sx2az048htysyh5efc6j6zdpp8claz"
]

# Randomly selecting 5 wallets
winning_wallets = random.sample(wallets, 5)

print(winning_wallets)
