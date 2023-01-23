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
        action = actions()
        if action == "Avalanche Report":
            print("Avi report")
            display_avi_report(reg)
        if action == "Weather Forecast":
            print("Weather")
            display_weather(reg)
        if action == "Recommended Gear":
            for gear in gear_list:
                print(gear)
        if action == "Change Region":
            continue
        if action == "Exit":
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
        choices=["Avalanche Report", "Weather forcast", "Recommended Gear", "Change Region",
                 Choice(value=None, name="Exit")],
    ).execute()
    return action


def display_avi_report(region):
    print("Avalanche Report for " + region + ":")
    next_action = inquirer.select(
        message="Would you like to: ",
        choices=["Calculate Slope Evaluation", "Go Back", "Select New Region",
                 Choice(value=None, name="Exit")],
    ).execute()
    return next_action


def display_weather(region):
    print("Weather forecast for " + region + ":")
    next_action = inquirer.select(
        message="Would you like to: ",
        choices=["Go Back", "Select New Region",
                 Choice(value=None, name="Exit")],
    ).execute()
    return next_action





main()
