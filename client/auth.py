import streamlit as st
import requests
from bs4 import BeautifulSoup
import webbrowser
class Authentication:
    def init_session():
        if 'isLogged' not in st.session_state:
            st.session_state.isLogged=False
    def login():
        payload = {'LoginForm[username]': '', 
                        'LoginForm[password]': ''
        }
        userData={
            'isLoggedIn':False,
            'username':'',
            'name':'',
            'gender':'',
            'department_id':''
        }
        Authentication.init_session()
        st.header("Sargam Chitram Thalam")
        container = st.container(border=True)
        container.subheader("Login with Etlab")
        with container.form("Login",border=False):
            username = st.text_input("Etlab username")
            password = st.text_input("Etlab password",type='password')
            submit = st.form_submit_button("Login")
            if submit:
                st.balloons()
                payload['LoginForm[username]']=username
                payload['LoginForm[password]']=password
                userSession = requests.session()
                userSession.post(url='https://sctce.etlab.in/user/login',
                                        data=payload
                                        )
                html=BeautifulSoup(userSession.get('https://sctce.etlab.in/student/profile').content,'html.parser')
                try:
                    name_tag=html.find('th',text='Name')
                    gender_tag=html.find('th',text='Gender')
                    university_id = html.find('th',text='University Reg No')
                    userData['isLoggedIn']=True
                    userData['username']=username
                    userData['password']=password
                    userData['name'] = name_tag.find_next('td').text
                    userData['gender'] = gender_tag.find_next('td').text
                    userData['department_id'] = university_id.find_next('td').text
                    st.session_state.isLogged=True
                except AttributeError:
                    userData['isLoggedIn']=False
                

        if userData['isLoggedIn']==True:
               apiSession = requests.session()
               getTokenData=apiSession.post(url='http://sstapi.pythonanywhere.com/accounts/api/signup/',
                               data=userData
                               )
               apiSession.post(url="http://sstsite.vercel.app/api/token",
                               data=getTokenData.json()
                               )
            