# global score in a games
# ==============================================================================
'''score = 0

def increase_score(points):
    global score
    score += points

increase_score(10)
print("score:",score)'''

# text-based adventure game:
# =========================================================================
def start_adventure():
    hero_name = input("enter your hero's name:")
    print(f"welcome,{hero_name}!you embark on an epic adventure")

start_adventure()

