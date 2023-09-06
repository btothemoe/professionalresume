import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import altair as alt



st.set_page_config(
    page_title="Bryan Moore Resume",
)

st.markdown("""
<style>
.big-font {
    font-size:60px !important;
    font-weight: bold !important;
    padding: 0px !important;
    margin: 0px !important;
    margin-top: -25px !important;
}

.medium-font {
    font-size: 18px;
    color: #D3D3D3;
    padding: 0px !important;
    margin: 0px !important;
    margin-top: 15px !important;
    margin-left: 3px !important;
    margin-bottom: 20px !important;
    line-height: 125%;
}
            
.links {
    text-align: center;
}
            
.left-link {
    text-align: left;
}
            
.right-link {
    text-align: right;
}
            
a {
    text-decoration: none !important;
    color: white !important;
    font-size: 17px;
}
            
a:hover {
    color: orange !important;
}
            
hr {
    margin-top: 5px !important;
    margin-bottom: 5px !important;
}
            

.techstack {
    border: 1px solid #5A5A5A !important;
    border-radius: 5px;
    padding: 8px !important;
    width: fit-content !important;
    margin-right: 20px;
}
            

</style>
""", unsafe_allow_html=True)



#Main Section
# Sidebar
#with st.sidebar:
#    st.write('Resume')
    

#Main Section
col1, col2= st.columns([2,5], gap="medium")

with col1:
    image = Image.open('assets/BryanResumeImage.png')
    st.image(image)

with col2:
    st.markdown('<p class="big-font">Bryan Moore</p>', unsafe_allow_html=True)
    st.markdown('<p class="medium-font">Data Engineer at Zumiez, building a better retail experience <br> for our customers for the last 5 years.</p>', unsafe_allow_html=True)

    
    st.markdown(':point_right:  bryanmoore@zumiez.com')


st.write('')
st.write('')

col1, col2, col3, col4, col5 = st.columns([1,2,1,2,1])

with col1:
    st.markdown('<p class="left-link"> <a href="https://www.linkedin.com/in/bryanallenmoore/">Linkedin</a> </p>', unsafe_allow_html=True)

with col2:
    st.markdown('<p class="links"> <a href="https://github.com/btothemoe">Github </a></p>', unsafe_allow_html=True)

with col3:
    st.markdown('<p class="links"> <a href="https://btothemoe.github.io/">Resume </a>  </p>', unsafe_allow_html=True)

with col4:
    st.markdown('<p class="links"> <a href="https://www.facebook.com/profile.php?id=644708834">Facebook </p>', unsafe_allow_html=True)
    
with col5:
    st.markdown('<p class="links"> <a href="https://www.instagram.com/brymoe/">Instagram </p>', unsafe_allow_html=True)
    

st.write('')

st.header('Skills & Qualifications')
st.markdown(':heavy_check_mark: 5 years of experience building data integrations')
st.markdown(':heavy_check_mark: Experience with multiple integration platforms')
st.markdown(':heavy_check_mark: Expert level SQL manipulator')
st.markdown(':heavy_check_mark: Advanced reporting skills')
st.markdown(':heavy_check_mark: All around fun guy to hang with')

st.header('Tech Stack')
st.write('')
st.markdown(
    '''<span class="techstack"> Python, JavaScript, Groovy </span> 
    <span class="techstack"> SQL, PostgreSQL, BigQuery, Snowflake</span>
    <span class="techstack"> Spark, Kafka</span>
    
        '''
    , unsafe_allow_html=True
)
st.write('')
st.markdown(
    '''<span class="techstack"> SSIS, Boomi, Airflow</span> 
    <span class="techstack"> SSRS, Power BI, Excel</span>
        '''
    , unsafe_allow_html=True
)
st.write('')

st.markdown("""---""")

st.header('Accomplishments')


chart_data = pd.DataFrame({
    'Type': ['Boomi Integrations','Stored Procedures','Confluence Pages', 'SSIS Packages', 'Excel Reports', 'SSRS Reports', 'JAMS Jobs'],
    'Total' : [55,113,63,8,12,10,12],
    'color' : ['#4cabe6', 'lightblue', '#4cabe6', 'lightblue','#4cabe6', 'lightblue', '#4cabe6']
})

chart = (
    alt.Chart(chart_data)
    .mark_bar()
    .encode(
        alt.X('Type', sort=None, axis=alt.Axis(labelAngle=-45)),
        alt.Y('Total'),
        alt.Color('color').scale(None),
        alt.Tooltip(['Type', 'Total']),
    ).properties(title="Completed Tasks")
)

st.altair_chart(chart, use_container_width=True)


chart_data = pd.DataFrame({
    'Jira Tickets': ['Total','Closed','Development','Bug','Story'],
    'Total' : [536,410,231,59,32],
    'color' : ['lightgray', '#1f8c62', '#4cabe6', '#e64b3c', '#60bc46']
})

chart = (
    alt.Chart(chart_data)
    .mark_bar()
    .encode(
        x=alt.X('Jira Tickets', sort=None, axis=alt.Axis(labelAngle=0)),
        y=alt.Y('Total'),
        color=alt.Color('color').scale(None),
        tooltip=alt.Tooltip(['Jira Tickets', 'Total']),
    ).properties(title="Jira Tickets")
)

st.altair_chart(chart, use_container_width=True)



st.markdown("""---""")



st.header('Awards & Certifications')

st.markdown("""---""")

#st.write("check out this [link](%s)" % url)
#st.markdown("check out this [link](%s)" % url)

url = "https://drive.google.com/file/d/19oGhjLCHCspf9cTGuxQzoRxijPpslbdm/view"
st.write('[🏆 Zumiez Team Of The Year - 2022](%s)' % url)

st.markdown("""---""")

url = "https://drive.google.com/file/d/1n7glY7munISWT_6_puXIM4RohBzxoQFi/view"
st.write('[🏆 Zumiez Project Team Of The Year - 2022](%s)' % url)

st.markdown("""---""")

url = "https://drive.google.com/file/d/1nG-4erE6I-uzd1tGEE1Rv2tLhbDvX_wp/view"
st.write('[🏆 Zumiez Team Of The Year - 2020](%s)' % url)

st.markdown("""---""")

url = "https://drive.google.com/file/d/12DyvNYgba8-rufJeWGiGO6cYwNlzhEGI/view"
st.write('[📜 Boomi Development and Application Architecture Certification](%s)' % url)

st.markdown("""---""")

url = "https://drive.google.com/file/d/1Tnl9xmOtYgEOeqU6QRNwtHAXVU28ZRiJ/view"
st.write('[📜 Boomi Professional Developer Certification](%s)' % url)

st.markdown("""---""")

url = "https://drive.google.com/file/d/15Q7fqwD4pnS0fPLW6W-v7vHXKHEHaZMu/view"
st.write('[📜 Boomi Associate Developer Certification](%s)' % url)

st.markdown("""---""")

st.header('Salary')

tab1, tab2, tab3 = st.tabs(["Base Compensation", "Total Compensation", "Retail Compensation"])

with tab1:
    #https://discuss.streamlit.io/t/how-to-build-line-chart-with-two-values-on-y-axis-and-sorded-x-axis-acording-string/9490/2

    chart_data = pd.DataFrame (
        {
            'Experience' : ['0 - 1 Years', '1 - 3 Years', '4 - 6 Years', '7 - 9 Years'],
            'Zumiez' : [59294, 64673, 72571, 75000],
            'Seattle' : [93437, 103526, 110879, 117030],
            'Washington' : [91038, 100111, 105296, 108655],
            'United States' : [83741, 93757, 101131, 108004]
        },
        columns=['Experience', 'Zumiez', 'Seattle', 'Washington', 'United States']
    )

    chart_data = chart_data.melt('Experience', var_name='Filter', value_name='Base Compensation')

    chart = alt.Chart(chart_data).mark_line(point=True).encode(
    x=alt.X('Experience',sort=None, axis=alt.Axis(labelAngle=0)),
    y=alt.Y('Base Compensation'),
    color=alt.Color("Filter")
    ).properties(title="Data Engineer - Base Compensation")
    st.altair_chart(chart, use_container_width=True)

with tab2:

    chart_data = pd.DataFrame (
        {
            'Experience' : ['0 - 1 Years', '1 - 3 Years', '4 - 6 Years', '7 - 9 Years'],
            'Zumiez' : [60961, 70173, 89437, 95000],
            'Seattle' : [108479, 121844, 132169, 141069],
            'Washington' : [105156, 116808, 124347, 129454],
            'United States' : [96064, 108672, 118503, 127562]
        },
        columns=['Experience', 'Zumiez', 'Seattle', 'Washington', 'United States']
    )

    chart_data = chart_data.melt('Experience', var_name='Filter', value_name='Base Compensation')

    chart = alt.Chart(chart_data).mark_line(point=True).encode(
    x=alt.X('Experience',sort=None, axis=alt.Axis(labelAngle=0)),
    y=alt.Y('Base Compensation'),
    color=alt.Color("Filter")
    ).properties(title="Data Engineer - Total Compensation")
    st.altair_chart(chart, use_container_width=True)

with tab3:
    chart_data = pd.DataFrame (
        {
            'Experience' : ['0 - 1 Years', '1 - 3 Years', '4 - 6 Years', '7 - 9 Years'],
            'Zumiez' : [60961, 70173, 89437, 95000],
            'Nike' : [118000, 128000, 141000, 156000],
            'Adidas' : [110000, 121000, 136000, 150000],
            'Nordstrom' : [109000, 124000, 135000, 145000],
            'REI' : [111000, 122000, 131000, 139000],
            'Urban Outfitters' : [100000, 110000, 124000, 134000],
            'Hot Topic' : [99000, 112000, 125000, 135000]
        },
        columns=['Experience', 'Zumiez', 'Nike', 'Adidas', 'Nordstrom', 'REI', 'Urban Outfitters', 'Hot Topic']
    )

    chart_data = chart_data.melt('Experience', var_name='Filter', value_name='Base Compensation')

    chart = alt.Chart(chart_data).mark_line(point=True).encode(
    x=alt.X('Experience',sort=None, axis=alt.Axis(labelAngle=0)),
    y=alt.Y('Base Compensation'),
    color=alt.Color("Filter")
    ).properties(title="Data Engineer - Retail Comparison")
    st.altair_chart(chart, use_container_width=True)

