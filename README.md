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

slides/                revealjs decks, plus STYLE.yml and check_style.py
ex/                    application exercises
checkins/              paper check-ins, typst to PDF, not published
data/                  course data as CSV, plus export-data.py
```

## Building

```bash
quarto render
```

**One time, before the first render.** Pages read their data over the web from
`https://lucymcgowan.github.io/sta-363-f26/data/`, so that students can copy the
exact same line into Colab. That means the data has to be published before a
render can fetch it. Push once with the data in place, wait for Pages to build,
then render:

```bash
python data/export-data.py     # needs ISLP installed, once
git add data && git commit -m "Add course data" && git push
# wait for the Pages build, then
quarto render
```

After that first push, ordinary renders work.

## Environment

Rendering needs Python with:

```
numpy pandas matplotlib scikit-learn statsmodels jupyter
```

`ISLP` is needed **only** to regenerate `data/*.csv` with
`data/export-data.py`. Nothing on the site requires it, and students never
install it.

From November the deep learning decks also need `torch`, `pytorch-lightning`,
`torchinfo`, and `torchmetrics`.

## Slides

Decks follow `slides/STYLE.yml`. Check before committing:

```bash
cd slides
python check_style.py            # prose, headings, lists, divs, figures
python check_style.py --layout   # also measures rendered slide heights
```

## Check-ins

Not part of the website. Render to PDF separately:

```bash
cd checkins
quarto render checkin-01.qmd
```

They use the typst engine, so no LaTeX install is needed.

## Schedule

Edit `sta-363-f26-schedule.csv` and re-render. Columns:

| Column | Meaning |
|---|---|
| `week` | week number, blank to merge with the row above |
| `date` | as displayed |
| `topic` | topic name |
| `slides` | path to the deck, or blank |
| `appex` | path to the application exercise, or blank |
| `assignment` | path to the problem set, or blank |
| `assessment` | check-in or exam label |
| `prepare` | reading due that day |

Icons link only when the source file exists, so the whole semester can be listed
without students hitting a 404.

---

Textbook: James, G., Witten, D., Hastie, T., Tibshirani, R., and Taylor, J.
(2023). *An Introduction to Statistical Learning with Applications in Python*.
Springer.
