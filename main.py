import math
import time
import replit
import colorama
from colorama import *
from math import tan, cos, sin, radians, degrees

#, asin, acos, atan, radians, degrees


num1 = 0.0
num2 = 0.0
sol = 0.0


def addition(pNum1, pNum2):
    print("The answer of your addition is ", round(pNum1 + pNum2, 2))

def multiply(pNum1, pNum2):
    print("The answer of your multiplication is ", round(pNum1 * pNum2, 2))

def divide(pNum1, pNum2):
    if pNum2 == 0:
        print("undefined")
    else:
        fTotal = print("The answer of your division is ", round(pNum1 / pNum2, 2))
    return(fTotal)

def subtract(pNum1, pNum2):
    print("The answer of your subtract is ", round(pNum1 - pNum2, 2))

def square(pNum1, pNum2):
    print("The answer of your squaring is ", round(pNum1 ** pNum2, 2))

def squareRoot(pNum1):
    print("The answer is ", round(math.sqrt(pNum1), 2))

def sine(pNum1): 
    print("The answer is ", round(math.sin(pNum1), 5))
    sine = sin(degrees(num1))

def cosine(pNum1):
    print("The answer is ", round(math.cos(pNum1), 5))

def tangent(pNum1):
    print("The answer is ", round(math.tan(pNum1), 5))
    tangent = tan(degrees(num1))

def hypotenuse(pNum1, pNum2):
    hyp = math.sqrt(pNum1**2 + pNum2**2)
    print("The hypotenuse is ", round(hyp, 2))

def adjacent(pNum1, pNum2):
    adj = math.sqrt(pNum1**2 - pNum2**2)
    print("The adjacent is ", round(adj, 2))

def opposite(pNum1, pNum2):
    opp = math.sqrt(pNum1**2 - pNum2**2)
    print("The opposite is ", round(opp, 2))


def start():
  print(Style.BRIGHT + Fore.CYAN)
  print("- - - - - WELCOME TO THE SHREKULATOR - - - - -")
  print("Instruction Manual:")
  print("For addition use +")
  print("For subtraction use -")
  print("For division use /")
  print("For multiplication use * OR x")
  print("For exponents use ** OR ^")
  print("To square root, use 'sqrt'")
  print("To find the hypotenuse, use 'hyp'")
  print("To find the adjacent, use 'adj'")
  print("To find the opposite, use 'opp'")
  print("To use sin use 'sin' (calculated in radians)")
  print("To use cos use 'cos' (calculated in radians)")
  print("To use tan use 'tan' (calculated in radians)")
  print("- - - - - - - - - - - - - - - -")
  operation = str(input("Enter the operation: "))
  if operation == "sqrt" or operation == "sin" or operation == "cos" or operation == "tan":
    num1 = float(input("Enter the number: "))
    if num1 == 69 or num1 == 420:
      print("Very nice")
  elif operation == "hyp":
    num1 = float(input("Enter the adjacent: "))
    num2 = float(input("Enter the opposite: "))
  elif operation == "adj":
    num1 = float(input("Enter the hypotenuse: "))
    num2 = float(input("Enter the opposite: "))
  elif operation == "opp":
    num1 = float(input("Enter the hypotenuse: "))
    num2 = float(input("Enter the adjacent: "))
  else:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    if num1 == 69 or num2 == 69:
      print("Shrek would very much like to do 69 with you")
    if num1 == 420 or num2 == 420:
      print("Shrek would very much like to smoke weed with you")
      #print("            .:.
#	                       :|:
#                        .:|:.
#                        ::|::
#         :.             ::|::             .:
#         :|:.          .::|::.          .:|:
#         ::|:.         :::|:::         .:|:;
#         `::|:.        :::|:::        .:|::'
#          ::|::.       :::|:::       .::|:;
#          `::|::.      :::|:::      .::|::'
#           :::|::.     :::|:::     .::|::;
#           `:::|::.    :::|:::    .::|::;'
#`::.        `:::|::.   :::|:::   .::|::;'      .:;'
#  `:::..     ¹::|::.  :::|:::  .::|::¹    ..::;'
#   `:::::.    ':|::. :::|::: .::|:'   ,::::;'
#       `:::::.    ':|:::::|:::::|:'   :::::;'
#         `:::::.:::::|::::|::::|::::.,:::;'
#            ':::::::::|:::|:::|:::::::;:'
#               ':::::::|::|::|:::::::''
#                    `::::::::::;'
#                   .:;'' ::: ``::.
#                        :':':
#                          ;")

  if operation == "+":
      addition(num1, num2)
  elif operation == "*" or operation == "x" :
      multiply(num1, num2)
  elif operation == "/":
      divide(num1, num2)
  elif operation == "-":
      subtract(num1, num2)
  elif operation == "**" or operation == "^":
      square(num1, num2)
  elif operation == "sqrt":
      squareRoot(num1)
  elif operation == "sin":
      sine(num1)
  elif operation == "cos":
      cosine(num1)
  elif operation == "tan":
      tangent(num1)
  elif operation == "hyp":
      hypotenuse(num1, num2)
  elif operation == "adj":
      adjacent(num1, num2)
  elif operation == "opp":
      opposite(num1, num2)
  else:
      print("Good question, I don't know everything Donkey!")
  
  time.sleep(1)
  print(Style.BRIGHT + Fore.GREEN)
  print(" ⢀⡴⠑⡄⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣤⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n ⠸⡇⠀⠿⡀⠀⠀⠀⣀⡴⢿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n ⠀⠀⠀⠀⠑⢄⣠⠾⠁⣀⣄⡈⠙⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀\n ⠀⠀⠀⠀⢀⡀⠁⠀⠀⠈⠙⠛⠂⠈⣿⣿⣿⣿⣿⠿⡿⢿⣆⠀⠀⠀⠀⠀⠀⠀\n ⠀⠀⠀⢀⡾⣁⣀⠀⠴⠂⠙⣗⡀⠀⢻⣿⣿⠭⢤⣴⣦⣤⣹⠀⠀⠀⢀⢴⣶⣆\n ⠀⠀⢀⣾⣿⣿⣿⣷⣮⣽⣾⣿⣥⣴⣿⣿⡿⢂⠔⢚⡿⢿⣿⣦⣴⣾⠁⠸⣼⡿\n ⠀⢀⡞⠁⠙⠻⠿⠟⠉⠀⠛⢹⣿⣿⣿⣿⣿⣌⢤⣼⣿⣾⣿⡟⠉⠀⠀⠀⠀⠀\n ⠀⣾⣷⣶⠇⠀⠀⣤⣄⣀⡀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀\n ⠀⠉⠈⠉⠀⠀⢦⡈⢻⣿⣿⣿⣶⣶⣶⣶⣤⣽⡹⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀\n ⠀⠀⠀⠀⠀⠀⠀⠉⠲⣽⡻⢿⣿⣿⣿⣿⣿⣿⣷⣜⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀\n ⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣷⣶⣮⣭⣽⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀\n ⠀⠀⠀⠀⠀⠀⣀⣀⣈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀\n ⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀ \n ⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀\n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠻⠿⠿⠿⠿⠛⠉")
  time.sleep(1)
  print(Style.BRIGHT + Fore.CYAN)
  restart = str(input("Do you want to restart (yes/no)? "))
  restart = restart.replace(" ", "")
  restart = restart.lower()
  if restart == "yes":
	  time.sleep(1)
	  replit.clear()
	  start()
  elif restart == "no":
    print("Ok, now get out of my swamp!")
  else:
    print("Ok, get out of my swamp!")
start() 