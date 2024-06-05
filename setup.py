from setuptools import setup, find_packages

setup(
    name='HtmlTestRunner-Ably',
    version='1.0.3',
    description='A customized version of HtmlTestRunner with exception handling',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/qa-inho-song/HtmlTestRunner-Ably',
    author='Inho Song',
    author_email='ablyqa@a-bly.com',
    license='MIT',
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',
    include_package_data=True,
)
