import wx


class Search(wx.Frame):
    def __init__(self, repo_name_p, data):
        super().__init__(None, title="Github信息查看", size=(300,500))
        panel = wx.Panel(parent=self)
        vbox = wx.BoxSizer(wx.VERTICAL)
        repo_name = wx.StaticText(panel, -1, '仓库名:{}'.format(repo_name_p))
        repo_star = wx.StaticText(panel, -1, '仓库星星数：{}'.format(data["stargazers_count"]))
        repo_watch = wx.StaticText(panel, -1, '仓库Watch数：{}'.format(data["watchers_count"]))
        repo_issues = wx.StaticText(panel, -1, '仓库Issues数：{}'.format(data["open_issues"]))
        repo_forks = wx.StaticText(panel, -1, '仓库Fork数：{}'.format(data['forks']))
        repo_size = wx.StaticText(panel, -1, '仓库大小：{}KB'.format(data['stargazers_count']))
        has_wiki = wx.StaticText(panel, -1, '仓库是否有Wiki?{}'.format(data['has_wiki']))
        has_pages = wx.StaticText(panel, -1, '仓库是否有Pages?{}'.format(data['has_pages']))
        language = wx.StaticText(panel, -1, '仓库主要使用的语言：{}'.format(data['language']))
        for i in [repo_name, repo_star, repo_watch, repo_issues, repo_forks, repo_size, has_wiki, has_pages, language]:
            vbox.Add(i, proportion=1, flag=wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL)
        panel.SetSizer(vbox)