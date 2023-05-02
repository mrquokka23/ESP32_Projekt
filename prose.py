from manim import *

import numpy as np

class ESP_prose(Scene):
    def construct(self):
        self.camera.background_color="#333333"
        prose = ImageMobject("assets\\Screenshot 2023-04-25 141657.jpg").shift(LEFT*3)
        text1 = Text("• ESP32-D0WDQ6 protsessor", font="Consolas", font_size=30)
        text2 = Text("• 448 KB ROM Mälu", font="Consolas", font_size=30).next_to(text1, DOWN)
        text3 = Text("• 520 KB SRAM Mälu", font="Consolas", font_size=30).next_to(text2, DOWN)
        text4 = Text("• RTC - 8KB kiiret mälu", font="Consolas", font_size=30).next_to(text3, DOWN)
        text5 = Text("• RTC - 8KB aeglast mälu", font="Consolas", font_size=30).next_to(text4, DOWN)
        text6 = Text("• 1Kbit eFuse mälu", font="Consolas", font_size=30).next_to(text5, DOWN)
        group = VGroup(text1, text2, text3, text4, text5, text6).shift(RIGHT*1).next_to(prose, RIGHT).arrange(DOWN, center=False, aligned_edge=LEFT)  

        gpio = Text("• GPIO", font="Consolas", font_size=30)
        adc = Text("• ADC", font="Consolas", font_size=30).next_to(gpio, DOWN)
        dac = Text("• DAC", font="Consolas", font_size=30).next_to(adc, DOWN)
        sdio = Text("• SDIO", font="Consolas", font_size=30).next_to(dac, DOWN)
        twai = Text("• TWAI", font="Consolas", font_size=30).next_to(sdio, DOWN)
        rmt = Text("• RMT", font="Consolas", font_size=30).next_to(twai, DOWN)
        pwm = Text("• PWM", font="Consolas", font_size=30).next_to(rmt, DOWN)
        tim = Text("• Timerid", font="Consolas", font_size=30).next_to(pwm, DOWN)
        eth = Text("• Ethernet", font="Consolas", font_size=30).next_to(tim, DOWN)
        spi = Text("• SPI", font="Consolas", font_size=30).next_to(eth, DOWN)
        uart = Text("• UART", font="Consolas", font_size=30).next_to(spi, DOWN)
        i2s = Text("• I2S", font="Consolas", font_size=30).next_to(uart, DOWN)
        i2c = Text("• I2C", font="Consolas", font_size=30).next_to(i2s, DOWN)
        touch = Text("• Mahtuvulik puuteandur", font="Consolas", font_size=30).next_to(i2c, DOWN)
        wifibt = Text("• WiFi ja Bluetooth", font="Consolas", font_size=30).next_to(touch, DOWN)
        
        group2 = VGroup(gpio, adc, dac, sdio, twai, rmt, pwm, tim).next_to(prose, RIGHT).shift(LEFT*0.5).arrange(DOWN, center=False, aligned_edge=LEFT)
        group3 = VGroup(eth, spi, uart, i2s, i2c, touch, wifibt).next_to(group2, RIGHT).shift(LEFT*1.5).arrange(DOWN, center=False, aligned_edge=LEFT)

        krypto = Text("• Kriptograafia kiirendi", font="Consolas", font_size=30)
        sha = Text("    • SHA", font="Consolas", font_size=30).next_to(krypto, DOWN)
        rsa = Text("    • RSA", font="Consolas", font_size=30).next_to(sha, DOWN)
        aes = Text("    • AES", font="Consolas", font_size=30).next_to(rsa, DOWN)
        rng = Text("• Juhusliku numbri generaator", font="Consolas", font_size=30).next_to(aes, DOWN)
        group4 = VGroup(krypto, sha, rsa, aes, rng).next_to(prose, RIGHT).arrange(DOWN, center=False, aligned_edge=LEFT)


        self.add(prose)
        self.play(prose.animate.shift(LEFT*1.5))
        self.play(prose.animate.scale(1.5))
        self.play(Write(text1))
        self.play(Write(text2))
        self.play(Write(text3))
        self.play(Write(text4))
        self.play(Write(text5))
        self.play(Write(text6))
        self.wait(2)
        self.play(FadeOut(group, shift=LEFT*3))	
        self.play(Write(gpio, run_time=0.5))
        self.play(Write(adc, run_time=0.5))
        self.play(Write(dac, run_time=0.5))
        self.play(Write(sdio, run_time=0.5))
        self.play(Write(twai, run_time=0.5))
        self.play(Write(rmt, run_time=0.5))
        self.play(Write(pwm, run_time=0.5))
        self.play(Write(tim, run_time=0.5))
        self.play(Write(eth, run_time=0.5))
        self.play(Write(spi, run_time=0.5))
        self.play(Write(uart, run_time=0.5))
        self.play(Write(i2s, run_time=0.5))
        self.play(Write(i2c, run_time=0.5))
        self.play(Write(touch, run_time=0.5))
        self.play(Write(wifibt, run_time=0.5))
        self.wait(2)
        self.play(FadeOut(group2, shift=LEFT*3), FadeOut(group3, shift=LEFT*3))
        self.play(Write(krypto, run_time=0.5))
        self.play(Write(sha, run_time=0.5))
        self.play(Write(rsa, run_time=0.5))
        self.play(Write(aes, run_time=0.5))
        self.play(Write(rng, run_time=0.5))
        self.wait(2)
        self.play(FadeOut(group4, shift=LEFT*3), FadeOut(prose, shift=LEFT*3))
        self.wait(2)
        	
       
