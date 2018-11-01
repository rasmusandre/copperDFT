#include "colors.inc"
#include "finish.inc"

global_settings {assumed_gamma 1 max_trace_level 6}
background {color White}
camera {orthographic
  right -20.35*x up 21.03*y
  direction 1.00*z
  location <0,0,50.00> look_at <0,0,0>}
light_source {<  2.00,   3.00,  40.00> color White
  area_light <0.70, 0, 0>, <0, 0.70, 0>, 3, 3
  adaptive 1 jitter}

#declare simple = finish {phong 0.7}
#declare pale = finish {ambient .5 diffuse .85 roughness .001 specular 0.200 }
#declare intermediate = finish {ambient 0.3 diffuse 0.6 specular 0.10 roughness 0.04 }
#declare vmd = finish {ambient .0 diffuse .65 phong 0.1 phong_size 40. specular 0.500 }
#declare jmol = finish {ambient .2 diffuse .6 specular 1 roughness .001 metallic}
#declare ase2 = finish {ambient 0.05 brilliance 3 diffuse 0.6 metallic specular 0.70 roughness 0.04 reflection 0.15}
#declare ase3 = finish {ambient .15 brilliance 2 diffuse .6 metallic specular 1. roughness .001 reflection .0}
#declare glass = finish {ambient .05 diffuse .3 specular 1. roughness .001}
#declare glass2 = finish {ambient .0 diffuse .3 specular 1. reflection .25 roughness .001}
#declare Rcell = 0.070;
#declare Rbond = 0.100;

#macro atom(LOC, R, COL, TRANS, FIN)
  sphere{LOC, R texture{pigment{color COL transmit TRANS} finish{FIN}}}
#end
#macro constrain(LOC, R, COL, TRANS FIN)
union{torus{R, Rcell rotate 45*z texture{pigment{color COL transmit TRANS} finish{FIN}}}
      torus{R, Rcell rotate -45*z texture{pigment{color COL transmit TRANS} finish{FIN}}}
      translate LOC}
#end

cylinder {< -6.65,  -6.65, -14.48>, <  0.59,   0.59, -14.48>, Rcell pigment {Black}}
cylinder {< -6.65,   0.59,  -7.24>, <  0.59,   7.83,  -7.24>, Rcell pigment {Black}}
cylinder {<  0.59,   0.59,   0.00>, <  7.83,   7.83,   0.00>, Rcell pigment {Black}}
cylinder {<  0.59,  -6.65,  -7.24>, <  7.83,   0.59,  -7.24>, Rcell pigment {Black}}
cylinder {< -6.65,  -6.65, -14.48>, < -6.65,   0.59,  -7.24>, Rcell pigment {Black}}
cylinder {<  0.59,   0.59, -14.48>, <  0.59,   7.83,  -7.24>, Rcell pigment {Black}}
cylinder {<  7.83,   0.59,  -7.24>, <  7.83,   7.83,   0.00>, Rcell pigment {Black}}
cylinder {<  0.59,  -6.65,  -7.24>, <  0.59,   0.59,   0.00>, Rcell pigment {Black}}
cylinder {< -6.65,  -6.65, -14.48>, <  0.59,  -6.65,  -7.24>, Rcell pigment {Black}}
cylinder {<  0.59,   0.59, -14.48>, <  7.83,   0.59,  -7.24>, Rcell pigment {Black}}
cylinder {<  0.59,   7.83,  -7.24>, <  7.83,   7.83,   0.00>, Rcell pigment {Black}}
cylinder {< -6.65,   0.59,  -7.24>, <  0.59,   0.59,   0.00>, Rcell pigment {Black}}
atom(< -6.65,  -6.65, -14.48>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #0 
atom(< -4.84,  -6.65, -12.67>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #1 
atom(< -3.03,  -6.65, -10.86>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #2 
atom(< -1.22,  -6.65,  -9.05>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #3 
atom(< -6.65,  -4.84, -12.67>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #4 
atom(< -4.84,  -4.84, -10.86>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #5 
atom(< -3.03,  -4.84,  -9.05>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #6 
atom(< -1.22,  -4.84,  -7.24>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #7 
atom(< -6.65,  -3.03, -10.86>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #8 
atom(< -4.84,  -3.03,  -9.05>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #9 
atom(< -3.03,  -3.03,  -7.24>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #10 
atom(< -1.22,  -3.03,  -5.43>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #11 
atom(< -6.65,  -1.22,  -9.05>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #12 
atom(< -4.84,  -1.22,  -7.24>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #13 
atom(< -3.03,  -1.22,  -5.43>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #14 
atom(< -1.22,  -1.22,  -3.62>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #15 
atom(< -4.84,  -4.84, -14.48>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #16 
atom(< -3.03,  -4.84, -12.67>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #17 
atom(< -1.22,  -4.84, -10.86>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #18 
atom(<  0.59,  -4.84,  -9.05>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #19 
atom(< -4.84,  -3.03, -12.67>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #20 
atom(< -3.03,  -3.03, -10.86>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #21 
atom(< -1.22,  -3.03,  -9.05>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #22 
atom(<  0.59,  -3.03,  -7.24>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #23 
atom(< -4.84,  -1.22, -10.86>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #24 
atom(< -3.03,  -1.22,  -9.05>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #25 
atom(< -1.22,  -1.22,  -7.24>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #26 
atom(<  0.59,  -1.22,  -5.43>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #27 
atom(< -4.84,   0.59,  -9.05>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #28 
atom(< -3.03,   0.59,  -7.24>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #29 
atom(< -1.22,   0.59,  -5.43>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #30 
atom(<  0.59,   0.59,  -3.62>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #31 
atom(< -3.03,  -3.03, -14.48>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #32 
atom(< -1.22,  -3.03, -12.67>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #33 
atom(<  0.59,  -3.03, -10.86>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #34 
atom(<  2.40,  -3.03,  -9.05>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #35 
atom(< -3.03,  -1.22, -12.67>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #36 
atom(< -1.22,  -1.22, -10.86>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #37 
atom(<  0.59,  -1.22,  -9.05>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #38 
atom(<  2.40,  -1.22,  -7.24>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #39 
atom(< -3.03,   0.59, -10.86>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #40 
atom(< -1.22,   0.59,  -9.05>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #41 
atom(<  0.59,   0.59,  -7.24>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #42 
atom(<  2.40,   0.59,  -5.43>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #43 
atom(< -3.03,   2.40,  -9.05>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #44 
atom(< -1.22,   2.40,  -7.24>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #45 
atom(<  0.59,   2.40,  -5.43>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #46 
atom(<  2.40,   2.40,  -3.62>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #47 
atom(< -1.22,  -1.22, -14.48>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #48 
atom(<  0.59,  -1.22, -12.67>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #49 
atom(<  2.40,  -1.22, -10.86>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #50 
atom(<  4.21,  -1.22,  -9.05>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #51 
atom(< -1.22,   0.59, -12.67>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #52 
atom(<  0.59,   0.59, -10.86>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #53 
atom(<  2.40,   0.59,  -9.05>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #54 
atom(<  4.21,   0.59,  -7.24>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #55 
atom(< -1.22,   2.40, -10.86>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #56 
atom(<  0.59,   2.40,  -9.05>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #57 
atom(<  2.40,   2.40,  -7.24>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #58 
atom(<  4.21,   2.40,  -5.43>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #59 
atom(< -1.22,   4.21,  -9.05>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #60 
atom(<  0.59,   4.21,  -7.24>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #61 
atom(<  2.40,   4.21,  -5.43>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #62 
atom(<  4.21,   4.21,  -3.62>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #63 
