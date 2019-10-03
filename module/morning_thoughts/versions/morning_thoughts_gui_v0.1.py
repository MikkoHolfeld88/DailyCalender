import wx
import wx.lib.platebtn as platebtn
import wx.lib.agw.shapedbutton as sb

class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title)

        self.InitUI()
        self.SetSize(640,480)
        self.Centre()

    def InitUI(self):
        mainWindow = wx.Panel(self)

        hbox = wx.BoxSizer(wx.HORIZONTAL)

        # Create 2 bitmaps for the button
        button_mic = wx.Bitmap("mic.png", wx.BITMAP_TYPE_PNG)
        button_cam = wx.Bitmap("cam.png", wx.BITMAP_TYPE_PNG)
        button_menu = wx.Bitmap("menu.png", wx.BITMAP_TYPE_PNG)
        button_play = wx.Bitmap("play.png", wx.BITMAP_TYPE_PNG)

        mic = wx.BitmapButton(mainWindow, 1, button_mic, (-1, -1), (55, 55))
        cam = sb.SBitmapButton(mainWindow, 2, button_cam, (-1, -1), (55, 55))
        menu = sb.SBitmapButton(mainWindow, 3, button_menu, (-1, -1), (55, 55))
        play = sb.SBitmapButton(mainWindow, 4, button_play, (-1, -1), (55, 55))
        ws_before = wx.StaticText(mainWindow,label="")
        ws_after = wx.StaticText(mainWindow,label="")

        hbox.Add(ws_before, 2, wx.EXPAND, 5)    # Whitespace on the Left
        hbox.Add(mic, 1, wx.ALIGN_LEFT, 5)
        hbox.Add(cam, 1, wx.ALIGN_LEFT, 5)
        hbox.Add(menu, 1, wx.ALIGN_LEFT, 5)
        hbox.Add(play, 1, wx.ALIGN_LEFT, 5)
        hbox.Add(ws_after, 2, wx.EXPAND, 5)     # Whitespace on the right

        play.SetUseFocusIndicator(False)
        #mic.SetUseFocusIndicator(False)
        cam.SetUseFocusIndicator(False)
        menu.SetUseFocusIndicator(False)



        mainWindow.SetSizer(hbox)

def main():

    app = wx.App()
    ex = Example(None, title='Monring_Thoughts')
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
