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
`upstream` is read-only source material for future updates. It should point to
`basnijholt/lovelace-ios-themes`, not an intermediate fork.

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

## Which Branch Should HACS Use?

HACS custom repositories generally track the repository's default branch unless
you install a specific release or branch through a different workflow.

For the simplest setup, make `origin/master` contain the cleaned-up fork:

- based on current `upstream/master`
- plus the grey theme variants
- without unrelated local experiments

That is why this command may be useful:

```powershell
git push --force-with-lease origin gray-theme-only:master
```

What it does:

- pushes local branch `gray-theme-only`
- updates remote branch `origin/master`
- replaces the current remote `master` history with the cleaned-up history
- refuses to push if `origin/master` changed since the last fetch

Implications:

- This rewrites the public history of your fork's `master` branch.
- Existing clones of your fork may need to rebase, reset, or reclone.
- HACS will see the cleaned-up `master` as the main version.
- Old experimental commits are no longer on `origin/master`, but they remain
  recoverable locally from `archive-full-fork-before-baseline` and from any
  pushed branches that still contain them.

This is reasonable for a personal fork when nobody else depends on its branch
history. If other people use this fork, prefer pushing `gray-theme-only` as a
normal branch first and changing the GitHub default branch to it.

Safer preview command:

```powershell
git push -u origin gray-theme-only
```

After checking the pushed branch on GitHub, either change the repository default
branch to `gray-theme-only` or replace `origin/master` with the force-with-lease
command above.

## Updating From Upstream

When upstream changes, update the fork like this:

```powershell
git switch gray-theme-only
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
git push --force-with-lease origin gray-theme-only:master
```

Use `--force-with-lease`, not plain `--force`, because it checks that the remote
branch has not moved unexpectedly.

## Troubleshooting

### HACS Still Shows The Old Theme

- Confirm HACS is installed from `https://github.com/tjuuljensen/lovelace-ios-themes`.
- Confirm the GitHub default branch or `origin/master` contains the grey changes.
- In HACS, redownload or update the theme.
- Restart Home Assistant or reload themes.
- Clear browser cache if dashboard assets still look stale.

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

If `gray-theme-only` tracks `upstream/master`, remove that tracking:

```powershell
git branch --unset-upstream gray-theme-only
```

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

Keep changes only when they are part of the grey theme or clearly documented as
intentional fork behavior. For Home Assistant frontend rendering issues, test in
the running HA instance; many visual behaviors cannot verify statically.
