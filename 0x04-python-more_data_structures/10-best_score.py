#!/usr/bin/python3
def best_score(a_dictionary):
    max_score = 0
    max_key = ""

    try:
        for key, value in a_dictionary.items():
            if value > max_score:
                max_score = value
                max_key = key
        return (max_key)
    finally:
        return None
  