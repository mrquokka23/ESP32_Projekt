from manim import *

import numpy as np

class ESP_arendusplaat(Scene):
    def construct(self):
        self.camera.background_color="#333333"
        esp32 = ImageMobject("assets\\esp32devkit1.png").scale(0.455)
        viigud = Text("Lihtsasti kasutatavad viigud", font="Consolas", font_size=30).next_to(esp32, RIGHT).shift(LEFT*2)
        pingeregulaator = Text("Pingeregulaator", font="Consolas", font_size=30).next_to(viigud, DOWN)
        usb_uart = Text("USB-UART sild", font="Consolas", font_size=30).next_to(pingeregulaator, DOWN)
        ellipse_viigud1 = Ellipse(width=0.4, height=4.3, color=RED, arc_center=np.array([-4.37, 0.3, 0.]))
        ellipse_viigud2 = Ellipse(width=0.4, height=4.3, color=RED, arc_center=np.array([-1.57, 0.3, 0.]))
        ellipse_pingeregulaator = Ellipse(width=1, height=1, color=RED, arc_center=np.array([-2.55, -0.8, 0.]))
        ellipse_usb = Ellipse(width=0.8, height=0.8, color=RED, arc_center=np.array([-3, -1.7, 0.]))
        espwroom = ImageMobject("assets\\espwroom.png").scale(0.455).shift(LEFT*3)
        prose = ImageMobject("assets\\Screenshot 2023-04-25 141657.jpg").shift(LEFT*3).scale(0.2)

        self.play(FadeIn(esp32))
        self.play(esp32.animate.shift(LEFT*3))
        self.play(Write(viigud),Create(ellipse_viigud1), Create(ellipse_viigud2))
        self.play(Write(pingeregulaator), Create(ellipse_pingeregulaator))
        self.play(Write(usb_uart), Create(ellipse_usb))
        self.play(FadeOut(viigud), FadeOut(pingeregulaator), FadeOut(usb_uart), FadeOut(ellipse_viigud1), FadeOut(ellipse_viigud2), FadeOut(ellipse_pingeregulaator), FadeOut(ellipse_usb))
        self.play(FadeIn(espwroom))
        self.play(FadeOut(esp32))
        self.play(espwroom.animate.shift(RIGHT*3).scale(1.45).shift(DOWN*1.5))
        self.play(espwroom.animate.shift(LEFT*3), run_time=2)
        self.play(FadeOut(espwroom), FadeIn(prose), prose.animate.scale(5))
        self.wait(2)