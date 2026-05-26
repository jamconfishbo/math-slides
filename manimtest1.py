from manim import *
from manim_slides import Slide

class FactoringPresentation(Slide):
    def construct(self):
        # --- COLOR DEFINITIONS ---
        X_COLOR = "#228B22"       # Dark Green (Forest Green)
        MAGIC_COLOR = "#FF8C00"   # Dark Orange

        # --- TITLE SYSTEM ---
        title = Text("Factoring Quadratics", color=BLUE).to_edge(UP, buff=0.4)
        self.play(Write(title))
        
        # Create a vertical dividing line down the middle
        divider = Line(UP * 2, DOWN * 3, color=GRAY_C, stroke_width=2)
        self.play(Create(divider))
        self.wait()
        self.next_slide()

        # --- LEFT SIDE ANCHOR POSITION ---
        text_position = LEFT * 3.5 + UP * 0.5

        # --- STEP 1: THE PROBLEM ---
        inst_1 = MarkupText(
            "<b>The Challenge:</b>\nFactor the given quadratic\nexpression completely.",
            font_size=22
        ).move_to(text_position)
        
        eq_1 = MathTex("6", "x", "^2", "+", "7", "x", "+ 2").move_to(RIGHT * 3 + UP * 1.5)
        eq_1[1].set_color(X_COLOR)     
        eq_1[2].set_color(WHITE)       
        eq_1[4].set_color(MAGIC_COLOR) 
        eq_1[5].set_color(X_COLOR)     
        
        self.play(FadeIn(inst_1), Write(eq_1))
        self.next_slide()

        # --- STEP 2: AC METHOD ---
        inst_2 = MarkupText(
            "<b>Step 1: AC Method</b>\nFind two numbers that\nmultiply to <i>a × c</i> (12)\nand add to <i>b</i> (7).\n\nMagic numbers: <span color='#FF8C00'>3</span> and <span color='#FF8C00'>4</span>.",
            font_size=20
        ).move_to(text_position)
        
        self.play(FadeOut(inst_1), FadeIn(inst_2))
        self.next_slide()

        # --- STEP 3: SPLIT THE MIDDLE TERM ---
        inst_3 = MarkupText(
            "<b>Step 2: Rewrite</b>\nSplit the middle term (7x)\nusing our magic numbers\n3 and 4.",
            font_size=20
        ).move_to(text_position)
        
        eq_2 = MathTex("= 6", "x", "^2", "+", "3", "x", "+", "4", "x", "+ 2")
        eq_2.next_to(eq_1, DOWN, buff=0.4, aligned_edge=LEFT)

        eq_2[1].set_color(X_COLOR)     
        eq_2[2].set_color(WHITE)       
        eq_2[4].set_color(MAGIC_COLOR) 
        eq_2[5].set_color(X_COLOR)     
        eq_2[7].set_color(MAGIC_COLOR) 
        eq_2[8].set_color(X_COLOR)     
        
        self.play(FadeOut(inst_2), FadeIn(inst_3))
        self.play(Write(eq_2))
        self.next_slide()

        # --- STEP 4: GROUPING (Replaces Equation 2) ---
        inst_4 = MarkupText(
            "<b>Step 3: Grouping</b>\nGroup the first two terms\nand the last two terms.",
            font_size=20
        ).move_to(text_position)
        
        # CHANGED: eq_3 now targets eq_1 as its positioning anchor instead of eq_2
        eq_3 = MathTex("= (6", "x", "^2", "+", "3", "x", ") + (", "4", "x", "+ 2)")
        eq_3.next_to(eq_1, DOWN, buff=0.4, aligned_edge=LEFT)

        eq_3[1].set_color(X_COLOR)     
        eq_3[2].set_color(WHITE)       
        eq_3[4].set_color(MAGIC_COLOR) 
        eq_3[5].set_color(X_COLOR)     
        eq_3[7].set_color(MAGIC_COLOR) 
        eq_3[8].set_color(X_COLOR)     
        
        self.play(FadeOut(inst_3), FadeIn(inst_4))
        # CHANGED: Added FadeOut(eq_2) alongside the layout introduction of eq_3
        self.play(FadeOut(eq_2), FadeIn(eq_3)) 
        self.next_slide()

        # --- STEP 5: FACTOR GCF ---
        inst_5 = MarkupText(
            "<b>Step 4: Factor GCF</b>\nExtract the Greatest Common\nFactor from each binomial group.\nNotice the orange colors disappear.",
            font_size=20
        ).move_to(text_position)
        
        eq_4 = MathTex("= 3", "x", "(2", "x", "+ 1) + 2(2", "x", "+ 1)")
        # CHANGED: Anchor is now eq_3, which behaves correctly since eq_3 took eq_2's layout coordinates
        eq_4.next_to(eq_3, DOWN, buff=0.4, aligned_edge=LEFT)
        eq_4[1].set_color(X_COLOR)
        eq_4[3].set_color(X_COLOR)
        eq_4[5].set_color(X_COLOR)
        
        self.play(FadeOut(inst_4), FadeIn(inst_5))
        self.play(Write(eq_4))
        self.next_slide()

        # --- STEP 6: FINAL SOLUTION ---
        inst_6 = MarkupText(
            "<b>Step 5: Final Product</b>\nFactor out the common\nbinomial block (2x + 1)\nto get your final answer.",
            font_size=20
        ).move_to(text_position)
        
        eq_5 = MathTex("= (2", "x", "+ 1)(3", "x", "+ 2)", color=GOLD)
        eq_5.next_to(eq_4, DOWN, buff=0.4, aligned_edge=LEFT)
        eq_5[1].set_color(X_COLOR)
        eq_5[3].set_color(X_COLOR)
        
        self.play(FadeOut(inst_5), FadeIn(inst_6))
        self.play(Write(eq_5))
        self.wait()