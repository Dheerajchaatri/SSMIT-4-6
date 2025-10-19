import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("📊 Student Performance Analyzer (Simple)")
st.write("Place 'StudentsPerformance.csv' next to app.py and run: streamlit run app.py")

# Load CSV
csv_name = "StudentsPerformance.csv"
try:
    df = pd.read_csv(csv_name)
except FileNotFoundError:
    st.error(f"Could not find '{csv_name}'. Download from Kaggle and put it next to app.py.")
    st.stop()

# Rename columns we use
df = df.rename(columns={
    "math score": "math_score",
    "reading score": "reading_score",
    "writing score": "writing_score"
})

# Create average
df["average_score"] = (df["math_score"] + df["reading_score"] + df["writing_score"]) / 3

# Show first rows
if st.checkbox("Show first 5 rows"):
    st.dataframe(df.head())

st.header("1) Descriptive Stats (Simple)")
st.write("Math mean:", float(df["math_score"].mean()))
st.write("Math median:", float(df["math_score"].median()))
st.write("Math mode:", float(df["math_score"].mode()[0]))
st.write("Reading mean:", float(df["reading_score"].mean()))
st.write("Writing mean:", float(df["writing_score"].mean()))
st.write("Average of averages:", float(df["average_score"].mean()))

st.header("2) Standard Deviation")
st.write(df[["math_score","reading_score","writing_score"]].std())

st.header("3) Correlation Heatmap")
fig1, ax1 = plt.subplots()
sns.heatmap(df[["math_score","reading_score","writing_score","average_score"]].corr(), annot=True, cmap="coolwarm", ax=ax1)
st.pyplot(fig1)

st.header("4) Histogram of Math Scores")
fig2, ax2 = plt.subplots()
ax2.hist(df["math_score"], bins=10)
ax2.set_xlabel("Math Score")
ax2.set_ylabel("Count")
st.pyplot(fig2)

st.header("5) Average Score by Gender (Bar)")
if "gender" in df.columns:
    means = df.groupby("gender")["average_score"].mean()
    fig3, ax3 = plt.subplots()
    ax3.bar(means.index, means.values)
    ax3.set_xlabel("Gender")
    ax3.set_ylabel("Average Score")
    st.pyplot(fig3)
else:
    st.info("Column 'gender' not found. Skipping bar plot.")

