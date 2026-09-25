@echo off
call .venv\Scripts\activate
python -m src.plan_template "%~1" --output plans\new-carousel.json
echo Plan created: plans\new-carousel.json
