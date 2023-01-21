from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window

kv='''
<MySwiper@MDSwiperItem>
    FilImage:
MDScreen:
    MDTopAppBar:
        id:toolbar
        title:"ma swiper app"
        elevation:10
        pos_hint:{"top":1}
    MDSwiper:
        size_hint_y:None
        height: root.height - toolbar.height - dp(15)
        y:root.height - self.height - toolbar.height - dp(10)
        MDSwiperItem:
            FitImage:
                source:"./img/Php.png"
                radius: [20,0]
        MDSwiperItem:
            FitImage:
                source:"./img/CSS.png"
                radius: [20,0]
        MDSwiperItem:
            FitImage:
                source:"./img/HTML.png"
                radius: [20,0]
        MDSwiperItem:
            FitImage:
                source:"./img/Python.png"
                radius: [20,0]
        MDSwiperItem:
            FitImage:
                source:"./img/SQL.png"
                radius: [20,0]
        MDSwiperItem:
            FitImage:
                source:"./img/perl.png"
                radius: [20,0]
'''
class Myapp(MDApp):
    def build(self):
        self.title = "Images Swiper"
        self.theme_cls.theme_style = 'Light'
        self.theme_cls.primary_palette = "DeepOrange"
        return Builder.load_string(kv)

Myapp().run()
