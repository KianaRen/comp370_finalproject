import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Data preparation (with sorting)
data = {
    'Total': [97, 26, 126, 110, 146],
    'Positive': [11, 2, 49, 6, 47],
    'Neutral': [27, 19, 58, 35, 64],
    'Negative': [59, 5, 19, 69, 35]
}
categories = [
    'Canadian\nPolitics', 
    'International\nPolitics', 
    'Personal\nLife', 
    'Resignation', 
    'US Relations'
]
df = pd.DataFrame(data, index=categories)

# *** Sorting the DataFrame by 'Total' descending ***
df = df.sort_values(by='Total', ascending=False)

# Setup the Plotting Environment
plt.figure(figsize=(10, 4)) 
colors = {
    'Positive': "#7CCE7E",  # Green
    'Neutral': "#FFE597",   # Yellow/Amber
    'Negative': "#E67F78"   # Red
}

# *** New order for stacking ***
attitudes_order = ['Negative', 'Neutral', 'Positive'] 
# ... rest of the plotting code ...

# The initial position for stacking the bars
# 'Negative' will be at the bottom (x=0), so we only need a cumulative tracking variable
cumulative_counts = np.zeros(len(df)) 

# 3. Create the Stacked Bars
for attitude in attitudes_order:
    
    # Plot the current attitude segment
    plt.barh(
        y=df.index,
        width=df[attitude],
        left=cumulative_counts,
        height=0.3,
        color=colors[attitude],
        label=attitude
    )
    
    # Update the starting point for the next segment
    cumulative_counts += df[attitude]
    
    # Add text labels (count and percentage) to the segments
    for i, count in enumerate(df[attitude]):
        # Only label non-zero segments
        if count > 0:
            percentage = (count / df['Total'][i]) * 100
            
            # Position the text slightly right of the segment's start point
            text_x = cumulative_counts[i] - (count / 2) 
            
            plt.text(
                text_x, 
                i, # Y-position (index of the category)
                f'{count}', 
                ha='center', 
                va='center',
                color='black',
                fontsize=9
            )

# 4. Finalize the Chart
plt.title('Attitude Distribution by Category for Trudeau Related News Articles', fontsize=14)
plt.xlabel('Total Number of Articles')
plt.ylabel('Category')
plt.legend(title='Attitude', bbox_to_anchor=(1, 1), loc='upper right')
plt.grid(axis='x', linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()