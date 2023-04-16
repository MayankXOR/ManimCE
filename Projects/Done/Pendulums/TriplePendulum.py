#@MayankXOR
#April14th2023
from manim import *
from manim_physics import *


class spacee(SpaceScene, ZoomedScene):
    def construct(self):
        self.camera.frame.shift(DOWN) 
        p = MultiPendulum(UP*2+2*RIGHT, UP*2+RIGHT*(2+(3.87/2))+UP*0.5, UP*2+UP+RIGHT*(2+3.87), bob_style={
            "color": PURPLE,
            "radius": 0.1
        }, rod_style={
            
        })
        self.add(p)
        self.make_rigid_body(p.bobs, friction=0)
        p.start_swinging()
        self.add(TracedPath(p.bobs[-1].get_center, stroke_color=BLUE, dissipating_time=0.5))
        self.add(TracedPath(p.bobs[-2].get_center, stroke_color=RED, dissipating_time=0.5))
        self.add(TracedPath(p.bobs[-3].get_center, stroke_color=GREEN, dissipating_time=0.5))
        self.wait(600)
