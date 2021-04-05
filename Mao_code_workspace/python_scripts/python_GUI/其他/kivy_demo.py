# -*- coding:utf-8 -*-
import kivy
# from kivy.deps import sdl2, glew
from kivy.app import App
from kivy.core.window import Window
from kivy.graphics import Color, Line, Rectangle
from kivy.properties import BooleanProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

kivy.require('1.11.1')  # 用你当前的kivy版本替换


# Kivy是一个很优秀的，基于Python的GUI库，可以利用Python快速编程的特点，快速的编写windows, linux, mac, android, ios等主流平台的应用程序。同wxPython、PyQt相比，最大的优点是可以快速地编写移动应用程序。

class MyButton(Button):
    focus = BooleanProperty(False)

    def __init__(self, **kwargs):
        super(MyButton, self).__init__(**kwargs)
        #        with self.canvas.before:
        rect = (self.pos[0] + 4, self.pos[1] + 4, self.size[0] - 8, self.size[1] - 8)
        with self.canvas.after:
            self.edge_color = Color(0, 0, 0, 0)
            self.edge = Line(rectangle=rect, width=4, joint='round')
            self.edge_center_color = Color(1, 1, 1, 0)
            self.edge_center = Line(rectangle=rect, width=1)

        # listen to size and position changes
        self.bind(pos=self.update_rect, size=self.update_rect)
        self.focus = False

    def update_rect(self, instance, value):
        rect = (self.pos[0] + 4, self.pos[1] + 4, self.size[0] - 8, self.size[1] - 8)
        self.edge.rectangle = rect
        self.edge_center.rectangle = rect

    def set_focus(self):
        self.focus = True
        self.parent.on_focus_changed(self)

    def on_focus(self, instance, focused):
        print('++++++++++++++on_focus:', focused)
        if focused:
            self.edge_color.rgba = (0.4, 0.4, 1, 1)
            self.edge_center_color.rgba = (1, 1, 1, 1)
        else:
            self.edge_color.rgba = (0, 0, 0, 0)
            self.edge_center_color.rgba = (0, 0, 0, 0)

    def on_press(self):
        pass

    def on_release(self):
        pass

    def on_touch_down(self, touch):
        print('++++++++++++++++++on_touch_down:', touch)
        if self.collide_point(*touch.pos):
            self.set_focus()
        super(MyButton, self).on_touch_down(touch)


class FocusTest(BoxLayout):
    def __init__(self, **kargs):
        super(FocusTest, self).__init__(**kargs)
        self.buttons = []
        btn1 = MyButton(text='1', on_press=self.on_press)
        btn1.size_hint = (0.5, 0.5)
        self.add_widget(btn1)

        Window.bind(on_key_down=self.on_key_down)

        btn = MyButton(text='2', on_press=self.on_press)
        btn.size_hint = (0.2, 0.2)
        btn.pos_hint = {'top': 0.8}
        self.add_widget(btn)

        btn = MyButton(text='3', on_press=self.on_press)
        btn.size_hint = (0.2, 0.3)
        self.add_widget(btn)

        self.children[-1].set_focus()

        self.index = len(self.children) - 1

        with self.canvas.before:
            Color(0, 1, 0, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)
            Color(1, 1, 0, 1)
            self.border = Line(rectangle=self.pos + self.size, width=3)

        # listen to size and position changes
        self.bind(pos=FocusTest.update_rect, size=FocusTest.update_rect)
        for item in self.children:
            print(item.text)

    def on_focus_changed(self, focusitem):
        index = 0
        for item in self.children:
            if focusitem is item:
                self.index = index
            else:
                item.focus = False
            index += 1

    def on_key_down(self, window, key, scancode, a, b):
        print('on_key_down:', key, scancode)
        if key == 275:  # left
            if self.index == 0:
                self.index = len(self.children) - 1
            else:
                self.index -= 1
        elif key == 276:  # right
            if self.index == len(self.children) - 1:
                self.index = 0
            else:
                self.index += 1
        self.children[self.index].set_focus()

    def on_key_up(self, window, key, scancode):
        pass

    def on_press(self, control):
        print(control)

    def on_release(self, control):
        print(control)

    def update_rect(self, value):
        self.rect.pos = self.pos
        self.rect.size = self.size
        self.border.rectangle = self.pos + self.size


class MyApp(App):
    def build(self):
        return FocusTest()

    def on_pause(self):
        return True


if __name__ == '__main__':
    MyApp().run()
