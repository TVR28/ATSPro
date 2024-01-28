mkdir -p ~/.streamlit/

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
[theme]\n\
primaryColor = '#2874A6'\n\
backgroundColor = '#D6EAF8'\n\
secondaryBackgroundColor = '#AED6F1'\n\
textColor = '#fff'\n\
" > ~/.streamlit/config.toml