call activate D:/env/sensor_api
@REM call activate sensor_api

set unittet_dir=%cd%
cd ..\
set coinespy_loc=%cd%\coinespy
set PYTHONPATH=%PYTHONPATH%;%cd%;%coinespy_loc%;%unittet_dir%

@echo [Generating flake8 report]
python -m flake8 --format=pylint --max-line-length=120 --exit-zero --ignore=F401,F403 --output-file=_unittest_/reports/flake8_report.txt

@echo [Generating lizard report in xml and html format]
python -m lizard -C 5 coinespy _unittest_/test_coines.py -o _unittest_/reports/lizard_coinespy_report.html
python -m lizard -C 5 coinespy _unittest_/test_coines.py -o _unittest_/reports/lizard_coinespy_report.xml

@echo [Generating pytest report in xml and html format]
python -m pytest -c _unittest_/pytest.ini