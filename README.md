# STI Knowledge Research Dashboard

## Interactive Visualization Dashboard for Gender Disparities Research

This is a comprehensive, user-friendly dashboard built with **Python**, **Streamlit**, and **Plotly** for visualizing and analyzing research data on STI knowledge among out-of-school youth.

---

## 📋 Features

### Dashboard Components:
1. **Left Panel - Interactive Visualizations**
   - 📊 Knowledge Level Distribution (Vertical Bar Chart)
   - 🥧 Gender Distribution (Donut Chart)
   - 📊 Gender vs Knowledge Level Comparison (Grouped Bar Chart)
   - 📊 Information Source Distribution (Horizontal Bar Chart)
   - 📈 Age vs Knowledge Score Trend (Scatter Plot with Trendline)

2. **Right Panel - Statistical Computations**
   - Overall Statistics (Total Respondents, Average Age, Average Score, Std Dev)
   - Gender Analysis (Average Score by Gender with counts and percentages)
   - Knowledge Level Breakdown (Distribution across levels)
   - Age Group Analysis (Average scores by age group)
   - Primary Information Sources (Top sources distribution)

3. **Interactive Filters (Sidebar)**
   - Filter by Gender
   - Filter by Age Group
   - Filter by Knowledge Level
   - Filter by Information Source
   - Real-time data updates based on selections

4. **Respondent List Section**
   - Complete table view of all respondents matching filters
   - Sortable and searchable columns
   - Download data as CSV option

---

## 🚀 Installation & Setup

### Prerequisites:
- Python 3.8 or higher
- pip (Python package manager)

### Step 1: Install Required Libraries

```bash
pip install -r requirements.txt
```

Or manually install:
```bash
pip install streamlit==1.28.0 pandas==2.0.3 plotly==5.17.0 numpy==1.24.3
```

### Step 2: Run the Dashboard

```bash
streamlit run app.py
```

The dashboard will open in your default browser at `http://localhost:8501`

---

## 📊 Data Structure

The dataset includes the following fields:
- **Respondent_ID**: Unique identifier (0001, 0002, etc.)
- **Age**: Respondent's age (15-34)
- **Gender**: Male or Female
- **Age_Group**: Categorized age groups (15-19, 20-24, 25-29, 30-34)
- **Knowledge_Score**: Numerical score 0-100
- **Knowledge_Level**: Categorical level (Have Knowledge, Moderate Knowledge, Least Knowledge)
- **Information_Source**: Source of STI information (Social Media, Health Workers, Peers, Educational Programs, Family)

---

## 🎨 Design & Layout

### Professional Formatting:
- **Color Scheme**: Professional blues, pinks, and accent colors
- **Typography**: Clear hierarchy and formal design
- **Responsiveness**: Works on different screen sizes
- **Accessibility**: High contrast, readable fonts

### Dashboard Layout:
```
┌─────────────────────────────────────────┐
│      HEADER - STI Knowledge Dashboard   │
├─────────────────────────────────────────┤
│ FILTERS │                               │
│ (Side)  │     LEFT COLUMN               │ RIGHT COLUMN
│         │  (Visualizations)             │ (Statistics)
│ Gender  │  - Charts                     │ - Metrics
│ Age     │  - Graphs                     │ - Computations
│ Know    │  - Analysis                   │ - Breakdowns
│ Source  │                               │
├─────────────────────────────────────────┤
│        RESPONDENT LIST & DATA            │
├─────────────────────────────────────────┤
│         PROJECT INFORMATION              │
└─────────────────────────────────────────┘
```

---

## 🔧 Customization

### To Use Your Own Data:

Replace the `generate_sample_data()` function with:

```python
# Load from CSV
df = pd.read_csv('your_data.csv')
```

Or connect to a database:

```python
import sqlite3
conn = sqlite3.connect('your_database.db')
df = pd.read_sql_query("SELECT * FROM respondents", conn)
```

### To Modify Visualizations:

Edit the chart configurations in the code. All charts are built with Plotly and can be customized by modifying:
- Colors palette
- Chart dimensions
- Hover information
- Labels and titles

---

## 📁 Project Files

```
graphs/
├── app.py                 # Main dashboard application
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

---

## ⌨️ Keyboard Shortcuts (in Streamlit)

- **Ctrl + Shift + M**: Toggle dark/light mode
- **Ctrl + Shift + R**: Rerun the app
- **R**: Rerun
- **Q**: Quit

---

## 🐛 Troubleshooting

### Issue: "streamlit: command not found"
**Solution:** Make sure you installed Streamlit: `pip install streamlit`

### Issue: Port 8501 is already in use
**Solution:** Run on a different port: `streamlit run app.py --server.port 8502`

### Issue: Charts not displaying
**Solution:** Clear cache and rerun: Press 'R' in the Streamlit interface

---

## 📧 Support

For issues or questions about the dashboard, please refer to:
- Streamlit Documentation: https://docs.streamlit.io/
- Plotly Documentation: https://plotly.com/python/
- Pandas Documentation: https://pandas.pydata.org/

---

## ✅ Research Information

**Project:** Gender Disparities in Knowledge of STIs among Out-of-School Youth
**Institution:** Mabini Colleges, Inc., Daet, Camarines Norte
**Department Advisor:** Dr. Caridad D. Garcia
**Partner Department:** College of Nursing (CON)
**Program:** Computational Science (Interactive Visualization)

---

Generated: March 2026
