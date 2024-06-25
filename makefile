install_requirements:
	@pip install -r requirements.txt

install:
	@pip install . -U

run_api:
	uvicorn api.fast:app --reload

make_run:
	python interface/main.py
