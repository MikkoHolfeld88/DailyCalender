from wx.lib.buttons import GenBitmapButton
import wx               # GUI
import wx.grid as gridlib
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

class Home(wx.Panel):
    def __init__(self, parent):
      super().__init__(parent)
      self.SetBackgroundColour(c_hell)
      wx.StaticText(self, 1, "HOMEMMEMEM")

class TraumSeite(wx.Panel):
    def __init__(self, parent):
      super().__init__(parent)
      self.SetBackgroundColour(c_hell)

class FuenfJahresPlanSeite(wx.Panel):
    def __init__(self, parent):
      super().__init__(parent)
      self.SetBackgroundColour(c_hell)
      wx.StaticText(self, 1, "HASODIAHSODIHASOID")

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
        """Constructor"""
        wx.Panel.__init__(self, parent=parent)

        grid = gridlib.Grid(self)
        grid.CreateGrid(25,12)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(grid, 0, wx.EXPAND)
        self.SetSizer(sizer)
        self.SetBackgroundColour(c_hell)

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

        # creating main-structure
        self.mainBox = wx.BoxSizer(wx.VERTICAL)         # MAINWINDOW = Everything
        self.navBox = wx.BoxSizer(wx.VERTICAL)          # Bar on the Right for Navigation
        self.windowBox = wx.BoxSizer(wx.HORIZONTAL)     # Window Left from the Navbar
        self.titleBox = wx.BoxSizer(wx.HORIZONTAL)      # Bar on Top with Date
        self.contentWindow = wx.BoxSizer(wx.VERTICAL)   # Necessarry for switching different panels in WindowBox

        # Initializing different MainPages (Home,Traum,Jahresplan...)
        self.init_contentPages()
        self.organize_contentPages()

        self.border = 5

        # ========================= NavBar ================================
        #Create NavButtons
        self.home_btn = GenBitmapButton(self, -1,wx.Bitmap(wx.Image("icon/home.png", wx.BITMAP_TYPE_PNG)))
        self.dream_btn = GenBitmapButton(self, -1,wx.Bitmap(wx.Image("icon/traum.png", wx.BITMAP_TYPE_PNG)))
        self.fiveyearplay_btn = GenBitmapButton(self, -1,wx.Bitmap(wx.Image("icon/5jahresplan.png", wx.BITMAP_TYPE_PNG)))
        self.yearplan_btn = GenBitmapButton(self, -1,wx.Bitmap(wx.Image("icon/jahresplan.png", wx.BITMAP_TYPE_PNG)))
        self.monthplan_btn = GenBitmapButton(self, -1,wx.Bitmap(wx.Image("icon/monatsplan.png", wx.BITMAP_TYPE_PNG)))
        self.dayplan_btn = GenBitmapButton(self, -1,wx.Bitmap(wx.Image("icon/tagesplan.png", wx.BITMAP_TYPE_PNG)))
        self.habittrrack_btn = GenBitmapButton(self, -1,wx.Bitmap(wx.Image("icon/habittrack.png", wx.BITMAP_TYPE_PNG)))

        #Storing NavButtonData
        navButtonDict = {
            self.home_btn: "home",
            self.dream_btn: "traum",
            self.fiveyearplay_btn: "5jahresplan",
            self.yearplan_btn: "jahresplan",
            self.monthplan_btn: "monatsplan",
            self.dayplan_btn: "tagesplan",
            self.habittrrack_btn: "habittrack",
        }

        #Design NavButtons
        for button in navButtonDict:
            self.set_NavigationButtons(button, str(navButtonDict[button]))
            self.design_NavigationButtons(button)
            self.navBox.Add(button, 1 , wx.ALL , self.border)
        #Bind NavButtons
        self.bind_NavigationButtons()

        self.navBox.AddStretchSpacer(3)

        # ========================= TitleBar ================================
        look = wx.Panel(self)

        self.close_btn = GenBitmapButton(self, -1,wx.Bitmap(wx.Image("icon/close.png", wx.BITMAP_TYPE_PNG)),(-1,-1),(65,-1))
        self.set_NavigationButtons(self.close_btn, str("close"))
        self.design_NavigationButtons(self.close_btn)
        self.close_btn.Bind(wx.EVT_BUTTON, self.OnCloseClicked)

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

        if int(aktuellerTag) > 9:
            self.titleBox.AddSpacer(70)
        else:
            self.titleBox.AddSpacer(50)
        self.titleBox.Add(dayHeader, wx.EXPAND | wx.ALL, wx.ALIGN_CENTER)
        self.titleBox.Add(monthHeader, wx.EXPAND | wx.ALL, wx.ALIGN_CENTER)
        self.titleBox.Add(self.close_btn, wx.ALL, wx.ALIGN_CENTER, 10)

        # ========================= MainWindow ================================

        self.windowBox.Add(self.navBox, -1, wx.EXPAND | wx.ALL)
        self.windowBox.Add(self.contentWindow, 10, wx.EXPAND |wx.ALL)
        self.mainBox.Add(self.titleBox, -1, wx.EXPAND | wx.ALL)
        self.mainBox.Add(self.windowBox, 10, wx.EXPAND | wx.ALL)

        self.SetSizer(self.mainBox)

    # ========================= Methoden ================================
    def set_NavigationButtons(self, button, name):
        # Function for dealing with Basic Button Setups (NavigationButtons)
        button.SetToolTip(name)
        button.SetBitmapSelected(wx.Bitmap(wx.Image("icon/"+name+"_selected.png", wx.BITMAP_TYPE_PNG)))
        button.SetBitmapFocus(wx.Bitmap(wx.Image("icon/"+name+"_focus.png", wx.BITMAP_TYPE_PNG)))

    def design_NavigationButtons(self, button):
        # Function for simplifying ButtonDesign
        button.SetBezelWidth(0)
        button.SetUseFocusIndicator(False)
        button.SetBackgroundColour(c_dunkel)

    def bind_NavigationButtons(self):
        self.home_btn.Bind(wx.EVT_BUTTON, self.OnHomeClicked)
        self.dream_btn.Bind(wx.EVT_BUTTON, self.OnDreamClicked)
        self.fiveyearplay_btn.Bind(wx.EVT_BUTTON, self.On5YearClicked)
        self.yearplan_btn.Bind(wx.EVT_BUTTON, self.OnYearClicked)
        self.monthplan_btn.Bind(wx.EVT_BUTTON, self.OnMonthClicked)
        self.dayplan_btn.Bind(wx.EVT_BUTTON, self.OnDayClicked)
        self.habittrrack_btn.Bind(wx.EVT_BUTTON, self.OnHabittrackClicked)

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

    def init_contentPages(self):
        #creating contentPages
        self.page_home = Home(self)
        self.page_traum = TraumSeite(self)
        self.page_fuenfJahresPlan = FuenfJahresPlanSeite(self)
        self.page_jahresplan = JahresSeite(self)
        self.page_monatsplan = MonatsSeite(self)
        self.page_tagesplan = TagesSeite(self)
        self.page_habittracker = HabitTracker(self)
        # Hiding UnseenPages at Programstart, Showing HomePage First
        self.panelSwitch(self.page_home)

    def organize_contentPages(self):
        pageList = [self.page_home, self.page_traum, self.page_fuenfJahresPlan,
                    self.page_jahresplan, self.page_monatsplan, self.page_tagesplan, self.page_habittracker]
        for page in pageList:
            self.contentWindow.Add(page,1, wx.EXPAND)

    def panelSwitch(self, page):
        pageList = [self.page_home, self.page_traum, self.page_fuenfJahresPlan, self.page_jahresplan, self.page_monatsplan, self.page_tagesplan, self.page_habittracker]
        pageList_shortend = pageList
        pageList_shortend.remove(page)
        page.Show()
        for pages in pageList_shortend:
            pages.Hide()
        self.Layout()

    # Event Handlers for Navigation
    def OnHomeClicked(self, e):
        self.panelSwitch(self.page_home)
        print("Home gedrückt")

    def OnDreamClicked(self, e):
        self.panelSwitch(self.page_traum)
        print("Traum gedrückt")

    def On5YearClicked(self, e):
        self.panelSwitch(self.page_fuenfJahresPlan)
        print("5-Jahresplan gedrückt")

    def OnYearClicked(self, e):
        self.panelSwitch(self.page_jahresplan)
        print("Jahresplan gedrückt")

    def OnMonthClicked(self, e):
        self.panelSwitch(self.page_monatsplan)
        self.Layout()
        print("Monatsplan gedrückt")

    def OnDayClicked(self, e):
        self.panelSwitch(self.page_tagesplan)
        print("Tagesplan gedrückt")

    def OnHabittrackClicked(self, e):
        self.panelSwitch(self.page_habittracker)
        print("Habittrack gedrückt")

    def OnCloseClicked(self, e):
        self.Destroy()

    # ========================= MainPages ================================



def main():
    app = wx.App()
    ex = Calender(None, title='calender')
    ex.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()
