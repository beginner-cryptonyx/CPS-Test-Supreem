from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.clock import Clock


class MainScreen(Screen):
    pass


class CpsCounter(Screen):
    pass


class scr4(Screen):
    pass


class scr5(Screen):
    pass


class scr6(Screen):
    pass


class resultsScreen(Screen):
    pass


class CountdownScreen(Screen):
    pass


class MasterWindow(ScreenManager):
    pass


CPS = 0


class CPS_trainer(App):
    def wait(self, *args):
        pass

    def SwitchCountdown1(self, *args):
        self.root.get_screen('countdown').ids.coundownTimer.color = (0, 2, 0, 1)
        self.root.get_screen('countdown').ids.coundownTimer.text = '3'

    def SwitchCountdown2(self, *args):
        self.root.get_screen('countdown').ids.coundownTimer.color = (234 / 255, 245 / 255, 22 / 255)
        self.root.get_screen('countdown').ids.coundownTimer.text = '2'

    def SwitchCountdown3(self, *args):
        self.root.get_screen('countdown').ids.coundownTimer.color = (1, 0, 0)
        self.root.get_screen('countdown').ids.coundownTimer.text = '1'

    def AddCPS(self):
        global CPS
        CPS += 1

    def StartCalcResult(self, *args, sec):
        Clock.schedule_once(self.CalcResult, sec)

    def CalcResult(self, sec, *args):
        self.root.current = 'resultScreen'
        if CPS != 0:
            result = int(CPS) / int(sec)
            self.root.get_screen('resultScreen').ids.resultLabel.text = str(result)
        else:
            self.root.get_screen('resultScreen').ids.resultLabel.text = "CPS:0; FACING COMPLICATION ERROR;" \
                                                                        " Don't you know division by 0 is not possible noob"

    def StartSwitchCountdown(self, scr, secnd, *args):
        def QuickSwitch(*args):
            self.root.current = scr
            self.StartCalcResult(sec=secnd)

        Clock.schedule_once(self.SwitchCountdown1, 0)
        Clock.schedule_once(self.SwitchCountdown2, 1)
        Clock.schedule_once(self.SwitchCountdown3, 2)
        Clock.schedule_once(QuickSwitch, 3)

    def ColorParityFix_Pressed(self, btn):
        if btn == 2:
            self.root.get_screen('mainScreen').ids.btn2.background_color = (200 / 255, 200 / 255, 20 / 255)
        elif btn == 3:
            self.root.get_screen('mainScreen').ids.btn3.background_color = (0.7, 0, 0, 1)
        elif btn == 5:
            self.root.get_screen('mainScreen').ids.btn5.background_color = (200 / 255, 200 / 255, 20 / 255)
        elif btn == 6:
            self.root.get_screen('mainScreen').ids.btn6.background_color = (0.7, 0, 0, 1)

    def ColorParityFix_Released(self, btn):
        if btn == 2:
            self.root.get_screen('mainScreen').ids.btn2.background_color = (234 / 255, 245 / 255, 22 / 255)
        elif btn == 3:
            self.root.get_screen('mainScreen').ids.btn3.background_color = (1, 0, 0, 1)
        elif btn == 5:
            self.root.get_screen('mainScreen').ids.btn5.background_color = (234 / 255, 245 / 255, 22 / 255)
        elif btn == 6:
            self.root.get_screen('mainScreen').ids.btn6.background_color = (1, 0, 0, 1)

    def build(self):
        bld = Builder.load_file("Main.kv")
        return bld


if __name__ == "__main__":
    CPS_trainer().run()
