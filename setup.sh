mkdir -p ~/.streamlit/

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
[theme]\n\
primaryColor = '#7393B3'\n\
backgroundColor = '#d3d3d3'\n\
secondaryBackgroundColor = '#ededed'\n\
textColor = '#000000'\n\
" > ~/.streamlit/config.toml
