# -*- coding: utf-8 -*-
# app_tools_home.py
# Streamlit homepage for Athina Logistics tools.

from pathlib import Path

import streamlit as st


APP_DIR = Path(__file__).resolve().parent
APP_TITLE = "Athina Logistics Tools"
LOGO_CANDIDATES = (
    APP_DIR / "logo.png",
    APP_DIR.parent / "logo.png",
    Path.cwd() / "logo.png",
)

TOOLS = [
    {
        "name": "E-Origin Duty Calculator/E-Origin关税计算",
        "description": "Calculate and recap IMA duty amounts from PDF files.",
        "url": "https://eoduty.streamlit.app/",
    },
    {
        "name": "VAT + EORI Checker/税号检测",
        "description": "Check VAT and EORI information and generate screenshots.",
        "url": "https://athinavatcheck.streamlit.app/",
    },
    {
        "name": "SGS Generator/SGS T1模板生成",
        "description": "Run invoice checks and generate the T1_SGS file.",
        "url": "https://athinainchecksgs.streamlit.app/",
    },
    {
        "name": "Controlled HS Checker/查验HS检测",
        "description": "Detect controlled HS codes in invoice Excel files.",
        "url": "https://controlhscheck.streamlit.app/",
    },
    {
        "name": "EWTP invoice editor/EWTP发票准备",
        "description": "Prepare invoice for upload on EWTP.",
        "url": "https://ewtpprepare.streamlit.app/",
    },
    {
        "name": "E-Origin invoice editor/E-Origin发票准备",
        "description": "Prepare invoice for upload on E-Origin.",
        "url": "https://eoriginprepare.streamlit.app/",
    },
    {
        "name": "Invoice info extract/提取发票信息",
        "description": "Extract multi info on invoices.",
        "url": "https://invoicextract.streamlit.app/",
    },
]


def find_logo_path():
    for logo_path in LOGO_CANDIDATES:
        if logo_path.exists():
            return logo_path

    return None


def configure_page():
    logo_path = find_logo_path()
    page_config = {
        "page_title": "Athina Logistics Tool",
        "layout": "wide",
    }

    if logo_path:
        page_config["page_icon"] = str(logo_path)

    st.set_page_config(**page_config)

    if logo_path:
        st.sidebar.image(str(logo_path), width=200)

    st.sidebar.markdown("### Athina Logistics")
    st.sidebar.caption("Global Access")


def render_tool_grid():
    for row_start in range(0, len(TOOLS), 2):
        cols = st.columns(2, gap="large")

        for col, tool in zip(cols, TOOLS[row_start : row_start + 2]):
            with col.container(border=True):
                st.subheader(tool["name"])
                st.write(tool["description"])
                st.link_button("Open tool", tool["url"], use_container_width=True)

        st.write("")


def main():
    configure_page()

    st.title(APP_TITLE)
    st.caption("Choose the tool you want to open.")

    render_tool_grid()


if __name__ == "__main__":
    main()
