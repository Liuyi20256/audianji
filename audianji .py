import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import time
import threading
import android.permissions

# 请求权限
android.permissions.request_permissions([
    android.permissions.PERMISSION.INTERNET,
    android.permissions.PERMISSION.WRITE_EXTERNAL_STORAGE,
    android.permissions.PERMISSION.READ_EXTERNAL_STORAGE
])


class AutoClickerUI(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = [20]
        self.spacing = 10

        # 点击次数输入框
        self.click_count_label = Label(text="点击次数:")
        self.add_widget(self.click_count_label)
        self.click_count_input = TextInput(hint_text="请输入点击次数", multiline=False)
        self.add_widget(self.click_count_input)

        # 点击间隔输入框
        self.click_interval_label = Label(text="点击间隔 (秒):")
        self.add_widget(self.click_interval_label)
        self.click_interval_input = TextInput(hint_text="请输入点击间隔", multiline=False)
        self.add_widget(self.click_interval_input)

        # 开始按钮
        self.start_button = Button(text="开始点击")
        self.start_button.bind(on_press=self.start_clicking)
        self.add_widget(self.start_button)

        # 停止按钮
        self.stop_button = Button(text="停止点击", disabled=True)
        self.stop_button.bind(on_press=self.stop_clicking)
        self.add_widget(self.stop_button)

        self.clicking = False

    def start_clicking(self, instance):
        try:
            click_count = int(self.click_count_input.text)
            click_interval = float(self.click_interval_input.text)
            self.clicking = True
            self.start_button.disabled = True
            self.stop_button.disabled = False
            threading.Thread(target=self.perform_clicks, args=(click_count, click_interval)).start()
        except ValueError:
            print("请输入有效的数字")

    def stop_clicking(self, instance):
        self.clicking = False
        self.start_button.disabled = False
        self.stop_button.disabled = True

    def perform_clicks(self, click_count, click_interval):
        count = 0
        while self.clicking and count < click_count:
            # 模拟点击操作
            print("点击操作")
            time.sleep(click_interval)
            count += 1
        self.clicking = False
        self.start_button.disabled = False
        self.stop_button.disabled = True


class AutoClickerApp(App):
    def build(self):
        return AutoClickerUI()


if __name__ == '__main__':
    AutoClickerApp().run()
    