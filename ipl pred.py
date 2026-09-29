from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

csv_path = Path(__file__).resolve().with_name("IPL2025Batters.csv")
output_dir = Path(__file__).resolve().parent / "outputs"
output_dir.mkdir(exist_ok=True)
df = pd.read_csv(csv_path)

# Display basic info
print("Dataset Preview:\n", df.head())
print("\nColumns:\n", df.columns)

df['Runs'] = pd.to_numeric(df['Runs'], errors='coerce')
df['SR'] = pd.to_numeric(df['SR'], errors='coerce')
df['AVG'] = pd.to_numeric(df['AVG'], errors='coerce')

# Drop null values
df.dropna(inplace=True)

# -----------------------------
top_runs = df.sort_values(by='Runs', ascending=False).head(10)

plt.figure(figsize=(10,5))
sns.barplot(x='Runs', y='Player Name', data=top_runs)
plt.title("Top 10 Run Scorers - IPL 2025")
plt.tight_layout()
plt.savefig(output_dir / "top_run_scorers.png", dpi=150, bbox_inches="tight")
plt.show()

print("\nTop Run Scorers:\n", top_runs[['Player Name','Runs']])

top_avg = df.sort_values(by='AVG', ascending=False).head(10)

plt.figure(figsize=(10,5))
sns.barplot(x='AVG', y='Player Name', data=top_avg)
plt.title("Top 10 Batting Average")
plt.tight_layout()
plt.savefig(output_dir / "top_batting_average.png", dpi=150, bbox_inches="tight")
plt.show()

top_sixes = df.sort_values(by='6s', ascending=False).head(10)

plt.figure(figsize=(10,5))
sns.barplot(x='6s', y='Player Name', data=top_sixes)
plt.title("Top 10 Six Hitters")
plt.tight_layout()
plt.savefig(output_dir / "top_six_hitters.png", dpi=150, bbox_inches="tight")
plt.show()

top_fours = df.sort_values(by='4s', ascending=False).head(10)

plt.figure(figsize=(10,5))
sns.barplot(x='4s', y='Player Name', data=top_fours)
plt.title("Top 10 Four Hitters")
plt.tight_layout()
plt.savefig(output_dir / "top_four_hitters.png", dpi=150, bbox_inches="tight")
plt.show()

team_runs = df.groupby('Team')['Runs'].sum().sort_values(ascending=False)

plt.figure(figsize=(10,5))
team_runs.plot(kind='bar')
plt.title("Team-wise Total Runs")
plt.xlabel("Team")
plt.ylabel("Runs")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(output_dir / "team_total_runs.png", dpi=150, bbox_inches="tight")
plt.show()
plt.figure(figsize=(8,5))
sns.scatterplot(x='Matches', y='Runs', data=df)
plt.title("Matches vs Runs")
plt.tight_layout()
plt.savefig(output_dir / "matches_vs_runs.png", dpi=150, bbox_inches="tight")
plt.show()

print("\n--- Key Insights ---")
print("1. Identified top run scorers in IPL 2025.")
print("2. Players with highest strike rates analyzed.")
print("3. Best average players identified.")
print("4. Power hitters (4s & 6s) analyzed.")
print("5. Team performance evaluated based on total runs.")

