import wx

class MeuPrograma(wx.Frame):
    def __init__(self, *args, **kw):
        super(MeuPrograma, self).__init__(*args, **kw)

        self.InitUI()

    def InitUI(self):
        pnl = wx.Panel(self)
        btn = wx.Button(pnl, label='Clique Aqui', pos=(50, 50))

        btn.Bind(wx.EVT_BUTTON, self.OnClick)

        self.SetSize((250, 200))
        self.SetTitle('Meu Programa com wxPython')
        self.Centre()

    def OnClick(self, e):
        wx.MessageBox('Você clicou no botão!', 'Mensagem', wx.OK | wx.ICON_INFORMATION)

def main():
    app = wx.App()
    frame = MeuPrograma(None)
    frame.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()
