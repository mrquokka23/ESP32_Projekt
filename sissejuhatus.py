from manim import *

class Sissejuhatus(Scene):
    def construct(self):
        self.camera.background_color="#333333"
        title = Text("Veebiliidesega mulla-", font="Consolas", font_size=70)
        title2 = Text("niiskuse mõõtja", font="Consolas", font_size=70).next_to(title, DOWN)

        self.play(Write(title))
        self.play(Write(title2))
        self.wait(25)
        self.play(FadeOut(title), FadeOut(title2))