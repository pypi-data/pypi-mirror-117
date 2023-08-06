# dzy Python package

Python package for all data pipelines, tools, analysis etc.

---

## Modules

__dw__ :

* for functions related to data warehousing on GCP (Cloud Storage, BigQuery)
* requires service account for authentication:
  `os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "path/to.json"`

__utils__ :
* for various helper functions

---

## Install and Usage

* install from one of the deployments mentioned below using `pip install`
* for testing / local development it can be installed directly from the folder via `pip install -e <FOLDER>`
* to import full module : `import dzy.dw` -> `dw.run_function()`
* to import function : `from dzy.dw import run_function()` -> `run_function()`

---

## Deployment

Currently deployed to both PyPI and GCP's Artifact Registry, as the latter one is currently in beta and not accessible from Cloud Functions.

A. [PyPI](https://pypi.org/project/dzy/#description) - public
* deployed via a Bitbucket pipeline, requires PyPI account variables, PYPI_USERNAME and PYPI_PASSWORD
* install via the usual `pip install dzy --upgrade`

B. [Artifact Registry](https://console.cloud.google.com/artifacts/python/deazy-dw/europe-west2/dzy?authuser=4&project=deazy-dw) - private
* deployed via [Cloudbuild](https://console.cloud.google.com/cloud-build/triggers?authuser=4&project=deazy-dw), requires setting Cloudbuild variables _REPO and _REGION
* [Keyring authentication](https://cloud.google.com/artifact-registry/docs/python/authentication)
* `pip install --extra-index-url https://europe-west2-pypi.pkg.dev/deazy-dw/data-dzy/simple/ dzy`
