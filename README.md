# iOS Themes

[![Action Status](https://github.com/basnijholt/lovelace-ios-themes/workflows/yamllint/badge.svg)](https://github.com/basnijholt/lovelace-ios-themes/actions)
[![hacs_badge](https://img.shields.io/badge/HACS-Default-orange.svg)](https://github.com/hacs/integration)
[![homeassistant_community](https://img.shields.io/badge/HA%20community-forum-brightgreen)](https://community.home-assistant.io/t/ios-dark-and-light-mode-with-easy-background-change/206215)
[![Github Stars](https://img.shields.io/github/stars/basnijholt/lovelace-ios-themes)](https://github.com/basnijholt/lovelace-ios-themes)

Forked from `basnijholt/lovelace-ios-themes`. This repository preserves the original MIT license and includes additional grey-theme variants.

Fork/HACS maintenance notes live in [`docs/FORK-MAINTENANCE.md`](docs/FORK-MAINTENANCE.md).

> The iOS Theme by @basnijholt and modified from @kalkih's [Gist](https://gist.github.com/kalkih/fbe84b371ef7f992c3bd51b235e2c299)

A generalized version of [*iOS Dark Mode Theme*](https://github.com/basnijholt/lovelace-ios-dark-mode-theme)!
This includes both **Dark and Light Mode** and 9 different HomeKit backgrounds.
Installing this theme adds 36 different themes:
- `ios-light-mode-dark-green`
- `ios-dark-mode-dark-green`
- `ios-light-mode-light-blue`
- `ios-dark-mode-light-blue`
- `ios-light-mode-light-green`
- `ios-dark-mode-light-green`
- `ios-light-mode-orange`
- `ios-dark-mode-orange`
- `ios-light-mode-blue-red`
- `ios-dark-mode-blue-red`
- `ios-light-mode-red`
- `ios-dark-mode-red`
- `ios-light-mode-dark-grey`
- `ios-dark-mode-dark-grey`
- `ios-light-mode-light-grey`
- `ios-dark-mode-light-grey`
- `ios-light-mode-dark-blue`
- `ios-dark-mode-dark-blue`
- `...` and versions with the `-alternative` suffix

---

## **🖼️ Backgrounds: Remote vs Local**

As of version **3.0.0**, we have introduced an alternative to Base64-encoded background images to boost performance.

By default, iOS Themes now use **remote background images** hosted on GitHub for faster caching and loading times. However, for users that prefer to host images locally on their Home Assistant setup (or in environments with poor internet connectivity), `-alternative` versions of the themes are available, which use locally hosted background images.

### **Remote Backgrounds (Default)**

- The default themes use background images stored in our GitHub repository.
- To switch to the default themes, no configuration beyond the installation steps is necessary.

### **Local Backgrounds (Alternative Versions)**

For the alternative themes, you will need to **download the images and store them locally** in your Home Assistant's `/config/www/ios-themes` directory. Home Assistant automatically serves files from the `www` folder under `/local/`.

---

<details>
<summary>📥 How to Download Backgrounds for Local Use (Alternative Themes)</summary>

### **Step-by-Step Local Background Setup**:

To use locally hosted background images, follow the instructions below.

1. **Create the necessary directory**:
   Open a terminal (or SSH into your Home Assistant setup) and run the following command to ensure the correct folder structure is in place:
   ```bash
   mkdir -p /config/www/ios-themes
   ```

2. **Download the background images**:
   Download the required background images using `wget` commands. This will store them in the `/config/www/ios-themes` folder.
   
   For example:
   ```bash
   # Dark Blue background
   wget -O /config/www/ios-themes/homekit-bg-dark-blue.jpg https://raw.githubusercontent.com/basnijholt/lovelace-ios-themes/master/themes/homekit-bg-dark-blue.jpg
   
   # Light Blue background
   wget -O /config/www/ios-themes/homekit-bg-dark-blue.jpg https://raw.githubusercontent.com/basnijholt/lovelace-ios-themes/master/themes/homekit-bg-light-blue.jpg
   
   # Add more backgrounds as needed for other themes
   ```

   Repeat the command for all the backgrounds you need (ensure to replace `dark-blue.jpg` with the appropriate background name from the themes you're using).

3. **Switch to the alternative theme**:
   In your Home Assistant profile settings, select the **alternative version** of the theme you want to use.  
   Example: `ios-dark-mode-dark-blue-alternative`

   **Important:** For images hosted locally, the background paths in the theme are referenced as `/local/ios-themes/...`.

---

### **Command Summary for Downloading Backgrounds**:

Here are commands to download all available backgrounds:

```bash
# Dark Blue
wget -O /config/www/ios-themes/homekit-bg-dark-blue.jpg https://raw.githubusercontent.com/basnijholt/lovelace-ios-themes/master/themes/homekit-bg-dark-blue.jpg

# Light Blue
wget -O /config/www/ios-themes/homekit-bg-light-blue.jpg https://raw.githubusercontent.com/basnijholt/lovelace-ios-themes/master/themes/homekit-bg-light-blue.jpg

# Dark Green
wget -O /config/www/ios-themes/homekit-bg-dark-green.jpg https://raw.githubusercontent.com/basnijholt/lovelace-ios-themes/master/themes/homekit-bg-dark-green.jpg

# Light Green
wget -O /config/www/ios-themes/homekit-bg-light-green.jpg https://raw.githubusercontent.com/basnijholt/lovelace-ios-themes/master/themes/homekit-bg-light-green.jpg

# Orange
wget -O /config/www/ios-themes/homekit-bg-orange.jpg https://raw.githubusercontent.com/basnijholt/lovelace-ios-themes/master/themes/homekit-bg-orange.jpg

# Blue Red
wget -O /config/www/ios-themes/homekit-bg-blue-red.jpg https://raw.githubusercontent.com/basnijholt/lovelace-ios-themes/master/themes/homekit-bg-blue-red.jpg

# Red
wget -O /config/www/ios-themes/homekit-bg-red.jpg https://raw.githubusercontent.com/basnijholt/lovelace-ios-themes/master/themes/homekit-bg-red.jpg

# Dark Grey
wget -O /config/www/ios-themes/homekit-bg-dark-grey.jpg https://raw.githubusercontent.com/tjuuljensen/lovelace-ios-themes/master/themes/homekit-bg-dark-grey.jpg

# Light Grey
wget -O /config/www/ios-themes/homekit-bg-light-grey.jpg https://raw.githubusercontent.com/tjuuljensen/lovelace-ios-themes/master/themes/homekit-bg-light-grey.jpg
```

---

After placing the images in the `/config/www/ios-themes/` directory, reload your Home Assistant theme settings (or restart Home Assistant) and enjoy using the responsive, locally hosted backgrounds!

</details>

---

## Screenshots

Screenshots of [my](https://github.com/basnijholt) Home-Assistant instance, [see the config files here :octocat:](https://github.com/basnijholt/home-assistant-config/).

Low quality `gif`, click [here](https://github.com/basnijholt/lovelace-ios-themes/raw/media/screenshots/overview.mp4) to see a `mp4` (or scroll down).

[![Theme - Overview](https://github.com/basnijholt/lovelace-ios-themes/raw/media/screenshots/overview.gif)](https://github.com/basnijholt/lovelace-ios-themes/raw/media/screenshots/overview.mp4)

### Overview

![Theme - Overview](https://github.com/basnijholt/lovelace-ios-themes/raw/media/screenshots/blue-red-dark.png)
![Theme - Overview](https://github.com/basnijholt/lovelace-ios-themes/raw/media/screenshots/blue-red-light.png)
![Theme - Overview](https://github.com/basnijholt/lovelace-ios-themes/raw/media/screenshots/dark-blue-dark.png)
![Theme - Overview](https://github.com/basnijholt/lovelace-ios-themes/raw/media/screenshots/dark-blue-light.png)
![Theme - Overview](https://github.com/basnijholt/lovelace-ios-themes/raw/media/screenshots/dark-green-dark.png)
![Theme - Overview](https://github.com/basnijholt/lovelace-ios-themes/raw/media/screenshots/dark-green-light.png)
![Theme - Overview](https://github.com/basnijholt/lovelace-ios-themes/raw/media/screenshots/light-blue-dark.png)
![Theme - Overview](https://github.com/basnijholt/lovelace-ios-themes/raw/media/screenshots/light-blue-light.png)
![Theme - Overview](https://github.com/basnijholt/lovelace-ios-themes/raw/media/screenshots/light-green-dark.png)
![Theme - Overview](https://github.com/basnijholt/lovelace-ios-themes/raw/media/screenshots/light-green-light.png)
![Theme - Overview](https://github.com/basnijholt/lovelace-ios-themes/raw/media/screenshots/orange-dark.png)
![Theme - Overview](https://github.com/basnijholt/lovelace-ios-themes/raw/media/screenshots/orange-light.png)
![Theme - Overview](https://github.com/basnijholt/lovelace-ios-themes/raw/media/screenshots/red-dark.png)
![Theme - Overview](https://github.com/basnijholt/lovelace-ios-themes/raw/media/screenshots/red-light.png)


## Installation

1. Installation of the themes with HACS.

* (If you do not have it yet) Install [HACS](https://hacs.xyz/docs/installation/manual).
* Go to the HACS Community Store.
* Click on the `THEMES` tab.
* Search and install the `iOS Themes`.

2. Add the following code to your `configuration.yaml` file (reboot required).

```yaml
frontend:
  ... # your configuration.
  themes: !include_dir_merge_named themes
  ... # your configuration.
```

3. Add the following line to your `lovelace-ui.yaml` or use the RAW editor:
```yaml
background: var(--background-image)
```

So the end result will be something like [this example](https://github.com/basnijholt/home-assistant-config/blob/master/lovelace-ui.yaml).

## Automations to easily switch
**WARNING: if you want to switch themes using automations, you need to go to your profile and select "Backend-selected" for Theme!**

It is recommended to use [these automations (`basnijholt/home-assistant-config/automations/frontend.yaml`)](https://github.com/basnijholt/home-assistant-config/blob/master/automations/frontend.yaml) in combination with these:
```yaml
input_select:
  theme:
    options:
      - blue-red
      - dark-blue
      - dark-green
      - light-blue
      - light-green
      - orange
      - red
      - dark-grey
      - light-grey
    icon: mdi:format-color-fill
  
input_boolean:
  dark_mode:
    name: Dark mode
    icon: mdi:theme-light-dark
  theme_alternative:
    name: Theme alternative (disable active state color)
```
Then add `input_select.theme`, `input_boolean.theme_alternative`, and `input_boolean.dark_mode` to your Lovelace UI.


## How does the code work

All the **36(!)** themes in [`themes/`](themes/) are **automatically generated** using [`create-themes.py`](create-themes.py) and the information in [`settings-light-dark.yaml`](settings-light-dark.yaml) is passed into [`template.jinja2`](template.jinja2).
The resulting file is [`themes/ios-themes.yaml`](themes/ios-themes.yaml) which contains all variants (different backgrounds and dark/light mode).
