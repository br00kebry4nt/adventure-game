game = {
    "Name": ["Description", "MenuA", "NodeA", "MenuB", "NodeB"], 
    "start": ["You are stranded in the jungle and night is approaching!", "Build a shelter", "shelter", "Explore the jungle", "explore"], 
    "shelter": ["You build a simple shelter.", "Get some rest", "rest", "Search for food", "food"], 
    "explore": ["The jungle is dangerous! You get lost and hear wild animals.", "Start over", "start", "Quit", "quit"], 
    "rest": ["You wake up feeling hungry.", "Search for food", "food", "Explore the nearby river", "river"], 
    "food": ["You find wild fruits but need to know they are safe to eat.", "Eat the fruits", "eat", "Keep searching", "search"], 
    "river": ["You reach a river with clean water but notice something on the horizon.", "Build a fire", "fire", "Swim across the river", "swim"], 
    "eat": ["The wild fruits were poisonous! You pass out!", "Start over", "start", "Quit", "quit"], 
    "search": ["You have caught a wild animal.", "Cook the animal", "cook", "Keep exploring", "explore"], 
    "swim": ["The current is strong and pulls you away.", "Start over", "start", "Quit", "quit"], 
    "fire": ["You build a fire to use the high-rising smoke as a signal.", "Fan the flames", "signal", "Wait for rescue", "wait"], 
    "cook": ["You cook the animal and feel better.", "Explore the area", "explore", "Follow the river", "river"], 
    "signal": ["The fire grows larger and becomes visible.", "Keep fanning the flames", "wait", "Look for other signals", "signal2"], 
    "wait": ["The rising smoke allows a rescue plane to spot you. You are saved!", "Start over", "start", "Quit", "quit"], 
    "signal2": ["You make more signals with sticks and rocks. The plane notices!", "Wait for pickup", "wait", "Keep signaling", "signal"], 
    "plane": ["The plane circles above and drops a ladder. Rescue is here!", "Wait for pickup", "wait", "Start over", "quit"]
}

def playNode(node):
    description, menuA, nodeA, menuB, nodeB = game[node]
    print(description)
    print(f"1. {menuA}")
    print(f"2. {menuB}")
    choice = input("Your choice (1 or 2): ")
    
    if choice == "1":
        return nodeA
    if choice == "2":
        return nodeB
    print("Please choose either 1 or 2.")
    return node

def getGame(): 
    presentNode = "start"
    while presentNode != "quit":
        presentNode = playNode(presentNode)

def main():
    getGame()

main()      