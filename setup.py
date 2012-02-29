from setuptools import setup,find_packages

setup(
    name = "billwatcher-malaysia",
    version = "0.1",
    url = "https://github.com/sweemeng/Malaysian-Bill-Watcher",
    license = "GPL",
    description = "A web app to make bills in parliament more visible, a sinar project",
    author = "sweemeng",
    packages = find_packages("billwatcher"),
    package_dir = {'':'billwatcher'},
    install_requires = [
        'setuptools',
        'bottle',
        'pyes',
        'SQLAlchemy',
        'PyRSS2Gen',
        'gevent',
        'greenlet',
        'gunicorn',
        'httplib2',
        'ipython',
        'oauth2',
        'python-twitter',
        'simplejson',
        'wsgiref',
        'beautifulsoup',
        ],
)
