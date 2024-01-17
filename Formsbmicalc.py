import streamlit as st

st.title('#BMI Calculator: ')

with st.form('BMI Calculator'):
	col1, col2, col3 = st.columns ([2,2,1])

with col1:
	weight = st.number_input('Enter your age in KGs')

with col2:
	height = st.number_input('Enter your height in m')

with col3:
	submit = st.form_submit_button('Calculate')

if submit :
	BMI = (weight)/(height*height)
	st.write('Your BMI is: ',BMI)

	if(BMI<=18.5):
		st.error('You are under-weight')
	elif(BMI>18.5 and BMI<=24.5):
		st.success('You are perfectly normal')
	elif(BMI>24.5 and BMI<=29):
		st.warning('You are obese')
	elif(BMI>29):
		st.error('You are Over Obese')



