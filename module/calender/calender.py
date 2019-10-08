from wx.lib.buttons import GenBitmapButton
import wx               # GUI
import datetime
import calendar
import planning_structures
from wx.lib.agw.flatnotebook import FlatNotebook as nb


# INITIALIZING GLOBAL VARIABLES
# gets current time via now.year / now.month / now.day / now.houer / now.minute / now.second
now = datetime.datetime.now()
aktuellesJahr = str(now.year)
aktuellerMonat = str(now.month)
aktuellerTag = str(now.day)

# Standard Fontstyles
schriftart = "Helvetica"
fontfamily = wx.MODERN
fontstyle = wx.FONTSTYLE_NORMAL
fontweight = wx.FONTWEIGHT_LIGHT

# Standard Color Scheme
c_hell = (229,204,255)
c_mittel = (76,0,153)
c_dunkel = (32,32,32)

# GUI external Data handling Classes

class Calender(wx.Frame):

    def __init__(self, parent, title):
        no_caption = wx.MINIMIZE_BOX | wx.MAXIMIZE_BOX | wx.RESIZE_BORDER | wx.SYSTEM_MENU | wx.CLOSE_BOX | wx.CLIP_CHILDREN
        # super().__init__(parent, title=title, style=no_caption)
        super().__init__(parent, title=title)

        self.InitUI()
        self.SetSize(1080,620)
        self.SetBackgroundColour(c_dunkel)
        self.Centre()
        self.Home(self)

    # ========================= Anordnung der Elemente der GUI ================================
    def InitUI(self):

        # Initializing different MainPages
        self.page_home = Home(self)
        self.page_traum = TraumSeite(self)
        self.page_fuenfJahresPlan = FuenfJahresPlanSeite(self)
        self.page_jahresplan = JahresSeite(self)
        self.page_monatsplan = MonatsSeite(self)
        self.page_tagesplan = TagesSeite(self)
        self.page_habittracker = HabitTracker(self)

        self.border = 5

        # creating main-structure
        self.mainBox = wx.BoxSizer(wx.HORIZONTAL)
        self.navBox = wx.BoxSizer(wx.VERTICAL)
        self.windowBox = wx.BoxSizer(wx.VERTICAL)
        self.titleBox = wx.BoxSizer(wx.HORIZONTAL)

        # ========================= NavBar ================================

        home_btn = GenBitmapButton(self, -1,wx.Bitmap(wx.Image("icon/home.png", wx.BITMAP_TYPE_PNG)))
        dream_btn = GenBitmapButton(self, -1,wx.Bitmap(wx.Image("icon/traum.png", wx.BITMAP_TYPE_PNG)))
        fiveyearplay_btn = GenBitmapButton(self, -1,wx.Bitmap(wx.Image("icon/5jahresplan.png", wx.BITMAP_TYPE_PNG)))
        yearplan_btn = GenBitmapButton(self, -1,wx.Bitmap(wx.Image("icon/jahresplan.png", wx.BITMAP_TYPE_PNG)))
        monthplan_btn = GenBitmapButton(self, -1,wx.Bitmap(wx.Image("icon/monatsplan.png", wx.BITMAP_TYPE_PNG)))
        dayplan_btn = GenBitmapButton(self, -1,wx.Bitmap(wx.Image("icon/tagesplan.png", wx.BITMAP_TYPE_PNG)))
        habittrrack_btn = GenBitmapButton(self, -1,wx.Bitmap(wx.Image("icon/habittrack.png", wx.BITMAP_TYPE_PNG)))

        navButtonList = [home_btn, dream_btn, fiveyearplay_btn, yearplan_btn, monthplan_btn, dayplan_btn, habittrrack_btn]
        for button in navButtonList:
            self.init_designNavigation(button)

        home_btn.Bind(wx.EVT_BUTTON, self.OnHomeClicked)
        dream_btn.Bind(wx.EVT_BUTTON, self.OnDreamClicked)
        fiveyearplay_btn.Bind(wx.EVT_BUTTON, self.On5YearClicked)
        yearplan_btn.Bind(wx.EVT_BUTTON, self.OnYearClicked)
        monthplan_btn.Bind(wx.EVT_BUTTON, self.OnMonthClicked)
        dayplan_btn.Bind(wx.EVT_BUTTON, self.OnDayClicked)
        habittrrack_btn.Bind(wx.EVT_BUTTON, self.OnHabittrackClicked)

        # Fügt die Navigationsbuttons dem Sizer hinzu
        for buttons in navButtonList:
            self.navBox.Add(buttons, 1 , wx.EXPAND | wx.ALL , self.border)

        self.navBox.AddStretchSpacer(3)

        # ========================= TitleBar ================================
        self.titleBox.Add(wx.StaticText(self, label="TEST"))

        # ========================= MainWindow ================================
        self.windowBox.Add(self.titleBox, 1, wx.EXPAND | wx.ALL)
        self.windowBox.Add(self.Home(self), 6, wx.EXPAND |wx.ALL)

        self.mainBox.Add(self.navBox, 1, wx.EXPAND | wx.ALL)
        self.mainBox.Add(self.windowBox, 10, wx.EXPAND | wx.ALL)

        self.SetSizer(self.mainBox)

    # ========================= Methoden ================================
    def init_designNavigation(self, button):
        # Function for simplifying ButtonDesign
        button.SetBezelWidth(0)
        button.SetUseFocusIndicator(False)
        button.SetBackgroundColour(c_dunkel)

    def OnHomeClicked(self, e):
        self.windowBox.Remove(1)
        self.windowBox.Add(self.Home(self), 6, wx.EXPAND |wx.ALL)
        self.windowBox.Layout()
        print("Home gedrückt")

    def OnDreamClicked(self, e):
        self.windowBox.Remove(1)
        self.windowBox.Add(self.TraumSeite(self), 6, wx.EXPAND |wx.ALL)
        self.windowBox.Layout()
        print("Traum gedrückt")

    def On5YearClicked(self, e):
        print("5-Jahresplan gedrückt")

    def OnYearClicked(self, e):
        print("Jahresplan gedrückt")

    def OnMonthClicked(self, e):
        print("Monatsplan gedrückt")

    def OnDayClicked(self, e):
        print("Tagesplan gedrückt")

    def OnHabittrackClicked(self, e):
        print("Habittrack gedrückt")

        # Tips zur Anordnung in BoxSizers
          # topsizer.Add(
          #       wx.TextCtrl(self, -1, "My text.", wx.DefaultPosition, wx.Size(100,60), wx.TE_MULTILINE),
          #       1,           # make vertically stretchable
          #       wx.EXPAND |  # make horizontally stretchable
          #       wx.ALL,      # and make border all around
          #       10)          # set border width to 10

        # Tip zu StaticText
            # parent (wx.Window) – Parent window. Should not be None.
            # id (wx.WindowID) – Control identifier. A value of -1 denotes a default value.
            # label (string) – Text label.
            # pos (wx.Point) – Window position.
            # size (wx.Size) – Window size.
            # style (long) – Window style. See wx.StaticText.
            # name (string) – Window name.

    class Home(wx.Panel):
        def __init__(self, parent):
          super().__init__(parent)
          self.SetBackgroundColour(c_hell)

    class TraumSeite(wx.Panel):
        def __init__(self, parent):
          super().__init__(parent)
          self.SetBackgroundColour(c_hell)

    class FuenfJahresPlanSeite(wx.Panel):
        def __init__(self, parent):
          super().__init__(parent)

    class JahresSeite(wx.Panel):
        def __init__(self, parent):
          super().__init__(parent)

    class MonatsSeite(wx.Panel):
        def __init__(self, parent):
          super().__init__(parent)

    class TagesSeite(wx.Panel):
        def __init__(self, parent):
          super().__init__(parent)

    class HabitTracker(wx.Panel):
        def __init__(self, parent):
          super().__init__(parent)

def main():
    app = wx.App()
    ex = Calender(None, title='calender')
    ex.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()
