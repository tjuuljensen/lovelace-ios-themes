# Render themes, creates them as separate files and as
# one combined file `ios-themes.yaml`.
# Part of https://github.com/tjuuljensen/lovelace-ios-themes
#
# This is a rewritten version of the original https://github.com/basnijholt/lovelace-ios-themes
# The alternative version which basnijholt uses, has been written out as I do not use it.
#
# iPhone seems to ALWAYS choose colors depending on the phone's dark mode sttings

from pathlib import Path
import jinja2
import yaml
from PIL import Image

# Load settings
with open("settings-light-dark.yaml", "r") as f:
    all_settings = yaml.safe_load(f)

def average_color(fname):
    """Calculate average color from an image and return it as a properly formatted rgba string."""
    with Image.open(fname) as img:
        img = img.convert('RGB')  # Ensure it's in RGB mode
        color = img.resize((1, 1)).getpixel((0, 0))
    return f'"rgba({color[0]}, {color[1]}, {color[2]}, 0.4)"'

def parse(x):
    """Encapsulate hex color codes in quotes to ensure proper YAML formatting."""
    return f'"{x}"' if x.startswith('#') else x

# Background colors, some predefined
BACKGROUND_COLORS = {
    # Suggested by @okets in issue #42
    "blue-red": "rgba(30, 2, 61, 0.4)",
    "dark-blue": "rgba(48, 69, 124, 0.4)",
    "dark-green": "rgba(48, 89, 71, 0.4)",
    "dark-grey": "rgba(82, 82, 82, 0.4)",
    "light-blue": "rgba(1, 195, 220, 0.4)",
    "light-green": "rgba(114, 188, 139, 0.4)",
    "light-grey": "rgba(45, 45, 45, 0.4)",
    "orange": "rgba(255, 229, 116, 0.4)",
    "red": "rgba(234, 88, 63, 0.4)"
}

# Jinja environment setup
env = jinja2.Environment(loader=jinja2.FileSystemLoader('./'))
template = env.get_template('template.jinja2')

# Define output file path
output_path = Path("themes/ios-themes.yaml")
output_path.parent.mkdir(parents=True, exist_ok=True)

# Write the combined file
with output_path.open("w") as f:
    f.write("# Generated iOS Themes\n")

    # Iterate over backgrounds and generate themes
    for background in sorted(Path("themes").glob("homekit-bg-*.jpg")):
        color = background.stem.split("homekit-bg-")[-1]
        if color in BACKGROUND_COLORS:
            app_header_background_color = BACKGROUND_COLORS[color]
        else:
            app_header_background_color = average_color(background)

        # Prepare settings for both light and dark modes, parsing as needed
        settings = {key: {mode: parse(all_settings[key][mode]) for mode in ['light', 'dark']} for key in all_settings}

        # Render template
        result = template.render(
            color=color,
            folder='hacsfiles',  # Adjust as necessary
            background_jpg=background.name,
            app_header_background_color=app_header_background_color,
            **settings
        )

        # Write to file
        f.write(result + "\n")

# Print success message
print("Themes generated successfully.")
