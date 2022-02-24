import numpy as np
from PIL import Image
import streamlit as st
from datetime import date
import plotly.graph_objects as go

#Ideas:
#1. add a Did you know section(show facts and stats)
#2. Add event schedule

def about_us():
    students = [
        {'name' : 's1', 'pic' : 'test-img.jpg'},
        {'name' : 's2', 'pic' : 'test-img.jpg'},
        {'name' : 's3', 'pic' : 'test-img.jpg'},
        {'name' : 's4', 'pic' : 'test-img.jpg'},
        {'name' : 's5', 'pic' : 'test-img.jpg'},
        {'name' : 's6', 'pic' : 'test-img.jpg'},
        {'name' : 's7', 'pic' : 'test-img.jpg'},
        {'name' : 's8', 'pic' : 'test-img.jpg'},
    ]

    lecturer = {'name' : 'Ms. Jehan', 'pic' : 'test-img.jpg'}
    #st.write(students[1]['name'])
    st.image(image=Image.open('UOW.jpg'),width=700)
    st.title("Hello! We Are Encanto!")
    st.write("We are students from UOW Malaysia KDU Glenmarie undertaking a subject called Global Social Responsibility")


    col = st.columns((1,1,1,1))
    next_row = 0
    for idx, i in enumerate(students):
        if next_row == 4:
            next_row = 0

        col[next_row].image(image=Image.open(students[idx]['pic']), width=125, caption='STUDENT')
        col[next_row].write(students[idx]['name'])
        next_row+=1

    col2 = st.columns((1,1,1,1))
    col2[0].image(image=Image.open(lecturer['pic']), width=175, caption='LECTURER')
    col2[0].write(lecturer['name'])

# def posters():
#     st.write("Poster 1")
#     st.write("Poster 2")

def event_overview():
    d0 = date.today()
    #d0 = today.strftime("%d/%m/%Y")
    d1 = date(2022, 4, 8)
    delta = d1 - d0
    st.title('Event Name: ')
    st.title('Event Date: 08/4/2022')
    st.title(str(f"{delta.days} days until the event!"))
    st.image(image=Image.open('event.jpg'))
    st.title('Event Objective: ')

    st.title("The event will be conducted on zoom")
    st.title("Link: not ready")

def event_schedule():
    st.title('Event schedule here')

def ngo():
    st.title("Our selected NGO")
    st.title('link to their website')
    st.title('other social medias')

def didyouknow():
    #st.write('testtesttesttesttesttesttesttesttesttesttesttesttesttesttest')
    fig = stats(np.arange(1,100),np.arange(1,100))
    #st.caption('Line graph')
    fig = stats(np.arange(100,1000),np.arange(5000,50000))
    fig = stats(np.arange(1,100),np.arange(1,100))

def stats(x,y):
    fig = go.Figure(data=go.Scatter(x=x, y=y))
    return st.plotly_chart(fig)


def main():
    sel_list = {
        'Event Overview' : event_overview,
        'Event Schedule' : event_schedule,
        'Our NGO' : ngo,
        'Did You Know?' : didyouknow,
        'About Us' : about_us,

                }
    sel = st.sidebar.radio("", list(sel_list.keys()))
    sel_list[sel]()


if __name__ == "__main__":
    main()
    #didyouknow()
