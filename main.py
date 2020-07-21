from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.clock import Clock


class Background(Widget):
    cloud_texture = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Create textures
        self.cloud_texture = Image(source="cloud.png").texture
        self.cloud_texture.wrap = 'repeat'
        # how big the image is before repeat, -1 inverts it
        # uvsize and uvpos are used to wrap the images
        self.cloud_texture.uvsize = (Window.width / self.cloud_texture.width, -1)

    def scroll_textures(self, time_passed):
        # update the uvpos of the texture
        self.cloud_texture.uvpos = (
            (self.cloud_texture.uvpos[0] + time_passed / 2.0) % Window.width, self.cloud_texture.uvpos[1])

        # redraw the texture
        texture = self.property('cloud_texture')
        texture.dispatch(self)


class MainApp(App):
    def on_start(self):
        # moving cloud
        Clock.schedule_interval(self.root.ids.background.scroll_textures, 1/60.)
    pass


MainApp().run()
