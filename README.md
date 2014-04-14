RedditSearchWidget
=============
This is a minimalist search widget for searching Reddit posts, using the wxPython GUI API and the Reddit API. Using this, you can search Reddit using specific criteria including:

- subreddit
- submission title
- submission time
- etc.

Installation & Dependencies
=============
To run this widget script, you will need the following items:

- **The RedditSearchWidget.py python file.** This can be downloaded from the main project page and installed in the local directory of your choosing. After you have installed this and the proper dependencies, you may run this script however you would like to, whether it be through the terminal or through an IDE.
- **Python 2.7.6** This is the latest update of Python 2. Python 3 is not officially compatible with wxPython as of now and the script will not compile with Python 3. The latest version of Python 2 is advisable, however it will probably work with any version of Python 2.6 or 2.7. This can be found here https://www.python.org/download/releases/2.7.6/
- **wxPython** The GUI API which can be found here http://wxpython.org/download.php. For Mac Users, the Cocoa build is recommended. 

Examples
=============
Here are some examples showing you how to use this search app. If you would prefer reading the instructions, scroll down to the FAQ section.

There are 3 ways you can get the search results:

- Display it in the window of the app
- Get it in a personal Reddit message
- Get it sent to your Gmail

The following videos demonstrate how to use each, respectively. 

[Display Demo](https://www.youtube.com/watch?v=PsaaO2hIyjw)

[Reddit PM Demo](https://www.youtube.com/watch?v=QvwyRUeosE4)

[Gmail Demo](https://www.youtube.com/watch?v=GuRXJHX4_Gk)

FAQ
=============

**WHAT DOES THIS WIDGET DO EXACTLY?**

This widget's purpose is to search subreddits for the keywords you give, given the parameters you give it.

**HOW DO I USE IT AND WHAT DOES EVERYTHING DO?**

There are multiple fields:

- **Message Choice** You can choose how you have the search result information messaged to you, the options are:

    - **_Display_** Display the results in a new window within the application.
    - **Reddit** Have the results mailed to you in a personal message.
    - **Gmail** Have the results sent to your gmail
    
- **Username/Password** If you chose either 'Reddit' or 'Gmail' for your message choice, you simply imput your Reddit Username or Gmail username (including '@gmail.com') along with your corresponding password.

- **Subreddit** This is the specific subreddit you want to search. Multiple subreddits is not supported at this time.

- **Keyword(s)** They are the keywords you are searching for in the posts. If you want to search for multiple words, separate words with a space. 

- **Get** Get, as in "get hot", or get the posts from the hot section of the subreddit. Hot is not your only option; your options are:

    - hot
    - new
    - rising
    - controversial
    - top
    
- **Items** This is how many of the most recent posts of the specified section The input has to be an integer between 1 and 100. 

- **From:** If you select "controverisal" or "top", this pops up and asks you to choose how recent you want the posts to be; your options are:

	- hour
    - day
    - week
    - month
    - year
    - all
    
- **Search** This determines which part of the post you want to search for your keyword. Selecting "comments" and "title" will return results that had the keyword in  the comments OR the title. Your options are:
	
    - Title
    - Text
    - Comments
    
![alt tag](http://i.imgur.com/5FJzI6U.png)    