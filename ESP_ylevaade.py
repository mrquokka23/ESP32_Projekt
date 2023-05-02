from manim import *

class ESP_Ylevaade_moodulid(Scene):
    def construct(self):
        self.camera.background_color="#333333"
        esp32 = ImageMobject("assets\\esp32.png").scale(1)
        esp32.to_edge(LEFT)
        esp2866 = ImageMobject("assets\\ESP2866.png").scale(0.5)
        esp2866.to_edge(RIGHT).shift(LEFT*1)

        pealkiri = Text("ESP moodulid", font="Consolas", font_size=50).to_edge(UP)

        self.play(Write(pealkiri))
        self.play(FadeIn(esp32))
        self.play(FadeIn(esp2866))
        self.wait(15)
        self.play(FadeOut(esp32), FadeOut(esp2866), FadeOut(pealkiri))
        self.wait(1)
