# Setup Instructions for Wedding Documentation

This document provides step-by-step instructions for setting up and maintaining your wedding documentation site on Read the Docs.

## Table of Contents

1. [Creating GitHub Repository](#creating-github-repository)
2. [Pushing Code to GitHub](#pushing-code-to-github)
3. [Connecting to Read the Docs](#connecting-to-read-the-docs)
4. [Building and Viewing Documentation](#building-and-viewing-documentation)
5. [Creating and Embedding Google Form](#creating-and-embedding-google-form)
6. [Adding Translations](#adding-translations)
7. [Updating Content](#updating-content)

---

## Creating GitHub Repository

### Option A: Using GitHub CLI (Recommended)

If you have GitHub CLI (`gh`) installed and authenticated:

1. Navigate to the project directory:
   ```bash
   cd /Users/pw1246/Desktop/projects/other/wedding/wedding-docs
   ```

2. Create the repository on GitHub:
   ```bash
   gh repo create wedding-docs --public --source=. --remote=origin --push
   ```

This will create a public repository called `wedding-docs` and push your code automatically.

### Option B: Manual Creation

1. Go to [GitHub.com](https://github.com) and sign in
2. Click the "+" icon in the top right corner and select "New repository"
3. Repository name: `wedding-docs`
4. Description: "Wedding 2026 Documentation"
5. Set visibility to **Public**
6. **Do NOT** initialize with README, .gitignore, or license (we already have these)
7. Click "Create repository"

---

## Pushing Code to GitHub

### If using Option A (GitHub CLI)
Skip this section - the code was already pushed.

### If using Option B (Manual)
Run these commands in your terminal:

```bash
cd /Users/pw1246/Desktop/projects/other/wedding/wedding-docs

# Initialize git (if not already done)
git init

# Add all files
git add .

# Create initial commit
git commit -m "Initial commit: Wedding documentation site"

# Add the remote repository (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/wedding-docs.git

# Push to GitHub
git branch -M main
git push -u origin main
```

---

## Connecting to Read the Docs

1. **Sign up/Login to Read the Docs**
   - Go to [readthedocs.org](https://readthedocs.org)
   - Sign in with your GitHub account (recommended) or create a new account

2. **Import Your Project**
   - Click on "Import a Project" or go to your dashboard
   - Click "Import a Project" → "Import Manually"
   - Fill in the form:
     - **Name**: `wedding-docs` (or your preferred name)
     - **Repository URL**: `https://github.com/YOUR_USERNAME/wedding-docs` (replace YOUR_USERNAME)
     - **Repository type**: Git
     - **Default branch**: `main` (or `master` if you used that)
     - **Project slug**: `wedding-docs` (this will be used in the URL)
     - **Language**: English
   - Click "Next"

3. **Configure Build Settings**
   - Read the Docs will automatically detect `.readthedocs.yaml` configuration
   - Verify these settings:
     - **Python version**: 3.11
     - **Build system**: Ubuntu 22.04
     - **Configuration file**: `docs/source/conf.py`
     - **Requirements file**: `requirements.txt`
   - Click "Build version" to trigger the first build

4. **Wait for Build**
   - The build will start automatically
   - It may take 2-5 minutes for the first build
   - You can monitor progress in the "Builds" tab

5. **View Your Documentation**
   - Once the build completes successfully, your documentation will be available at:
     `https://wedding-docs.readthedocs.io/`
   - You can also find this URL in your project settings

---

## Building and Viewing Documentation

### Local Build (Optional)

To preview documentation locally before pushing changes:

```bash
cd /Users/pw1246/Desktop/projects/other/wedding/wedding-docs

# Install dependencies
pip install -r requirements.txt

# Build the documentation
cd docs
sphinx-build -b html source build

# Open in browser (macOS)
open build/index.html
```

### On Read the Docs

- Every time you push changes to GitHub, Read the Docs will automatically rebuild
- You can also manually trigger builds from the Read the Docs dashboard
- Builds typically take 2-5 minutes

---

## Creating and Embedding Google Form

### Step 1: Create the Google Form

1. Go to [Google Forms](https://forms.google.com)
2. Sign in with your Google account
3. Click "Blank" to create a new form
4. Add a title: "Wedding 2026 - RSVP"

### Step 2: Add Form Fields

Suggested fields for your RSVP form:

1. **Name** (Short answer, Required)
   - Question: "Full Name"
   - Make it required

2. **Email** (Short answer, Required)
   - Question: "Email Address"
   - Make it required

3. **Which celebration(s) will you attend?** (Checkboxes or Multiple choice)
   - Options:
     - "Turkey Wedding - May 2, 2026"
     - "China Wedding - September 2026"
     - "Both celebrations"
     - "Cannot attend"

4. **Number of Guests** (Short answer)
   - Question: "Total number of guests (including yourself)"

5. **Dietary Restrictions** (Paragraph, Optional)
   - Question: "Any dietary restrictions or special requirements?"

6. **Additional Notes** (Paragraph, Optional)
   - Question: "Any additional notes or questions?"

### Step 3: Get the Form Link

1. Click the "Send" button in the top right
2. Click the link icon (🔗)
3. Copy the form URL (it will look like: `https://docs.google.com/forms/d/e/XXXXXXXXX/viewform`)

### Step 4: Convert to Short Link (Optional but Recommended)

1. Paste the form URL into [Google's URL Shortener](https://goo.gl) or use the form's built-in shortener
2. Or use the form's "Share" option to get a shortened link
3. The shortened link will look like: `https://forms.gle/XXXXXXXXX`

### Step 5: Embed in Documentation

1. Open `docs/source/index.rst` in your editor
2. Find the RSVP section:
   ```rst
   `RSVP Form <https://forms.gle/PLACEHOLDER>`_
   ```
3. Replace `https://forms.gle/PLACEHOLDER` with your actual Google Form URL
4. Save the file

### Step 6: Alternative - Embed as iframe

If you want to embed the form directly in the page instead of linking to it:

1. In your Google Form, click "Send" → "Link" icon
2. Get the embed URL (it will look like: `https://docs.google.com/forms/d/e/XXXXXXXXX/viewform?embedded=true`)
3. In `docs/source/index.rst`, replace the RSVP section with:

   ```rst
   RSVP
   ----

   Please fill out the form below to RSVP:

   .. raw:: html

      <iframe src="https://docs.google.com/forms/d/e/XXXXXXXXX/viewform?embedded=true" width="640" height="1000" frameborder="0" marginheight="0" marginwidth="0">Loading…</iframe>
   ```

4. Replace `XXXXXXXXX` with your actual form ID

### Step 7: Commit and Push

```bash
cd /Users/pw1246/Desktop/projects/other/wedding/wedding-docs
git add docs/source/index.rst
git commit -m "Update RSVP form link"
git push
```

Read the Docs will automatically rebuild with the new form link.

---

## Adding Translations

### Step 1: Enable Translations in Read the Docs

1. Go to your Read the Docs project dashboard
2. Navigate to "Admin" → "Translations"
3. Click "Add a translation"
4. Select:
   - **Turkish** (tr) - Language: Turkish
   - **Chinese** (zh_CN) - Language: Chinese (Simplified)
5. Click "Create"

### Step 2: Install Translation Tools Locally

```bash
cd /Users/pw1246/Desktop/projects/other/wedding/wedding-docs
pip install sphinx-intl babel
```

### Step 3: Create Translation Files

```bash
cd docs
sphinx-intl update -p source/_build/gettext -l tr -l zh_CN
```

This creates translation template files in `docs/source/locale/tr/LC_MESSAGES/` and `docs/source/locale/zh_CN/LC_MESSAGES/`.

### Step 4: Translate Content

1. Edit the `.po` files in:
   - `docs/source/locale/tr/LC_MESSAGES/index.po` (Turkish)
   - `docs/source/locale/zh_CN/LC_MESSAGES/index.po` (Chinese)

2. Translate the `msgstr` fields. For example, in Turkish `index.po`:
   ```po
   msgid "Wedding 2026"
   msgstr "Düğün 2026"
   ```

3. Repeat for `faq.po` files

### Step 5: Build Translations

```bash
cd docs
sphinx-intl build -d source/locale
```

### Step 6: Test Locally

```bash
sphinx-build -b html -D language=tr source build-tr
sphinx-build -b html -D language=zh_CN source build-zh
```

### Step 7: Commit and Push

```bash
cd /Users/pw1246/Desktop/projects/other/wedding/wedding-docs
git add docs/source/locale/
git commit -m "Add Turkish and Chinese translations"
git push
```

Read the Docs will automatically detect and build the translations. Users can switch languages using the language selector in the documentation.

---

## Updating Content

### Updating Hotel Recommendations

1. Edit `docs/source/faq.rst`
2. Find the "Hotel Recommendations" section under Turkey or China Wedding
3. Replace "TBD" with your hotel recommendations:

   ```rst
   Hotel Recommendations
   ~~~~~~~~~~~~~~~~~~~~~~
   
   We recommend the following hotels:
   
   **Hotel Name 1**
   - Address: [Address]
   - Website: `Link <https://example.com>`_
   - Phone: [Phone number]
   
   **Hotel Name 2**
   ...
   ```

4. Save, commit, and push:
   ```bash
   git add docs/source/faq.rst
   git commit -m "Update hotel recommendations"
   git push
   ```

### Updating Directions

1. Edit `docs/source/faq.rst`
2. Find the "How to Get from Airport to Venue" section
3. Replace "TBD" with directions:

   ```rst
   How to Get from Airport to Venue
   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   
   **Option 1: Taxi**
   - Approximate cost: [Amount]
   - Duration: [Time]
   
   **Option 2: Shuttle**
   - Details: [Information]
   
   **Option 3: Public Transportation**
   - Instructions: [How to get there]
   ```

4. Save, commit, and push

### Updating Dates

1. Edit `docs/source/index.rst`
2. Update the dates as needed
3. Commit and push

---

## Troubleshooting

### Build Fails on Read the Docs

- Check the build logs in Read the Docs dashboard
- Common issues:
  - Missing dependencies in `requirements.txt`
  - Syntax errors in `.rst` files
  - Incorrect paths in `conf.py`

### Images Not Showing

- Ensure images are in `docs/source/_static/images/`
- Check image paths in `.rst` files use `_static/images/filename`
- Verify image filenames match exactly (case-sensitive)

### Translations Not Appearing

- Ensure locale files are committed to git
- Check that translations are enabled in Read the Docs dashboard
- Verify `.po` files have been compiled (or let Read the Docs handle it)

---

## Need Help?

- Read the Docs documentation: https://docs.readthedocs.io/
- Sphinx documentation: https://www.sphinx-doc.org/
- Google Forms help: https://support.google.com/docs/answer/6281888

