def update(game_map):
    """Updated the game_map depending on version

    :param game_map: The currently loaded GameMap object
    :type game_map: class GameMap
    :return: True/False depending on if any updates occurred
    :rtype: boolean

    """
    updated = False

    if game_map.version == "0.1.1":
        import locations
        updated = True
        game_map.locations = []
        game_map.locations.append(locations.Location("First room"))
        game_map.player.location = game_map.locations[0]
        game_map.version = "0.2.0"

    if game_map.version == "0.2.0":
        import locations
        first_room = game_map.locations[0]
        del game_map.locations
        game_map.locations = {}
        game_map.locations["first room"] = first_room
        game_map.locations["second room"] = locations.Location("Second room")
        game_map.locations["first room"].available_locations["second room"] = game_map.locations["second room"]
        game_map.locations["second room"].available_locations["first room"] = game_map.locations["first room"]
        game_map.version = "0.3.0"

    return updated
