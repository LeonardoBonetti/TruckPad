def str_to_bool(s):
    if s in ['True', 'true', '1']:
        return True
    elif s in ['False', 'false', '0']:
        return False
    elif s is None:
        return None
    else:
        raise ValueError  # evil ValueError that doesn't tell you what the wrong value was
