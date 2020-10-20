# LCBgo
Get notifications for when your favourite liquor is in stock at LCBO!

This project is a work in progress but here is how you can run the checkInventory script:

## Requirements
You will need to have installed the following libraries:
 - BeautifulSoup4
 - urllib

## How to Run
Clone the repository and enter the sending and receiving email addresses (Must be Gmail for now) in checkInventory.py.
Set the sending email password as an environment variable with the key "GPASS" (or modify the file to include the password)

To run the script in a terminal, cd to the working directory and run ```python3 checkInventory.py```

If the bottle in question is in stock you will receive an email!