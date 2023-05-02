from manim import *

class Komponendid(Scene):
    def construct(self):
        self.camera.background_color="#333333"
        pealkiri = Tex("Vajalikud komponendid", tex_template=TexTemplateLibrary.threeb1b, font_size=50).to_edge(UP)
        ul1 = Underline(pealkiri)
        komponent1 = Tex("1. ESP32 arendusplaat", tex_template=TexTemplateLibrary.threeb1b, font_size=30).next_to(pealkiri, DOWN)
        komponent2 = Tex("2. Maketeerimislaud", tex_template=TexTemplateLibrary.threeb1b, font_size=30).next_to(komponent1, DOWN)
        komponent3 = Tex("3. Ribakaabel või juhtmed sensori tegemiseks", tex_template=TexTemplateLibrary.threeb1b, font_size=30).next_to(komponent2, DOWN)
        komponent4 = Tex("4. Juhtmed ühendamiseks", tex_template=TexTemplateLibrary.threeb1b, font_size=30).next_to(komponent3, DOWN)
        komponent5 = Tex("5. Jootmistarvikud", tex_template=TexTemplateLibrary.threeb1b, font_size=30).next_to(komponent4, DOWN)
        komponent6 = Tex("6. Liim või silikoon juhtme otsa veekindlaks tegemiseks", tex_template=TexTemplateLibrary.threeb1b, font_size=30).next_to(komponent5, DOWN)
        komponent7 = Tex("7. Mikro USB kaabel", tex_template=TexTemplateLibrary.threeb1b, font_size=30).next_to(komponent6, DOWN)
        komponent8 = Tex("8. 5V toiteadapter", tex_template=TexTemplateLibrary.threeb1b, font_size=30).next_to(komponent7, DOWN)
        alapealkiri = Tex("Valikuline", tex_template=TexTemplateLibrary.threeb1b, font_size=50).next_to(komponent8, DOWN)	
        ul2 = Underline(alapealkiri)
        valik1 = Tex("9. Joodetav maketeerimislaud", tex_template=TexTemplateLibrary.threeb1b, font_size=30).next_to(alapealkiri, DOWN)
        valik2 = Tex("10. 3D-printer", tex_template=TexTemplateLibrary.threeb1b, font_size=30).next_to(valik1, DOWN)

        self.play(Write(pealkiri), Write(ul1))
        self.play(Write(komponent1))
        self.play(Write(komponent2))
        self.play(Write(komponent3))
        self.play(Write(komponent4))
        self.play(Write(komponent5))
        self.play(Write(komponent6))
        self.play(Write(komponent7))
        self.play(Write(komponent8))
        self.wait(4.5)
        self.play(Write(alapealkiri), Write(ul2))
        self.play(Write(valik1))
        self.play(Write(valik2))
        self.wait(3)
        self.play(FadeOut(pealkiri), FadeOut(ul1), FadeOut(komponent1), FadeOut(komponent2), FadeOut(komponent3), FadeOut(komponent4), FadeOut(komponent5), FadeOut(komponent6), FadeOut(komponent7), FadeOut(komponent8), FadeOut(alapealkiri), FadeOut(ul2), FadeOut(valik1), FadeOut(valik2))
        
        