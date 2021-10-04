'''#!/usr/bin/env python
import wx

class helfrm(wx.Frame):
    #A frame to say hello world
    def __init__(self, *args, **kw):
        # ensure the parent's __init__ is called
        super(helfrm, self).__init__(*args, **kw)

        penl = wx.Panel(self)

        #for a much bold effect
        sk = wx.StaticText(penl, label = 'Helo Wrld!')
        fnt = sk.GetFont()
        fnt.PointSized +=10
        fnt = fnt.Bold()
        sk.SetFont(fnt)

        # and create a sizer to manage the layout of child widgets
        szer = wx.BoxSizer(wx.VERTICAL)
        szer.Add(sk, wx.SizerFlags().Border(wx.Top|wx.Left, 25))
        penl.SetSizer(szer)

        #Make a menu Bar

        self.makeMenuBar()

        #Adding a status bar

        self.CreateStatusBar()
        self.SetStatusText("Aa gaye aap bhi!!")

    def makemnubar(self):
        """
        A menu bar is composed of menus, which are composed of menu items.
        This method builds a set of menus and binds handlers to be called
        when the menu item is selected.
        """

        #make a file with hello and exit items
        filemnu = wx.Menu()

        #the "\t..." key also acts as an accelerator key which also triggers the same event

        heloitm = filemnu.Append(-1, "&Hello...\tCtrl-H", "help string shown in the status bar for this menu")
        filemnu.AppendSeparator()

        #When using a stock ID we don't need to specify the menu item's label

        extitm = filemnu.Append(wx.ID_EXIT)

        #Helpful menu for the exit

        hlpmnu = wx.Menu()
        abtitm = hlpmnu.Append(wx.ID_ABOUT)

        # Make the menu bar and add the two menus to it. The '&' defines
        # that the next letter is the "mnemonic" for the menu item. On the
        # platforms that support it those letters are underlined and can be
        # triggered from the keyboard.

        mnubr = wx.MenuBar()
        mnubr.Append(filemnu,"&File")
        mnubr.Append(hlpmnu,"&Help")

        #give the menu bar to the frame

        self.SetMenuBar(mnubr)
        
        # Finally, associate a handler function with the EVT_MENU event for
        # each of the menu items. That means that when that menu item is
        # activated then the associated handler function will be called.
        self.Bind(wx.EVT_MENU, self.OnHello, heloitm)
        self.Bind(wx.EVT_MENU, self.OnExit, extitm)
        self.Bind(wx.EVT_MENU, self.OnAbout, abtitm)

        #defining onhello onexit onabout

    def OnHello(self,event):
        wx.MessageBox("Hello! Aap yahan.. Kaise???")
    
    def OnExit(self,event):
        self.Close = True
    
    def OnAbout(self,event):
        wx.MessageBox("Hello! Main aisa hi ek pirogiram hun!!","Don't Mind me Plz!", wx.OK|wx.ICON_INFORMATION)

if __name__ == '__main__':
    # When this module is run (not imported) then create the app, the
    # frame, show it, and start the event loop.

    # Next, create an application object.
    ap = wx.App()
    
    # Then a frame.
    frm = wx.Frame(None, title="Hello World 2")
    
    # Show it.
    frm.Show()
    # Start the event loop.
    ap.MainLoop()
'''

#!/usr/bin/env python
"""
Hello World, but with more meat.
"""

import wx

class HelloFrame(wx.Frame):
    """
    A Frame that says Hello World
    """

    def __init__(self, *args, **kw):
        # ensure the parent's __init__ is called
        super(HelloFrame, self).__init__(*args, **kw)

        # create a panel in the frame
        pnl = wx.Panel(self)

        # put some text with a larger bold font on it
        st = wx.StaticText(pnl, label="Hello World!")
        font = st.GetFont()
        font.PointSize += 10
        font = font.Bold()
        st.SetFont(font)

        # and create a sizer to manage the layout of child widgets
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(st, wx.SizerFlags().Border(wx.TOP|wx.LEFT, 25))
        pnl.SetSizer(sizer)

        # create a menu bar
        self.makeMenuBar()

        # and a status bar
        self.CreateStatusBar()
        self.SetStatusText("Welcome to wxPython!")


    def makeMenuBar(self):
        """
        A menu bar is composed of menus, which are composed of menu items.
        This method builds a set of menus and binds handlers to be called
        when the menu item is selected.
        """

        # Make a file menu with Hello and Exit items
        fileMenu = wx.Menu()
        # The "\t..." syntax defines an accelerator key that also triggers
        # the same event
        helloItem = fileMenu.Append(-1, "&Hello...\tCtrl-H",
                "Help string shown in status bar for this menu item")
        fileMenu.AppendSeparator()
        # When using a stock ID we don't need to specify the menu item's
        # label
        exitItem = fileMenu.Append(wx.ID_EXIT)

        # Now a help menu for the about item
        helpMenu = wx.Menu()
        aboutItem = helpMenu.Append(wx.ID_ABOUT)

        # Make the menu bar and add the two menus to it. The '&' defines
        # that the next letter is the "mnemonic" for the menu item. On the
        # platforms that support it those letters are underlined and can be
        # triggered from the keyboard.
        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu, "&File")
        menuBar.Append(helpMenu, "&Help")

        # Give the menu bar to the frame
        self.SetMenuBar(menuBar)

        # Finally, associate a handler function with the EVT_MENU event for
        # each of the menu items. That means that when that menu item is
        # activated then the associated handler function will be called.
        self.Bind(wx.EVT_MENU, self.OnHello, helloItem)
        self.Bind(wx.EVT_MENU, self.OnExit,  exitItem)
        self.Bind(wx.EVT_MENU, self.OnAbout, aboutItem)


    def OnExit(self, event):
        """Close the frame, terminating the application."""
        self.Close(True)


    def OnHello(self, event):
        """Say hello to the user."""
        wx.MessageBox("Hello again from wxPython")


    def OnAbout(self, event):
        """Display an About Dialog"""
        wx.MessageBox("This is a wxPython Hello World sample",
                      "About Hello World 2",
                      wx.OK|wx.ICON_INFORMATION)


if __name__ == '__main__':
    # When this module is run (not imported) then create the app, the
    # frame, show it, and start the event loop.
    app = wx.App()
    frm = HelloFrame(None, title='Hello World 2')
    frm.Show()
    app.MainLoop()