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
# from clint.textui import puts, indent, colored
# from time import sleep
# from clint.textui import progress


gear_list = ["shovel", "probe", "beacon", "flashlight or headlamp", "fire-making kit", "signaling device", "Extra food and water", "Extra clothing",
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
                if next_action == "Calculate Slope Evaluation":
                    avaluator()
                if next_action == "Go Back":
                    continue

            if action == "Weather forecast":
                print("Weather")
                next_action_ = display_weather(reg)
                if next_action == "Go Back":
                    continue

            if action == "Recommended Gear":
                print("Essential list of gear for backcountry exploration:")
                for gear in gear_list:
                    print(gear)
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


def regions():
    region = inquirer.select(
        message="Where will you go?",
        choices=["Revelstoke", "Golden", "Banff", "Yoho", "Fernie", Choice(value=None, name="Exit")],
    ).execute()
    return region


def actions():
    action = inquirer.select(
        message="Select Mountain Info you would like to view: ",
        choices=["Avalanche Report", "Weather forecast", "Recommended Gear", "Change Region",
                 Choice(value=None, name="Exit")],
    ).execute()
    return action


def display_avi_report(region):
    print("Avalanche Report for " + region + ":")
    next_action_ = inquirer.select(
        message="Would you like to: ",
        choices=["Calculate Slope Evaluation", "Go Back",
                ],
    ).execute()
    return next_action_


def display_weather(region):
    print("Weather forecast for " + region + ":")
    return next_action()


def next_action():
    next_action_ = inquirer.select(
        message="Would you like to: ",
        choices=["Go Back"],
    ).execute()
    return next_action_


def avaluator():
    pass



main()
