from datetime import datetime as dt

players = {}

def get_age_diff(duration_in_s):
    days    = divmod(duration_in_s, 86400)
    hours   = divmod(days[1], 3600)        
    minutes = divmod(hours[1], 60)               
    seconds = divmod(minutes[1], 1)  
    return [days,hours,minutes,seconds]

def get_dob_obj(dob_str):
    return dt.strptime(dob_str,"%d %b %Y") 

def add_player(name,dob_str):
    players[name] = get_dob_obj(dob_str)

def print_age(dob_str,name):
    dob_obj = get_dob_obj(dob_str)
    curr_date = dt.now()
    if dob_obj > curr_date:
        print("You haven't been born yet!")
    else:
        time_diff_in_s = (curr_date - dob_obj).total_seconds()
        time_diff_calc = [delta[0] for delta in  get_age_diff(time_diff_in_s)]            
        print("Time between dates: {:.0f} days, {:.0f} hours, {:.0f} minutes and {:.0f} seconds".format(*time_diff_calc))
        add_player(name,dob_str)

def is_younger(name,age_obj,curr_name):
    return curr_name != name and age_obj > players.get(curr_name)

def print_younger_players(curr_name):
    younger_players = [ name for (name,age_obj) in players.items() if is_younger(name,age_obj,curr_name)]
    if len(younger_players):
        print("You are older than {} player(s)".format(str(len(younger_players))))
        print("Players younger than you are -",sep=" ")
        print(*younger_players,sep=" , ")
    else:
        print("You are the youngest!")

def play():
    while True:
        print("What is your name?")
        name = input()
        print("It's great to meet you, " + name)
        print("Your name has {} letters".format(str(len(name))))
        print("Enter your Date of Birth ( Ex. 7 mar 1997 )")
        dob_str = input()
        print_age(dob_str,name)
        if len(players) > 1:
            print_younger_players(name)
        print("Press 0 to exit")
        choice = input()
        if not int(choice):
            break
        else:
            print(players)
    

print("Hello World")
play()