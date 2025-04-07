#Alex Anderson, Savings Goal Tracker

def goals_tracker(goals):
    current_goals = []

    if goals != None:
        for goal in goals:
            current_goals.append(goal)
    else:
        goals = {}
    
    if current_goals != []:
        choice = input("Do you want to 1(make new goals) or 2(add to previous goals): ")

    goal_name = input()
    goal_amount = input()
    earned = input()

