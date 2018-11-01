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

cylinder {< -7.31,  -6.80, -13.19>, < -6.39,   0.65,  -6.23>, Rcell pigment {Black}}
cylinder {<  0.81,  -6.60,  -6.95>, <  1.73,   0.85,   0.01>, Rcell pigment {Black}}
cylinder {<  7.97,   0.62,  -8.11>, <  8.90,   8.07,  -1.15>, Rcell pigment {Black}}
cylinder {< -0.15,   0.42, -14.34>, <  0.78,   7.87,  -7.38>, Rcell pigment {Black}}
cylinder {< -7.31,  -6.80, -13.19>, <  0.81,  -6.60,  -6.95>, Rcell pigment {Black}}
cylinder {< -6.39,   0.65,  -6.23>, <  1.73,   0.85,   0.01>, Rcell pigment {Black}}
cylinder {<  0.78,   7.87,  -7.38>, <  8.90,   8.07,  -1.15>, Rcell pigment {Black}}
cylinder {< -0.15,   0.42, -14.34>, <  7.97,   0.62,  -8.11>, Rcell pigment {Black}}
cylinder {< -7.31,  -6.80, -13.19>, < -0.15,   0.42, -14.34>, Rcell pigment {Black}}
cylinder {< -6.39,   0.65,  -6.23>, <  0.78,   7.87,  -7.38>, Rcell pigment {Black}}
cylinder {<  1.73,   0.85,   0.01>, <  8.90,   8.07,  -1.15>, Rcell pigment {Black}}
cylinder {<  0.81,  -6.60,  -6.95>, <  7.97,   0.62,  -8.11>, Rcell pigment {Black}}
atom(< -5.52,  -5.00, -13.48>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #0 
atom(< -3.73,  -3.19, -13.77>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #1 
atom(< -1.94,  -1.39, -14.05>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #2 
atom(< -5.28,  -6.75, -11.63>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #3 
atom(< -3.49,  -4.95, -11.92>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #4 
atom(< -1.70,  -3.14, -12.21>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #5 
atom(<  0.09,  -1.34, -12.49>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #6 
atom(< -3.25,  -6.70, -10.07>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #7 
atom(< -1.46,  -4.90, -10.36>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #8 
atom(<  0.33,  -3.09, -10.65>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #9 
atom(<  2.12,  -1.29, -10.94>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #10 
atom(< -1.22,  -6.65,  -8.51>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #11 
atom(<  0.57,  -4.85,  -8.80>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #12 
atom(<  2.36,  -3.04,  -9.09>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #13 
atom(<  4.15,  -1.24,  -9.38>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #14 
atom(< -7.08,  -4.94, -11.45>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #15 
atom(< -5.29,  -3.14, -11.74>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #16 
atom(< -3.50,  -1.33, -12.03>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #17 
atom(< -1.71,   0.48, -12.31>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #18 
atom(< -5.05,  -4.89,  -9.89>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #19 
atom(< -3.26,  -3.08, -10.18>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #20 
atom(< -1.47,  -1.28, -10.47>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #21 
atom(<  0.32,   0.53, -10.75>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #22 
atom(< -3.02,  -4.84,  -8.33>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #23 
atom(< -1.23,  -3.03,  -8.62>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #24 
atom(<  0.56,  -1.23,  -8.91>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #25 
atom(<  2.35,   0.58,  -9.20>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #26 
atom(< -0.99,  -4.79,  -6.77>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #27 
atom(<  0.80,  -2.98,  -7.06>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #28 
atom(<  2.59,  -1.18,  -7.35>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #29 
atom(<  4.38,   0.63,  -7.64>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #30 
atom(< -6.85,  -3.08,  -9.71>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #31 
atom(< -5.06,  -1.27, -10.00>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #32 
atom(< -3.27,   0.53, -10.29>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #33 
atom(< -1.47,   2.34, -10.57>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #34 
atom(< -4.82,  -3.03,  -8.15>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #35 
atom(< -3.03,  -1.22,  -8.44>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #36 
atom(< -1.24,   0.58,  -8.73>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #37 
atom(<  0.55,   2.39,  -9.02>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #38 
atom(< -2.79,  -2.98,  -6.59>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #39 
atom(< -1.00,  -1.17,  -6.88>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #40 
atom(<  0.79,   0.63,  -7.17>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #41 
atom(<  2.58,   2.44,  -7.46>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #42 
atom(< -0.76,  -2.93,  -5.03>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #43 
atom(<  1.03,  -1.12,  -5.32>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #44 
atom(<  2.82,   0.69,  -5.61>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #45 
atom(<  4.61,   2.49,  -5.90>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #46 
atom(< -6.62,  -1.21,  -7.97>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #47 
atom(< -4.83,   0.59,  -8.26>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #48 
atom(< -3.03,   2.40,  -8.55>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #49 
atom(< -1.24,   4.20,  -8.83>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #50 
atom(< -4.59,  -1.16,  -6.41>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #51 
atom(< -2.80,   0.64,  -6.70>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #52 
atom(< -1.01,   2.45,  -6.99>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #53 
atom(<  0.79,   4.25,  -7.28>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #54 
atom(< -2.56,  -1.11,  -4.85>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #55 
atom(< -0.77,   0.69,  -5.14>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #56 
atom(<  1.02,   2.50,  -5.43>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #57 
atom(<  2.82,   4.30,  -5.72>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #58 
atom(< -0.53,  -1.06,  -3.29>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #59 
atom(<  1.26,   0.74,  -3.58>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #60 
atom(<  3.05,   2.55,  -3.87>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #61 
atom(<  4.84,   4.35,  -4.16>, 1.17, rgb <0.78, 0.50, 0.20>, 0.0, ase2) // #62 
