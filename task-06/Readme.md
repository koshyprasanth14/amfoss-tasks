Before starting with this project, I already had a basic understanding of Python. However, creating a Discord bot required further knowledge of Python and its libraries. I installed the required libraries, including Discord.py and Beautiful Soup, using pip. 

To retrieve live cricket scores, I used Beautiful Soup to scrape a cricket based website. This involved sending HTTP requests and parsing HTML content.

I faced several challenges during development, including debugging issues in my code. Learning to identify and fix errors was a significant part of the process.
I implemented error handling mechanisms to provide users with informative error messages when the bot encountered problems.

I created a Discord bot on the Discord Developer Portal, which provided me with a unique bot token.
I invited the bot to my Discord server, giving it the necessary permissions to send messages and read messages.

I started by defining the basic structure of my bot using Discord.py, including setting up event listeners and command handlers.
I implemented the following commands:
        /livescore: Displays live scores for ongoing cricket matches using Beautiful Soup to scrape cricket websites.
        /csv: Sends a CSV file containing details of live scores asked for up to that point. I used Python's CSV module to manage data.
        /help: Provides information about available commands and how to use them.

I extensively tested the bot's functionality on my Discord server, ensuring that it responded correctly to commands and handled errors.

Despite facing tough challenges and debugging issues, the end result is a functional bot that provides cricket enthusiasts with live scores and match details. 
