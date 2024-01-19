from setuptools import setup, find_packages

setup(
    name='taskiq-elastic-apm',
    version='0.1.0',
    license="MIT",
    author="Eugene Shershen",
    author_email='h0rn3t.null@gmail.com',
    description='A middleware for TaskIQ with Elastic APM integration',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/h0rn3t/taskiq-elastic-apm',
    packages=find_packages(),
    install_requires=[
        'taskiq>=0.10.4',
        'elasticapm>=6.20.0',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)