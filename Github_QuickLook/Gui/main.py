from ..Reql.reql import reql
from .search import Search
import wx

class Root(wx.Frame):
    def __init__(self):
        super().__init__(None, title="Github信息快速查看器", size=(400,150))
        panel = wx.Panel(parent=self)
        vbox = wx.BoxSizer(wx.VERTICAL)
        hbox = wx.BoxSizer()
        Label_prompt = wx.StaticText(panel, -1, "请输入仓库名：")
        self.Entry_owner = wx.TextCtrl(panel)
        Label_slash = wx.StaticText(panel, -1, "/", )
        self.Entry_repo = wx.TextCtrl(panel)
        Button_ok = wx.Button(panel, -1, "查看")
        hbox.Add(Label_prompt, proportion=2)
        hbox.Add(self.Entry_owner, proportion=2, flag=wx.LEFT, border=5)
        hbox.Add(Label_slash, proportion=1, flag=wx.LEFT | wx.RIGHT, border=2)
        hbox.Add(self.Entry_repo, proportion=2, flag=wx.RIGHT, border=5)
        vbox.Add(hbox, proportion=1, flag=wx.ALL, border=10)
        vbox.Add(Button_ok, proportion=1, flag=wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL | wx.ALL, border=10)
        panel.SetSizer(vbox)
        self.Bind(wx.EVT_BUTTON, self.search, Button_ok)
    def search(self, event):
        json_data = reql(self.Entry_owner.GetValue(), self.Entry_repo.GetValue())
        if json_data:
            Search(json_data['full_name'], json_data).Show()
        
        else:
            c_dialog = wx.MessageDialog(None, "没有这个仓库~", "提示", wx.YES_DEFAULT | wx.ICON_QUESTION) 

            if c_dialog.ShowModal() == wx.ID_YES: 
                c_dialog.Destroy()  # 则关闭提示框
                self.Destroy()
App = wx.App()
root = Root()
root.Show()
App.MainLoop()
