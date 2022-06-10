#!/usr/bin/python3
def best_score(a_dictionary):

    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None
    elif len(a_dictionary) > 0:
        new_k = a_dictionary.keys()
        max_key = max(new_k)
    return (max_key)
