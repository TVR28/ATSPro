mkdir -p ~/.streamlit/

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
[theme]\n\
primaryColor = '#7393B3'\n\
backgroundColor = '#7393B3'\n\
secondaryBackgroundColor = '#A9A9A9'\n\
textColor = '#000000'\n\
" > ~/.streamlit/config.toml
