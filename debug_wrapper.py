import os
import sys
import streamlit.web.cli as stcli

# OpenMP fix
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

# Milvus debug note: ensure conda environment activated
sys.argv = ["streamlit", "run", "app.py", "--server.port", "8506"]

if __name__ == "__main__":
    stcli.main()

