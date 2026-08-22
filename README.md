# STA 363: Statistical Learning, Fall 2026

Course website source. Wake Forest University, Department of Statistical Sciences.

Site: <https://lucymcgowan.github.io/sta-363-f26>

## Layout

```
_quarto.yml            site config, navbar, sidebar
_variables.yml         course details used across pages
custom.scss            site theme, light
dark.scss              site theme, dark
www/fontawesome/       vendored Font Awesome 6.7.2
_extensions/           the {{< fa >}} shortcode

index.qmd              home
schedule.qmd           built from sta-363-f26-schedule.csv
syllabus.qmd           policies and grading
colab.qmd              getting started with Colab
python-guide.qmd       R to Python translation
data.qmd               data catalog
troubleshooting.qmd    common errors
help.qmd               office hours and resources

STYLE.yml              writing and formatting rules for every .qmd
check_style.py         validates them

slides/                revealjs decks
ex/                    application exercises
checkins/              paper check-ins, typst to PDF, not published
data/                  course data as CSV, plus export-data.py
```


---

Textbook: James, G., Witten, D., Hastie, T., Tibshirani, R., and Taylor, J.
(2023). *An Introduction to Statistical Learning with Applications in Python*.
Springer.
