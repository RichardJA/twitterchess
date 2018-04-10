input = "This new a test string".split()[1]

command_list = ["new", "reject", "move", "board", "retire", "games", "stats", "commands"]

if input in command_list:
    print("success")
else:
    print("fail")
