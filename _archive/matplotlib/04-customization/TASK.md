# Task 04: Customization

## Objective
Control every visual aspect of a matplotlib figure: colors, themes, fonts, ticks, grids, and rcParams.

## What to Learn
- `rcParams`: setting defaults globally vs per-figure

```python
plt.rcParams["font.size"] = 14          # global, affects all subsequent figures
fig, ax = plt.subplots()
ax.set(title="big font")
plt.rcParams.update(plt.rcParamsDefault) # reset
```

- Built-in styles: `plt.style.use()`, `plt.style.context()`

```python
plt.style.use("ggplot")        # permanent for this session
with plt.style.context("dark_background"):
    fig, ax = plt.subplots()   # only applies inside the block
    ax.plot([1, 2, 3])
```

- Custom colormaps and color cycles
- Tick formatting: `FuncFormatter`, `MaxNLocator`, `MultipleLocator`

```python
from matplotlib.ticker import FuncFormatter, MultipleLocator
ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: f"{v:.0%}"))
ax.xaxis.set_major_locator(MultipleLocator(2))  # tick every 2 units
```

- Spine manipulation: hiding, moving

```python
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
```

- Grid customization: which, axis, linestyle

## Exercises

### 1. `apply_style_context(style_name, plot_func)`
Run `plot_func()` inside a `plt.style.context(style_name)` and return the resulting Figure. `plot_func` takes no args and returns a Figure.

```python
def my_plot():
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3], [1, 4, 9])
    return fig

fig = apply_style_context("ggplot", my_plot)
```

### 2. `clean_axis_plot(x, y)`
Plot y vs x with: no top/right spines, major grid (light gray, dashed), y-axis formatted as percentages (values are 0-1), x-ticks at multiples of 2. Return the Figure.

```python
x = np.arange(0, 20, 0.5)
y = np.random.default_rng(42).uniform(0, 1, len(x))
fig = clean_axis_plot(x, y)
```

### 3. `custom_colormap_heatmap(data, cmap_colors=None)`
Display a 2D array as a heatmap. If `cmap_colors` is provided (list of colors), build a `LinearSegmentedColormap` from them. Add a colorbar with a label "Intensity". Return the Figure.

```python
data = np.random.default_rng(42).normal(size=(10, 10))
fig = custom_colormap_heatmap(data, cmap_colors=["#000000", "#ff6600", "#ffff00"])
```
