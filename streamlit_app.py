import math
import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(page_title="MATTERVERSE | Material Discovery Lab", page_icon="⚛️", layout="wide")

MATERIALS = [
    {"id":"silicon","name":"Silicon","formula":"Si","category":"Semiconductor","structure":"Diamond cubic","density":2.329,"melting_point":1414,"band_gap":1.12,"description":"A foundational semiconductor used in integrated circuits and photovoltaic cells.","color":"#78b8ff"},
    {"id":"graphene","name":"Graphene","formula":"C","category":"Nanomaterial","structure":"2D hexagonal lattice","density":2.267,"melting_point":">3000","band_gap":0.0,"description":"A single atomic layer of carbon arranged in a hexagonal lattice.","color":"#65d6c2"},
    {"id":"copper","name":"Copper","formula":"Cu","category":"Metal","structure":"Face-centred cubic","density":8.96,"melting_point":1084.6,"band_gap":0.0,"description":"A highly conductive metal widely used in electrical wiring.","color":"#e5a05b"},
    {"id":"tio2","name":"Titanium dioxide","formula":"TiO₂","category":"Ceramic / Nanomaterial","structure":"Rutile / Anatase","density":4.23,"melting_point":1843,"band_gap":3.0,"description":"A functional oxide used in pigments, photocatalysis and UV protection.","color":"#b39bff"},
    {"id":"cnt","name":"Carbon nanotube","formula":"C","category":"Nanomaterial","structure":"Cylindrical graphene sheet","density":1.3,"melting_point":"~3550","band_gap":"Varies","description":"A nanoscale carbon cylinder with distinctive mechanical and electrical properties.","color":"#72d9d1"},
]
BY_ID = {m["id"]: m for m in MATERIALS}

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=DM+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@400;500;600;700&display=swap');
:root{color-scheme:dark}
.stApp{background:radial-gradient(ellipse at 78% 0%,#10283a 0%,#07111d 48%);color:#e9f0f8}
html,body,[class*="css"]{font-family:'DM Sans',sans-serif}
h1,h2,h3{font-family:'Space Grotesk',sans-serif!important;letter-spacing:-.7px}
[data-testid="stSidebar"]{background:#081522;border-right:1px solid #203246}
[data-testid="stMetric"]{background:#0b1b2a;border:1px solid #20394b;padding:16px;border-radius:12px}
[data-testid="stMetricLabel"]{color:#8ca1b3}
[data-testid="stMetricValue"]{color:#80ded5}
.stTabs [data-baseweb="tab-list"]{gap:8px;border-bottom:1px solid #20394b}
.stTabs [data-baseweb="tab"]{color:#9cafc0}
.stTabs [aria-selected="true"]{color:#80ded5}
div[data-testid="stVerticalBlockBorderWrapper"]{border-color:#294457!important}
.mv-kicker{font:10px 'DM Mono',monospace;letter-spacing:2px;color:#80d9d1;margin-bottom:10px}
.mv-card{background:linear-gradient(130deg,#102536,#0a1a29);border:1px solid #274155;border-radius:16px;padding:24px 26px;margin:8px 0 16px}
.mv-card p{color:#9ab0c0;line-height:1.7}
.mv-muted{color:#8ca1b3;font-size:13px}
.mv-chip{display:inline-block;border:1px solid #315b6c;border-radius:20px;padding:5px 10px;color:#80ded5;font-size:11px;margin:3px}
footer{visibility:hidden}
</style>
""", unsafe_allow_html=True)

def atom_figure(kind):
    n = 5 if kind == "graphene" else 3
    pts = []
    for x in range(-n,n+1):
        for y in range(-n,n+1):
            for z in range(-n,n+1):
                if kind == "graphene" and z != 0: continue
                if kind == "graphene" and (x+y) % 2: continue
                if kind != "graphene" and (x+y+z) % 2: continue
                scale = .58 if kind == "graphene" else .8
                pts.append((x*scale,y*scale,z*.8))
    color = BY_ID.get(kind, BY_ID["silicon"])["color"]
    fig = go.Figure(go.Scatter3d(x=[p[0] for p in pts],y=[p[1] for p in pts],z=[p[2] for p in pts],mode="markers",marker=dict(size=6,color=color,opacity=.9,line=dict(width=0))))
    fig.update_layout(height=360,margin=dict(l=0,r=0,t=0,b=0),paper_bgcolor="rgba(0,0,0,0)",plot_bgcolor="rgba(0,0,0,0)",scene=dict(xaxis=dict(visible=False),yaxis=dict(visible=False),zaxis=dict(visible=False),bgcolor="rgba(0,0,0,0)",aspectmode="data"),showlegend=False)
    return fig

def prop(label,value):
    st.caption(label.upper())
    st.markdown(f"**{value}**")

st.sidebar.markdown("## ⚛️ MATTERVERSE")
st.sidebar.caption("MATERIAL DISCOVERY LAB")
st.sidebar.markdown("---")
st.sidebar.markdown("**ENGINEERING MATERIALS**")
st.sidebar.markdown("Explore · Visualise · Calculate · Compare")
st.sidebar.markdown("---")
st.sidebar.caption("EDUCATIONAL BUILD · 2026")
st.title("MATTERVERSE")
st.markdown('<div class="mv-kicker">ENGINEERING MATERIALS · DIGITAL ATLAS</div>',unsafe_allow_html=True)
st.markdown("A visual workspace for understanding materials, structures and nanoscale properties.")
overview, library, nano, compare = st.tabs(["◈ Overview","▦ Materials","⚗ Nano Lab","⇄ Compare"])

with overview:
    chosen = st.selectbox("Featured material", [m["name"] for m in MATERIALS], index=0, key="featured")
    current = next(m for m in MATERIALS if m["name"] == chosen)
    left,right = st.columns([1,1.2],gap="large")
    with left:
        st.markdown('<div class="mv-card">',unsafe_allow_html=True)
        st.markdown('<div class="mv-kicker">FEATURED STRUCTURE</div>',unsafe_allow_html=True)
        st.header(current["name"])
        st.markdown(f"### :green[{current['formula']}]")
        st.write(current["description"])
        st.markdown(f'<span class="mv-chip">{current["category"]}</span><span class="mv-chip">{current["structure"]}</span>',unsafe_allow_html=True)
        st.markdown("</div>",unsafe_allow_html=True)
    with right:
        st.markdown('<div class="mv-kicker">ATOMIC LATTICE · INTERACTIVE 3D</div>',unsafe_allow_html=True)
        kind = current["id"] if current["id"] in ("graphene","copper") else "silicon"
        st.plotly_chart(atom_figure(kind),use_container_width=True,config={"displayModeBar":False})
    a,b,c,d = st.columns(4)
    a.metric("Materials indexed",f"{len(MATERIALS):02d}")
    b.metric("Discovery modes","04")
    c.metric("Exploration scale","10⁻⁹ m")
    d.metric("Calculator","Ready")
    st.subheader("Start exploring")
    cards = st.columns(4)
    for col,m in zip(cards,MATERIALS[:4]):
        with col:
            st.markdown(f"**{m['name']}**")
            st.caption(f"{m['formula']} · {m['category']}")
            st.metric("Density",f"{m['density']} g/cm³")

with library:
    st.subheader("Material library")
    query = st.text_input("Search material, formula or category",placeholder="Try silicon, carbon, semiconductor...")
    filtered = [m for m in MATERIALS if query.lower() in (m["name"]+" "+m["formula"]+" "+m["category"]+" "+m["structure"]).lower()]
    names = [m["name"] for m in filtered]
    if names:
        selected_name = st.selectbox("Select a material",names)
        m = next(x for x in filtered if x["name"] == selected_name)
        l,r = st.columns([1,1.2],gap="large")
        with l:
            st.markdown(f"### {m['name']} · :green[{m['formula']}]")
            st.write(m["description"])
            st.markdown(f'<span class="mv-chip">{m["category"]}</span><span class="mv-chip">{m["structure"]}</span>',unsafe_allow_html=True)
        with r:
            kind = m["id"] if m["id"] in ("graphene","copper") else "silicon"
            st.plotly_chart(atom_figure(kind),use_container_width=True,config={"displayModeBar":False})
        x1,x2,x3 = st.columns(3)
        x4,x5,x6 = st.columns(3)
        for col,label,value in [(x1,"Formula",m["formula"]),(x2,"Structure",m["structure"]),(x3,"Density",f"{m['density']} g/cm³"),(x4,"Melting point",f"{m['melting_point']} °C"),(x5,"Band gap",f"{m['band_gap']} eV"),(x6,"Category",m["category"])]:
            with col: prop(label,value)
    else:
        st.info("No materials match that search.")

with nano:
    st.subheader("Nanoparticle sphere calculator")
    st.markdown("Estimate geometric volume, surface area and mass from particle diameter and material density.")
    l,r = st.columns(2,gap="large")
    with l:
        diameter = st.slider("Particle diameter (nm)",1,500,50)
        density_options = {"Graphene / Carbon":2.267,"Silicon":2.329,"Titanium dioxide":4.23,"Copper":8.96}
        material = st.selectbox("Material density",list(density_options.keys()))
        density = density_options[material]
        st.metric("Density",f"{density:.3f} g/cm³")
        calculate = st.button("Calculate properties",type="primary",use_container_width=True)
    with r:
        if calculate or "nano_result" in st.session_state:
            radius_cm = diameter*1e-7/2
            volume = (4/3)*math.pi*radius_cm**3
            mass = volume*density
            st.markdown('<div class="mv-kicker">CALCULATION OUTPUT</div>',unsafe_allow_html=True)
            st.metric("Estimated particle mass",f"{mass*1e15:.4g} fg")
            p1,p2 = st.columns(2)
            p1.metric("Volume",f"{volume:.3e} cm³")
            p2.metric("Surface area",f"{math.pi*diameter**2:.2f} nm²")
            st.caption("Ideal spherical particle assumption. Real nanoparticles may be non-spherical and exhibit surface effects.")
            st.session_state["nano_result"] = True
        else:
            st.info("Set the particle parameters and click Calculate properties.")

with compare:
    st.subheader("Compare material properties")
    selected_names = st.multiselect("Choose materials", [m["name"] for m in MATERIALS], default=["Silicon","Graphene"])
    selected = [m for m in MATERIALS if m["name"] in selected_names]
    if selected:
        rows = [{"Property":label,**{m["name"]:m[key] for m in selected}} for label,key in [("Formula","formula"),("Category","category"),("Structure","structure"),("Density (g/cm³)","density"),("Melting point (°C)","melting_point"),("Band gap (eV)","band_gap")]]
        st.dataframe(pd.DataFrame(rows),use_container_width=True,hide_index=True)
        numeric = [m for m in selected if isinstance(m["density"],(int,float))]
        if numeric:
            chart = pd.DataFrame({"Material":[m["name"] for m in numeric],"Density (g/cm³)":[m["density"] for m in numeric]})
            st.bar_chart(chart,x="Material",y="Density (g/cm³)")
    if len(selected)<2:
        st.caption("Select at least two materials to compare their properties.")

st.divider()
st.caption("MATTERVERSE · BUILT FOR MATERIALS SCIENCE LEARNING · Reference values are educational and not certified engineering design data.")
