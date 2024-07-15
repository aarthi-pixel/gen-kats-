import pandas as pd
import ipywidgets as widgets
from IPython.display import display, clear_output, Image, HTML
import os

# Load CSV files (adjust the path or URL as necessary)
mushroom_biryani_df = pd.read_csv('/content/mushroom_biryani_ingredients.csv', index_col=0)
vegetable_biryani_df = pd.read_csv('/content/vegetable_biryani_ingredients.csv', index_col=0)
fish_biryani_df = pd.read_csv('/content/fish_biryani_ingredients.csv', index_col=0)
chicken_biryani_df = pd.read_csv('/content/chicken_biryani_ingredients.csv', index_col=0)

# Dropdown widget for selecting veg/non-veg option
veg_nonveg_dropdown = widgets.Dropdown(
    options=['Vegetarian', 'Non-Vegetarian'],
    value='Vegetarian',
    description='Type:'
)

# Dropdown widget for selecting biryani type
biryani_type_dropdown = widgets.Dropdown(
    options=['Mushroom Biryani', 'Vegetable Biryani'],
    value='Mushroom Biryani',
    description='Biryani Type:'
)

# Function to update biryani types based on veg/non-veg selection
def update_biryani_options(change):
    if change['new'] == 'Vegetarian':
        biryani_type_dropdown.options = ['Mushroom Biryani', 'Vegetable Biryani']
        biryani_type_dropdown.value = 'Mushroom Biryani'
    else:
        biryani_type_dropdown.options = ['Chicken Biryani', 'Fish Biryani']
        biryani_type_dropdown.value = 'Chicken Biryani'

# Observe changes in veg/non-veg dropdown
veg_nonveg_dropdown.observe(update_biryani_options, names='value')

# Slider for entering quantity
quantity_slider = widgets.IntSlider(
    value=1,
    min=1,
    max=10,
    step=1,
    description='Quantity (kg):',
    disabled=False,
    continuous_update=False,
    orientation='horizontal',
    readout=True,
    readout_format='d'
)

# Button to trigger ingredient display
display_button = widgets.Button(
    description='Show Ingredients',
    disabled=False,
    button_style='info',
    tooltip='Click to show ingredients'
)

# Output widget for displaying ingredients
output = widgets.Output()

# Function to handle button click and display ingredients
def show_ingredients(button):
    with output:
        clear_output()  # Clear previous output
        biryani_type = biryani_type_dropdown.value
        quantity = quantity_slider.value

        if biryani_type == 'Mushroom Biryani':
            df = mushroom_biryani_df
        elif biryani_type == 'Vegetable Biryani':
            df = vegetable_biryani_df
        elif biryani_type == 'Chicken Biryani':
            df = chicken_biryani_df
        elif biryani_type == 'Fish Biryani':
            df = fish_biryani_df
        else:
            print("Invalid biryani type")

        if quantity in df.index:
            ingredients = df.loc[quantity].to_dict()

            # Display the headline
            display(HTML(f"<h2 style='color: darkblue;'>INGREDIENTS TO COOK</h2>"))

            # Display the ingredients
            print(f"{biryani_type} Ingredients for {quantity} kg:")
            for ingredient, amount in ingredients.items():
                print(f"{ingredient}: {amount}")

            # Display the vessel selection headline
            display(HTML(f"<h2 style='color: darkblue;'>VESSEL SELECTION</h2>"))

            # Display the vessel image if it exists
            vessel_image_path = "/content/vessel.png"
            if os.path.exists(vessel_image_path):
                display(Image(vessel_image_path, width=300, height=300))
            else:
                print("")

            # Display the corresponding image
            image_path = f"/content/{quantity}kg.png"
            if os.path.exists(image_path):
                display(Image(image_path, width=400, height=400))
            else:
                print(f"No image found for {quantity} kg {biryani_type}.")
        else:
            print(f"No data found for {quantity} kg {biryani_type}")

# Link button click to function
display_button.on_click(show_ingredients)

# Display widgets
display(veg_nonveg_dropdown, biryani_type_dropdown, quantity_slider, display_button, output)
