from sty import Style, RgbFg, fg, bg, ef, rs


class message:

    """
    To use this modelue 
    Msg.Warn_print(text: str)
    """
    @staticmethod
    def WarnPrint(text,end=None):

        text = str(text)
        fg.YELLOW = Style(RgbFg(255, 204, 0))
        Warning_text = fg.YELLOW + text + fg.rs
        print(Warning_text,end=end)

    @staticmethod
    def ErrorPrint(text,end=None):
        text = str(text)
        fg.RED = Style(RgbFg(255, 100, 0))
        Error_text = fg.RED + text + fg.rs
        print(Error_text,end=end)

    @staticmethod
    def SuccessPrint(text,end=None):
        text = str(text)
        fg.GREEN = Style(RgbFg(0, 255, 12))
        Success_text = fg.GREEN + text + fg.rs
        print(Success_text,end=end)

    @staticmethod
    def InfoPrint(text,end=None):
        text = str(text)
        fg.WHITE = Style(RgbFg(255, 255, 255))
        Info_text = fg.WHITE + text + fg.rs
        print(Info_text,end=end)

    @staticmethod
    def HilightPrint(text,end=None):
        text = str(text)
        fg.WHITE = Style(RgbFg(102, 205, 255))
        Info_text = fg.WHITE + text + fg.rs
        print(Info_text,end=end)