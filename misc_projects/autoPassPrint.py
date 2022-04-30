import pyautogui
import subprocess
import sys

contactPerson = "[contact info here]"
browserLocation = "[browser directory here]"
browserSelect = "[browser here (lowercase)]"
screenshotFolder = "[screenshot folder here]"
webLink = "[weblink here]"

# Name screenshots to [browserSelect]PatronBox, [browser]CreateVisitor, [browser]CreateButton, [browser]PrintVisitorLink

try: 
    startup = pyautogui.confirm(
        text="Hi there.\nThis script will open a browser and try to auto-print guest passes.\nSome input will be needed right after this message and the first time the print page comes up.\nA pop up will appear when this has finished running.\nPlease click OK to continue or Cancel to exit.", 
        title = "Info", 
        buttons = ["OK", "Cancel"]
        )
    if startup == "Cancel":
        exit()
    
    status = True
    # Request number of passes to print
    while status is True:
        try:
            numPasses = int(
                pyautogui.prompt(
                    text="Please enter number of passes to print", 
                    title="Number of passes to print", 
                    default="15"
                    )
                )
            if numPasses == 0:
                pyautogui.alert("No passes to print. This script will now close.")
                status = False
                sys.exit()
            elif numPasses < 0:
                pyautogui.alert("Can't print a negative number of items. This script will now close.")
                status = False
                sys.exit()
            elif numPasses >= 20:
                pyautogui.alert(f"You have requested a large number of passes to print ({numPasses}). Please try entering a smaller number (less than 20).")
                continue
            elif numPasses >= 1:
                status = False
                break
        except ValueError:
            pyautogui.alert("Please enter a valid number")
        except TypeError:
            pyautogui.alert("No passes to print. This script will now close.")
            sys.exit()

    # Start Chrome
    subprocess.Popen(f"{browserLocation}{browserSelect}.exe")
    pyautogui.sleep(1)

    # Maximize the browser
    frontwindow = pyautogui.getActiveWindow()
    frontwindow.maximize()
    pyautogui.sleep(1)

    # Type URL
    pyautogui.write(f"{webLink}", 0.001)
    pyautogui.press("enter")

    # Wait for page to load
    pyautogui.sleep(1)
    
    # TODO: Check that there's no login page
    # TODO: If there's a login page, wait for user to log in

    # Navigate to the Create Visitor page
    try:
        location = pyautogui.locateOnScreen(f"{screenshotFolder}{browserSelect}PatronBox.png")
        pyautogui.moveTo(location)
        pyautogui.click(location)
        pyautogui.sleep(1)
        createVisitor = pyautogui.locateOnScreen(
            f"{screenshotFolder}{browserSelect}CreateVisitor.png"
        )
        pyautogui.moveTo(createVisitor)
        pyautogui.click(createVisitor)
        pyautogui.sleep(1)
    except pyautogui.ImageNotFoundException:
        pyautogui.alert(
            f"An error has occurred. Please print guest passes manually and contact {contactPerson} about this message. (Error in page navigation)"
            )
        
    # Create a visitor
    try:
        createButton = pyautogui.locateOnScreen(f"{screenshotFolder}{browserSelect}CreateButton.png")
        pyautogui.moveTo(createButton)
        pyautogui.click(createButton)
        pyautogui.sleep(1)

        # Prepare to print the first visitor slip
        printVisitor = pyautogui.locateOnScreen(
            f"{screenshotFolder}{browserSelect}PrintVisitorLink.png"
        )
        pyautogui.moveTo(printVisitor)
        pyautogui.click(printVisitor)
        pyautogui.sleep(1)

        pyautogui.alert(
            "IMPORTANT: Please ensure the receipt printer is selected before returning to this window and pressing OK."
        )
        # TODO: Check that the receipt printer is selected
        # TODO: Select the receipt printer automatically if it isn't the active printer
        # TODO: Create an on-screen print counter

        pyautogui.press("enter")
        pyautogui.sleep(1)

        # Print additional visitor passes (indicated from above input)
        count = 1
        while count < numPasses:
            createButton = pyautogui.locateOnScreen(
                f"{screenshotFolder}{browserSelect}CreateButton.png"
            )
            pyautogui.moveTo(createButton)
            pyautogui.click(createButton)
            pyautogui.sleep(1.2)

            printVisitor = pyautogui.locateOnScreen(
                f"{screenshotFolder}{browserSelect}PrintVisitorLink.png"
            )
            pyautogui.moveTo(printVisitor)
            pyautogui.click(printVisitor)
            pyautogui.sleep(1.2)

            pyautogui.press("enter")
            pyautogui.sleep(1.2)
            count += 1
    except pyautogui.ImageNotFoundException:
        pyautogui.alert(
            f"An error has occurred. Please print guest passes manually and contact {contactPerson} about this message. (Error in print loop)"
        )
    pyautogui.alert(f"Finished printing {numPasses} passes!")
    sys.exit()
except pyautogui.FailSafeException:
    pyautogui.alert("Script stopped. Fail-safe triggered by mouse moving to a corner of the screen.")
    sys.exit()