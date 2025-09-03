def analyze_drive(lanes: list[int]) -> tuple[int, int]:
    """
    Analyzes the driving behavior based on lane positions.
    
    Args:
        lanes (list[int]): List of lane positions at each second (0, 1, or 2).
    
    Returns:
        tuple[int, int]: (number of lane changes, number of dangerous maneuvers)
    """
    if not lanes or len(lanes) == 1: #If the lanes list is empty then pass through the function 
        pass

    #Initial values for the Lane Changes and the Dangerous Maneuvers
    lane_changes = 0
    dangerous_man = 0

    #Looping through the provided list to check for Lane Changes and Dangerous Maneuvers
    for i in range(1, len(lanes)):
        previous = lanes[i - 1]
        current = lanes[i]


        if current != previous:
            lane_changes += 1
        if (previous == 0 and current == 2) or (previous == 2 and current == 0):
            dangerous_man += 1


    return (lane_changes, dangerous_man)
