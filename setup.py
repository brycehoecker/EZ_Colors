from setuptools import setup, find_packages

setup(
    name='color_text_pkg',
    version='1.0.0',
    packages=find_packages(),
    description='Color text in terminal',
    long_description=open('README.md').read() if os.path.exists('README.md') else '',
    long_description_content_type='text/markdown',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/color_text_pkg',  # Optional
    install_requires=[
        # Any dependencies, if you have them
    ],
)
