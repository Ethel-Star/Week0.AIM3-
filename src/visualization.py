import matplotlib.pyplot as plt
import seaborn as sns

def plot_histograms(df, columns, title="Distribution of Columns"):
    """
    Plots histograms for the specified columns in the DataFrame.
    """
    missing_cols = [col for col in columns if col not in df.columns]
    if missing_cols:
        print(f"Warning: The following columns are missing and won't be plotted: {missing_cols}")
        columns = [col for col in columns if col in df.columns]

    num_columns = len(columns)
    plt.figure(figsize=(5 * num_columns, 4))
    for i, column in enumerate(columns, 1):
        plt.subplot(1, num_columns, i)
        sns.histplot(df[column], kde=True)
        plt.title(f'{column} Distribution')
    plt.tight_layout()
    plt.suptitle(title, y=1.02)
    plt.show()

def plot_pairplot(df, columns, title="Pairplot of Columns"):
    """
    Plots a pairplot for the specified columns in the DataFrame.
    """
    valid_cols = [col for col in columns if col in df.columns]
    if not valid_cols:
        print("No valid columns found for pairplot.")
        return

    sns.pairplot(df[valid_cols])
    plt.suptitle(title, y=1.02)
    plt.show()

def plot_correlation_heatmap(df, columns, title="Correlation Heatmap"):
    """
    Plots a heatmap of correlations for the specified columns.
    """
    valid_cols = [col for col in columns if col in df.columns]
    if len(valid_cols) < 2:
        print("At least two valid columns are required for a correlation heatmap.")
        return

    plt.figure(figsize=(10, 8))
    sns.heatmap(df[valid_cols].corr(), annot=True, cmap='coolwarm', fmt=".2f")
    plt.title(title)
    plt.show()

def plot_boxplot(df, columns, title="Boxplot of Columns"):
    """
    Plots a boxplot for the specified columns in the DataFrame.
    """
    valid_cols = [col for col in columns if col in df.columns]
    if not valid_cols:
        print("No valid columns found for boxplot.")
        return

    plt.figure(figsize=(12, 6))
    sns.boxplot(data=df[valid_cols])
    plt.title(title)
    plt.show()
def plot_bubble_chart(df, x, y, size, color=None, title="Bubble Chart", xlabel=None, ylabel=None):
    plt.figure(figsize=(10, 6))
    scatter = plt.scatter(
        df[x],
        df[y],
        s=df[size] * 10,  # Scale size for better visualization
        c=df[color] if color else 'blue',  # Color based on column or default blue
        alpha=0.6,
        edgecolors='w',
        cmap='viridis' if color else None
    )
    if color:
        plt.colorbar(scatter, label=color)
    
    plt.title(title)
    plt.xlabel(xlabel or x)
    plt.ylabel(ylabel or y)
    plt.grid(True)
    plt.show()
