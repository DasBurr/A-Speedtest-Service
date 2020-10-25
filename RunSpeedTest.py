import speedtest

st = speedtest.Speedtest()

st.download()
st.upload()

print(st.results)