def fuse_readings(sensor1: list[int], sensor2: list[int], sensor3: list[int]) -> list:
    """
    Combines sensor readings using majority vote logic.
    Falls back to averaging when there is no consensus.
    
    Args:
        sensor1, sensor2, sensor3 (list[int]): Readings from 3 sensors.
    
    Returns:
        list: Final fused readings for each timestep.
              - Majority value if at least 2 sensors agree.
              - Average value if no consensus.
    """
    if not sensor1 or not sensor2 or not sensor3:
        pass

    fused = []

    for x, y, z in zip(sensor1, sensor2, sensor3):

        if x == y or x == z:
            fused.append(x)
        elif y == z:
            fused.append(y)
        else:
            avg = (x + y + z) / 3
            fused.append(avg)

    return fused
