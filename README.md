# TaxSnap Legal Documents

This directory contains the legal documents for TaxSnap application.

## Setup GitHub Pages

1. **Create a new repository** named `taxsnap-legal` (or similar)

2. **Push this docs folder** to the repository:
```bash
cd /home/vxl1/MyApps/tax-snap-app/tax_snap/docs
git init
git add .
git commit -m "Initial legal documents"
git remote add origin https://github.com/[your-username]/taxsnap-legal.git
git push -u origin main
```

3. **Enable GitHub Pages**:
   - Go to repository Settings
   - Navigate to Pages section
   - Source: Deploy from branch
   - Branch: main
   - Folder: / (root)
   - Save

4. **Access your documents** at:
   - `https://[your-username].github.io/taxsnap-legal/`
   - Or use custom domain

## Structure

```
docs/
├── index.html              # Landing page
├── terms-v2.html          # Current Terms & Conditions
├── privacy-v1.html        # Privacy Policy (to be created)
├── changelog.html         # Version history (to be created)
├── versions.json          # Version tracking
├── terms-and-conditions.md # Source markdown
└── convert-md-to-html.py  # Conversion script
```

## Updating Documents

1. Edit the markdown file (`terms-and-conditions.md`)
2. Run conversion: `python3 convert-md-to-html.py`
3. Update `versions.json` with new version info
4. Commit and push changes
5. Documents update automatically via GitHub Pages

## In-App Integration

The app will fetch `versions.json` to check for updates:

```dart
// Check for T&C updates
final response = await http.get(
  Uri.parse('https://[your-username].github.io/taxsnap-legal/versions.json')
);
final versions = json.decode(response.body);
final currentVersion = versions['terms']['current'];
```

## Alternative: Firebase Hosting

If you prefer Firebase Hosting:

```bash
firebase init hosting
# Select docs as public directory
# Configure as single-page app: No
# Set up automatic builds: No

firebase deploy --only hosting
```

Your documents will be available at:
`https://taxsnap-legal.web.app/`

## Custom Domain

To use a custom domain like `legal.taxsnap.com.au`:
1. Add CNAME file with domain name
2. Configure DNS settings
3. Enable HTTPS in GitHub Pages settings