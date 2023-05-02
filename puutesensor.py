from manim import *
from colour import Color

red = Color("red")
colors = list(red.range_to(Color("green"), 101))

class ESP_Ylevaade(Scene):
    
    def construct(self):
        def translate(value):
            leftMin = 0
            leftMax = 3
            rightMin = 0
            rightMax = 100
            # Figure out how 'wide' each range is
            leftSpan = leftMax - leftMin
            rightSpan = rightMax - rightMin

            # Convert the left range into a 0-1 range (float)
            valueScaled = float(value - leftMin) / float(leftSpan)

            # Convert the 0-1 range into a value in the right range.
            return rightMin + (valueScaled * rightSpan)
        self.camera.background_color="#333333"
        pealkiri = Text("Puutesensor", font="Consolas", font_size=50).to_edge(UP)
        mootmisvahemik = Axes(x_length=8, y_length=1.5, x_range=[0, 10, 1], y_range=[0, 4, 1], x_axis_config={"numbers_to_include": [1, 2, 3, 4, 5, 6, 7, 8, 9]}, y_axis_config={"numbers_to_include": [0]}).next_to(pealkiri, DOWN)
        horiz1 = mootmisvahemik.plot(lambda x: 1, color=BLUE, x_range=[0,2])
        vert1 = mootmisvahemik.plot(lambda x: 20*x-39, color=BLUE, x_range=[2,2.099])
        horiz2 = mootmisvahemik.plot(lambda x: 3, color=BLUE, x_range=[2.1,8])
        vert2 = mootmisvahemik.plot(lambda x: -20*x+163, color=BLUE, x_range=[8,8.1])
        horiz3 = mootmisvahemik.plot(lambda x: 1, color=BLUE, x_range=[8.1,10])
        #vahemik = mootmisvahemik.plot_line_graph(x_values=[0, 2, 2.1, 8, 8.1, 10], y_values=[1, 1, 3, 3, 1, 1], line_color=BLUE, add_vertex_dots=False)
        def func0(x):
            if x < 2:
                return 0
            elif x < 2.1:
                return 20*x-39
            elif x < 8:
                return 3
            elif x < 8.1:
                return -20*x+163
            else:
                return 0
        vahemik = mootmisvahemik.plot(func0, color=BLUE, x_range=[0,10])
        viigupinge = Axes(x_length=8, y_length=1.7, x_range=[0, 10, 1], y_range=[0, 4, 1], x_axis_config={"numbers_to_include": [1, 2, 3, 4, 5, 6, 7, 8, 9]}, y_axis_config={"numbers_to_include": [0]}).next_to(mootmisvahemik, DOWN)
        vrefmax = viigupinge.plot(lambda x: 3, color=LIGHT_GRAY, x_range=[0,10], stroke_width=0.5)
        vrefmaxdashed = DashedVMobject(vrefmax, num_dashes=100)
        vrefmin = viigupinge.plot(lambda x: 1, color=LIGHT_GRAY, x_range=[0,10], stroke_width=0.5)
        vrefmindashed = DashedVMobject(vrefmin, num_dashes=100)
        def func1(x):
            if x < 2:
                return 0
            elif x < 3:
                return 3*x-6
            elif x < 4:
                return -2*x+9
            elif x < 5:
                return 2*x-7
            elif x < 6:
                return -2*x+13
            elif x < 7:
                return 2*x-11
            elif x < 8.5:
                return -2*x+17
            else:
                return 0
        trianglewave = viigupinge.plot(func1, color=BLUE, x_range=[0,10])
        horiz4 = viigupinge.plot(lambda x: 0, color=BLUE, x_range=[0,2])
        sl1 = viigupinge.plot(lambda x: 3*x-6, color=BLUE, x_range=[2,3])
        sl2 = viigupinge.plot(lambda x: -2*x+9, color=BLUE, x_range=[3,4])
        sl3 = viigupinge.plot(lambda x: 2*x-7, color=BLUE, x_range=[4,5])
        sl4 = viigupinge.plot(lambda x: -2*x+13, color=BLUE, x_range=[5,6])
        sl5 = viigupinge.plot(lambda x: 2*x-11, color=BLUE, x_range=[6,7])
        sl6 = viigupinge.plot(lambda x: -2*x+17, color=BLUE, x_range=[7,8.5])
        horiz5 = viigupinge.plot(lambda x: 0, color=BLUE, x_range=[8.5,10])
        #triangleWave = viigupinge.plot_line_graph(x_values=[0, 2, 3, 4, 5, 6, 7, 8.5, 10], y_values=[0, 0, 3, 1, 3, 1, 3, 0, 0], line_color=BLUE, add_vertex_dots=False)

        def func2(x):
            if x < 2:
                return 3
            elif x < 3:
                return 0
            elif x < 4:
                return 3
            elif x < 5:
                return 0
            elif x < 6:
                return 3
            elif x < 7:
                return 0
            elif x < 8:
                return 3
            else:
                return 3
        
        valjund = Axes(x_length=8, y_length=1.5, x_range=[0, 10, 1], y_range=[0, 4, 1], x_axis_config={"numbers_to_include": [1, 2, 3, 4, 5, 6, 7, 8, 9]}, y_axis_config={"numbers_to_include": [0]}).next_to(viigupinge, DOWN)
        squarewave = valjund.plot(func2, color=BLUE, x_range=[0,10])
        vert3 = valjund.plot(lambda y: 2, color=BLUE, x_range=[2,2.01])
        #squarewave = valjund.plot_line_graph(x_values=[0, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 10], y_values=[3, 3, 0, 0, 3, 3, 0, 0, 3, 3, 0, 0, 3, 3, 3], line_color=BLUE, add_vertex_dots=False)
        tex = Tex(r"Väljund", tex_template=TexTemplateLibrary.threeb1b).scale(0.5)
        labels1 = mootmisvahemik.get_y_axis_label(Tex("START").scale(0.5), edge=UL, direction=UL, )
        labels2 = viigupinge.get_y_axis_label(Tex("Viigu pinge").scale(0.5), edge=UL, direction=UL)
        labels3 = valjund.get_y_axis_label(tex, edge=UL, direction=UL)
        labels4 = Text("DREFH").scale(0.3).next_to(vrefmaxdashed, LEFT)
        labels5 = Text("DREFL").scale(0.3).next_to(vrefmindashed, LEFT)

        xlabels = mootmisvahemik.get_x_axis_label(Tex("t").scale(0.5), edge=DR)
        xlabels2 = viigupinge.get_x_axis_label(Tex("t").scale(0.5), edge=DR)
        xlabels3 = valjund.get_x_axis_label(Tex("t").scale(0.5), edge=DR)

        self.play(Write(pealkiri))
        self.play(Create(mootmisvahemik), Create(viigupinge), Create(vrefmaxdashed), Create(vrefmindashed),Create(valjund))
        self.play(Create(labels1), Create(labels2), Create(labels3), Create(labels4), Create(labels5))
        self.play(Create(xlabels), Create(xlabels2), Create(xlabels3))
        self.play(Create(vahemik, run_time=4), Create(trianglewave, run_time=4), Create(squarewave, run_time=4))

        
        

        full = SVGMobject("assets\\full.svg").scale(1.5).next_to(viigupinge, RIGHT).shift(RIGHT*0.5)
        empty = SVGMobject("assets\\empty.svg").scale(0.5).next_to(viigupinge, RIGHT)
        self.wait(18)
        
        

        self.play(FadeIn(full))
        for i in range(2):
            area1 = valjund.get_riemann_rectangles(squarewave, x_range=[0, 0], color=RED, fill_opacity=0.5, dx=0.003, stroke_width=0)
            area2 = valjund.get_riemann_rectangles(squarewave, x_range=[0, 0], color=RED, fill_opacity=0.5, dx=0.003, stroke_width=0)
            t=ValueTracker(0)
            self.play(Create(area1))
            area1.add_updater(lambda k: k.become(valjund.get_riemann_rectangles(squarewave, x_range=[2.8, t.get_value()], color=RED, fill_opacity=0.5, dx=0.003, stroke_width=0)) if( t.get_value() > 3 and t.get_value() < 4 and not i is 0) else None)
            area1.remove_updater(lambda k: k.become(valjund.get_riemann_rectangles(squarewave, x_range=[2.8, t.get_value()], color=RED, fill_opacity=0.5, dx=0.003, stroke_width=0)) if( t.get_value() > 3 and t.get_value() < 4 and not i is 0) else None)
            self.play(Create(area2))
            area2.add_updater(lambda f: f.become(valjund.get_riemann_rectangles(squarewave, x_range=[4.8, t.get_value()], color=RED, fill_opacity=0.5, dx=0.003, stroke_width=0)) if( t.get_value() > 5 and t.get_value() < 6 and not i is 0) else None)
            area2.remove_updater(lambda f: f.become(valjund.get_riemann_rectangles(squarewave, x_range=[4.8, t.get_value()], color=RED, fill_opacity=0.5, dx=0.003, stroke_width=0)) if( t.get_value() > 5 and t.get_value() < 6 and not i is 0) else None)

            initalpoint =[viigupinge.coords_to_point(t.get_value(), func1(t.get_value()))]
            dot = Dot(point=initalpoint, color=RED)
            dot.add_updater(lambda l: l.move_to(viigupinge.coords_to_point(t.get_value(), func1(t.get_value()))))
            self.add(dot)
            full[5].add_updater(lambda m: m.set_color(colors[round(translate(func1(t.get_value())))]))
            if i == 0:
                self.play(t.animate.set_value(2), run_time=7-2.3, rate_func=linear)
                self.play(t.animate.set_value(3), run_time=1, rate_func=linear)
                self.play(t.animate.set_value(10), run_time=6, rate_func=linear)
                self.wait(16)
            else:
                self.play(t.animate.set_value(4), run_time=4, rate_func=linear)
                self.play(t.animate.set_value(10), run_time=8, rate_func=linear)
                self.wait(16)
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )
        
        self.wait(2)
