#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.9.6 on Wed Nov 18 19:35:31 2020
#

import wx

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((366, 316))
        self.first = wx.SpinCtrl(self, wx.ID_ANY, "0", min=0, max=255)
        self.second = wx.SpinCtrl(self, wx.ID_ANY, "0", min=0, max=255)
        self.third = wx.SpinCtrl(self, wx.ID_ANY, "0", min=0, max=255)
        self.cpnl = wx.Panel(self, wx.ID_ANY)
        self.btn = wx.Button(self, wx.ID_ANY, "Change Color")
        self.idhex = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_CENTRE)

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyFrame.__set_properties
        self.SetTitle("Color mixer")
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame.__do_layout
        mainsizer = wx.BoxSizer(wx.VERTICAL)
        sizer_3 = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_1 = wx.BoxSizer(wx.HORIZONTAL)
        label_1 = wx.StaticText(self, wx.ID_ANY, "Red:")
        sizer_1.Add(label_1, 1, 0, 0)
        label_2 = wx.StaticText(self, wx.ID_ANY, "Green:")
        sizer_1.Add(label_2, 1, 0, 0)
        label_3 = wx.StaticText(self, wx.ID_ANY, "Blue:")
        sizer_1.Add(label_3, 1, 0, 0)
        mainsizer.Add(sizer_1, 0, wx.EXPAND, 0)
        sizer_2.Add(self.first, 1, 0, 0)
        sizer_2.Add(self.second, 1, 0, 0)
        sizer_2.Add(self.third, 1, 0, 0)
        mainsizer.Add(sizer_2, 0, wx.EXPAND, 0)
        mainsizer.Add(self.cpnl, 2, wx.EXPAND, 0)
        sizer_3.Add(self.btn, 1, wx.EXPAND, 0)
        sizer_3.Add(self.idhex, 0, wx.EXPAND, 0)
        mainsizer.Add(sizer_3, 1, wx.EXPAND, 0)
        self.SetSizer(mainsizer)
        self.Layout()
        # end wxGlade

# end of class MyFrame

class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

# end of class MyApp

if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()