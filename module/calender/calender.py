import wx               # GUI
import datetime
import calendar
from wx.lib.agw.flatnotebook import FlatNotebook as nb

# gets current time via now.year / now.month / now.day / now.houer / now.minute / now.second

now = datetime.datetime.now()
aktuellesJahr = str(now.year)
aktuellerMonat = str(now.month)
aktuellerTag = str(now.day)

schriftart = "Helvetica"
fontfamily = wx.MODERN
fontstyle = wx.FONTSTYLE_NORMAL
fontweight = wx.FONTWEIGHT_LIGHT

color_hell = (229,204,255)
color_mittel = (76,0,153)
color_dunkel = (32,32,32)

class Calender(wx.Frame):

    def __init__(self, parent, title):
        # no_caption = wx.MINIMIZE_BOX | wx.MAXIMIZE_BOX | wx.RESIZE_BORDER | wx.SYSTEM_MENU | wx.CLOSE_BOX | wx.CLIP_CHILDREN
        # super(Example, self).__init__(parent, title=title, style=no_caption)
        super().__init__(parent, title=title)

        self.InitUI()
        self.SetSize(1080,620)
        # self.SetBackgroundColour(color_dunkel)
        self.Centre()

    def InitUI(self):

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        vbox = wx.BoxSizer(wx.VERTICAL)

        notebook = nb(self)
        notebook.AddPage(JahresSeite(notebook),"Jahr")
        notebook.AddPage(MonatsSeite(notebook),"Monat")
        notebook.AddPage(TagesSeite(notebook),"Tag")


        vbox.Add(wx.Button(self,label="1"))
        vbox.Add(wx.Button(self,label="2"))
        vbox.Add(wx.Button(self,label="3"))
        vbox.Add(wx.Button(self,label="4"))
        hbox.Add(vbox, 1, wx.EXPAND)
        hbox.Add(notebook, 10, wx.EXPAND)

        self.SetSizer(hbox)






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




class JahresSeite(wx.Panel):
    def __init__(self, parent):
      super().__init__(parent)

      self.border = 5

      hbox_1 = wx.BoxSizer(wx.HORIZONTAL)

      h1 = wx.Font(20, fontfamily, fontstyle, wx.FONTWEIGHT_BOLD, False, schriftart)   # Standard Überschrift
      text_1 = wx.StaticText(self,-1,aktuellesJahr,style = wx.ALIGN_CENTER) # Standard Label
      text_1.SetFont(h1)                                                    # Setting Font
      text_1.SetForegroundColour(color_dunkel)                              # set text color

      hbox_1.Add(text_1, 1, wx.EXPAND | wx.ALL, self.border)



class MonatsSeite(wx.Panel):
    def __init__(self, parent):
      super().__init__(parent)


class TagesSeite(wx.Panel):
    def __init__(self, parent):
      super().__init__(parent)



def main():
    app = wx.App()
    ex = Calender(None, title='calender')
    ex.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()
