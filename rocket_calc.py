import math
from tabnanny import check
import streamlit as st
st.title("Rocket Physics Calculator 🚀")
st.header('Center Of Gravity Calculations')
nose_w= st.number_input('Enter the weight of the nose in grams (G): ' )
Body_w= st.number_input('Enter the weight of the body in grams (G): ' )
battery_w= st.number_input('Enter the weight of the battery in grams(G): ' )
motor_w= st.number_input('Enter the weight of the motor in grams (G): ' )
nose_x = st.number_input("Enter distance from tip to nose cone center (cm): ")
battery_x = st.number_input("Enter distance from tip to battery center (cm): ")
motor_x = st.number_input("Enter distance from tip to motor center (cm): ")
body_x = st.number_input("Enter distance from tip to body center (cm): ")
total_weightG = nose_w + Body_w + battery_w + motor_w
Center_of_Gravity = 0.0
if total_weightG>0:
 Center_of_Gravity = ((nose_w * nose_x) + (Body_w * body_x) + (battery_w * battery_x) + (motor_w * motor_x)) / total_weightG
 st.write(f'The CG of this rocket {Center_of_Gravity:.2f}: ')
 st.write(f' The total weight of this rocket is {total_weightG:.2f} ')
else:
 st.write('please enter values')
SQ=st.radio('would you like to find your CP?' , ['No','Yes'])
if SQ== 'Yes':
 st.header('Center Of Pressure Calculations')
 length=st.number_input('what is the length of nose cone ')
 Shape=st.radio('Select Nose Cone Shape',['Conical','ogive','parabolic','Elliptical'])
 if Shape=='ogive':
  x_n=length *  0.467
 elif Shape =='Conical':
  x_n=(2/3)*length
 elif Shape == 'parabolic':
  x_n=0.500*length
 elif Shape == 'Elliptical':
  x_n=(1/3)*length
 D= st.number_input('diameter of Rocket body ' )
 S=st.number_input('what is the fin span in cm ' )
 root=st.number_input('the length of the fin where it attaches to the body ' )
 tip=st.number_input('the length of the flat outer edge of the fin ')
 front_sweep=st.number_input('Distance from the front of the root to the front of the tip along the body: ')
 F= st.number_input('number of fins ' )
 X_b = st.number_input("Distance from nose tip to the FRONT edge of the fin root: ")
 if D > 0 and root > 0 and tip > 0 and S > 0 and F > 0:
  R = D / 2
  mid = front_sweep + (tip / 2) - (root / 2)
  K = 1 + (R / (R + S))
  numerator = 4 * F * ((S / D) ** 2)
  denominator = 1 + math.sqrt(1 + (2 * mid / (root + tip)) ** 2)
  Cn_f = K * (numerator / denominator)

  line_1 = (mid * (root + 2 * tip)) / (3 * (root + tip))
  line_2 = (1 / 3) * ((root + tip) - ((root * tip) / (root + tip)))
  X_f = X_b + (line_1 - line_2)
  Cn_f = K * (numerator / denominator)
  cn_n=2
  Center_of_pressure=((cn_n*x_n)+(Cn_f*X_f))/(cn_n+Cn_f)
  st.write(f'The CP of this rocket {Center_of_pressure:.2f}')
  static_margin = (Center_of_pressure - Center_of_Gravity) / D
  if 1>static_margin:
   st.write('the rocket is unstable margin is to small This rocket will not push against the wind ')
  elif 1<=static_margin<=2:
   st.write('the rocket is stable margin Your rocket will push back normally ')
  elif 2<=static_margin:
   st.write('This rocket is to stable Rocket will Over Correct')

elif SQ== 'No':
 st.write('HAVE AN AMAZING DAYYYYYYYY!!!!!!!!!!!!!!!!!!!!')
