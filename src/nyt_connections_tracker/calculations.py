def calculate_average_guesses(avg, tot, guesses):
    """Calculate running average of guesses."""
    return round((avg * (tot - 1) + guesses) / tot, 2)
