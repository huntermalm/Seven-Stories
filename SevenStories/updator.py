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
        game_map.player.location = game_map.get_location("First room")
        game_map.version = "0.2.0"

    return updated
