import os               # FileDialog
import shutil           # Deleting folder
import wx               # GUI
import time             # for creating TimeStamp / Showing Date
import pygame           # playing audio
import spracheingabe    # Speech to Text
from gtts import gTTS   # Text to Speech

class App(wx.Frame):

    def __init__(self, parent, title):
        super(App, self).__init__(parent, title=title)

        self.InitUI()
        self.deletingOldAudioFiles()
        self.SetSize(840,580)
        self.Centre()
        pygame.init()

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

        img_mic = wx.Bitmap("icon/mic.png", wx.BITMAP_TYPE_PNG)
        self.button_mic = wx.Button(self,wx.ID_ANY,size=(img_mic.GetWidth()+10, img_mic.GetHeight()+10))
        self.button_mic.SetBitmap(img_mic)
        self.button_mic.Bind(wx.EVT_BUTTON, self.OnClickedMic)

        img_play = wx.Bitmap("icon/play.png", wx.BITMAP_TYPE_PNG)
        self.button_play = wx.Button(self,wx.ID_ANY,size=(img_play.GetWidth()+10, img_play.GetHeight()+10))
        self.button_play.SetBitmap(img_play)
        self.button_play.Bind(wx.EVT_BUTTON, self.OnClickedPlay)

        img_save = wx.Bitmap("icon/save.png", wx.BITMAP_TYPE_PNG)
        self.button_save = wx.Button(self,wx.ID_ANY,size=(img_save.GetWidth()+10, img_save.GetHeight()+10))
        self.button_save.SetBitmap(img_save)
        self.button_save.Bind(wx.EVT_BUTTON, self.OnClickedSave)

        img_load = wx.Bitmap("icon/load.png", wx.BITMAP_TYPE_PNG)
        self.button_load = wx.Button(self,wx.ID_ANY,size=(img_load.GetWidth()+10, img_load.GetHeight()+10))
        self.button_load.SetBitmap(img_load)
        self.button_load.Bind(wx.EVT_BUTTON, self.OnClickedLoad)

        img_menu = wx.Bitmap("icon/menu.png", wx.BITMAP_TYPE_PNG)
        self.button_menu = wx.BitmapButton(self,wx.ID_ANY,size=(img_menu.GetWidth()+10, img_menu.GetHeight()+10))
        self.button_menu.SetBitmap(img_menu)
        self.button_menu.Bind(wx.EVT_BUTTON, self.OnClickedMenu)

        # Binds Close Event to OnClose Function
        self.Bind(wx.EVT_CLOSE, self.OnClose)

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

        # Tips zur Anordnung in BoxSizers
          # topsizer.Add(
          #       wx.TextCtrl(self, -1, "My text.", wx.DefaultPosition, wx.Size(100,60), wx.TE_MULTILINE),
          #       1,           # make vertically stretchable
          #       wx.EXPAND |  # make horizontally stretchable
          #       wx.ALL,      # and make border all around
          #       10)          # set border width to 10

        # ICON MENÜ wird der Hbox_Menu angeordnet
        hbox_menu.Add(self.button_mic, wx.ID_ANY, wx.CENTER | wx.ALL,5 )
        hbox_menu.Add(self.button_play, wx.ID_ANY, wx.CENTER | wx.ALL,5  )
        hbox_menu.Add(self.button_save, wx.ID_ANY, wx.CENTER | wx.ALL,5  )
        hbox_menu.Add(self.button_load, wx.ID_ANY, wx.CENTER | wx.ALL,5  )
        hbox_menu.Add(self.button_menu, wx.ID_ANY, wx.CENTER | wx.ALL, 5 )

        # Hauptfenster Eingabe anordnen
        vbox_eingabe.Add(self.datum,2,wx.EXPAND | wx.ALL, 20)           #  Add(window, proportion=0, flag=0, border=0, userData=None)
        vbox_eingabe.Add(self.title_eingabe,2,wx.EXPAND | wx.ALL, 20)
        vbox_eingabe.Add(self.texteingabe,10,wx.EXPAND | wx.ALL, 20)

        # Vbox Column-Ordnung wird angeordnet
        vbox.Add(hbox_menu,1, wx.EXPAND | wx.ALL)
        vbox.Add(vbox_eingabe,6, wx.EXPAND | wx.ALL)
        vbox.AddSpacer(20)

        self.SetSizer(vbox)

    def OnClickedMic(self, event):
        # changing bitmap
        self.button_mic.SetBitmap(wx.Bitmap("icon/rec.png", wx.BITMAP_TYPE_PNG))
        self.Update()
        print("Mic gedrückt")
        text = spracheingabe.OnSpeak()
        # überschreibt Gedanken eingeben... oder hängt etwas dran falls nicht Gedanken eingeben...
        if self.texteingabe.GetValue() == "Gedanken eingeben...":
            self.texteingabe.SetValue(text)
        else:
            self.texteingabe.AppendText(" " + text)
        # changing bitmap
        self.button_mic.SetBitmap(wx.Bitmap("icon/mic.png", wx.BITMAP_TYPE_PNG))
        self.Update()

    def OnClickedPlay(self, event):
        # changing bitmap
        print("Play gedrückt")
        self.button_play.SetBitmap(wx.Bitmap("icon/playdisabled.png", wx.BITMAP_TYPE_PNG))
        self.Update()
        # handling audiofile
        dateiname = self.createAudiofile(gTTS(text=self.texteingabe.GetValue(), lang="de", slow=False))
        self.playingAudiofile(dateiname)
        # handling stop / play
        self.button_play.Bind(wx.EVT_BUTTON, self.OnClickedPause)
        SONG_END = pygame.USEREVENT + 1
        pygame.mixer.music.set_endevent(SONG_END)
        # Procedure for SongEnd
        whileVar = True
        while whileVar:
            for event in pygame.event.get():
                if event.type == SONG_END:
                    print("Audio Wiedergabe beendet")
                    self.PlayButtonBackToNormal()
                    whileVar = False

    # Zusatzmethoden zum Button "Play"
    def createAudiofile(self, textToSpeech):
        zeitstempel = (time.strftime("%d%m%Y_%H%M%S"))
        dateiname = "audio/morning_thoughts_tts_" + zeitstempel + "_.mp3"
        textToSpeech.save(dateiname)
        return dateiname

    def playingAudiofile(self, datei):
        pygame.mixer.quit()
        pygame.mixer.init(frequency=50000)
        pygame.mixer.music.load(datei)
        pygame.mixer.music.play()

    def PlayButtonBackToNormal(self):
        self.button_play.SetBitmap(wx.Bitmap("icon/play.png", wx.BITMAP_TYPE_PNG))
        self.button_play.Bind(wx.EVT_BUTTON, self.OnClickedPlay)
        self.Update()

    def OnClickedPause(self,event):
        pygame.mixer.music.stop()
        print("Audiowiedergabe unterbrochen")
        self.PlayButtonBackToNormal()

    def CheckingFile(self, filename):
        dateiListe = []
        dir_path = os.path.dirname(os.path.realpath(__file__))
        for root, dirs, files in os.walk(dir_path):
            for file in files:
                if file.endswith('.mp3'):
                    dateiListe.append(file)
        if filename in dateiListe :
            return True

    # Button Save / Speichern
    def OnClickedSave(self, event):
        print("Speichern gedrückt")
        zeitstempel = (time.strftime("%d%m%Y_%H%M%S"))
        if self.title_eingabe.GetValue() == "Titel eingeben...":
            speichername = "morning_thoughts_text_" + zeitstempel + ".txt"
        else:
            speichername = str(self.title_eingabe.GetValue()) + "_" + zeitstempel + ".txt"
        speicherort = "data/" + speichername
        fh = open(speicherort, "w")
        print(self.texteingabe.GetValue(), file = fh)
        fh.close()

    def OnClickedLoad(self, event):
        print("Laden gedrückt")
        wildcard = "TXT files (*.txt)|*.txt"
        dialog = wx.FileDialog(self, "Open Text Files", wildcard=wildcard,
                               style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        if dialog.ShowModal() == wx.ID_CANCEL:
            return
        path = dialog.GetPath()
        dateiname = dialog.GetFilename()
        if os.path.exists(path):
            with open(path) as fobj:
                for line in fobj:
                    self.texteingabe.WriteText(line)
                self.title_eingabe.SetValue(dateiname)

    def OnClickedMenu(self, event):
        print("Menu gedrückt")

    def OnClose(self, event):
        print("close")
        self.Destroy()

    def deletingOldAudioFiles(self):
        # löschen der erstellten Audiofiles von TTS
        dateiListe = []
        dir_path = os.path.dirname(os.path.realpath(__file__))
        for root, dirs, files in os.walk(dir_path):
            for file in files:
                if file.endswith('.mp3'):
                    os.remove("audio/" + file)

def main():
    app = wx.App()
    ex = App(None, title='Morning_Thoughts')
    ex.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()
