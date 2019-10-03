import wx
import time

class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title)

        self.InitUI()
        self.SetSize(840,580)
        self.Centre()

    def InitUI(self):

        # Grundstruktur wird geladen
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox_eingabe = wx.BoxSizer(wx.VERTICAL)
        hbox_menu = wx.BoxSizer(wx.HORIZONTAL)

        # Navigationsleisten Bilder werden geladen und an Funktionen gebunden
        # for later Implementation of nicer Buttons:
        # path="path to bitmap"
        # size=(size of bitmap)
        # b=GenBitmapButton(Parent,wx.ID_ANY, bitmap=wx.Bitmap(path), style=wx.NO_BORDER|wx.BU_EXACTFIT,size=size)

        img_mic = wx.Bitmap("mic.png", wx.BITMAP_TYPE_PNG)
        self.button_mic = wx.Button(self,wx.ID_ANY,size=(img_mic.GetWidth()+10, img_mic.GetHeight()+10))
        self.button_mic.SetBitmap(img_mic)
        self.button_mic.Bind(wx.EVT_BUTTON, self.OnClickedMic)

        # img_mic = wx.Bitmap("mic.png", wx.BITMAP_TYPE_PNG)
        # self.button_mic = wx.BitmapButton(self,wx.ID_ANY,img_mic,(img_mic.GetWidth()+10, img_mic.GetHeight()+10))
        # self.button_mic.Bind(wx.EVT_BUTTON, self.OnClickedMic)

        img_cam = wx.Bitmap("cam.png", wx.BITMAP_TYPE_PNG)
        self.button_cam = wx.Button(self,wx.ID_ANY,size=(img_cam.GetWidth()+10, img_cam.GetHeight()+10))
        self.button_cam.SetBitmap(img_cam)
        self.button_cam.Bind(wx.EVT_BUTTON, self.OnClickedCam)

        img_play = wx.Bitmap("play.png", wx.BITMAP_TYPE_PNG)
        self.button_play = wx.Button(self,wx.ID_ANY,size=(img_play.GetWidth()+10, img_play.GetHeight()+10))
        self.button_play.SetBitmap(img_play)
        self.button_play.Bind(wx.EVT_BUTTON, self.OnClickedPlay)

        img_menu = wx.Bitmap("menu.png", wx.BITMAP_TYPE_PNG)
        self.button_menu = wx.BitmapButton(self,wx.ID_ANY,size=(img_menu.GetWidth()+10, img_menu.GetHeight()+10))
        self.button_menu.SetBitmap(img_menu)
        self.button_menu.Bind(wx.EVT_BUTTON, self.OnClickedMenu)

        #Schrift-Deisgn
        font_datum = wx.Font(16, wx.DECORATIVE, wx.NORMAL, wx.NORMAL, faceName="Helvetica") #wx.Font(pointSize, family, style, weight, underline=False, faceName="", encoding=wx.FONTENCODING_DEFAULT
        # font_title = wx.Font(16, wx.MODERN, wx.NORMAL, wx.NORMAL, faceName="Helvetica")
        font_texteingabe = wx.Font(12, wx.MODERN, wx.NORMAL, wx.NORMAL, False, "Helvetica")

        # Eingabe von Titel und Text
        self.datum = wx.StaticText(self, label="Datum: " + time.strftime("%d.%m.%Y"))
        self.datum.SetFont(font_datum)
        # self.title = wx.StaticText(self, label="Titel: ")
        # self.title.SetFont(font_title)
        self.title_eingabe = wx.TextCtrl(self, -1., "Titel eingeben...", style=wx.ALIGN_LEFT)
        self.title_eingabe.SetFont(font_texteingabe)
        self.texteingabe = wx.TextCtrl(self,-1, "Gedanken eingeben...", style = wx.TE_MULTILINE)
        self.texteingabe.SetFont(font_texteingabe)

        # Tips zur ANordnung in BoxSizers
          # topsizer.Add(
          #       wx.TextCtrl(self, -1, "My text.", wx.DefaultPosition, wx.Size(100,60), wx.TE_MULTILINE),
          #       1,           # make vertically stretchable
          #       wx.EXPAND |  # make horizontally stretchable
          #       wx.ALL,      # and make border all around
          #       10)          # set border width to 10

        # ICON MENÜ wird der Hbox_Menu angeordnet
        hbox_menu.Add(self.button_mic, wx.ID_ANY, wx.CENTER | wx.ALL,5 )
        hbox_menu.Add(self.button_cam, wx.ID_ANY, wx.CENTER | wx.ALL,5  )
        hbox_menu.Add(self.button_play, wx.ID_ANY, wx.CENTER | wx.ALL,5  )
        hbox_menu.Add(self.button_menu, wx.ID_ANY, wx.CENTER | wx.ALL, 5 )

        # Hauptfenster Eingabe anordnen
        vbox_eingabe.Add(self.datum,2,wx.EXPAND | wx.ALL, 20)           #  Add(window, proportion=0, flag=0, border=0, userData=None)
        # vbox_eingabe.Add(self.title,2,wx.EXPAND | wx.ALL, 20)
        vbox_eingabe.Add(self.title_eingabe,2,wx.EXPAND | wx.ALL, 20)
        vbox_eingabe.Add(self.texteingabe,10,wx.EXPAND | wx.ALL, 20)

        # Vbox Colum-Ordnung wird angeordnet
        vbox.Add(hbox_menu,1, wx.EXPAND | wx.ALL)
        vbox.Add(vbox_eingabe,6, wx.EXPAND | wx.ALL)
        vbox.AddSpacer(20)

        self.SetSizer(vbox)

    def OnClickedMic(self, event):
        self.button_mic.SetBitmap(wx.Bitmap("rec.png", wx.BITMAP_TYPE_PNG))
        print("Mic gedrückt")


        # self.button_mic.SetBitmap(wx.Bitmap("mic.png", wx.BITMAP_TYPE_PNG))


    def OnClickedCam(self, event):
        print("Cam gedrückt")

    def OnClickedPlay(self, event):
        print("Play gedrückt")

    def OnClickedMenu(self, event):
        print("Menu gedrückt")

def main():

    app = wx.App()
    ex = Example(None, title='Monring_Thoughts')
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
