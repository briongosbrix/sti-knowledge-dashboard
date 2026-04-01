import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime
import numpy as np
import folium
from streamlit_folium import st_folium

# Configure page
st.set_page_config(
    page_title="STI Knowledge Research Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Add custom CSS - Easier on the eyes with softer colors
st.markdown("""
    <style>
    .main {
        background-color: #f5f7fa;
    }
    .metric-card {
        background-color: white;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.08);
        margin-bottom: 15px;
    }
    .header-title {
        color: #2c3e50;
        font-size: 32px;
        font-weight: 600;
        margin-bottom: 5px;
    }
    .header-subtitle {
        color: #7f8c8d;
        font-size: 14px;
        margin-bottom: 20px;
        font-weight: 400;
    }
    .study-info-card {
        background: linear-gradient(135deg, #ecf0f1 0%, #ffffff 100%);
        padding: 30px;
        border-radius: 10px;
        border-left: 4px solid #3498db;
        margin-bottom: 20px;
    }
    .info-section {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 8px;
        margin-bottom: 15px;
        border-left: 3px solid #95a5a6;
    }
    </style>
""", unsafe_allow_html=True)

# ============================================================================
# DATA GENERATION
# ============================================================================

def generate_sample_data(n_records=150):
    """Generate comprehensive sample dataset for STI Knowledge research"""
    np.random.seed(42)
    
    respondent_ids = [f"{i:04d}" for i in range(1, n_records + 1)]
    ages = np.random.randint(15, 35, n_records)
    genders = np.random.choice(['Male', 'Female'], n_records, p=[0.48, 0.52])
    
    knowledge_levels = []
    knowledge_scores = []
    
    for age, gender in zip(ages, genders):
        base_score = 40 + (age - 15) * 2 + (10 if gender == 'Female' else 0)
        noise = np.random.normal(0, 15)
        score = np.clip(base_score + noise, 0, 100)
        knowledge_scores.append(score)
        
        if score >= 70:
            knowledge_levels.append('Have Knowledge')
        elif score >= 40:
            knowledge_levels.append('Moderate Knowledge')
        else:
            knowledge_levels.append('Least Knowledge')
    
    info_sources = np.random.choice(
        ['Social Media', 'Health Workers', 'Peers', 'Educational Programs', 'Family'],
        n_records,
        p=[0.30, 0.25, 0.20, 0.15, 0.10]
    )
    
    age_groups = pd.cut(ages, bins=[14, 19, 24, 29, 34], 
                        labels=['15-19', '20-24', '25-29', '30-34'])
    
    barangays = np.random.choice(['Barangay Poblacion', 'Barangay Bagay', 'Barangay Catagoan'], 
                                  n_records, p=[0.35, 0.35, 0.30])
    
    barangay_coords = {
        'Barangay Poblacion': (14.1160, 121.6450),
        'Barangay Bagay': (14.1100, 121.6350),
        'Barangay Catagoan': (14.1050, 121.6550)
    }
    
    lats = []
    lons = []
    for barangay in barangays:
        base_lat, base_lon = barangay_coords[barangay]
        lat = base_lat + np.random.uniform(-0.005, 0.005)
        lon = base_lon + np.random.uniform(-0.005, 0.005)
        lats.append(lat)
        lons.append(lon)
    
    df = pd.DataFrame({
        'Respondent_ID': respondent_ids,
        'Age': ages,
        'Gender': genders,
        'Age_Group': age_groups,
        'Knowledge_Score': knowledge_scores,
        'Knowledge_Level': knowledge_levels,
        'Information_Source': info_sources,
        'Barangay': barangays,
        'Latitude': lats,
        'Longitude': lons
    })
    
    return df

# Load data
df = generate_sample_data(150)

# ============================================================================
# MAIN HEADER
# ============================================================================

st.markdown('<div class="header-title">🏥 STI Knowledge Research Dashboard</div>', 
            unsafe_allow_html=True)
st.markdown(
    '<div class="header-subtitle">Gender Disparities in Knowledge of STIs among Out-of-School Youth</div>',
    unsafe_allow_html=True
)

st.divider()

# ============================================================================
# CREATE TABS
# ============================================================================

tab1, tab2, tab3, tab4 = st.tabs(["📚 Study Info", "📊 Dashboard", "🗺️ Map", "📥 Downloads"])

# ============================================================================
# TAB 1: STUDY INFORMATION
# ============================================================================

with tab1:
    st.markdown("### 📖 Research Study Information")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        <div class="study-info-card">
        
        #### Research Title
        **Gender Disparities in Knowledge of Sexually Transmitted Infections (STIs) among Out-of-School Youth**
        
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="info-section">
        
        #### Objective
        To assess and analyze the gender disparities in knowledge of STIs among out-of-school youth in the community, identifying key information sources and factors that influence health awareness.
        
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="info-section">
        
        #### Research Scope
        - **Target Population:** Out-of-school youth aged 15-34
        - **Geographic Area:** Daet, Camarines Norte (3 Barangays)
        - **Respondents:** 150+ participants
        - **Focus:** Gender perspectives on STI knowledge and health awareness
        
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="info-section">
        
        **Institution**
        
        Mabini Colleges, Inc.
        
        **Department**
        
        College of Computer Studies
        
        **Partner**
        
        College of Nursing (CON)
        
        **Location**
        
        Daet, Camarines Norte
        
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="info-section">
        
        **Department Advisor**
        
        Dr. Caridad D. Garcia
        
        </div>
        """, unsafe_allow_html=True)
    
    st.divider()
    
    st.markdown("""
    <div class="info-section">
    
    #### Methodology
    
    **Research Design:** Descriptive Cross-sectional Study
    
    **Data Collection:** 
    - Structured questionnaires
    - Demographic information (age, gender)
    - STI knowledge assessment (scored 0-100)
    - Information sources identification
    
    **Variables Measured:**
    - Knowledge Level (0-100 scale)
    - Gender Distribution
    - Age Groups (15-19, 20-24, 25-29, 30-34)
    - Primary Information Sources (Social Media, Health Workers, Peers, Educational Programs, Family)
    - Geographic Distribution (3 Barangays)
    
    </div>
    """, unsafe_allow_html=True)

# ============================================================================
# TAB 2: DASHBOARD
# ============================================================================

with tab2:
    st.markdown("### 📊 Data Analysis Dashboard")
    st.markdown("**Use filters below to explore the data**")
    
    # Filters
    st.markdown("#### 🔍 Filters")
    filter_col1, filter_col2, filter_col3, filter_col4 = st.columns(4)
    
    with filter_col1:
        selected_gender = st.multiselect(
            "Gender",
            options=df['Gender'].unique(),
            default=df['Gender'].unique(),
            key="gender_filter"
        )
    
    with filter_col2:
        selected_age_group = st.multiselect(
            "Age Group",
            options=sorted(df['Age_Group'].dropna().unique()),
            default=sorted(df['Age_Group'].dropna().unique()),
            key="age_filter"
        )
    
    with filter_col3:
        selected_knowledge = st.multiselect(
            "Knowledge Level",
            options=df['Knowledge_Level'].unique(),
            default=df['Knowledge_Level'].unique(),
            key="knowledge_filter"
        )
    
    with filter_col4:
        selected_info_source = st.multiselect(
            "Information Source",
            options=df['Information_Source'].unique(),
            default=df['Information_Source'].unique(),
            key="source_filter"
        )
    
    # Apply filters
    filtered_df = df[
        (df['Gender'].isin(selected_gender)) &
        (df['Age_Group'].isin(selected_age_group)) &
        (df['Knowledge_Level'].isin(selected_knowledge)) &
        (df['Information_Source'].isin(selected_info_source))
    ]
    
    # ====== RESPONDENT LIST (SIDEBAR - ONLY IN DASHBOARD TAB) ======
    display_respondents = filtered_df.copy()
    display_respondents['Knowledge_Score'] = display_respondents['Knowledge_Score'].round(1)
    display_respondents = display_respondents.sort_values('Respondent_ID')
    
    st.sidebar.markdown("### 📋 Dashboard Respondents")
    st.sidebar.markdown(f"**Total: {len(filtered_df)}**")
    st.sidebar.divider()
    
    st.sidebar.dataframe(
        display_respondents[['Respondent_ID', 'Age', 'Gender', 'Knowledge_Score']],
        height=500,
        column_config={
            'Respondent_ID': st.column_config.TextColumn(label='ID', width='small'),
            'Age': st.column_config.NumberColumn(label='Age', width='small'),
            'Gender': st.column_config.TextColumn(label='Gen', width='small'),
            'Knowledge_Score': st.column_config.NumberColumn(label='Score', width='small'),
        },
        hide_index=True
    )
    
    st.sidebar.divider()
    
    st.info(f"📊 Showing {len(filtered_df)} of {len(df)} respondents")
    st.divider()
    
    # Visualizations and Statistics (full width, no left column)
    viz_col, stats_col = st.columns([3.5, 3])
    
    with viz_col:
        st.markdown("### 📈 Visualizations")
        
        # Row 1: Knowledge Distribution
        viz1_col, viz2_col = st.columns(2)
        
        with viz1_col:
            st.markdown("#### Knowledge Level Distribution")
            knowledge_counts = filtered_df['Knowledge_Level'].value_counts()
            colors_knowledge = ['#2ecc71', '#f39c12', '#e74c3c']
            
            fig_knowledge = go.Figure(data=[go.Bar(
                x=knowledge_counts.index,
                y=knowledge_counts.values,
                marker=dict(color=colors_knowledge, line=dict(color='white', width=2)),
                text=knowledge_counts.values,
                textposition='outside',
                hovertemplate='<b>%{x}</b><br>Count: %{y}<extra></extra>'
            )])
            fig_knowledge.update_layout(
                height=300,
                title_font_size=14,
                xaxis_title="Knowledge Level",
                yaxis_title="Count",
                template="plotly_white",
                margin=dict(l=0, r=0, t=30, b=0),
                showlegend=False
            )
            st.plotly_chart(fig_knowledge, width='stretch')
        
        with viz2_col:
            st.markdown("#### Gender Distribution")
            gender_counts = filtered_df['Gender'].value_counts()
            colors_gender = ['#3498db', '#e91e63']
            
            fig_gender = go.Figure(data=[go.Pie(
                labels=gender_counts.index,
                values=gender_counts.values,
                hole=0.4,
                marker=dict(colors=colors_gender, line=dict(color='white', width=2)),
                hovertemplate='<b>%{label}</b><br>Count: %{value}<br>Percentage: %{percent}<extra></extra>'
            )])
            fig_gender.update_layout(
                height=300,
                title_font_size=14,
                template="plotly_white",
                margin=dict(l=0, r=0, t=30, b=0)
            )
            st.plotly_chart(fig_gender, width='stretch')
        
        # Row 2: Gender vs Knowledge
        st.markdown("#### Gender vs Knowledge Level")
        gender_knowledge = pd.crosstab(filtered_df['Knowledge_Level'], filtered_df['Gender'])
        
        fig_grouped = go.Figure()
        
        for gender in gender_knowledge.columns:
            fig_grouped.add_trace(go.Bar(
                x=gender_knowledge.index,
                y=gender_knowledge[gender],
                name=gender,
                marker=dict(color='#3498db' if gender == 'Male' else '#e91e63'),
                text=gender_knowledge[gender],
                textposition='outside',
                hovertemplate=f'<b>{gender}</b><br>%{{x}}<br>Count: %{{y}}<extra></extra>'
            ))
        
        fig_grouped.update_layout(
            height=300,
            barmode='group',
            xaxis_title="Knowledge Level",
            yaxis_title="Count",
            template="plotly_white",
            hovermode='x unified',
            margin=dict(l=0, r=0, t=30, b=0)
        )
        st.plotly_chart(fig_grouped, width='stretch')
        
        # Row 3: Information Source
        st.markdown("#### Information Source Distribution")
        
        source_counts = filtered_df['Information_Source'].value_counts()
        colors_source = ['#9b59b6', '#1abc9c', '#f39c12', '#e67e22', '#34495e']
        
        fig_source = go.Figure(data=[go.Bar(
            y=source_counts.index,
            x=source_counts.values,
            orientation='h',
            marker=dict(color=colors_source[:len(source_counts)], line=dict(color='white', width=2)),
            text=source_counts.values,
            textposition='outside',
            hovertemplate='<b>%{y}</b><br>Count: %{x}<extra></extra>'
        )])
        fig_source.update_layout(
            height=250,
            xaxis_title="Count",
            yaxis_title="Source",
            template="plotly_white",
            margin=dict(l=0, r=0, t=30, b=0),
            showlegend=False
        )
        st.plotly_chart(fig_source, width='stretch')
        
        # Row 4: Age vs Score
        st.markdown("#### Age vs Knowledge Score")
        
        fig_scatter = px.scatter(
            filtered_df,
            x='Age',
            y='Knowledge_Score',
            color='Gender',
            size='Knowledge_Score',
            hover_data={'Age': True, 'Knowledge_Score': ':.1f', 'Gender': True},
            color_discrete_map={'Male': '#3498db', 'Female': '#e91e63'}
        )
        fig_scatter.update_layout(
            height=300,
            xaxis_title="Age (Years)",
            yaxis_title="Knowledge Score (0-100)",
            template="plotly_white",
            hovermode='closest',
            margin=dict(l=0, r=0, t=30, b=0)
        )
        st.plotly_chart(fig_scatter, width='stretch')
    
    with stats_col:
        st.markdown("### 📊 Statistics")
        
        total_respondents = len(filtered_df)
        avg_age = filtered_df['Age'].mean()
        avg_score = filtered_df['Knowledge_Score'].mean()
        std_score = filtered_df['Knowledge_Score'].std()
        
        col1, col2 = st.columns(2)
        col1.metric("Total", total_respondents)
        col2.metric("Avg Age", f"{avg_age:.1f}")
        
        col1.metric("Avg Score", f"{avg_score:.1f}")
        col2.metric("Std Dev", f"{std_score:.2f}")
        
        with st.expander("📐 Calculation Details", expanded=False):
            st.markdown(f"""
**Total Respondents:** {total_respondents}

**Average Age:** {avg_age:.1f} years

**Average Score:** {avg_score:.1f}/100

**Standard Deviation:** {std_score:.2f}
            """)
        
        st.divider()
        
        st.markdown("#### Gender Analysis")
        gender_stats = filtered_df.groupby('Gender').agg({
            'Knowledge_Score': ['mean', 'count']
        }).round(2)
        
        gender_stats.columns = ['Avg Score', 'Count']
        
        for gender in gender_stats.index:
            score = gender_stats.loc[gender, 'Avg Score']
            count = int(gender_stats.loc[gender, 'Count'])
            pct = (count / total_respondents * 100) if total_respondents > 0 else 0
            st.metric(f"👤 {gender}", f"{score:.1f}", f"{count} ({pct:.1f}%)")
        
        st.divider()
        
        st.markdown("#### Knowledge Levels")
        knowledge_dist = filtered_df['Knowledge_Level'].value_counts()
        
        for level in ['Have Knowledge', 'Moderate Knowledge', 'Least Knowledge']:
            if level in knowledge_dist.index:
                count = knowledge_dist[level]
                pct = (count / total_respondents * 100) if total_respondents > 0 else 0
                st.metric(level, count, f"{pct:.1f}%")

# ============================================================================
# TAB 3: GEOGRAPHIC MAP
# ============================================================================

with tab3:
    st.markdown("### 🗺️ Geographic Distribution by Barangay")
    
    # Filters for map
    st.markdown("#### 📍 Filter Data")
    map_filter_col1, map_filter_col2, map_filter_col3, map_filter_col4 = st.columns(4)
    
    with map_filter_col1:
        map_selected_gender = st.multiselect(
            "Gender (Map)",
            options=df['Gender'].unique(),
            default=df['Gender'].unique(),
            key="map_gender_filter"
        )
    
    with map_filter_col2:
        map_selected_age_group = st.multiselect(
            "Age Group (Map)",
            options=sorted(df['Age_Group'].dropna().unique()),
            default=sorted(df['Age_Group'].dropna().unique()),
            key="map_age_filter"
        )
    
    with map_filter_col3:
        map_selected_knowledge = st.multiselect(
            "Knowledge Level (Map)",
            options=df['Knowledge_Level'].unique(),
            default=df['Knowledge_Level'].unique(),
            key="map_knowledge_filter"
        )
    
    with map_filter_col4:
        map_selected_info_source = st.multiselect(
            "Information Source (Map)",
            options=df['Information_Source'].unique(),
            default=df['Information_Source'].unique(),
            key="map_source_filter"
        )
    
    # Apply map filters
    map_filtered_df = df[
        (df['Gender'].isin(map_selected_gender)) &
        (df['Age_Group'].isin(map_selected_age_group)) &
        (df['Knowledge_Level'].isin(map_selected_knowledge)) &
        (df['Information_Source'].isin(map_selected_info_source))
    ]
    
    st.info(f"📍 Showing {len(map_filtered_df)} respondent locations")
    
    map_col1, map_col2 = st.columns([2, 1])
    
    with map_col1:
        # Create map
        m = folium.Map(
            location=[14.1100, 121.6450],
            zoom_start=13,
            tiles="OpenStreetMap"
        )
        
        barangay_centers = {
            'Barangay Poblacion': (14.1160, 121.6450),
            'Barangay Bagay': (14.1100, 121.6350),
            'Barangay Catagoan': (14.1050, 121.6550)
        }
        
        barangay_colors = {
            'Barangay Poblacion': '#3498db',
            'Barangay Bagay': '#e74c3c',
            'Barangay Catagoan': '#2ecc71'
        }
        
        # Add barangay boundaries
        for barangay, (lat, lon) in barangay_centers.items():
            folium.Circle(
                location=(lat, lon),
                radius=400,
                popup=barangay,
                color=barangay_colors[barangay],
                fill=True,
                fillColor=barangay_colors[barangay],
                fillOpacity=0.3,
                weight=3
            ).add_to(m)
        
        # Add respondent markers
        for idx, row in map_filtered_df.iterrows():
            folium.CircleMarker(
                location=(row['Latitude'], row['Longitude']),
                radius=6,
                popup=f"<b>ID: {row['Respondent_ID']}</b><br>Age: {row['Age']}<br>Score: {row['Knowledge_Score']:.1f}<br>Barangay: {row['Barangay']}",
                color=barangay_colors[row['Barangay']],
                fill=True,
                fillColor=barangay_colors[row['Barangay']],
                fillOpacity=0.7,
                weight=2
            ).add_to(m)
        
        st_folium(m, width=700, height=500)
    
    with map_col2:
        st.markdown("#### Barangay Summary")
        
        barangay_stats = map_filtered_df['Barangay'].value_counts()
        
        for barangay in ['Barangay Poblacion', 'Barangay Bagay', 'Barangay Catagoan']:
            if barangay in barangay_stats.index:
                count = barangay_stats[barangay]
                pct = (count / len(map_filtered_df) * 100) if len(map_filtered_df) > 0 else 0
                color = barangay_colors[barangay]
                st.markdown(f"<span style='color:{color}'>●</span> **{barangay}**", unsafe_allow_html=True)
                st.markdown(f"  {count} resp ({pct:.1f}%)")
            else:
                st.markdown(f"<span style='color:{barangay_colors[barangay]}'>●</span> **{barangay}**", unsafe_allow_html=True)
                st.markdown(f"  0 resp (0%)")
        
        st.divider()
        
        with st.expander("📍 How to use", expanded=False):
            st.markdown("""
- **Circles:** Barangay areas
- **Dots:** Respondent locations
- **Click:** View respondent details
- **Zoom:** Scroll to zoom in/out
            """)

# ============================================================================
# TAB 4: DOWNLOADS
# ============================================================================

with tab4:
    st.markdown("### 📥 Download Data")
    
    st.markdown("#### Respondent List")
    
    # Create display dataframe
    display_df = df.copy()
    display_df = display_df.sort_values('Respondent_ID')
    
    st.dataframe(
        display_df[['Respondent_ID', 'Age', 'Gender', 'Age_Group', 'Knowledge_Score', 'Knowledge_Level', 'Barangay']],
        width='stretch',
        height=400
    )
    
    st.divider()
    
    st.markdown("#### Export Options")
    
    col1, col2 = st.columns(2)
    
    with col1:
        csv = display_df.to_csv(index=False)
        st.download_button(
            label="📥 Download CSV",
            data=csv,
            file_name=f"STI_Data_{datetime.now().strftime('%Y%m%d')}.csv",
            mime="text/csv"
        )
    
    with col2:
        st.info("✅ CSV file includes all respondent data and can be used in Excel or other tools")

# ============================================================================
# FOOTER
# ============================================================================

st.divider()
st.markdown("""
---
**Research Project Information**
- **Title:** Gender Disparities in Knowledge of STIs among Out-of-School Youth
- **Institution:** Mabini Colleges, Inc. - College of Computer Studies
- **Advisor:** Dr. Caridad D. Garcia
- **Partner:** College of Nursing (CON)
- **Location:** Daet, Camarines Norte

*This dashboard provides interactive visualization and analysis of STI knowledge research data.*
""")
