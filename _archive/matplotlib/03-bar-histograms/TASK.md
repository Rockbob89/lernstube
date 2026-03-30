# Task 03: Bar Charts & Histograms

## Objective
Build grouped bars, stacked bars, horizontal bars, and histograms with full control.

## What to Learn
- `ax.bar()` / `ax.barh()`: width, align, color, edgecolor
- Grouped bars: offset positions with numpy arithmetic

```python
x = np.arange(len(categories))
width = 0.35
ax.bar(x - width/2, values_a, width, label="A")
ax.bar(x + width/2, values_b, width, label="B")
ax.set_xticks(x, categories)
```

- Stacked bars: `bottom` parameter

```python
ax.bar(x, values_a, label="A")
ax.bar(x, values_b, bottom=values_a, label="B")  # B starts where A ends
```

- `ax.hist()`: bins, density, histtype, cumulative
- Adding value labels on bars

```python
for bar in ax.patches:
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height(),
            f"{bar.get_height():.0f}", ha="center", va="bottom")
```

## Exercises

### 1. `grouped_bar_chart(categories, group_data)`
Side-by-side bars for each group. `group_data` maps group_name -> list of values (one per category). Add x-tick labels, legend. Return the Figure.

```python
fig = grouped_bar_chart(
    ["Q1", "Q2", "Q3", "Q4"],
    {"Product A": [20, 35, 30, 35], "Product B": [25, 32, 34, 20]}
)
```

### 2. `stacked_bar_chart(categories, group_data)`
Same input format as above but stacked. Add value labels in the center of each segment. Return the Figure.

```python
fig = stacked_bar_chart(
    ["Engineering", "Marketing", "Sales"],
    {"Salary": [500, 300, 200], "Tools": [100, 150, 50], "Travel": [50, 200, 150]}
)
```

### 3. `histogram_comparison(datasets, labels, bins=30)`
Overlay multiple histograms with transparency. Add legend and mean lines (vertical dashed) for each dataset. Return the Figure.

```python
rng = np.random.default_rng(42)
fig = histogram_comparison(
    [rng.normal(0, 1, 1000), rng.normal(2, 1.5, 1000)],
    ["Control", "Treatment"],
)
```
