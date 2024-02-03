import streamlit as st 
from client.auth import Authentication
from client.dash import Dashboard
class App:
    def run():
        Authentication.login()
if __name__=="__main__":
    app =App
    app.run()