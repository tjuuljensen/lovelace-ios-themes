# Fork Maintenance

This repository is a personal fork of `basnijholt/lovelace-ios-themes`.

The goal is to keep upstream compatibility work from `basnijholt` while adding
a small set of local color/background variants.

## Current Configuration

Use these Git remotes:

```text
origin    https://github.com/tjuuljensen/lovelace-ios-themes.git
upstream  https://github.com/basnijholt/lovelace-ios-themes.git
```

`origin` is the fork that Home Assistant / HACS installs from. `upstream` is the
canonical source for updates.

The maintained branch for this fork is `master`.

`upstream` should be fetch-only. Keep its push URL disabled:

```powershell
git remote set-url --push upstream DISABLED
```

Check the setup:

```powershell
git remote -v
git branch -vv
```

Expected:

- `master` tracks `origin/master`
- `upstream` fetch points to `basnijholt/lovelace-ios-themes`
- `upstream` push shows `DISABLED`

## Local Fork Changes

This fork should stay close to upstream. The expected local differences are:

- extra `themes/homekit-bg-*.jpg` background files
- matching color entries in `create-themes.py`
- generated theme entries in `themes/ios-themes.yaml`
- README and this maintenance document

Avoid carrying unrelated Home Assistant frontend experiments in this branch.
If a visual fix is needed later, keep it as a separate branch until it is tested
in a running Home Assistant instance.

Current local color variants include:

```text
dark-grey
light-grey
magenta-purple
navy-purple
teal-cyan
```

## HACS Setup

Install this fork as a HACS custom repository:

1. Open **HACS** in Home Assistant.
2. Open the three-dot menu.
3. Select **Custom repositories**.
4. Add this repository URL:

   ```text
   https://github.com/tjuuljensen/lovelace-ios-themes
   ```

5. Select **Theme** as the category.
6. Install **iOS Themes - Dark Mode and Light Mode**.
7. Make sure Home Assistant loads themes:

   ```yaml
   frontend:
     themes: !include_dir_merge_named themes
   ```

8. Restart Home Assistant or reload themes after installation or updates.

Do not add this repository as a Dashboard or Plugin custom repository. If HACS
says `Repository structure for master is not compliant` and prefixes the message
with `<Plugin ...>`, remove that custom repository entry and add it again as
category **Theme**.

For dashboard backgrounds, set this at the dashboard raw config top level:

```yaml
background: var(--background-image)
```

## CDN And Local Backgrounds

The generated standard themes use jsDelivr URLs like this:

```text
https://cdn.jsdelivr.net/gh/tjuuljensen/lovelace-ios-themes@master/themes/homekit-bg-dark-grey.jpg
```

Because those URLs reference `@master`, the image files must exist on the
`master` branch. That is why `master` is the maintained branch for this fork.

Images rarely change. If an image is changed and jsDelivr still serves the old
file, purge the exact URL with jsDelivr's purge tool:

```text
https://www.jsdelivr.com/tools/purge
```

The `-alternative` themes use local `/local/ios-themes/...` paths. Home
Assistant maps `/local/...` to `/config/www/...`, so those images must be copied
to `/config/www/ios-themes` if you use alternative themes.

HACS does not run arbitrary post-install copy scripts for safety. Copying local
backgrounds is a manual step or a Home Assistant automation/script that you own.

Manual copy from an SSH/terminal session on Home Assistant:

```bash
mkdir -p /config/www/ios-themes

wget -O /config/www/ios-themes/homekit-bg-blue-red.jpg https://raw.githubusercontent.com/tjuuljensen/lovelace-ios-themes/master/themes/homekit-bg-blue-red.jpg
wget -O /config/www/ios-themes/homekit-bg-dark-blue.jpg https://raw.githubusercontent.com/tjuuljensen/lovelace-ios-themes/master/themes/homekit-bg-dark-blue.jpg
wget -O /config/www/ios-themes/homekit-bg-dark-green.jpg https://raw.githubusercontent.com/tjuuljensen/lovelace-ios-themes/master/themes/homekit-bg-dark-green.jpg
wget -O /config/www/ios-themes/homekit-bg-dark-grey.jpg https://raw.githubusercontent.com/tjuuljensen/lovelace-ios-themes/master/themes/homekit-bg-dark-grey.jpg
wget -O /config/www/ios-themes/homekit-bg-light-blue.jpg https://raw.githubusercontent.com/tjuuljensen/lovelace-ios-themes/master/themes/homekit-bg-light-blue.jpg
wget -O /config/www/ios-themes/homekit-bg-light-green.jpg https://raw.githubusercontent.com/tjuuljensen/lovelace-ios-themes/master/themes/homekit-bg-light-green.jpg
wget -O /config/www/ios-themes/homekit-bg-light-grey.jpg https://raw.githubusercontent.com/tjuuljensen/lovelace-ios-themes/master/themes/homekit-bg-light-grey.jpg
wget -O /config/www/ios-themes/homekit-bg-magenta-purple.jpg https://raw.githubusercontent.com/tjuuljensen/lovelace-ios-themes/master/themes/homekit-bg-magenta-purple.jpg
wget -O /config/www/ios-themes/homekit-bg-navy-purple.jpg https://raw.githubusercontent.com/tjuuljensen/lovelace-ios-themes/master/themes/homekit-bg-navy-purple.jpg
wget -O /config/www/ios-themes/homekit-bg-orange.jpg https://raw.githubusercontent.com/tjuuljensen/lovelace-ios-themes/master/themes/homekit-bg-orange.jpg
wget -O /config/www/ios-themes/homekit-bg-red.jpg https://raw.githubusercontent.com/tjuuljensen/lovelace-ios-themes/master/themes/homekit-bg-red.jpg
wget -O /config/www/ios-themes/homekit-bg-teal-cyan.jpg https://raw.githubusercontent.com/tjuuljensen/lovelace-ios-themes/master/themes/homekit-bg-teal-cyan.jpg
```

After copying, reload themes or restart Home Assistant.

## Updating From Upstream

When upstream changes:

```powershell
git switch master
git fetch upstream
git rebase upstream/master
python create-themes.py
python -m py_compile create-themes.py
python -c "import yaml; yaml.safe_load(open('themes/ios-themes.yaml', encoding='utf-8'))"
git diff --check
```

Then inspect the fork delta:

```powershell
git diff --stat upstream/master..HEAD
git diff upstream/master..HEAD -- create-themes.py README.md docs/FORK-MAINTENANCE.md
```

Expected differences should remain small and related to the custom color
variants. If upstream changed `template.jinja2` or `settings-light-dark.yaml`,
rerunning `create-themes.py` should carry those upstream changes into the
generated theme file.

Publish normal updates:

```powershell
git push origin master
```

If the branch was intentionally rebuilt/squashed, publish with:

```powershell
git push --force-with-lease origin master
```

Use `--force-with-lease`, not plain `--force`, because it checks that the remote
branch has not moved unexpectedly.

## Troubleshooting

### HACS Still Shows The Old Theme

- Confirm HACS is installed from `https://github.com/tjuuljensen/lovelace-ios-themes`.
- Confirm the custom repository category is **Theme**.
- Confirm the GitHub default branch is `master`.
- In HACS, redownload or update the theme.
- Restart Home Assistant or reload themes.
- Clear browser cache if dashboard assets still look stale.

### HACS Says Repository Structure Is Not Compliant

- Confirm the custom repository category is **Theme**.
- If it was added as Dashboard or Plugin, remove it from HACS custom
  repositories and add it again as **Theme**.
- Confirm `hacs.json` exists on `master`.
- Confirm `themes/ios-themes.yaml` exists on `master`.

### Custom Theme Names Are Missing

Check that `themes/ios-themes.yaml` contains the expected names:

```powershell
rg "dark-grey|light-grey|magenta-purple|navy-purple|teal-cyan" themes/ios-themes.yaml
```

If not, rerun:

```powershell
python create-themes.py
```

### Backgrounds Do Not Load

For standard themes:

- confirm `themes/ios-themes.yaml` references `cdn.jsdelivr.net/gh/tjuuljensen/lovelace-ios-themes@master`
- confirm the referenced image exists on the remote `master` branch
- purge the jsDelivr URL if the image recently changed

For `-alternative` themes:

- confirm the image exists in `/config/www/ios-themes`
- confirm Home Assistant serves it at `/local/ios-themes/<filename>.jpg`
- reload themes or restart Home Assistant after copying files

### Git Tries To Push To Upstream

Check branch tracking:

```powershell
git branch -vv
```

`master` should track `origin/master`, not `upstream/master`.

Confirm upstream push is disabled:

```powershell
git remote -v
```

The upstream push URL should show `DISABLED`.

### Unsure Whether A Local Change Is Worth Keeping

Compare the fork to upstream:

```powershell
git diff --stat upstream/master..HEAD
git diff upstream/master..HEAD
```

Keep changes only when they are part of the custom color variants or clearly
documented as intentional fork behavior. For Home Assistant frontend rendering
issues, test in the running HA instance; many visual behaviors cannot verify
statically.
