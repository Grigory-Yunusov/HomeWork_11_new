def game(terra, power):
    player_power = power
    for layer in terra:
        for line in layer:
            if player_power >= line:
                player_power += line
            else:
                break
    return player_power

