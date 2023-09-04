to create a coverage report

python3 -m pytest <testfile> --cov= <directory>/<file to test> --cov-report html

or just
python3 -m pytest --cov --cov-report html