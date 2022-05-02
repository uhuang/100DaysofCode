"""This script attempts to automate the procedure to print guest passes for public computing.
It uses screenshots to locate and click the appropriate buttons/tabs.
When naming screenshots, add the browser name in lowercase to:
PatronBox, CreateVisitor, CreateButton, PrintVisitorLink
This script assumes screenshots are saved as .png. Adjust accordingly if otherwise.
Required: Python 3.2 or higher, pyautogui (can be installed via pip)
"""

import subprocess
import sys
import tkinter
import pyautogui
from tkinter import *
from tkinter import ttk

CONTACT_PERSON = "Una (huang@portlib.org)"
BROWSER_LOCATION = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\"
BROWSER_SELECT = "chrome"
SCREENSHOT_FOLDER = "C:\\Users\\PC\\Desktop\\Minor Coding Projects\\screenshots\\"
SITE_LINK = "https://print.portlandlibrary.com/SignUp/"

try:
    startup = pyautogui.confirm(
        text="""Hi there.
        This script will open a browser and try to auto-print guest passes.
        Some input will be needed right after this message and the first time the print page comes up.
        A pop up will appear when this has finished running.
        DO NOT use the mouse/keyboard after entering the input (unless otherwise indicated).
        Please click OK to continue or Cancel to exit.""",
        title="Info",
        buttons=["OK", "Cancel"],
    )
    if startup == "Cancel":
        sys.exit()
    # Request number of passes to print
    while True:
        try:
            NUM_PASSES = int(
                pyautogui.prompt(
                    text="Please enter number of passes to print",
                    title="Number of passes to print",
                    default="15",
                )
            )
            if NUM_PASSES == 0:
                pyautogui.alert("No passes to print. Exiting.")
                sys.exit()
            elif NUM_PASSES < 0:
                pyautogui.alert("Can't print a negative number of items. Exiting.")
                sys.exit()
            elif NUM_PASSES >= 20:
                pyautogui.alert(
                    f"You have requested a large number of passes ({NUM_PASSES}).\
                    \nPlease try entering a smaller number (less than 20)."
                )
                continue
            elif NUM_PASSES >= 1:
                break
        except ValueError:
            pyautogui.alert("Please enter a valid number")
        except TypeError:
            pyautogui.alert("No passes to print. Exiting.")
            sys.exit()
    # Start browser
    subprocess.Popen(f"{BROWSER_LOCATION}{BROWSER_SELECT}.exe")
    pyautogui.sleep(1)

    # Maximize the browser
    frontwindow = pyautogui.getActiveWindow()
    frontwindow.maximize()
    pyautogui.sleep(1)

    # Type URL
    pyautogui.write(f"{SITE_LINK}", 0.001)
    pyautogui.press("enter")

    # Wait for page to load
    pyautogui.sleep(1)

    # Check for lack of login page
    while True:
        try:
            screen_check = pyautogui.locateOnScreen(
                f"{SCREENSHOT_FOLDER}{BROWSER_SELECT}PatronBox.png"
            )
            if screen_check == None:
                pyautogui.alert("Please log in to Pharos before clicking OK to continue.")
            else:
                break
        except pyautogui.ImageNotFoundException:
            pyautogui.alert(
                "An error has occurred. \n"
                f"Please print passes manually and contact {CONTACT_PERSON}."
                "(Error: Login check loop)"
            )
            sys.exit()
    # Navigate to the Create Visitor page
    try:
        location = pyautogui.locateOnScreen(
            f"{SCREENSHOT_FOLDER}{BROWSER_SELECT}PatronBox.png"
        )
        pyautogui.moveTo(location)
        pyautogui.click(location)
        pyautogui.sleep(1)
        createVisitor = pyautogui.locateOnScreen(
            f"{SCREENSHOT_FOLDER}{BROWSER_SELECT}CreateVisitor.png"
        )
        pyautogui.moveTo(createVisitor)
        pyautogui.click(createVisitor)
        pyautogui.sleep(1)
    except pyautogui.ImageNotFoundException:
        pyautogui.alert(
            f"""An error has occurred.
            Please print passes manually and contact {CONTACT_PERSON}.
            (Error in page navigation)"""
        )
        sys.exit()
    # Create a visitor
    try:
        createButton = pyautogui.locateOnScreen(
            f"{SCREENSHOT_FOLDER}{BROWSER_SELECT}CreateButton.png"
        )
        pyautogui.moveTo(createButton)
        pyautogui.click(createButton)
        pyautogui.sleep(1)

        # Prepare to print the first visitor slip
        printVisitor = pyautogui.locateOnScreen(
            f"{SCREENSHOT_FOLDER}{BROWSER_SELECT}PrintVisitorLink.png"
        )
        pyautogui.moveTo(printVisitor)
        pyautogui.click(printVisitor)
        pyautogui.sleep(1)

        pyautogui.alert(
            """IMPORTANT:
            Please ensure the receipt printer is selected before returning to this window and pressing OK."""
        )
        # Check that the receipt printer is selected
        while True:
            try:
                receiptPrinter = pyautogui.locateOnScreen(
                    f"{SCREENSHOT_FOLDER}{BROWSER_SELECT}ReceiptPrinterCheck.png"
                    )
                if receiptPrinter == None:
                    pyautogui.alert("Please set the printer to Receipt Printer")
                else:
                    break
            except pyautogui.ImageNotFoundException:
                pyautogui.alert("An error has occurred. \n"
                f"Please print passes manually and contact {CONTACT_PERSON}.\n"
                "(Error: Receipt printer check)"
                )
        # TODO: Select the receipt printer automatically if it isn't the active printer
        printButton = pyautogui.locateOnScreen(
            f"{SCREENSHOT_FOLDER}{BROWSER_SELECT}PrintButton.png"
            )
        pyautogui.moveTo(printButton)
        pyautogui.click(printButton)
        # pyautogui.press("enter")
        pyautogui.sleep(1)

        # Print additional visitor passes (indicated from above input)
        COUNT = 1
        # TODO: Create an on-screen print counter using tkinter
        while COUNT < NUM_PASSES:
            # win = Tk()
            # win.geometry("200x100")
            # Label(win, text= f"Printing {COUNT} of {NUM_PASSES}...",font=('Helvetica bold', 15)).pack(pady=20)
            # win.attributes('-topmost',True)
            createButton = pyautogui.locateOnScreen(
                f"{SCREENSHOT_FOLDER}{BROWSER_SELECT}CreateButton.png"
            )
            pyautogui.moveTo(createButton)
            pyautogui.click(createButton)
            pyautogui.sleep(1.2)

            printVisitor = pyautogui.locateOnScreen(
                f"{SCREENSHOT_FOLDER}{BROWSER_SELECT}PrintVisitorLink.png"
            )
            pyautogui.moveTo(printVisitor)
            pyautogui.click(printVisitor)
            pyautogui.sleep(1.2)

            pyautogui.press("enter")
            pyautogui.sleep(1.2)
            COUNT += 1
            # win.mainloop()
            # win.destroy()
    except pyautogui.ImageNotFoundException:
        pyautogui.alert(
            f"""An error has occurred.
            Please print passes manually and contact {CONTACT_PERSON}.
            (Error in print loop)"""
        )
    pyautogui.alert(f"Finished printing {NUM_PASSES} passes!")
    sys.exit()
except pyautogui.FailSafeException:
    pyautogui.alert(
        "Script stopped. Failsafe activated by mouse moving to a corner of the screen."
    )
    sys.exit()
