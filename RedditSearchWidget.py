import wx
import wx.lib.agw.hyperlink as hl

#Thread frame where results are printed
class ThreadFrame(wx.Frame):
    def __init__(self, title):
        #Constructor
        wx.Frame.__init__(self, parent=None, size = (500, 400))
        self.ThreadPanel = ThreadPanel(self)
        self.SetTitle(title)
        self.CreateStatusBar()
        self.SetStatusText("Enjoy your threads! Close this window to get back to the main one.")
        self.Center()

class ThreadPanel(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)
        self.frame = parent
                #CREATE GENERALSIZER FOR THREADS
        self.threadSizer = wx.FlexGridSizer(rows = 101, cols=2, vgap=10, hgap=10)
        self.SetSizer(self.threadSizer)
        self.SetAutoLayout(1)

#Main frame where input is gotten
class MainFrame(wx.Frame):
    def __init__(self, statusText="Check the FAQ if you have questions!", button="displayButton", title="Reddit Search Application", ):
        #Constructor
        wx.Frame.__init__(self, parent=None, size=(375, 600))
        self.SetTitle(title)
        self.MainPanel = MainPanel(self)
        trueButton = getattr(self.MainPanel, button)
        trueButton.SetValue(True)
        self.CreateStatusBar()
        self.SetStatusText(statusText)
        self.Center()

        menuBar = wx.MenuBar()
        menu1 = wx.Menu()

        menu1.Append(1, "&FAQ", "Click this for all your questions!")
        menu1.AppendSeparator()

        menu1.Append(2, "E&xit", "Exit the application.")

        menuBar.Append(menu1, "File")

        self.SetMenuBar(menuBar)

class MainPanel(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)
        self.frame = parent

        #CREATE THE GENERAL SIZER
        self.sizer = wx.BoxSizer(wx.VERTICAL)

        #ADD WELCOME TEXT
        welcomeString = "Search any subreddit for anything you want.\n\n" \
                        "If this is your first time using this, read the FAQ\n" \
                        "in the menu.\n\n" \
                        "And remember, the statusbar is your best friend!\n"
        welcomeText = wx.StaticText(self, -1, welcomeString, size=(-1,-1))
        font = wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL)
        welcomeText.SetFont(font)

        self.sizer.Add(welcomeText, 0, wx.ALIGN_CENTER | wx.TOP, 20)

        #ADD CHOICE BUTTONS
        self.buttonSizer = wx.BoxSizer(wx.HORIZONTAL)

        self.displayButton = wx.RadioButton(self, -1, "Display", style=wx.RB_GROUP)
        self.displayButton.Bind(wx.EVT_RADIOBUTTON, self.onDisplay)
        self.displayButton.SetValue(True)

        self.redditButton = wx.RadioButton(self, -1, "Reddit")
        self.redditButton.Bind(wx.EVT_RADIOBUTTON, self.onReddit)

        self.gmailButton= wx.RadioButton(self, -1, "Gmail")
        self.gmailButton.Bind(wx.EVT_RADIOBUTTON, self.ongmail)

        self.buttonSizer.AddMany([(self.displayButton, 0, wx.ALIGN_CENTER | wx.BOTTOM | wx.RIGHT | wx.TOP, 10),
                                  (self.redditButton, 0, wx.ALIGN_RIGHT | wx.BOTTOM | wx.RIGHT | wx.LEFT | wx.TOP, 10),
                                  (self.gmailButton, 0, wx.ALIGN_CENTER | wx.BOTTOM | wx.LEFT | wx.TOP, 10)])

        self.sizer.Add(self.buttonSizer, 0, wx.CENTER)

        #CREATE GRID SIZER FOR ALMOST EVERYTHING ELSE
        self.gridSizer = wx.FlexGridSizer(rows=100, cols=2)

        # gmail
        self.gmailLabel = wx.StaticText(self, -1, "Gmail: ")
        self.gmailForm = wx.TextCtrl(self, -1, "Gmail goes here", size = (200, -1))
        self.gmailForm.Bind(wx.EVT_LEFT_DOWN, lambda event: self.gmailForm.Clear())
        self.gmailForm.Bind(wx.EVT_KEY_UP, lambda event: self.gmailForm.Clear() if event.GetUnicodeKey() == wx.WXK_TAB else None)
        self.gridSizer.Add(self.gmailLabel, 0, wx.TOP | wx.LEFT | wx.BOTTOM | wx.ALIGN_LEFT, 10)
        self.gridSizer.Add(self.gmailForm, 0, wx.TOP | wx.RIGHT | wx.BOTTOM | wx.ALIGN_LEFT, 10)
        self.gmailLabel.Hide()
        self.gmailForm.Hide()

        # Username
        self.usernameForm = wx.TextCtrl(self, -1, "Reddit username goes here.", size=(200, -1))
        self.usernameLabel = wx.StaticText(self, -1, "Username: ")
        self.gridSizer.Add(self.usernameLabel, 0, wx.TOP | wx.LEFT | wx.BOTTOM | wx.ALIGN_LEFT, 10)
        self.gridSizer.Add(self.usernameForm, 0, wx.TOP | wx.RIGHT | wx.BOTTOM | wx.ALIGN_LEFT, 10)
        self.usernameForm.Bind(wx.EVT_LEFT_DOWN, lambda event: self.usernameForm.Clear())
        self.usernameForm.Bind(wx.EVT_KEY_UP, lambda event: self.usernameForm.Clear() if event.GetUnicodeKey() == wx.WXK_TAB else None)
        self.usernameLabel.Hide()
        self.usernameForm.Hide()

        # Password
        self.passwordForm = wx.TextCtrl(self, -1, size=(200, -1), style=wx.TE_PASSWORD)
        self.passwordLabel = wx.StaticText(self, -1, "Password: ")
        self.gridSizer.Add(self.passwordLabel, 0, wx.TOP | wx.LEFT | wx.BOTTOM | wx.ALIGN_LEFT, 10)
        self.gridSizer.Add(self.passwordForm, 0, wx.wx.TOP | wx.RIGHT | wx.BOTTOM | wx.ALIGN_LEFT, 10)
        self.passwordForm.Hide()
        self.passwordLabel.Hide()

        # Subreddit
        self.subredditForm = wx.TextCtrl(self, -1, "Case Sensitive!", size=(200, -1))
        self.subredditLabel = wx.StaticText(self, -1, "Subreddit: /r/")
        self.gridSizer.Add(self.subredditLabel, 0, wx.TOP | wx.LEFT | wx.BOTTOM | wx.ALIGN_LEFT, 10)
        self.gridSizer.Add(self.subredditForm, 0, wx.TOP | wx.RIGHT | wx.BOTTOM | wx.ALIGN_LEFT, 10)
        self.subredditForm.Bind(wx.EVT_LEFT_DOWN, lambda event: self.subredditForm.Clear())
        self.subredditForm.Bind(wx.EVT_KEY_UP, lambda event: self.subredditForm.Clear() if event.GetUnicodeKey() == wx.WXK_TAB else None)

        # Keywords
        self.keyWordsForm = wx.TextCtrl(self, -1, "Separate words with spaces.", size=(200, -1))
        self.keyWordsLabel = wx.StaticText(self, -1, "Keyword(s): ")
        self.gridSizer.Add(self.keyWordsLabel, 0, wx.wx.TOP | wx.LEFT | wx.BOTTOM | wx.ALIGN_LEFT, 10)
        self.gridSizer.Add(self.keyWordsForm, 0, wx.TOP | wx.RIGHT | wx.BOTTOM | wx.ALIGN_LEFT, 10)
        self.keyWordsForm.Bind(wx.EVT_LEFT_DOWN, lambda event: self.keyWordsForm.Clear())
        self.keyWordsForm.Bind(wx.EVT_KEY_UP, lambda event: self.keyWordsForm.Clear() if event.GetUnicodeKey() == wx.WXK_TAB else None)
        self.keyWordsForm.Bind(wx.EVT_LEFT_DOWN, lambda event: self.frame.SetStatusText("Leave this blank if you want the most recent posts!"))

        #Get
        getList = ['hot', 'new', 'rising', 'controversial', 'top']
        self.getChoice = wx.Choice(self, -1, size=(200, -1), choices = getList)
        self.getChoice.Bind(wx.EVT_CHOICE, self.onChoice)
        self.getLabel = wx.StaticText(self, -1, "Get: ")

        self.gridSizer.Add(self.getLabel, 0, wx.TOP | wx.BOTTOM | wx.LEFT | wx.ALIGN_LEFT, 10)
        self.gridSizer.Add(self.getChoice, 0, wx.TOP | wx.BOTTOM | wx.RIGHT | wx.ALIGN_LEFT, 10)

        # Items
        self.itemsForm = wx.TextCtrl(self, -1, "Enter a number 1-100!", size=(200, -1))
        self.itemsLabel = wx.StaticText(self, -1, "Items: ")
        self.gridSizer.Add(self.itemsLabel, 0, wx.TOP | wx.LEFT | wx.BOTTOM | wx.ALIGN_LEFT, 10)
        self.gridSizer.Add(self.itemsForm, 0, wx.TOP | wx.RIGHT | wx.BOTTOM | wx.ALIGN_LEFT, 10)
        self.itemsForm.Bind(wx.EVT_LEFT_DOWN, lambda event: self.itemsForm.Clear())
        self.itemsForm.Bind(wx.EVT_KEY_UP, lambda event: self.itemsForm.Clear() if event.GetUnicodeKey() == wx.WXK_TAB else None)

        #Time
        timeList = ['hour', 'day', 'week', 'month', 'year', 'all']
        self.timeChoice = wx.Choice(self, -1, (200, -1), choices=timeList)
        self.timeLabel = wx.StaticText(self, -1, "from: ")
        self.gridSizer.Add(self.timeLabel, 0, wx.TOP | wx.BOTTOM | wx.LEFT | wx.ALIGN_RIGHT, 10)
        self.gridSizer.Add(self.timeChoice, 0, wx.TOP | wx.BOTTOM | wx.RIGHT | wx.ALIGN_LEFT, 10)
        self.timeChoice.Hide()
        self.timeLabel.Hide()


        #ADD CHECK BOXES
        self.searchLabel = wx.StaticText(self, -1, "Search: ")

        self.checkSizer = wx.FlexGridSizer(rows=1,cols=3, hgap=10)
        self.titleBox = wx.CheckBox(self, 0, "Title", (50,-1))
        self.titleBox.SetValue(True)
        self.textBox = wx.CheckBox(self, 0, "Text", (50,-1))
        self.commentsBox= wx.CheckBox(self, 0, "Comments", (100,-1))


        self.checkSizer.AddMany([ (self.titleBox),
                                  (self.textBox),
                                  (self.commentsBox)])

        self.gridSizer.Add(self.searchLabel, 0, wx.LEFT | wx.TOP | wx.BOTTOM | wx.ALIGN_LEFT, 10)
        self.gridSizer.Add(self.checkSizer, 0, wx.RIGHT | wx.TOP | wx.BOTTOM | wx.ALIGN_LEFT, 10)


        #ADD GRIDSIZER TO ENTIRE SIZER
        self.sizer.Add(self.gridSizer, 0, wx.ALIGN_CENTER)

        #ADD SEARCH BUTTON
        self.submitButton = wx.Button(self, 10, "Search")
        self.Bind(wx.EVT_BUTTON, self.OnSubmit, self.submitButton)
        self.sizer.Add(self.submitButton, 0, wx.ALIGN_CENTER | wx.TOP | wx.LEFT | wx.BOTTOM, 10)

        self.SetSizer(self.sizer)

    def onReddit(self, event):
        self.gridSizer.Hide(self.gmailLabel)
        self.gridSizer.Remove(self.gmailLabel)
        self.gridSizer.Hide(self.gmailForm)
        self.gridSizer.Remove(self.gmailForm)

        self.gridSizer.Show(self.usernameForm)
        self.gridSizer.Show(self.usernameLabel)
        self.gridSizer.Show(self.passwordForm)
        self.gridSizer.Show(self.passwordLabel)
        self.sizer.Layout()

    def ongmail(self, event):
        self.gridSizer.Hide(self.usernameLabel)
        self.gridSizer.Remove(self.usernameLabel)
        self.gridSizer.Hide(self.usernameForm)
        self.gridSizer.Remove(self.usernameForm)

        self.gridSizer.Show(self.passwordForm)
        self.gridSizer.Show(self.passwordLabel)

        self.gmailForm.Show()
        self.gmailLabel.Show()
        self.sizer.Layout()

    def onDisplay(self, event):
        self.gridSizer.Hide(self.gmailLabel)
        self.gridSizer.Remove(self.gmailLabel)
        self.gridSizer.Hide(self.gmailForm)
        self.gridSizer.Remove(self.gmailForm)

        self.gridSizer.Hide(self.usernameLabel)
        self.gridSizer.Remove(self.usernameLabel)
        self.gridSizer.Hide(self.usernameForm)
        self.gridSizer.Remove(self.usernameForm)

        self.gridSizer.Hide(self.passwordLabel)
        self.gridSizer.Remove(self.passwordLabel)
        self.gridSizer.Hide(self.passwordForm)
        self.gridSizer.Remove(self.passwordForm)

        self.sizer.Layout()

    def onChoice(self, event):
        choice = self.getChoice.GetStringSelection()

        showList = ['controversial', 'top']

        if choice in showList:
            self.gridSizer.Show(self.timeChoice)
            self.gridSizer.Show(self.timeLabel)
            self.sizer.Layout()
        else:
            self.gridSizer.Hide(self.timeChoice)
            self.gridSizer.Hide(self.timeLabel)
            self.sizer.Layout()

    def OnSubmit(self, event):
        subredditText = self.subredditForm.GetValue()
        choice = self.getChoice.GetStringSelection()
        choiceIndex = self.getChoice.GetSelection()
        keyWordsText = self.keyWordsForm.GetValue()
        itemsText = self.itemsForm.GetValue()

        #import python reddit api wrapper
        import praw

        #get reddit object with user_agent
        r = praw.Reddit(user_agent='Subreddit Scanner by /u/appogiatura')

        #CHECK IF PROPER USERNAME/PASSWORD COMBINATION
        password = self.passwordForm.GetValue()
        if self.redditButton.GetValue():
            username = self.usernameForm.GetValue()
            try:
                r.login(username, password)
            except praw.errors.InvalidUserPass:
                wx.GetApp().Destroy()
                if __name__ == '__main__':
                    app = wx.App(False)
                    frame = MainFrame("Invalid username or password! Try again", "redditButton")
                    frame.MainPanel.usernameForm.Show()
                    frame.MainPanel.usernameLabel.Show()
                    frame.MainPanel.passwordForm.Show()
                    frame.MainPanel.passwordLabel.Show()
                    frame.MainPanel.subredditForm.SetValue(subredditText)
                    frame.MainPanel.keyWordsForm.SetValue(keyWordsText)
                    frame.MainPanel.itemsForm.SetValue(keyWordsText)
                    frame.MainPanel.getChoice.SetSelection(choiceIndex)
                    frame.MainPanel.gridSizer.Layout()
                    frame.MainPanel.sizer.Layout()
                    frame.Show(True)
                    app.MainLoop()

        elif self.gmailButton.GetValue():
            import smtplib
            username = self.gmailForm.GetValue()
            try:
                server = smtplib.SMTP("smtp.gmail.com", 587)
                server.ehlo()
                server.starttls()
                server.login(username, password)
            except smtplib.SMTPAuthenticationError:
                wx.GetApp().Destroy()
                if __name__ == '__main__':
                    app = wx.App(False)

                    #RESET TO PREVIOUS CORRECT VALUES
                    frame = MainFrame("Invalid gmail or password! Try again", "gmailButton")
                    frame.MainPanel.usernameForm.Show()
                    frame.MainPanel.usernameLabel.Show()
                    frame.MainPanel.passwordForm.Show()
                    frame.MainPanel.passwordLabel.Show()
                    frame.MainPanel.gridSizer.Hide(frame.MainPanel.usernameForm)
                    frame.MainPanel.gridSizer.Hide(frame.MainPanel.usernameLabel)
                    frame.MainPanel.gridSizer.Show(frame.MainPanel.gmailForm)
                    frame.MainPanel.gridSizer.Show(frame.MainPanel.gmailLabel)
                    frame.MainPanel.subredditForm.SetValue(subredditText)
                    frame.MainPanel.keyWordsForm.SetValue(keyWordsText)
                    frame.MainPanel.itemsForm.SetValue(itemsText)
                    frame.MainPanel.getChoice.SetSelection(choiceIndex)
                    frame.MainPanel.gridSizer.Layout()
                    frame.MainPanel.sizer.Layout()
                    frame.Show(True)
                    app.MainLoop()

        #CHECK IF SUBREDDIT EXISTS
        try:
            subreddit = r.get_subreddit(subredditText, fetch=True)
        except praw.errors.InvalidSubreddit:
            if self.redditButton.GetValue():
                username = self.usernameForm.GetValue()
                rightButton = "redditButton"
            elif self.gmailButton.GetValue():
                username = self.gmailForm.GetValue()
                rightButton = "gmailButton"
            else:
                rightButton = "displayButton"

            wx.GetApp().Destroy()
            if __name__ == '__main__':
                app = wx.App(False)
                frame = MainFrame("Invalid Subreddit! Try again", rightButton)
                if rightButton == "gmailButton" or rightButton == "redditButton":
                    frame.MainPanel.usernameForm.Show()
                    frame.MainPanel.usernameLabel.Show()
                    frame.MainPanel.passwordForm.Show()
                    frame.MainPanel.passwordLabel.Show()
                    frame.MainPanel.usernameForm.SetValue(username)
                frame.MainPanel.keyWordsForm.SetValue(keyWordsText)
                frame.MainPanel.itemsForm.SetValue(itemsText)
                frame.MainPanel.getChoice.SetSelection(choiceIndex)
                frame.MainPanel.gridSizer.Layout()
                frame.MainPanel.sizer.Layout()
                frame.Show(True)
                app.MainLoop()

        #CHECK IF PROPER ITEMS ENTERED
        try:
            itemsNumber = int(itemsText)
        except ValueError:
            if self.redditButton.GetValue():
                username = self.usernameForm.GetValue()
                rightButton = "redditButton"
            elif self.gmailButton.GetValue():
                username = self.gmailForm.GetValue()
                rightButton = "gmailButton"
            else:
                rightButton = "displayButton"

            wx.GetApp().Destroy()
            if __name__ == '__main__':
                app = wx.App(False)
                frame = MainFrame("Invalid items number! Try again", rightButton)
                if rightButton == "gmailButton" or rightButton == "redditButton":
                    frame.MainPanel.usernameForm.Show()
                    frame.MainPanel.usernameLabel.Show()
                    frame.MainPanel.passwordForm.Show()
                    frame.MainPanel.passwordLabel.Show()
                    frame.MainPanel.usernameForm.SetValue(username)
                frame.MainPanel.keyWordsForm.SetValue(keyWordsText)
                frame.MainPanel.subredditForm.SetValue(subredditText)
                frame.MainPanel.getChoice.SetSelection(choiceIndex)
                frame.MainPanel.gridSizer.Layout()
                frame.MainPanel.sizer.Layout()
                frame.Show(True)
                app.MainLoop()
                frame.Show(True)
                app.MainLoop()

        if itemsNumber > 100:
            if self.redditButton.GetValue():
                username = self.usernameForm.GetValue()
                rightButton = "redditButton"
            elif self.gmailButton.GetValue():
                username = self.gmailForm.GetValue()
                rightButton = "gmailButton"
            else:
                rightButton = "displayButton"
            wx.GetApp().Destroy()
            if __name__ == '__main__':
                app = wx.App(False)
                frame = MainFrame("Invalid items number! Try again", rightButton)
                if rightButton == "gmailButton" or rightButton == "redditButton":
                    frame.MainPanel.usernameForm.Show()
                    frame.MainPanel.usernameLabel.Show()
                    frame.MainPanel.passwordForm.Show()
                    frame.MainPanel.passwordLabel.Show()
                    frame.MainPanel.usernameForm.SetValue(username)
                frame.MainPanel.keyWordsForm.SetValue(keyWordsText)
                frame.MainPanel.subredditForm.SetValue(subredditText)
                frame.MainPanel.getChoice.SetSelection(choiceIndex)
                frame.MainPanel.gridSizer.Layout()
                frame.MainPanel.sizer.Layout()
                frame.Show(True)
                app.MainLoop()
                frame.Show(True)
                app.MainLoop()

        #CHECK IF MORE THAN 20 POST'S COMMENTS ARE BEING CHECKED
        if (itemsNumber>20 and self.commentsBox.IsChecked()):
            wx.GetApp().Destroy()
            if __name__ == '__main__':
                app = wx.App(False)
                frame = MainFrame("You can't search that many post's comments. You don't have time.")
                frame.MainPanel.keyWordsForm.SetValue(keyWordsText)
                frame.MainPanel.subredditForm.SetValue(subredditText)
                frame.MainPanel.getChoice.SetSelection(choiceIndex)
                frame.MainPanel.gridSizer.Layout()
                frame.MainPanel.sizer.Layout()
                frame.Show(True)
                app.MainLoop()
                frame.Show(True)
                app.MainLoop()

        timeChoiceList = ['controversial', 'top']

        choiceMethodString = "get_{0}".format(choice)
        if choice in timeChoiceList:
            choiceMethodString += "_from_{0}".format(self.timeChoice.GetStringSelection())

        #
        import re
        keyWordsList = re.sub("[^\w]", " ", keyWordsText).split()
        for i in keyWordsList:
            i = i.lower()

        #list to put submission short links and titles
        submissionLinkList = []
        submissionTitleList = []

        #Is each box checked
        commentsBoolean = self.commentsBox.IsChecked()
        titleBoolean = self.titleBox.IsChecked()
        textBoolean = self.textBox.IsChecked()

        #Iterate through posts
        for submission in getattr(subreddit, choiceMethodString)(limit=itemsNumber):
            title = submission.title
            submissionTitle = submission.title.lower()
            submissionText = submission.selftext.lower()

            if keyWordsText != "":
                hasTitle = False
                hasText = False

                if titleBoolean:
                    hasTitle = any(string in (submissionTitle or submissionText) for string in keyWordsList)

                if textBoolean:
                    hasText = any(string in (submissionText) for string in keyWordsList)

                if hasTitle or hasText:
                    submissionLinkList.append(submission.short_link)
                    submissionTitleList.append(title)

                if commentsBoolean:
                    comments = praw.helpers.flatten_tree(submission.comments)
                    try:
                        for comment in comments:
                            hasComments = any(string in comment.body for string in keyWordsList)

                            if hasComments:
                                submissionLinkList.append(comment.permalink)
                                submissionTitleList.append(title)
                                break
                    except AttributeError:
                        continue
            else:
                submissionLinkList.append(submission.short_link)
                submissionTitleList.append(submission.title)

        #SEND MESSAGE OR DISPLAY
        if len(submissionLinkList) != 0:
            subject = "{0} Threads in /r/{1} containing '{2}'".format(choice, subredditText, keyWordsList[0].upper())
            subject = subject[:1].upper() + subject[1:]
            #IF REDDIT CHOSEN AS MESSAGE CHOICE
            if self.redditButton.GetValue():
                message = ""
                for i in range(len(submissionLinkList)):
                    message += "{0}. [{1}]({2})\n".format(i+1, submissionTitleList[i], submissionLinkList[i])
                r.user.send_message(subject=subject, message = message)
                self.frame.SetStatusText("Done, check your inbox!")
            #IF GMAIL CHOSEN
            elif self.gmailButton.GetValue():

                FROM = self.gmailForm.GetValue()
                TO = self.gmailForm.GetValue()

                message = """\From: {0}\nTo: {1}\nSubject: {2}\n\n""".format(FROM, TO, subject)

                for i in range(len(submissionLinkList)):
                    message += "{0}. {1} {2}\n\n".format(i+1, submissionTitleList[i], submissionLinkList[i])


                sender = self.gmailForm.GetValue()
                password = self.passwordForm.GetValue()

                server = smtplib.SMTP("smtp.gmail.com", 587)
                server.ehlo()
                server.starttls()
                server.login(sender, password)
                server.sendmail(sender, sender, message)
                server.close()

                self.frame.SetStatusText("Done, check your inbox!")
            #IF DISPLAY CHOSEN
            else:
                threadFrame = ThreadFrame(subject)
                for i in range(len(submissionTitleList)):
                    # submissionTitleText = wx.StaticText(threadFrame, -1, submissionTitleList[i])
                    # threadFrame.ThreadPanel.threadSizer.Add(submissionTitleText)
                    number = wx.StaticText(threadFrame, -1, str(i+1) + ".")
                    hyper = hl.HyperLinkCtrl(threadFrame, -1, submissionTitleList[i], URL= submissionLinkList[i])

                    threadFrame.ThreadPanel.threadSizer.Add(number)
                    threadFrame.ThreadPanel.threadSizer.Add(hyper)
                threadFrame.ThreadPanel.threadSizer.Layout()
                threadFrame.Show()

            self.passwordForm.Clear()
        else:
            wx.GetApp().Destroy()
            if __name__ == '__main__':
                app = wx.App(False)
                frame = MainFrame("Nothing found, try different keywords or different search options!")
                frame.MainPanel.keyWordsForm.SetValue(keyWordsText)
                frame.MainPanel.subredditForm.SetValue(subredditText)
                frame.MainPanel.getChoice.SetSelection(choiceIndex)
                frame.MainPanel.gridSizer.Layout()
                frame.Show(True)
                app.MainLoop()


if __name__ == '__main__':
    app = wx.App(False)
    frame = MainFrame()
    frame.Show(True)
    app.MainLoop()



