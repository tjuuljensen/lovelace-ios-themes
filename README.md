# iOS Themes Extended

[![Action Status](https://github.com/tjuuljensen/lovelace-ios-themes/workflows/yamllint/badge.svg)](https://github.com/tjuuljensen/lovelace-ios-themes/actions)
[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/hacs/integration)
[![homeassistant_community](https://img.shields.io/badge/HA%20community-forum-brightgreen)](https://community.home-assistant.io/t/ios-dark-and-light-mode-with-easy-background-change/206215)
[![Github Stars](https://img.shields.io/github/stars/tjuuljensen/lovelace-ios-themes)](https://github.com/tjuuljensen/lovelace-ios-themes)

Forked from `imonlinux/lovelace-ios-themes`, itself a fork of `basnijholt/lovelace-ios-themes`. This repository preserves the original MIT license and includes additional grey-theme variants ported from my earlier fork, `tjuuljensen/lovelace-ios-themes-old`.

> The iOS Theme by @basnijholt and modified from @kalkih's [Gist](https://gist.github.com/kalkih/fbe84b371ef7f992c3bd51b235e2c299)

A generalized version of [*iOS Dark Mode Theme*](https://github.com/basnijholt/lovelace-ios-dark-mode-theme).
This fork includes both **Dark and Light Mode** and 9 different HomeKit backgrounds.
Installing this theme adds 36 different themes:

- `ios-light-mode-blue-red`
- `ios-dark-mode-blue-red`
- `ios-light-mode-dark-blue`
- `ios-dark-mode-dark-blue`
- `ios-light-mode-dark-green`
- `ios-dark-mode-dark-green`
- `ios-light-mode-light-blue`
- `ios-dark-mode-light-blue`
- `ios-light-mode-light-green`
- `ios-dark-mode-light-green`
- `ios-light-mode-orange`
- `ios-dark-mode-orange`
- `ios-light-mode-red`
- `ios-dark-mode-red`
- `ios-light-mode-dark-grey`
- `ios-dark-mode-dark-grey`
- `ios-light-mode-light-grey`
- `ios-dark-mode-light-grey`
- `...` and versions with the `-alternative` suffix

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

### HACS

This fork is not part of the default HACS repository list. Add it as a custom repository first:

1. Install and configure [HACS](https://www.hacs.xyz/docs/use/download/download/) if you do not already have it.
2. In Home Assistant, open **HACS** from the sidebar.
3. Open the three-dot menu in the top right and choose **Custom repositories**.
4. Add `https://github.com/tjuuljensen/lovelace-ios-themes`.
5. Select **Theme** as the category.
6. Click **Add**, then install **iOS Themes - Dark Mode and Light Mode** from HACS.

After installation, add the following to your `configuration.yaml` and restart Home Assistant:

```yaml
frontend:
  themes: !include_dir_merge_named themes
```

### Manual

Copy `themes/ios-themes.yaml` and the `homekit-bg-*.jpg` files into a folder under your Home Assistant `themes` directory, for example:

```text
/config/themes/ios-themes/
```

Then make sure Home Assistant loads the themes directory:

```yaml
frontend:
  themes: !include_dir_merge_named themes
```

Restart Home Assistant or reload themes after changing the files.

## Dashboard Background

Open your dashboard, select **Edit dashboard** (pencil icon) -> **Open dashboard menu** -> **Raw configuration editor**, and add this at the top level:

```yaml
background: var(--background-image)
```

So the end result will be something like [this example](https://github.com/basnijholt/home-assistant-config/blob/master/lovelace-ui.yaml).

## Automations To Easily Switch

**Note:** To switch themes via automations or the UI helpers below, go to your profile (**Settings** -> **[your name]**) and set **Theme** to **Backend-selected**.

It is recommended to use [these automations (`basnijholt/home-assistant-config/automations/frontend.yaml`)](https://github.com/basnijholt/home-assistant-config/blob/master/automations/frontend.yaml) in combination with these helpers:

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

You can define these helpers in `configuration.yaml` as shown above, or create them via **Settings** -> **Devices & services** -> **Helpers**. Then add `input_select.theme`, `input_boolean.theme_alternative`, and `input_boolean.dark_mode` to your dashboard.

## What Extended Means

The extended part is intentionally small. This fork keeps the original theme generation model and adds two grey HomeKit backgrounds, producing the extra `dark-grey` and `light-grey` theme families in both light and dark modes. It also carries compatibility updates for newer Home Assistant frontend variables.

## Changes From The Original Repo

- Added `homekit-bg-dark-grey.jpg` and `homekit-bg-light-grey.jpg`.
- Added `dark-grey` and `light-grey` theme families.
- Increased the generated theme set from 28 to 36 variants.
- Updated generated CDN links to this fork.
- Updated Home Assistant 2025.5+ theme variables after Polymer `paper-*` component removal.
- Added Home Assistant 2026.4+ form background variables for Web Awesome input components.
- Updated this README to document custom HACS installation for the fork.

## Compatibility

### HA 2025.5+

This theme has been modernized to remove deprecated variables and add support for UI components introduced in Home Assistant 2025.5.

**Removed** (Polymer/`paper-*` components were removed in HA 2025.5):

- `paper-slider-*` - sliders now follow `--primary-color` / `--accent-color` automatically
- `paper-toggle-button-*` - switches use `switch-checked-*` variables
- `paper-listbox-background-color`
- `paper-card-background-color`
- `paper-item-icon-color` / `paper-item-icon-active-color`
- Vaadin `--vaadin-text-field-*` input variables

**Updated:**

- `paper-dialog-background-color` -> `dialog-background-color`

**Added** (view tab styling for `ha-tabs` / `sl-tab` in HA 2025.5+):

- `app-header-selection-bar-color` - active view tab indicator bar color
- `sl-color-primary-600` - active view tab text/icon color
- `sl-color-neutral-600` - inactive view tab text/icon color

### HA 2026.4+

HA 2026.4 migrated input components from Material Design (`ha-textfield`) to Web Awesome (`ha-input`) and introduced semantic form background variables that default to a near-white neutral color.

Without theme overrides, dark mode themes can render `select` and other input entity rows with a near-white background while `--primary-text-color` remains `#FFF`, producing invisible white-on-white text.

This fork sets the following variables for generated themes:

- `ha-color-form-background`
- `ha-color-form-background-hover`
- `ha-color-form-background-disabled`

## How The Code Works

All 36 themes in [`themes/`](themes/) are automatically generated using [`create-themes.py`](create-themes.py). Shared light/dark values come from [`settings-light-dark.yaml`](settings-light-dark.yaml), and the generated YAML is rendered through [`template.jinja2`](template.jinja2).

The resulting file is [`themes/ios-themes.yaml`](themes/ios-themes.yaml), which contains all background, dark/light, and standard/alternative variants.

## Potential Improvements

- Add updated screenshots for the grey variants.
- Add release tags so HACS users get clearer versioned updates.
- Move the generator commit reference into one documented release variable.
- Review newer Home Assistant frontend variables as the Web Awesome migration continues.
- Add a small validation workflow that regenerates `themes/ios-themes.yaml` and fails when generated output is stale.
