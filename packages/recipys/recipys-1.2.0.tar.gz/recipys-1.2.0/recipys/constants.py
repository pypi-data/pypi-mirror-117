"""
Global constants of application
"""

# Real time delay between two executions of application (ethical scraping)
from typing import List


MIN_SECONDS_REQUEST: float = 10.0


# Seconds to wait between requests to same endpoint (ethical scraping)
WAIT_BETWEEN_PINGS: int = 1


# Rich colors for printed messages
COLOR_RECIPE_MAIN: str = "steel_blue"
COLOR_RECIPE_SECONDARY: str = "light_slate_grey"
COLOR_ERROR: str = "orange_red1"
COLOR_WARNING: str = "gold1"
COLOR_INFORMATION: str = "deep_sky_blue1"
COLOR_HIGHLIGHT_SEARCHED_MEAL: str = "indian_red"
COLOR_HIGHLIGHT_SEARCHED_INGREDIENT: str = "deep_sky_blue1"


# Standard messages
MESSAGE_INVALID_ARGS: str = f"""\
It seems the input arguments are invalid

You can only use [bold {COLOR_ERROR}]one[/bold {COLOR_ERROR}] \
of the accepted meals :
[bold {COLOR_ERROR}]breakfast[/bold {COLOR_ERROR}], \
[bold {COLOR_ERROR}]lunch[/bold {COLOR_ERROR}], \
[bold {COLOR_ERROR}]dinner[/bold {COLOR_ERROR}] or \
[bold {COLOR_ERROR}]desert[/bold {COLOR_ERROR}]

Or if you are specifying ingredients, be sure to use the keyword \
[bold {COLOR_INFORMATION}]with[/bold {COLOR_INFORMATION}] before \
the ingredients list (for example: [bold {COLOR_INFORMATION}]\
recipys with potato beans[/bold {COLOR_INFORMATION}])
"""

MESSAGE_INVALID_INGREDIENT: str = f"""\
It seems the input arguments are invalid

Please make sure to specify valid ingredients after the \
[bold {COLOR_ERROR}]with[/bold {COLOR_ERROR}]' keyword
(valid ingredients have at least one letter, not only symbols)
"""


# Key strings to cut recipe metadata, as starting point
KEY_STRINGS_CUT_FROM_RECIPE: List[str] = [
    "source:",
    "submitted by",
    "from:",
    "\nfrom",
    "recipe by",
    "created by",
    "historical note",
    "recipe from",
    "posted on",
    "posted by",
    "mm and upload by",
]


# Key strings to detect ingredients are inside preparation
KEY_STRINGS_INGREDIENTS_MISSING: List[str] = [
    "See below ingredients",
]


KEY_STRING_DIVIDE_INGREDIENTS_FROM_PREPARATION: List[str] = [
    "\n\n",
]
