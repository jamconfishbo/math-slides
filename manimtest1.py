from manim import *
from manim_slides import Slide

class FactoringPresentation(Slide):
    def construct(self):
        # 1. Title and Problem Introduction
        title = Text("Factoring Quadratics", color=BLUE).to_edge(UP)
        equation = MathTex("6x^2", "+7x", "+2").next_to(title, DOWN, buff=0.5)
        
        self.play(Write(title))
        self.play(Write(equation))
        self.wait()
        
        # Pause and wait for user input (click/keypress) to move to the next slide
        self.next_slide() 

        # 2. The AC Method Explanation
        ac_text = MarkupText(
            "<b>Step 1: AC Method</b>\nFind two numbers that multiply to <span color='green'>a × c</span> and add to <span color='yellow'>b</span>.",
            font_size=24
        ).to_edge(LEFT, buff=1).shift(UP*0.5)
        
        ac_calc = MathTex(
            "a \\times c = 6 \\times 2 = 12", 
            "\\quad b = 7"
        ).scale(0.8).next_to(ac_text, DOWN, aligned_edge=LEFT)
        
        self.play(FadeIn(ac_text))
        self.play(Write(ac_calc))
        self.next_slide()

        # 3. Finding the Factors
        factors_text = MarkupText(
            "The magic numbers are <b>3</b> and <b>4</b>:\n3 × 4 = 12\n3 + 4 = 7", 
            font_size=24, color=GREEN
        ).next_to(ac_calc, DOWN, aligned_edge=LEFT, buff=0.5)
        
        self.play(Write(factors_text))
        self.next_slide()

        # 4. Splitting the Middle Term
        split_equation = MathTex("6x^2", "+3x", "+4x", "+2").next_to(title, DOWN, buff=0.5)
        
        # Transform the original 7x into 3x + 4x
        self.play(
            TransformMatchingTex(equation, split_equation),
            FadeOut(ac_text, ac_calc, factors_text)
        )
        self.next_slide()

        # 5. Grouping and Factoring
        group_text = MarkupText(
            "<b>Step 2: Factor by Grouping</b>\nGroup the first two and last two terms.",
            font_size=24
        ).to_edge(LEFT, buff=1)
        
        grouped_eq = MathTex("(6x^2 + 3x)", "+", "(4x + 2)").next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(group_text), TransformMatchingTex(split_equation, grouped_eq))
        self.next_slide()

        # Factor out GCF from both groups
        gcf_eq = MathTex("3x(2x + 1)", "+", "2(2x + 1)").next_to(title, DOWN, buff=0.5)
        self.play(TransformMatchingTex(grouped_eq, gcf_eq))
        self.next_slide()

        # 6. Final Solution
        final_text = MarkupText("<b>Final Factored Form!</b>", font_size=28, color=GOLD).to_edge(LEFT, buff=1)
        final_eq = MathTex("(2x + 1)(3x + 2)").scale(1.2).next_to(title, DOWN, buff=0.5).set_color(GOLD)
        
        self.play(
            FadeTransform(group_text, final_text),
            TransformMatchingTex(gcf_eq, final_eq)
        )
        self.wait()