from random import choice


def get_random_color_name():
    debug_colors = [
        "red",
        "pink",
        "purple",
        "indigo",
        "blue",
        "cyan",
        "teal",
        "green",
        "lime",
        "yellow",
        "amber",
        "orange",
        "brown",
        "grey",
    ]

    return choice(debug_colors)
