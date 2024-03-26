def get_fullname(first_name, last_name, middle_name=None):
    if not middle_name:
        return first_name + " " + last_name
    else:    
        return first_name + " " + middle_name + " " + last_name
