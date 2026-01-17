"""

Q: given [A,B,C] write all possible combinations where B is not in the middle

Step 1: draw all the possible paths on paper.

Step 2: understand what I need to store. 
    - main res. 
    - I need my arrangement so far. arrangement
    - I need to know which index in path to add my value at. seat_index
    - I need track what I have used so far. used = set()

Step 3: Figure out my choices. here, choice, i.e current_person = anything from A,B,C where person not in used. 

Step 4: When do you return? If seat index == 3, and arrangment is full

Step 5: Any paths to avoid / prune? if seat_index == 1, and current_person = B, then avoid that path. 

"""
