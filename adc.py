from manim import *

import numpy as np


class ESP_adc(Scene):
    def construct(self):
        self.camera.background_color = "#333333"
        graph = Axes(
            x_range=[0, 12, 1],
            y_range=[0, 3.5, 0.5],
            x_length=10,
            y_length=5,
            axis_config={
                "color": WHITE,
                "stroke_width": 2,
            },
            x_axis_config={
                "numbers_to_include": np.arange(0, 12, 1),
                "numbers_with_elongated_ticks": np.arange(0, 12, 1),
            },
            y_axis_config={
                "numbers_to_include": np.arange(0, 4, 1),
                "numbers_with_elongated_ticks": np.arange(0, 4, 1),
            }
        )
        vinline = graph.plot_line_graph(x_values=[0, 12], y_values=[
                                        1.5, 1.5], line_color=GREEN, add_vertex_dots=False)
        vcmp1 = graph.plot_line_graph(x_values=[0, 2], y_values=[
                                      3.3/2, 3.3/2], line_color=RED, add_vertex_dots=False)
        vcmp2 = graph.plot_line_graph(x_values=[2, 4], y_values=[
                                      3.3/4, 3.3/4], line_color=RED, add_vertex_dots=False)
        vcmp3 = graph.plot_line_graph(x_values=[4, 6], y_values=[
                                      3.3/4+3.3/8, 3.3/4+3.3/8], line_color=RED, add_vertex_dots=False)
        vcmp4 = graph.plot_line_graph(x_values=[6, 8], y_values=[
                                      3.3/4+3.3/8+3.3/16, 3.3/4+3.3/8+3.3/16], line_color=RED, add_vertex_dots=False)
        vcmp5 = graph.plot_line_graph(x_values=[8, 10], y_values=[
                                      3.3/4+3.3/8+3.3/16+3.3/32, 3.3/4+3.3/8+3.3/16+3.3/32], line_color=RED, add_vertex_dots=False)
        vcmp6 = graph.plot_line_graph(x_values=[10, 12], y_values=[
                                      3.3/4+3.3/8+3.3/16+3.3/64, 3.3/4+3.3/8+3.3/16+3.3/64], line_color=RED, add_vertex_dots=False)
        vcmp1text = Tex(f"{round(3.3/2, 3)} V", font_size=30,
                        color=RED).next_to(vcmp1, UP)
        vcmp1bin = Tex("100000", font_size=30, color=RED).next_to(vcmp1, DOWN)
        vcmp2text = Tex(f"{round(3.3/4, 3)} V", font_size=30,
                        color=RED).next_to(vcmp2, UP)
        vcmp2bin = Tex("010000", font_size=30, color=RED).next_to(vcmp2, DOWN)
        vcmp3text = Tex(f"{round(3.3/4+3.3/8, 3)} V",
                        font_size=30, color=RED).next_to(vcmp3, UP)
        vcmp3bin = Tex("011000", font_size=30, color=RED).next_to(vcmp3, DOWN)
        vcmp4text = Tex(f"{round(3.3/4+3.3/8+3.3/16, 3)} V",
                        font_size=30, color=RED).next_to(vcmp4, UP)
        vcmp4bin = Tex("011100", font_size=30, color=RED).next_to(vcmp4, DOWN)
        vcmp5text = Tex(f"{round(3.3/4+3.3/8+3.3/16+3.3/32, 3)} V",
                        font_size=30, color=RED).next_to(vcmp5, UP)
        vcmp5bin = Tex("011110", font_size=30, color=RED).next_to(vcmp5, DOWN)
        vcmp6text = Tex(f"{round(3.3/4+3.3/8+3.3/16+3.3/64, 3)} V",
                        font_size=30, color=RED).next_to(vcmp6, UP)
        vcmp6bin = Tex("011101", font_size=30, color=RED).next_to(vcmp6, DOWN)

        vcmp1text.shift(DOWN*0.15)
        vcmp1bin.shift(UP*0.15)
        vcmp1textbg = BackgroundRectangle(
            vcmp1text, color="#333333", fill_opacity=0.6)
        vcmp1binbg = BackgroundRectangle(
            vcmp1bin, color="#333333", fill_opacity=0.6)

        vcmp2text.shift(DOWN*0.15)
        vcmp2bin.shift(UP*0.15)
        vcmp2textbg = BackgroundRectangle(
            vcmp2text, color="#333333", fill_opacity=0.6)
        vcmp2binbg = BackgroundRectangle(
            vcmp2bin, color="#333333", fill_opacity=0.6)

        vcmp3text.shift(DOWN*0.15)
        vcmp3bin.shift(UP*0.15)
        vcmp3textbg = BackgroundRectangle(
            vcmp3text, color="#333333", fill_opacity=0.6)
        vcmp3binbg = BackgroundRectangle(
            vcmp3bin, color="#333333", fill_opacity=0.6)

        vcmp4text.shift(DOWN*0.15)
        vcmp4bin.shift(UP*0.15)
        vcmp4textbg = BackgroundRectangle(
            vcmp4text, color="#333333", fill_opacity=0.6)
        vcmp4binbg = BackgroundRectangle(
            vcmp4bin, color="#333333", fill_opacity=0.6)

        vcmp5text.shift(DOWN*0.15)
        vcmp5bin.shift(UP*0.15)
        vcmp5textbg = BackgroundRectangle(
            vcmp5text, color="#333333", fill_opacity=0.6)
        vcmp5binbg = BackgroundRectangle(
            vcmp5bin, color="#333333", fill_opacity=0.6)

        vcmp6text.shift(DOWN*0.15)
        vcmp6bin.shift(UP*0.15)
        vcmp6textbg = BackgroundRectangle(
            vcmp6text, color="#333333", fill_opacity=0.6)
        vcmp6binbg = BackgroundRectangle(
            vcmp6bin, color="#333333", fill_opacity=0.6)

        image = SVGMobject("assets/sar.svg").shift(UR*2).scale(1.5)
        vtect = Tex(r"$V_{in} = 1.5 V$", font_size=30,
                    color=GREEN).next_to(image[15], LEFT)
        num11 = Tex("1", font_size=30, color=RED).next_to(
            image[2], LEFT).shift(RIGHT*0.3)
        num12 = Tex("0", font_size=30, color=RED).next_to(
            image[3], LEFT).shift(RIGHT*0.3)
        num13 = Tex("0", font_size=30, color=RED).next_to(
            image[4], LEFT).shift(RIGHT*0.3)
        num14 = Tex("0", font_size=30, color=RED).next_to(
            image[5], LEFT).shift(RIGHT*0.3)
        num15 = Tex("0", font_size=30, color=RED).next_to(
            image[6], LEFT).shift(RIGHT*0.3)
        num16 = Tex("0", font_size=30, color=RED).next_to(
            image[7], LEFT).shift(RIGHT*0.3)
        dots = Tex("...", font_size=30, color=RED).next_to(
            image[7], RIGHT).shift(LEFT*0.3)
        group1 = VGroup(num11, num12, num13, num14, num15, num16)

        num21 = Tex("0", font_size=30, color=RED).next_to(
            image[2], LEFT).shift(RIGHT*0.3)
        num22 = Tex("1", font_size=30, color=RED).next_to(
            image[3], LEFT).shift(RIGHT*0.3)
        num23 = Tex("0", font_size=30, color=RED).next_to(
            image[4], LEFT).shift(RIGHT*0.3)
        num24 = Tex("0", font_size=30, color=RED).next_to(
            image[5], LEFT).shift(RIGHT*0.3)
        num25 = Tex("0", font_size=30, color=RED).next_to(
            image[6], LEFT).shift(RIGHT*0.3)
        num26 = Tex("0", font_size=30, color=RED).next_to(
            image[7], LEFT).shift(RIGHT*0.3)
        group2 = VGroup(num21, num22, num23, num24, num25, num26)

        num31 = Tex("0", font_size=30, color=RED).next_to(
            image[2], LEFT).shift(RIGHT*0.3)
        num32 = Tex("1", font_size=30, color=RED).next_to(
            image[3], LEFT).shift(RIGHT*0.3)
        num33 = Tex("1", font_size=30, color=RED).next_to(
            image[4], LEFT).shift(RIGHT*0.3)
        num34 = Tex("0", font_size=30, color=RED).next_to(
            image[5], LEFT).shift(RIGHT*0.3)
        num35 = Tex("0", font_size=30, color=RED).next_to(
            image[6], LEFT).shift(RIGHT*0.3)
        num36 = Tex("0", font_size=30, color=RED).next_to(
            image[7], LEFT).shift(RIGHT*0.3)
        group3 = VGroup(num31, num32, num33, num34, num35, num36)

        num41 = Tex("0", font_size=30, color=RED).next_to(
            image[2], LEFT).shift(RIGHT*0.3)
        num42 = Tex("1", font_size=30, color=RED).next_to(
            image[3], LEFT).shift(RIGHT*0.3)
        num43 = Tex("1", font_size=30, color=RED).next_to(
            image[4], LEFT).shift(RIGHT*0.3)
        num44 = Tex("1", font_size=30, color=RED).next_to(
            image[5], LEFT).shift(RIGHT*0.3)
        num45 = Tex("0", font_size=30, color=RED).next_to(
            image[6], LEFT).shift(RIGHT*0.3)
        num46 = Tex("0", font_size=30, color=RED).next_to(
            image[7], LEFT).shift(RIGHT*0.3)
        group4 = VGroup(num41, num42, num43, num44, num45, num46)

        num51 = Tex("0", font_size=30, color=RED).next_to(
            image[2], LEFT).shift(RIGHT*0.3)
        num52 = Tex("1", font_size=30, color=RED).next_to(
            image[3], LEFT).shift(RIGHT*0.3)
        num53 = Tex("1", font_size=30, color=RED).next_to(
            image[4], LEFT).shift(RIGHT*0.3)
        num54 = Tex("1", font_size=30, color=RED).next_to(
            image[5], LEFT).shift(RIGHT*0.3)
        num55 = Tex("1", font_size=30, color=RED).next_to(
            image[6], LEFT).shift(RIGHT*0.3)
        num56 = Tex("0", font_size=30, color=RED).next_to(
            image[7], LEFT).shift(RIGHT*0.3)
        group5 = VGroup(num51, num52, num53, num54, num55, num56)

        num61 = Tex("0", font_size=30, color=RED).next_to(
            image[2], LEFT).shift(RIGHT*0.3)
        num62 = Tex("1", font_size=30, color=RED).next_to(
            image[3], LEFT).shift(RIGHT*0.3)
        num63 = Tex("1", font_size=30, color=RED).next_to(
            image[4], LEFT).shift(RIGHT*0.3)
        num64 = Tex("1", font_size=30, color=RED).next_to(
            image[5], LEFT).shift(RIGHT*0.3)
        num65 = Tex("0", font_size=30, color=RED).next_to(
            image[6], LEFT).shift(RIGHT*0.3)
        num66 = Tex("1", font_size=30, color=RED).next_to(
            image[7], LEFT).shift(RIGHT*0.3)
        group6 = VGroup(num61, num62, num63, num64, num65, num66)

        vin = Tex(r"$V_{in}$", font_size=30,
                  color=GREEN).next_to(vinline, LEFT)

        self.play(Write(graph))
        self.play(Create(image))
        self.wait(1)
        self.play(Write(vtect))
        self.play(Create(vinline))
        self.play(Write(vin))
        self.play(Create(group1), Create(dots))
        self.wait(0.3)
        self.play(Create(vcmp1textbg), Create(vcmp1binbg))
        self.play(Write(vcmp1text), TransformFromCopy(
            group1, vcmp1bin), Create(vcmp1))
        self.play(Create(vcmp2textbg), Create(vcmp2binbg))
        self.play(ReplacementTransform(group1, group2))
        self.play(Write(vcmp2text), TransformFromCopy(
            group2, vcmp2bin), Create(vcmp2))
        self.play(ReplacementTransform(group2, group3))
        self.play(Create(vcmp3textbg), Create(vcmp3binbg))
        self.play(Write(vcmp3text), TransformFromCopy(
            group3, vcmp3bin), Create(vcmp3))
        self.play(ReplacementTransform(group3, group4))
        self.play(Create(vcmp4textbg), Create(vcmp4binbg))
        self.play(Write(vcmp4text), TransformFromCopy(
            group4, vcmp4bin), Create(vcmp4))
        self.play(ReplacementTransform(group4, group5))
        self.play(Create(vcmp5textbg), Create(vcmp5binbg))
        self.play(Write(vcmp5text), TransformFromCopy(
            group5, vcmp5bin), Create(vcmp5))
        self.play(ReplacementTransform(group5, group6))
        self.play(Create(vcmp6textbg), Create(vcmp6binbg))
        self.play(Write(vcmp6text), TransformFromCopy(
            group6, vcmp6bin), Create(vcmp6))
        temp = []
        for mob in self.mobjects:
            if mob == vcmp6bin:
                continue
            else:
                temp.append(mob)
        self.play(
            *[FadeOut(mob)for mob in temp]
        )
        self.play(vcmp6bin.animate.move_to(ORIGIN).scale(2.5))

        calculation1 = Tex(
            r"$\frac{3.3V}{2} = 1.65V$", font_size=30, color=GREEN)
        calculation2 = Tex(r"$\frac{3.3V}{4} = 0.825V$", font_size=30, color=GREEN).next_to(
            calculation1, RIGHT)
        calculation3 = Tex(r"$\frac{3.3V}{8} = 0.4125V$", font_size=30, color=GREEN).next_to(
            calculation2, RIGHT)
        calculation4 = Tex(r"$\frac{3.3V}{16} = 0.2063V$", font_size=30, color=GREEN).next_to(
            calculation3, RIGHT)
        calculation5 = Tex(r"$\frac{3.3V}{32} = 0.1031V$", font_size=30, color=GREEN).next_to(
            calculation4, RIGHT)
        calculation6 = Tex(r"$\frac{3.3V}{64} = 0.0516V$", font_size=30, color=GREEN).next_to(
            calculation5, RIGHT)

        calcgroup = VGroup(calculation1, calculation2, calculation3,
                           calculation4, calculation5, calculation6).next_to(vcmp6bin, DOWN)

        summa = Tex(r"$0 \times 1.65V + 1 \times 0.825V + 1 \times 0.4125V + 1 \times 0.2063V + 0 \times 0.1031V + 1 \times 0.0516V \approx 1.495V$",
                    font_size=30, color=GREEN).next_to(calcgroup, DOWN)
        summa[0][0].set_color(RED)
        summa[0][7].set_color(RED)
        summa[0][17].set_color(RED)
        summa[0][27].set_color(RED)
        summa[0][37].set_color(RED)
        summa[0][47].set_color(RED)
        

        self.play(TransformFromCopy(vcmp6bin, calcgroup))
        self.play(TransformFromCopy(calcgroup, summa))
        

        self.wait(5)
