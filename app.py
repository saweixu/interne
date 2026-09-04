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
        "title": "E-Origin Duty Calculator",
        "subtitle": "E-Origin税金单关税计算",
        "description": "Calculate and recap IMA duty amounts from PDF files.",
        "category": "Duty",
        "url": "https://eoduty.streamlit.app/",
        "accent": "#006b72",
    },
    {
        "title": "VAT + EORI Checker",
        "subtitle": "批量税号检查+截图",
        "description": "Check VAT and EORI information and generate screenshots.",
        "category": "Compliance",
        "url": "https://athinavatcheck.streamlit.app/",
        "accent": "#2563eb",
    },
    {
        "title": "SGS ROT T1 Generator",
        "subtitle": "SGS 鹿特丹T1模板生成",
        "description": "Run invoice checks and generate the T1_SGS file.",
        "category": "SGS",
        "url": "https://checksgst1.streamlit.app/",
        "accent": "#7c3aed",
    },
    {
        "title": "Controlled HS Checker",
        "subtitle": "查验HS检测",
        "description": "Detect controlled HS codes in invoice Excel files.",
        "category": "HS",
        "url": "https://controlhscheck.streamlit.app/",
        "accent": "#dc2626",
    },
    {
        "title": "EWTP Invoice Editor",
        "subtitle": "EWTP 发票修改",
        "description": "Prepare invoices for upload on EWTP.",
        "category": "Invoice",
        "url": "https://ewtpprepare.streamlit.app/",
        "accent": "#0891b2",
    },
    {
        "title": "E-Origin Invoice Editor",
        "subtitle": "E-Origin 发票修改",
        "description": "Prepare invoices for upload on E-Origin.",
        "category": "Invoice",
        "url": "https://eoriginprepare.streamlit.app/",
        "accent": "#ca8a04",
    },
    {
        "title": "Invoice Info Extract",
        "subtitle": "发票信息提取",
        "description": "Extract multiple details from invoices.",
        "category": "Extract",
        "url": "https://invoicextract.streamlit.app/",
        "accent": "#16a34a",
    },
    {
        "title": "Invoice Split",
        "subtitle": "箱单发票拆分",
        "description": "Split boxes in one box.",
        "category": "Invoice",
        "url": "https://splitinvoice.streamlit.app/",
        "accent": "#16a34a",
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

    st.markdown(
        """
        <style>
            :root {
                --brand: #006b72;
                --ink: #172033;
                --muted: #6b7280;
                --line: #d8dee9;
                --surface: #ffffff;
                --soft: #f6f8fb;
            }

            .block-container {
                max-width: 1280px;
                padding-top: 4rem;
                padding-bottom: 3rem;
            }

            section[data-testid="stSidebar"] {
                background: #f2f5f8;
                border-right: 1px solid #e2e8f0;
            }

            section[data-testid="stSidebar"] img {
                border-radius: 8px;
                background: white;
                padding: 6px;
                border: 1px solid #e5e7eb;
            }

            h1 {
                color: var(--ink);
                font-size: 2.35rem;
                line-height: 1.1;
                letter-spacing: 0;
                margin-bottom: 0.35rem;
            }

            h2, h3, h4 {
                color: var(--ink);
                letter-spacing: 0;
            }

            .home-kicker {
                color: var(--brand);
                font-weight: 700;
                text-transform: uppercase;
                font-size: 0.76rem;
                letter-spacing: 0.08em;
                margin-bottom: 0.35rem;
            }

            .home-copy {
                color: var(--muted);
                font-size: 0.98rem;
                margin-bottom: 1.65rem;
            }

            .tool-accent {
                width: 44px;
                height: 4px;
                border-radius: 999px;
                margin-bottom: 1.05rem;
            }

            .tool-category {
                display: inline-flex;
                align-items: center;
                color: #475569;
                background: #f1f5f9;
                border: 1px solid #e2e8f0;
                border-radius: 999px;
                padding: 0.16rem 0.52rem;
                font-size: 0.76rem;
                font-weight: 650;
                margin-bottom: 0.72rem;
            }

            .tool-title {
                color: var(--ink);
                font-size: 1.18rem;
                font-weight: 760;
                line-height: 1.25;
                margin-bottom: 0.22rem;
            }

            .tool-subtitle {
                color: #334155;
                font-size: 0.95rem;
                font-weight: 620;
                line-height: 1.25;
                min-height: 1.25rem;
                margin-bottom: 0.75rem;
            }

            .tool-description {
                color: #475569;
                font-size: 0.94rem;
                line-height: 1.45;
                min-height: 2.8rem;
                margin-bottom: 1rem;
            }

            div[data-testid="stVerticalBlockBorderWrapper"] {
                border-color: var(--line);
                border-radius: 8px;
                background: var(--surface);
                box-shadow: 0 1px 2px rgba(15, 23, 42, 0.04);
                transition: border-color 120ms ease, box-shadow 120ms ease, transform 120ms ease;
            }

            div[data-testid="stVerticalBlockBorderWrapper"]:hover {
                border-color: #b6c3d1;
                box-shadow: 0 8px 22px rgba(15, 23, 42, 0.08);
                transform: translateY(-1px);
            }

            div.stLinkButton > a {
                border-radius: 7px;
                border: 1px solid #cfd8e3;
                background: #ffffff;
                color: var(--ink);
                font-weight: 650;
                height: 2.42rem;
                justify-content: center;
            }

            div.stLinkButton > a:hover {
                border-color: var(--brand);
                color: var(--brand);
                background: #f8fbfc;
            }

            .tool-count {
                color: #475569;
                background: var(--soft);
                border: 1px solid #e2e8f0;
                border-radius: 8px;
                padding: 0.7rem 0.85rem;
                font-size: 0.92rem;
                margin-bottom: 1.35rem;
            }

            @media (max-width: 900px) {
                .block-container {
                    padding-top: 2.2rem;
                }

                h1 {
                    font-size: 2rem;
                }
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    if logo_path:
        st.sidebar.image(str(logo_path), width=200)

    st.sidebar.markdown("### Athina Logistics")
    st.sidebar.caption("Global Access")
    st.sidebar.caption("Tools by Sawei X.")


def render_header():
    st.markdown('<div class="home-kicker">Internal Tool Portal</div>', unsafe_allow_html=True)
    st.title(APP_TITLE)
    st.markdown(
        '<div class="home-copy">Choose a workflow and open the right Streamlit tool.</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        f'<div class="tool-count">{len(TOOLS)} tools available for daily customs and invoice workflows.</div>',
        unsafe_allow_html=True,
    )


def render_tool_card(col, tool):
    with col.container(border=True):
        st.markdown(
            f'<div class="tool-accent" style="background:{tool["accent"]};"></div>',
            unsafe_allow_html=True,
        )
        st.markdown(f'<div class="tool-category">{tool["category"]}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="tool-title">{tool["title"]}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="tool-subtitle">{tool["subtitle"]}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="tool-description">{tool["description"]}</div>', unsafe_allow_html=True)
        st.link_button("Open tool", tool["url"], use_container_width=True)


def render_tool_grid():
    for row_start in range(0, len(TOOLS), 2):
        cols = st.columns(2, gap="large")
        for col, tool in zip(cols, TOOLS[row_start : row_start + 2]):
            render_tool_card(col, tool)
        st.write("")


def main():
    configure_page()
    render_header()
    render_tool_grid()


if __name__ == "__main__":
    main()
