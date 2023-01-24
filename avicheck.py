# Author: Brenda Levy
# GitHub username: bqujiada
# Date: 1/23/23 
# Description: Backcountry Planning App

from InquirerPy import inquirer
from InquirerPy.base.control import Choice
# from InquirerPy.separator import Separator
import pyfiglet
from datetime import datetime

# import requests
from clint.textui import puts, indent, colored

# from time import sleep
# from clint.textui import progress


gear_list = ["shovel", "probe", "beacon", "flashlight or headlamp", "fire-making kit", "signaling device",
             "Extra food and water", "Extra clothing",
             "First aid kit", "Pocket knife/multitool", "sun protection", "sun projection", "emergency shelter - tarp"]


def main():
    """main driver function"""
    reg = None
    hello_text = pyfiglet.figlet_format("AVI-CHECK", font="colossal", width=110)
    bye_text = pyfiglet.figlet_format("Goodbye", font="colossal", width=110)
    print(hello_text)
    print("** Welcome to AVI-CHECK, your one stop for trip planning and mountain safety")
    print("** Use this took to check the current avalanche report, weather forecast, recommended gear, "
          "and calculate slope evaluations")
    print("** Today is", datetime.now())
    print("** Use the arrow keys to get started!")
    while True:
        print("\n")
        region = regions()
        if region == "Golden":
            print("Golden")
            reg = "Golden"
        if region == "Banff":
            print("Banff")
            reg = "Banff"
        if region == "Revelstoke":
            print("Revelstoke")
            reg = "Revelstoke"
        if region == "Fernie":
            print("Fernie")
            reg = "Fernie"
        if region is None:
            break
        while True:
            breaker = False
            action = actions()
            if action == "Avalanche Report":
                print("Avi report")
                next_action_ = display_avi_report(reg)
                if next_action_ == "Calculate Slope Evaluation":
                    avaluator(reg)
                if next_action == "Go Back":
                    continue

            if action == "Weather forecast":
                print("Weather")
                next_action_ = display_weather(reg)
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
    region = inquirer.select(
        message="Where will you go?",
        choices=["Revelstoke", "Golden", "Banff", "Fernie", Choice(value=None, name="Exit")],
    ).execute()
    return region


def actions():
    print("\n")
    action = inquirer.select(
        message="Select Mountain Info you would like to view: ",
        choices=["Avalanche Report", "Weather forecast", "Recommended Gear", "Change Region",
                 Choice(value=None, name="Exit")],
    ).execute()
    return action


def display_avi_report(region):
    """displays avalanche report"""
    print("\n")
    print("Avalanche Report for " + region + ":")
    next_action_ = inquirer.select(
        message="Would you like to: ",
        choices=["Calculate Slope Evaluation", "Go Back",
                 ],
    ).execute()
    return next_action_


def display_weather(region):
    """displays weather report"""
    print("\n")
    print("Weather forecast for " + region + ":")
    return next_action()


def next_action():
    """go back option"""
    print("\n")
    next_action_ = inquirer.select(
        message="Would you like to: ",
        choices=["Go Back"],
    ).execute()
    return next_action_


def avaluator(reg):
    """calculates a slope evaluation based on avalanche terrain rating and danger rating"""
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
        print("Given an elevation at " + elevation + " in " + reg + " and an ATES rating of " + ates + " your slope "
                                                                                                      "evaluation "
                                                                                                      "is ")
        next_action_ = inquirer.select(
            message="Would you like to: ",
            choices=["Use Avaluator again", "Go Back"],
        ).execute()
        if next_action_ == "Go Back":
            break


main()
