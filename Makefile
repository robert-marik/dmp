# Makefile pro učební text Dynamické modely populací
#
# Všechny příkazy běží v mamba prostředí $(ENV) (vytvoří se příkazem `make env`).
# Přehled cílů vypíše `make` nebo `make help`.

ENV       ?= dmp
PYTHON    ?= 3.12
MAMBA     ?= mamba
RUN       := $(MAMBA) run -n $(ENV)

BUILD     := _build
HTML      := $(BUILD)/html
CHECK_DIR := $(BUILD)/check

# Kapitola pro `make chapter`, např. `make chapter CH=13`
CH        ?= 13

CONDA_PKGS := numpy scipy matplotlib pandas openpyxl jupytext ipykernel ipywidgets \
	nbconvert nbclient mesa ghp-import "jupyter-book<2" sphinx-book-theme myst-nb \
	sphinx-togglebutton sphinx-copybutton sphinx-comments sphinx-external-toc \
	sphinx-design sphinxcontrib-bibtex sphinx-notfound-page
PIP_PKGS   := sphinx-proof sphinx-last-updated-by-git

# Soubory, které při spuštění notebooků vzniknou nebo se přepíšou jako vedlejší produkt
GENERATED_TRACKED   := latex/log_konst.pdf latex/log_konst_usili.pdf latex/log_konst_usili_allee.pdf
GENERATED_UNTRACKED := kombi/data.xlsx

.DEFAULT_GOAL := help
.PHONY: help env env-update env-remove kernel html sphinx chapter open serve \
	pdf upload clean clean-generated status

help: ## Vypíše přehled cílů
	@echo "Použití: make <cíl> [ENV=$(ENV)] [CH=$(CH)]"
	@echo
	@grep -E '^[a-zA-Z_-]+:.*## ' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = ":.*## "}; {printf "  \033[36m%-16s\033[0m %s\n", $$1, $$2}'

# ---------------------------------------------------------------- prostředí

env: ## Vytvoří mamba prostředí (výchozí dmp) se všemi balíčky (pokud ještě neexistuje)
	@if $(MAMBA) env list | grep -qE '^\s*$(ENV)\s'; then \
		echo "Prostředí $(ENV) už existuje, pro aktualizaci použijte 'make env-update'."; \
	else \
		$(MAMBA) create -y -n $(ENV) -c conda-forge python=$(PYTHON) $(CONDA_PKGS) && \
		$(RUN) pip install $(PIP_PKGS) && \
		$(MAKE) --no-print-directory kernel; \
	fi

env-update: ## Doinstaluje/aktualizuje balíčky v existujícím prostředí
	$(MAMBA) install -y -n $(ENV) -c conda-forge $(CONDA_PKGS)
	$(RUN) pip install -U $(PIP_PKGS)

env-remove: ## Smaže mamba prostředí
	$(MAMBA) env remove -y -n $(ENV)

kernel: ## Zaregistruje Jupyter kernel prostředí
	$(RUN) python -m ipykernel install --user --name $(ENV) --display-name "Python ($(ENV))"

# ---------------------------------------------------------------- sestavení

html: ## Sestaví HTML verzi knihy (scripts/build.sh, včetně úprav pro web) do _build/html
	cd scripts && $(RUN) bash build.sh

sphinx: ## Rychlé sestavení HTML čistým sphinx-build (bez úprav z build.sh)
	$(RUN) sphinx-build . $(HTML) -b html

chapter: ## Spustí jednu přednášku jako notebook a ověří, že doběhne (CH=13)
	@mkdir -p $(CHECK_DIR)
	cd prednaska && $(RUN) jupytext --to ipynb --execute $(CH).md -o ../$(CHECK_DIR)/$(CH).ipynb
	@echo "Výsledek: $(CHECK_DIR)/$(CH).ipynb"

open: ## Otevře sestavenou knihu v prohlížeči
	xdg-open $(HTML)/index.html >/dev/null 2>&1 &

serve: ## Spustí lokální webový server s knihou na http://localhost:8000
	$(RUN) python -m http.server 8000 --directory $(HTML)

pdf: ## Sestaví PDF verzi (scripts/build_latex.sh; vyžaduje xelatex a vlna)
	@command -v xelatex >/dev/null || { echo "Chybí xelatex (TeX Live)."; exit 1; }
	@command -v vlna >/dev/null || { echo "Chybí vlna (balík vlna / TeX Live)."; exit 1; }
	cd scripts && $(RUN) bash build_latex.sh

upload: ## Zveřejní _build/html na GitHub Pages (větev gh-pages)
	@test -f $(HTML)/index.html || { echo "Nejprve spusťte 'make html'."; exit 1; }
	$(RUN) ghp-import -n -p $(HTML)

# ---------------------------------------------------------------- úklid

status: ## Ukáže, zda sestavení nezměnilo verzované soubory
	@git status --short

clean-generated: ## Vrátí soubory přepsané při spouštění notebooků (PDF v latex/, kombi/data.xlsx)
	git checkout -- $(GENERATED_TRACKED)
	rm -f $(GENERATED_UNTRACKED)

clean: ## Smaže adresář _build
	rm -rf $(BUILD)
