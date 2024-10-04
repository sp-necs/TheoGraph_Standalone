import streamlit as st
import streamlit.web.cli as stcli
import streamlit.runtime.scriptrunner.magic_funcs
import pandas as pd
import plotly.express as px
from datetime import datetime as dt
import os, sys

if __name__ == "__main__":
    sys.argv = [
        "streamlit",
        "run",
        os.path.abspath(os.path.join(os.getcwd(), "TheographApp.py")),
        "--global.developmentMode=false"
    ]
    sys.exit(stcli.main())