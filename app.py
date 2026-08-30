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
        "name": "EO Duty Calculator",
        "description": "Calculate and recap IMA duty amounts from PDF files.",
        "url": "https://eoduty.streamlit.app/",
        "accent": "#0f766e",
    },
    {
        "name": "VAT + EORI Checker",
        "description": "Check VAT and EORI information and generate screenshots.",
        "url": "https://athinavatcheck.streamlit.app/",
        "accent": "#2563eb",
    },
    {
        "name": "Invoice Check + SGS Generator",
        "description": "Run invoice checks and generate the T1_SGS file.",
        "url": "https://athinainchecksgs.streamlit.app/",
        "accent": "#7c3aed",
    },
    {
        "name": "Controlled HS Checker",
        "description": "Detect controlled HS codes in invoice Excel files.",
        "url": "https://controlhscheck.streamlit.app/",
        "accent": "#dc2626",
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


def inject_styles():
    st.markdown(
        """
        <style>
        .main .block-container {
            max-width: 1180px;
            padding-top: 5rem;
        }

        .tool-grid {
            display: grid;
            grid-template-columns: repeat(2, minmax(0, 1fr));
            gap: 18px;
            margin-top: 28px;
        }

        .tool-card {
            display: block;
            min-height: 162px;
            padding: 24px;
            border: 1px solid #e5e7eb;
            border-radius: 8px;
            background: #ffffff;
            color: #111827;
            text-decoration: none;
            box-shadow: 0 1px 2px rgba(15, 23, 42, 0.05);
            transition: border-color 140ms ease, box-shadow 140ms ease, transform 140ms ease;
        }

        .tool-card:hover {
            border-color: var(--accent);
            box-shadow: 0 14px 30px rgba(15, 23, 42, 0.10);
            transform: translateY(-2px);
            text-decoration: none;
        }

        .tool-card:focus {
            outline: 3px solid color-mix(in srgb, var(--accent), transparent 70%);
            outline-offset: 3px;
        }

        .tool-topline {
            width: 46px;
            height: 4px;
            border-radius: 999px;
            background: var(--accent);
            margin-bottom: 22px;
        }

        .tool-title {
            font-size: 1.2rem;
            line-height: 1.3;
            font-weight: 700;
            color: #111827;
            margin-bottom: 10px;
        }

        .tool-description {
            color: #6b7280;
            line-height: 1.5;
            margin-bottom: 20px;
        }

        .tool-action {
            color: var(--accent);
            font-weight: 700;
        }

        @media (max-width: 760px) {
            .main .block-container {
                padding-top: 2.5rem;
            }

            .tool-grid {
                grid-template-columns: 1fr;
            }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_tool_grid():
    cards = []

    for tool in TOOLS:
        cards.append(
            f"""
            <a class="tool-card" style="--accent: {tool["accent"]};" href="{tool["url"]}" target="_self" rel="noopener">
                <div class="tool-topline"></div>
                <div class="tool-title">{tool["name"]}</div>
                <div class="tool-description">{tool["description"]}</div>
                <div class="tool-action">Open tool</div>
            </a>
            """
        )

    st.markdown(f'<div class="tool-grid">{"".join(cards)}</div>', unsafe_allow_html=True)


def main():
    configure_page()
    inject_styles()

    st.title(APP_TITLE)
    st.caption("Choose the tool you want to open.")

    render_tool_grid()


if __name__ == "__main__":
    main()
