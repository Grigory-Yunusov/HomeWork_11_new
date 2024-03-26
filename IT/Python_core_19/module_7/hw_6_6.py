def get_recipe(path, search_id):
    result = None
    with open(path, "r") as f:
        for line in f:
            parts = line.strip().split(",")
            if parts[0] == search_id:
                result = {"id": parts[0], "name": parts[1], "ingredients": parts[2:]}
                break  # Додано "break" для припинення пошуку після знаходження відповідного рецепту
    return result
