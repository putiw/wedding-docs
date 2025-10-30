# Wedding 2026 Documentation

Sphinx-based documentation website for Puti & Birol's 2026 wedding celebrations, hosted on Read the Docs.

## Events

- **Turkey Wedding**: May 2, 2026 - Antalya, Turkey
- **China Wedding**: September 2026 (Saturday TBD) - Beijing, China

## Documentation Site

View the live documentation at: [wedding-docs.readthedocs.io](https://wedding-docs.readthedocs.io/)

## Local Development

```bash
pip install -r requirements.txt
cd docs
sphinx-build -b html source build
open build/index.html  # macOS
```

## Multi-language setup (localized sidebars)

Read the Docs shows the sidebar from the active language build. To switch sidebar language with the page, build one site per language and add them as Translations on RTD.

1. Extract messages and create locale files:
   ```bash
   sphinx-build -b gettext docs/source docs/_build/gettext
   pip install sphinx-intl
   sphinx-intl update -p docs/_build/gettext -l zh_CN -l tr
   ```
2. Translate `.po` files under `docs/locale/<lang>/LC_MESSAGES/`.
3. Build per language locally:
   ```bash
   sphinx-build -D language=en docs/source docs/_build/html
   sphinx-build -D language=zh_CN docs/source docs/_build/html-zh
   sphinx-build -D language=tr docs/source docs/_build/html-tr
   ```
4. On Read the Docs, create one main project (English) and add the Chinese and Turkish projects as Translations (Admin → Translations). The language switcher will then change the entire UI and sidebar.

