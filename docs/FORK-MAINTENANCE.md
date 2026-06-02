# Fork Maintenance

This repository is a personal fork of `basnijholt/lovelace-ios-themes`.

The maintenance goal is simple:

- Let upstream development drive fixes and compatibility updates.
- Keep only the local grey theme variants in this fork.
- Avoid carrying unrelated Home Assistant frontend experiments unless they are
  intentionally reintroduced as separate, documented changes.

## Repository Model

Use these remotes:

```text
origin    https://github.com/tjuuljensen/lovelace-ios-themes.git
upstream  https://github.com/basnijholt/lovelace-ios-themes.git
```

`origin` is the repository Home Assistant / HACS should install from.
`upstream` is read-only source material for future updates.

The GitHub default branch for this fork is `feature/new-colors`. That branch is
the maintained fork branch:

- it starts from `basnijholt/lovelace-ios-themes`
- it adds only the grey theme variants and fork documentation
- it is the branch HACS should see when adding this repository as a custom theme

The local `master` branch may still exist as an old historical branch. Do not
develop on it. Do not merge it into `feature/new-colors`.

As a local safety guard, set the upstream push URL to a disabled value:

```powershell
git remote set-url --push upstream DISABLED
```

The fork should normally contain only these local differences from upstream:

- `themes/homekit-bg-dark-grey.jpg`
- `themes/homekit-bg-light-grey.jpg`
- `dark-grey` and `light-grey` entries in `create-themes.py`
- regenerated `themes/ios-themes.yaml`
- small README/documentation updates explaining the grey variants

## HACS Setup

Because the grey variants are not intended for upstream right now, install this
fork as a HACS custom repository.

1. In Home Assistant, open **HACS**.
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

For dashboard backgrounds, set this at the dashboard raw config top level:

```yaml
background: var(--background-image)
```

## Branches And Publishing

The configured repository default branch is `feature/new-colors`. Keep that as the
source of truth for this fork.

Normal publishing command:

```powershell
git push origin feature/new-colors
```

If a local clone still has the old branch setup, use this once:

```powershell
git branch --set-upstream-to origin/feature/new-colors feature/new-colors
```

Avoid plain `git push` until `git branch -vv` shows `feature/new-colors` tracking
`origin/feature/new-colors`.

`master` is not the development branch for this fork. If it exists on GitHub, it
is only a compatibility or historical branch. Do not force-push `master` unless
you intentionally want to make `master` match `feature/new-colors` for a tool that
cannot follow the default branch.

## Updating From Upstream

When upstream changes, update the fork like this:

```powershell
git switch feature/new-colors
git fetch upstream
git rebase upstream/master
python create-themes.py
python -m py_compile create-themes.py
python -c "import yaml; yaml.safe_load(open('themes/ios-themes.yaml', encoding='utf-8'))"
git diff --check
```

Then inspect the diff:

```powershell
git diff --stat upstream/master..HEAD
git diff upstream/master..HEAD -- create-themes.py README.md docs/FORK-MAINTENANCE.md
```

Expected differences should remain small:

- grey background images
- grey color entries
- generated grey theme sections
- fork maintenance documentation

If upstream changed `template.jinja2` or `settings-light-dark.yaml`, rerunning
`create-themes.py` should carry those upstream changes into the generated theme
file.

Publish the updated fork:

```powershell
git push origin feature/new-colors
```

No force push is needed for normal updates because `feature/new-colors` is the
default branch.

## Troubleshooting

### HACS Still Shows The Old Theme

- Confirm HACS is installed from `https://github.com/tjuuljensen/lovelace-ios-themes`.
- Confirm the GitHub default branch is `feature/new-colors`.
- Confirm `origin/feature/new-colors` contains the grey changes.
- In HACS, redownload or update the theme.
- Restart Home Assistant or reload themes.
- Clear browser cache if dashboard assets still look stale.

### HACS Says Repository Structure Is Not Compliant

- Confirm the custom repository category is **Theme**.
- If it was added as Dashboard or Plugin, remove it from HACS custom
  repositories and add it again as **Theme**.
- Confirm `hacs.json` exists in the default branch.
- Confirm `themes/ios-themes.yaml` exists in the default branch.

### Grey Theme Names Are Missing

Check that `themes/ios-themes.yaml` contains these names:

```text
ios-light-mode-dark-grey
ios-dark-mode-dark-grey
ios-light-mode-light-grey
ios-dark-mode-light-grey
```

If not, rerun:

```powershell
python create-themes.py
```

### Grey Backgrounds Do Not Load

The standard theme variants use jsDelivr URLs generated from `create-themes.py`.
The alternative variants use local `/local/ios-themes/...` background paths.

Check:

- the two grey JPG files exist in `themes/`
- `themes/ios-themes.yaml` references `tjuuljensen/lovelace-ios-themes`
- Home Assistant has downloaded the latest HACS files
- dashboard raw config contains `background: var(--background-image)`

### Git Tries To Push To Upstream

Check branch tracking:

```powershell
git branch -vv
```

If `feature/new-colors` tracks `upstream/master`, remove that tracking:

```powershell
git branch --unset-upstream feature/new-colors
```

Confirm upstream push is disabled:

```powershell
git remote -v
```

The upstream push URL should show `DISABLED`.

Then set the correct tracking branch:

```powershell
git branch --set-upstream-to origin/feature/new-colors feature/new-colors
```

### Unsure Whether A Local Change Is Worth Keeping

Compare the fork to upstream:

```powershell
git diff --stat upstream/master..HEAD
git diff upstream/master..HEAD
```

Keep changes only when they are part of the grey theme or clearly documented as
intentional fork behavior. For Home Assistant frontend rendering issues, test in
the running HA instance; many visual behaviors cannot verify statically.
