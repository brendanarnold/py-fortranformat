
Update versions in setup.py and __init__.py

Test build with:
python setup.py build sdist --formats=gztar bdist_wininst

Upload with:
python setup.py sdist --formats=gztar bdist_wininst upload
