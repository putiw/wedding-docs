# Wedding 2026 Documentation

Welcome to the wedding documentation repository for Puti & Birol's 2026 celebrations!

This repository contains the source files for a Sphinx-based documentation website hosted on Read the Docs.

## Events

- **Turkey Wedding**: May 2, 2026 - Antalya, Turkey
- **China Wedding**: September 2026 (Saturday TBD) - Beijing, China

## Documentation Site

The documentation is hosted on Read the Docs. Once connected, you can view it at:
`https://wedding-docs.readthedocs.io/`

## Local Development

To build and preview the documentation locally:

1. Install the requirements:
   ```bash
   pip install -r requirements.txt
   ```

2. Build the documentation:
   ```bash
   cd docs
   sphinx-build -b html source build
   ```

3. Open `docs/build/index.html` in your browser to view the documentation.

## Project Structure

```
wedding-docs/
├── README.md                 # This file
├── requirements.txt          # Python dependencies
├── .readthedocs.yaml        # Read the Docs configuration
├── .gitignore               # Git ignore patterns
└── docs/
    └── source/
        ├── conf.py          # Sphinx configuration
        ├── index.rst        # Main documentation page
        ├── faq.rst          # FAQ page
        └── _static/
            └── images/      # Images and static assets
```

## Contributing

For detailed instructions on:
- Setting up the GitHub repository
- Connecting to Read the Docs
- Adding translations
- Embedding Google Forms

Please see `SETUP_INSTRUCTIONS.md` in this repository.

## License

Private project - All rights reserved.

