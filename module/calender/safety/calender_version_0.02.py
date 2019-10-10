from wx.lib.buttons import GenBitmapButton
import wx               # GUI
import datetime
import calendar
import planning_structures
from wx.adv import CalendarCtrl, GenericCalendarCtrl, CalendarDateAttr

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
c_hover_text = (241,196,15)

class Calender(wx.Frame):

    def __init__(self, parent, title):
        no_caption = wx.MINIMIZE_BOX | wx.MAXIMIZE_BOX | wx.SYSTEM_MENU | wx.CLOSE_BOX | wx.CLIP_CHILDREN
        # super().__init__(parent, title=title, style=no_caption)
        super().__init__(parent, title=title)

        self.InitUI()
        self.SetSize(1080,620)
        self.SetBackgroundColour(c_dunkel)
        self.Centre()

    # ========================= Anordnung der Elemente der GUI ================================
    def InitUI(self):

        # Initializing different MainPages
        self.page_home = self.Home(self)
        self.page_traum = self.TraumSeite(self)
        self.page_fuenfJahresPlan = self.FuenfJahresPlanSeite(self)
        self.page_jahresplan = self.JahresSeite(self)
        self.page_monatsplan = self.MonatsSeite(self)
        self.page_tagesplan = self.TagesSeite(self)
        self.page_habittracker = self.HabitTracker(self)

        self.border = 5

        # creating main-structure
        self.mainBox = wx.BoxSizer(wx.VERTICAL)
        self.navBox = wx.BoxSizer(wx.VERTICAL)
        self.windowBox = wx.BoxSizer(wx.HORIZONTAL)
        self.titleBox = wx.BoxSizer(wx.HORIZONTAL)

        # ========================= NavBar ================================



    #def setNavigationButtons(self, button, name):


        self.home_btn = GenBitmapButton(self, -1,wx.Bitmap(wx.Image("icon/home.png", wx.BITMAP_TYPE_PNG)))
        self.dream_btn = GenBitmapButton(self, -1,wx.Bitmap(wx.Image("icon/traum.png", wx.BITMAP_TYPE_PNG)))
        self.fiveyearplay_btn = GenBitmapButton(self, -1,wx.Bitmap(wx.Image("icon/5jahresplan.png", wx.BITMAP_TYPE_PNG)))
        self.yearplan_btn = GenBitmapButton(self, -1,wx.Bitmap(wx.Image("icon/jahresplan.png", wx.BITMAP_TYPE_PNG)))
        self.monthplan_btn = GenBitmapButton(self, -1,wx.Bitmap(wx.Image("icon/monatsplan.png", wx.BITMAP_TYPE_PNG)))
        self.dayplan_btn = GenBitmapButton(self, -1,wx.Bitmap(wx.Image("icon/tagesplan.png", wx.BITMAP_TYPE_PNG)))
        self.habittrrack_btn = GenBitmapButton(self, -1,wx.Bitmap(wx.Image("icon/habittrack.png", wx.BITMAP_TYPE_PNG)))

        self.home_btn.SetToolTip("Home")
        self.dream_btn.SetToolTip("Traum")
        self.fiveyearplay_btn.SetToolTip("5-Jahresplan")
        self.yearplan_btn.SetToolTip("Jahresplan")
        self.monthplan_btn.SetToolTip("Monatsüberblick")
        self.dayplan_btn.SetToolTip("Tagesübersicht")
        self.habittrrack_btn.SetToolTip("Habittracker")

        self.home_btn.SetBitmapSelected(wx.Bitmap(wx.Image("icon/home_selected.png", wx.BITMAP_TYPE_PNG)))
        self.dream_btn.SetBitmapSelected(wx.Bitmap(wx.Image("icon/traum_selected.png", wx.BITMAP_TYPE_PNG)))
        self.fiveyearplay_btn.SetBitmapSelected(wx.Bitmap(wx.Image("icon/5jahresplan_selected.png", wx.BITMAP_TYPE_PNG)))
        self.yearplan_btn.SetBitmapSelected(wx.Bitmap(wx.Image("icon/jahresplan_selected.png", wx.BITMAP_TYPE_PNG)))
        self.monthplan_btn.SetBitmapSelected(wx.Bitmap(wx.Image("icon/monatsplan_selected.png", wx.BITMAP_TYPE_PNG)))
        self.dayplan_btn.SetBitmapSelected(wx.Bitmap(wx.Image("icon/tagesplan_selected.png", wx.BITMAP_TYPE_PNG)))
        self.habittrrack_btn.SetBitmapSelected(wx.Bitmap(wx.Image("icon/habittrack_selected.png", wx.BITMAP_TYPE_PNG)))

        self.home_btn.SetBitmapFocus(wx.Bitmap(wx.Image("icon/home_focus.png", wx.BITMAP_TYPE_PNG)))
        self.dream_btn.SetBitmapFocus(wx.Bitmap(wx.Image("icon/traum_focus.png", wx.BITMAP_TYPE_PNG)))
        self.fiveyearplay_btn.SetBitmapFocus(wx.Bitmap(wx.Image("icon/5jahresplan_focus.png", wx.BITMAP_TYPE_PNG)))
        self.yearplan_btn.SetBitmapFocus(wx.Bitmap(wx.Image("icon/jahresplan_focus.png", wx.BITMAP_TYPE_PNG)))
        self.monthplan_btn.SetBitmapFocus(wx.Bitmap(wx.Image("icon/monatsplan_focus.png", wx.BITMAP_TYPE_PNG)))
        self.dayplan_btn.SetBitmapFocus(wx.Bitmap(wx.Image("icon/tagesplan_focus.png", wx.BITMAP_TYPE_PNG)))
        self.habittrrack_btn.SetBitmapFocus(wx.Bitmap(wx.Image("icon/habittrack_focus.png", wx.BITMAP_TYPE_PNG)))

        navButtonList = [self.home_btn, self.dream_btn, self.fiveyearplay_btn, self.yearplan_btn, self.monthplan_btn, self.dayplan_btn, self.habittrrack_btn]
        for button in navButtonList:
            self.init_designNavigation(button)

        self.home_btn.Bind(wx.EVT_BUTTON, self.OnHomeClicked)
        self.dream_btn.Bind(wx.EVT_BUTTON, self.OnDreamClicked)
        self.fiveyearplay_btn.Bind(wx.EVT_BUTTON, self.On5YearClicked)
        self.yearplan_btn.Bind(wx.EVT_BUTTON, self.OnYearClicked)
        self.monthplan_btn.Bind(wx.EVT_BUTTON, self.OnMonthClicked)
        self.dayplan_btn.Bind(wx.EVT_BUTTON, self.OnDayClicked)
        self.habittrrack_btn.Bind(wx.EVT_BUTTON, self.OnHabittrackClicked)

        # Fügt die Navigationsbuttons dem Sizer hinzu
        for buttons in navButtonList:
            self.navBox.Add(buttons, 1 , wx.ALL , self.border)

        self.navBox.AddStretchSpacer(3)

        # ========================= TitleBar ================================
        look = wx.Panel(self)

        font_dayHeader = wx.Font(28, fontfamily, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, schriftart)
        if int(aktuellerTag) < 10:
            titleBox_day = "  " + "0" + aktuellerTag + " " + self.getWeekday()
        else:
            titleBox_day = aktuellerTag + " " + self.getWeekday()
        dayHeader = wx.StaticText(self, 1, titleBox_day)
        dayHeader.SetFont(font_dayHeader)
        dayHeader.SetForegroundColour(wx.Colour(c_hell))

        font_monthHeader = wx.Font(12, wx.FONTFAMILY_SWISS, wx.NORMAL, wx.FONTWEIGHT_LIGHT, False, "Verdana")
        monthHeader = wx.StaticText(self, 1, self.getMonth())
        monthHeader.SetFont(font_monthHeader)
        monthHeader.SetForegroundColour(wx.Colour(c_hell))

        self.close_btn = GenBitmapButton(self, -1,wx.Bitmap(wx.Image("icon/close.png", wx.BITMAP_TYPE_PNG)),(-1,-1),(65,-1))
        self.close_btn.SetToolTip("Beenden")
        self.close_btn.Bind(wx.EVT_BUTTON, self.OnCloseClicked)
        self.init_designNavigation(self.close_btn)
        self.close_btn.SetBitmapSelected(wx.Bitmap(wx.Image("icon/close_selected.png", wx.BITMAP_TYPE_PNG)))
        self.close_btn.SetBitmapFocus(wx.Bitmap(wx.Image("icon/close_focus.png", wx.BITMAP_TYPE_PNG)))

        self.titleBox.AddSpacer(50)
        self.titleBox.Add(dayHeader, wx.EXPAND | wx.ALL, wx.ALIGN_CENTER)
        self.titleBox.Add(monthHeader, wx.EXPAND | wx.ALL, wx.ALIGN_CENTER)
        self.titleBox.Add(self.close_btn, wx.ALL, wx.ALIGN_CENTER, 10)

        # ========================= MainWindow ================================
        self.windowBox.Add(self.navBox, -1, wx.EXPAND | wx.ALL)
        self.windowBox.Add(self.page_home, 10, wx.EXPAND |wx.ALL)
        self.mainBox.Add(self.titleBox, -1, wx.EXPAND | wx.ALL)
        self.mainBox.Add(self.windowBox, 10, wx.EXPAND | wx.ALL)

        self.SetSizer(self.mainBox)

    # ========================= Methoden ================================
    def init_designNavigation(self, button):
        # Function for simplifying ButtonDesign
        button.SetBezelWidth(0)
        button.SetUseFocusIndicator(False)
        button.SetBackgroundColour(c_dunkel)

    def getWeekday(self):
        switcher = { 0: "MO", 1: "DI", 2: "MI", 3: "DO",  4: "FR", 5: "SA",  6: "SO"}
        return switcher.get(datetime.datetime.today().weekday(), "Ungültiger Tag")

    def getMonth(self):
        switcher = {
            1: "Januar",
            2: "Februar",
            3: "März",
            4: "April",
            5: "Mai",
            6: "Juni",
            7: "Juli",
            8: "August",
            9: "September",
            10: "Oktober",
            11: "November",
            12: "Dezember"
        }
        return switcher.get(int(aktuellerMonat), "Ungültiger Monat")

    # Event Handler for Navigation
    def OnHomeClicked(self, e):

        print("Home gedrückt")

    def OnDreamClicked(self, e):

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

    def OnCloseClicked(self, e):
        self.Destroy()

    # Main Pages
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
          self.SetBackgroundColour(c_hell)

    class JahresSeite(wx.Panel):
        def __init__(self, parent):
          super().__init__(parent)
          self.SetBackgroundColour(c_hell)

    class MonatsSeite(wx.Panel):
        def __init__(self, parent):
          super().__init__(parent)
          self.SetBackgroundColour(c_hell)

    class TagesSeite(wx.Panel):
        def __init__(self, parent):
          super().__init__(parent)
          self.SetBackgroundColour(c_hell)

    class HabitTracker(wx.Panel):
        def __init__(self, parent):
          super().__init__(parent)
          self.SetBackgroundColour(c_hell)

def main():
    app = wx.App()
    ex = Calender(None, title='calender')
    ex.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()
