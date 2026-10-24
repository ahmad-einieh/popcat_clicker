# popcat_clicker

A short Python/Selenium browser-automation experiment that opens `https://popcat.click/` and attempts 10,000 clicks on the first `div` element.

## Requirements

- Windows: the script uses a Windows path to `chromedriver.exe` in the working directory.
- Python 3 and Google Chrome.
- A ChromeDriver version compatible with your installed Chrome. The bundled driver is historical and may not match current browsers.
- A Selenium version supporting the legacy `webdriver.Chrome(path)` constructor, such as Selenium 3.141.0.

## Setup and run

Create and activate a Python virtual environment, then:

```bat
python -m pip install selenium==3.141.0
python popcat_click.py
```

Run from the repository directory so the driver can be found. Updating Chrome alone is not sufficient: ChromeDriver and the legacy Selenium API must also be compatible. Modern Python/transitive dependencies may require further compatibility work.

## Behavior and limitations

- The URL, selector, and click count are hardcoded in [`popcat_click.py`](popcat_click.py).
- There is no explicit page-load wait, retry handling, or automatic `driver.quit()` cleanup.
- Site changes or a non-clickable first `div` can stop the script; compatibility with the current site is unverified.

Use automation only where permitted by the site's rules. This repository is a historical Selenium exercise, not a maintained automation tool.
