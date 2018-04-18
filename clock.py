#!/usr/bin/env python

import time
import datetime

try:
    import unicornhathd as unicorn
    print("unicorn hat hd detected")
except ImportError:
    from unicorn_hat_sim import unicornhathd as unicorn

unicorn.rotation(180)
unicorn.brightness(0.5)

secondsProgressRow = 10

# There are 4 different types of patterns used when generating
# a number that is to be placed in a rectangle 3X5 pixels. Combinations of these
# are used to create a number pattern such as:
#   * * *
#   *
#   * * *
#   *   *
#   * * *

# 1) * * * Full Row
# 2) *   * Both Sides
# 3)     * Right Side
# 4) *     Left Side

# Composition methods
def fullLine(start, row):
  for x in range(start, start+3):
    unicorn.set_pixel(x, row, 255, 255, 255)

def bothSides(start, row):
  unicorn.set_pixel(start, row, 255, 255, 255)
  unicorn.set_pixel(start+2, row, 255, 255, 255)

def leftSide(start, row):
  unicorn.set_pixel(start, row, 255, 255, 255)

def rightSide(start, row):
  unicorn.set_pixel(start+2, row, 255, 255, 255)

# Numbers
def displayZero(x, y):
  clearNumberPixels(x, y)
  fullLine(x, y)
  bothSides(x, y-1)
  bothSides(x, y-2)
  bothSides(x, y-3)
  fullLine(x, y-4)
  unicorn.show()

def displayOne(x, y):
  clearNumberPixels(x, y)
  rightSide(x, y)
  rightSide(x, y-1)
  rightSide(x, y-2)
  rightSide(x, y-3)
  rightSide(x, y-4)
  unicorn.show()

def displayTwo(x, y):
  clearNumberPixels(x, y)
  fullLine(x, y)
  rightSide(x, y-1)
  fullLine(x, y-2)
  leftSide(x, y-3)
  fullLine(x, y-4)
  unicorn.show()

def displayThree(x, y):
  clearNumberPixels(x, y)
  fullLine(x, y)
  rightSide(x, y-1)
  fullLine(x, y-2)
  rightSide(x, y-3)
  fullLine(x, y-4)
  unicorn.show()

def displayFour(x, y):
  clearNumberPixels(x, y)
  bothSides(x, y)
  bothSides(x, y-1)
  fullLine(x, y-2)
  rightSide(x, y-3)
  rightSide(x, y-4)
  unicorn.show()

def displayFive(x, y):
  clearNumberPixels(x, y)
  fullLine(x, y)
  leftSide(x, y-1)
  fullLine(x, y-2)
  rightSide(x, y-3)
  fullLine(x, y-4)
  unicorn.show()

def displaySix(x, y):
  clearNumberPixels(x, y)
  fullLine(x, y)
  leftSide(x, y-1)
  fullLine(x, y-2)
  bothSides(x, y-3)
  fullLine(x, y-4)
  unicorn.show()

def displaySeven(x, y):
  clearNumberPixels(x, y)
  fullLine(x, y)
  rightSide(x, y-1)
  rightSide(x, y-2)
  rightSide(x, y-3)
  rightSide(x, y-4)
  unicorn.show()

def displayEight(x, y):
  clearNumberPixels(x, y)
  fullLine(x, y)
  bothSides(x, y-1)
  fullLine(x, y-2)
  bothSides(x, y-3)
  fullLine(x, y-4)
  unicorn.show()

def displayNine(x, y):
  clearNumberPixels(x, y)
  fullLine(x, y)
  bothSides(x, y-1)
  fullLine(x, y-2)
  rightSide(x, y-3)
  fullLine(x, y-4)
  unicorn.show()

def displayNumber(x,y, number):
  if number == 0:
    displayZero(x,y)
  elif number == 1:
    displayOne(x,y)
  elif number == 2:
    displayTwo(x,y)
  elif number == 3:
    displayThree(x,y)
  elif number == 4:
    displayFour(x,y)
  elif number == 5:
    displayFive(x,y)
  elif number == 6:
    displaySix(x,y)
  elif number == 7:
    displaySeven(x,y)
  elif number == 8:
    displayEight(x,y)
  elif number == 9:
    displayNine(x,y)

# Clears the pixels in a rectangle. x,y is the top left corner of the rectangle
# and its dimensions are 3X5
def clearNumberPixels(x, y):
  for y1 in range(y, y-5, -1):
    for x1 in range(x, x+3):
      # print("x1 = "+str(x1)+" y1 = "+str(y1))
      unicorn.set_pixel(x1, y1, 0, 0, 0)
  unicorn.show()

def displayTimeDots(x, y):
  unicorn.set_pixel(x, y-1, 255, 0, 0)
  unicorn.set_pixel(x, y-3, 255, 0, 0)
  unicorn.show()

def displayDateDots(x, y):
  unicorn.set_pixel(x+1, y, 255, 0, 0)
  unicorn.set_pixel(x+1, y-1, 255, 0, 0)
  unicorn.set_pixel(x+1, y-2, 255, 0, 0)
  unicorn.set_pixel(x, y-2, 255, 0, 0)
  unicorn.set_pixel(x, y-3, 255, 0, 0)
  unicorn.set_pixel(x, y-4, 255, 0, 0)
  unicorn.show()  

# Gets a specific part of the current time, passed to strftime, then it is
# split into its individual numbers and converted into integers. Used to feed
# the display with numbers
def getMinuteParts():
  minute = datetime.datetime.now().strftime("%M")
  return [int(x) for x in minute]

def getTimeParts(timePart):
  parts = datetime.datetime.now().strftime(timePart)
  return [int(x) for x in parts]  

def setStartingSecondsProgressRow():
  # Grey starting bit
  unicorn.set_pixel(0, secondsProgressRow, 100, 100, 100)
  unicorn.set_pixel(1, secondsProgressRow, 100, 100, 100)

  # Making red part
  for x in range(2,14):
    unicorn.set_pixel(x, secondsProgressRow, 200, 50, 50)

  # Grey ending bit
  unicorn.set_pixel(14, secondsProgressRow, 100, 100, 100)
  unicorn.set_pixel(15, secondsProgressRow, 100, 100, 100)

displayedHourParts = getTimeParts('%H')
displayedMinuteParts = getTimeParts('%M')
displayedMonthParts = getTimeParts('%m')
displayedDayParts = getTimeParts('%d')

# Display Current Time
displayNumber(0,15, displayedHourParts[0])
displayNumber(4,15, displayedHourParts[1])
displayTimeDots(7,15)
displayNumber(9,15, displayedMinuteParts[0])
displayNumber(13,15, displayedMinuteParts[1])

# Display Day and Month
displayNumber(0,9, displayedDayParts[0])
displayNumber(4,9, displayedDayParts[1])
displayDateDots(7,9)
displayNumber(9,9, displayedMonthParts[0])
displayNumber(13,9, displayedMonthParts[1])

# set the seconds progress row
setStartingSecondsProgressRow()

current_milli_time = lambda: int(round(time.time() * 1000))

step = 0

try:
  while True:
    hourParts = getTimeParts('%H')
    minuteParts = getTimeParts('%M')
    dayParts = getTimeParts('%d')
    monthParts = getTimeParts('%m')

    # TIME Details
    # Only update first hour number if it is different to what is currently displayed
    if hourParts[0] != displayedHourParts[0]:
      displayedHourParts[0] = hourParts[0]
      displayNumber(0,15, hourParts[0])

    # Only update second hour number if it is different to what is currently displayed
    if hourParts[1] != displayedHourParts[1]:
      displayedHourParts[1] = hourParts[1]
      displayNumber(4,15, hourParts[1])

    # Only update first minute number if it is different to what is currently displayed
    if minuteParts[0] != displayedMinuteParts[0]:
      displayedMinuteParts[0] = minuteParts[0]
      displayNumber(9,15, minuteParts[0])

    # Only update second minute number if it is different to what is currently displayed
    if minuteParts[1] != displayedMinuteParts[1]:
      displayedMinuteParts[1] = minuteParts[1]
      displayNumber(13,15, minuteParts[1])

    # MONTH Details
    # Only update first day number if it is different to what is currently displayed
    if dayParts[0] != displayedDayParts[0]:
      displayedDayParts[0] = dayParts[0]
      displayNumber(0,9, dayParts[0])

    # Only update second day number if it is different to what is currently displayed
    if dayParts[1] != displayedDayParts[1]:
      displayedDayParts[1] = dayParts[1]
      displayNumber(4,9, dayParts[1])

    # Only update first month number if it is different to what is currently displayed
    if monthParts[0] != displayedMonthParts[0]:
      displayedMonthParts[0] = monthParts[0]
      displayNumber(9,9, monthParts[0])

    # Only update second month number if it is different to what is currently displayed
    if monthParts[1] != displayedMonthParts[1]:
      displayedMonthParts[1] = monthParts[1]
      displayNumber(13,9, monthParts[1])

    # Calculating how many seconds pixels to light up
    currentSeconds = datetime.datetime.now().second
    percentOfMinuteComplete = int((float(currentSeconds)/60.0)*100)
    pixelsToLightUp = int((12.0/100.0)*float(percentOfMinuteComplete))

    # Make the whole progress row red
    if pixelsToLightUp == 0:
      setStartingSecondsProgressRow()

    # Making completed pixels green
    for x in range(2, pixelsToLightUp+2):
      unicorn.set_pixel(x, secondsProgressRow, 0, 100, 0)

    # Setting current pixel brighter green
    unicorn.set_pixel(pixelsToLightUp+2, secondsProgressRow, 0, 255, 0)
    unicorn.show()
    # Sleep for 0.5 because the display doesn't need to update that often
    time.sleep(0.5)
except KeyboardInterrupt:
  unicorn.off()