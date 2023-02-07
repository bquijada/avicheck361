# Author: Brenda Levy
# GitHub username: bqujiada
# Date: 1/23/23 
# Description: Back-country Planning App

import region
from InquirerPy import inquirer
from InquirerPy.base.control import Choice
# from InquirerPy.separator import Separator
import pyfiglet
from datetime import datetime
from bs4 import BeautifulSoup

import requests
from clint.textui import puts, indent, colored
import matrix
from time import sleep
from rich.console import Console

# from time import sleep
# from clint.textui import progress

reg_coord = ["lat=50.993293&long=-118.197407", "lat=52.2201&long=-117.0303", "lat=49.7028&long=-122.9247",
             "lat=51.4918&long=-116.0205", "lat=49.4899&long=-117.3174"]

gear_list = ["shovel", "probe", "beacon", "flashlight or headlamp", "fire-making kit", "signaling device",
             "Extra food and water", "Extra clothing",
             "First aid kit", "Pocket knife/multitool", "sun protection", "sun projection", "emergency shelter - tarp"]


def main():
    """main driver function"""
    location = None
    hello_text = pyfiglet.figlet_format("AVI-CHECK", font="colossal", width=110)
    bye_text = pyfiglet.figlet_format("See you later", font="colossal", width=110)
    print(hello_text)
    print(" Welcome to AVI-CHECK, your one stop for trip planning and mountain safety!")
    print(" Use this tool to check the current avalanche report, weather forecast, recommended gear, "
          "and calculate slope evaluations")
    print(" Today is", datetime.now())
    print(" Use the arrow keys to get started!")
    while True:
        print("\n")
        place = regions()
        if place == "Jasper":
            print("Jasper")
            region_1 = region.Region("Jasper", reg_coord[1])
            location = region_1
        if place == "Squamish":
            print("Squamish")
            region_2 = region.Region("Squamish", reg_coord[2])
            location = region_2
        if place == "Revelstoke":
            print("Revelstoke")
            region_0 = region.Region("Revelstoke", reg_coord[0])
            location = region_0
        if place == "Banff":
            print("Banff")
            region_3 = region.Region("Banff", reg_coord[3])
            location = region_3
        if place is None:
            break
        while True:
            breaker = False
            action = actions()
            if action == "Avalanche Report":
                next_action_ = display_avi_report(location)
                if next_action == "Go Back":
                    continue

            if action == "Weather forecast":
                next_action_ = display_weather(location)
                if next_action == "Go Back":
                    continue

            if action == "Recommended Gear":
                gear_rec()
                next_action_ = next_action()
                if next_action == "Go Back":
                    continue

            if action == "Change Region":
                break
            if action is None:
                breaker = True
                break
        if breaker:
            break
    print(bye_text)


def gear_rec():
    print("\n")
    print("Essential list of gear for backcountry exploration:")
    for gear in gear_list:
        with indent(2, quote="~"):
            puts(colored.green(gear))


def regions():
    """menu of regions for user to select"""
    location = inquirer.select(
        message="Where will you go?",
        choices=["Revelstoke", "Jasper", "Squamish", "Banff", Choice(value=None, name="Exit")],
    ).execute()
    return location


def actions():
    print("\n")
    action = inquirer.select(
        message="Select Mountain Info you would like to view: ",
        choices=["Avalanche Report", "Weather forecast", "Recommended Gear", "Change Region",
                 Choice(value=None, name="Exit")],
    ).execute()
    return action


def display_avi_report(location):
    """displays avalanche report"""
    print("\n")
    print("Avalanche Report for " + location.get_name() + ":")
    report = get_report(location)
    next_action_ = inquirer.select(
        message="Would you like to: ",
        choices=["Calculate Slope Evaluation", "Go Back",
                 ],
    ).execute()
    if next_action_ == "Calculate Slope Evaluation":
        avaluator(report, location)
    return next_action_


def progress_avi():
    console = Console()
    tasks = [f"{n}" for n in range(1, 3)]

    with console.status("[bold magenta]Loading avalanche report...") as status:
        while tasks:
            task = tasks.pop(0)
            sleep(1)


def progress_weather():
    console = Console()
    tasks = [f"{n}" for n in range(1, 3)]

    with console.status(spinner='weather', status="[bold green]Loading weather...") as status:
        while tasks:
            task = tasks.pop(0)
            sleep(1)


def get_report(location):
    """search for avalanche report"""
    coordinates = location.get_coord()
    progress_avi()
    response = requests.get('https://api.avalanche.ca/forecasts/en/products/point?' + coordinates)
    result = response.json()
    summary = result['report']['highlights']
    print(BeautifulSoup(summary, features='html.parser').text)
    danger = result['report']['dangerRatings']
    danger2 = danger[0]
    danger_rating = []
    print("\n")
    for x in danger2:
        for y in danger2[x]:
            elev = danger2[x][y]
            if y == "alp":
                alp = elev.get('rating').get('value')
                if alp == 'low':
                    puts("Danger rating in Alpine: " + colored.green(alp))
                elif alp == 'moderate':
                    puts("Danger rating in Alpine: " + colored.yellow(alp))
                else:
                    puts("Danger rating in Alpine: " + colored.red(alp))
                danger_rating.append(alp)
            if y == "tln":
                tln = elev.get('rating').get('value')
                if tln == 'low':
                    puts("Danger rating at Tree line: " + colored.green(tln))
                elif tln == 'moderate':
                    puts("Danger rating at Tree line: " + colored.yellow(tln))
                else:
                    puts("Danger rating at Tree line: " + colored.red(tln))
                danger_rating.append(tln)
            if y == "btl":
                btl = elev.get('rating').get('value')
                if btl == 'low':
                    puts("Danger rating Below Tree Line: " + colored.green(btl))
                elif btl == 'moderate':
                    puts("Danger rating Below Tree Line: " + colored.yellow(btl))
                else:
                    puts("Danger rating Below Tree Line: " + colored.red(btl))
                danger_rating.append(btl)
    return danger_rating


def find_color(section):
    """color codes danger ratings"""
    if section == 'low':
        puts("Danger rating in Alpine: " + colored.green(section))
    elif section == 'moderate':
        puts("Danger rating in Alpine: " + colored.yellow(section))
    else:
        puts("Danger rating in Alpine: " + colored.red(section))


def get_weather(coord):
    """search for weather forecast"""
    progress_weather()
    response = requests.get('https://api.avalanche.ca/forecasts/en/products/point?' + coord)
    result = response.json()
    summary = result['report']['summaries']
    for x in summary:
        if x['type']['value'] == 'weather-summary':
            summary = x['content']
            print(BeautifulSoup(summary, features='html.parser').text)


def display_weather(location):
    """displays weather report"""
    print("\n")
    print("Weather forecast for " + location.get_name() + ":")
    get_weather(location.get_coord())
    return next_action()


def next_action():
    """go back option"""
    print("\n")
    next_action_ = inquirer.select(
        message="Would you like to: ",
        choices=["Go Back"],
    ).execute()
    return next_action_


def avaluator(report, reg):
    """gathers information to calculate slope evaluation based on avalanche terrain rating and danger rating"""
    print("\n")
    print("The Avaluator is a trip planner that evaluates the potential risk of a slope given "
          "the avalanche danger rating and the avalanche terrain rating (ATES), returning a warning of"
          " caution, extra caution, or not recommended. To proceed please select the elevation and "
          "terrain rating.")
    print("\n")
    while True:
        elevation = inquirer.select(
            message="What elevation will you be recreating in: ",
            choices=["Alpine", "Tree Line", "Below Tree Line"],
        ).execute()
        ates = inquirer.select(
            message="What kind of terrain will you be on: ",
            choices=["simple", "challenging", "complex"],
        ).execute()
        print("\n")
        if elevation == "Alpine":
            choice = 0
        elif elevation == "Tree Line":
            choice = 1
        else:
            choice = 2
        choices = ["simple", "challenging", "complex"]
        choices_dr = ["extreme", "high", "considerable", "moderate", "low"]
        ates_num = choices.index(ates)
        dr_num = choices_dr.index(report[choice])
        prompt_1 = "Given an elevation at " + elevation + " in " + reg.get_name() + " your danger rating is " + report[choice] + "."
        prompt_2 = " This combined with an ATES rating of " + ates + " results in a slope evaluation of: "
        puts("Given an elevation at " + elevation + " in " + reg.get_name() + " your danger rating is " + colored.red(report[choice]))
        puts("This combined with an ATES rating of " + colored.green(ates) + " results in a slope evaluation of: ")
        prompt_3 = slope_eval(ates_num, dr_num)
        total_prompt = (prompt_1 + prompt_2 + prompt_3)
        print("\n")
        next_action_ = inquirer.select(message="Would you like to: ",
                                       choices=["Use Avaluator again", "Send to a Friend", "Go Back"],
                                       ).execute()
        if next_action_ == "Go Back":
            break
        if next_action_ == "Send to a Friend":
            send_to_friend(total_prompt)


def slope_eval(ates, dr):
    """looks at matrix to determine the slope evaluation and displays it for user"""
    nr = matrix.Recommendation("Not Recommended",
                               "The current conditions for this terrain are very dangerous and it is "
                               "recommended to either change terrain or postpone the trip to when conditions "
                               "are better.")
    ec = matrix.Recommendation("Extra Caution",
                               "The current conditions for this terrain are dangerous. If you choose to "
                               "proceed, take extra caution and make conservative choices.")
    c = matrix.Recommendation("Caution ",
                              "The current conditions for this terrain are reasonable, but always take caution while "
                              "recreating in the back-country")
    arr = [nr, nr, nr], [nr, nr, nr], [c, ec, nr], [c, c, ec], [c, c, ec]
    answer = arr[dr][ates]
    puts(colored.red(answer.get_name()))
    puts(answer.get_reason())
    return answer.get_name() + ". " + answer.get_reason()


def send_to_friend(prompt):
    pass


main()
