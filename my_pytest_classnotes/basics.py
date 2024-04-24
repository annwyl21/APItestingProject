# docs.pytest.org/en/latest/contents.html#toc

# files must start test_*.py or end *_test.py

# if tests are in a class there should be no constructor, __init__
# functions must follow naming convention above
# class must also follow naming convention

#RUN TESTS
# pytest <options>
# pytest <options> /path/to/test/files
# py.test <options> /path/to/test/filesc
# python -m pytest <options> /path/to/test/files (to use it as a module, hence -m)

# <options>
# -m module
# -s see the output

#RUN WITH MARKERS
# pytest -m smoke
# pytest -m "smoke or regression" ./tests
# pytest -m "smoke and regression" ./tests
# pytest -m "not prod" ./tests

# GET RID of unregistered mark warnings
# file must be located in root directory - root where the tests are running from

# First option
# [pytest]
# markers = 
#     smoke
#     regression
#     fe
#     slow

# REPORTS
# pytest --html=demo_report.html
# add this tag --self-contained-html otherwise it creates an assets folder with a style.css, making it more difficult to share


# Second Option
# [pytest]
# filterwarnings = 
#     ignore::pytest.PytestUnknownMarkWarning