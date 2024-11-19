from setuptools import setup, find_packages

setup(
    name='xTechTrader',
    version='1.0.0',
    packages=find_packages(where="src"),
    install_requires=[
        'tweepy>=3.10.0', 'solana>=0.30.0', 'transformers>=4.20.0', 
        'torch>=1.12.0', 'requests>=2.27.0'
    ],
    package_dir={"": "src"},
    include_package_data=True,
    description="AI-driven cryptocurrency trader with social media integration",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    author="Your Name",
    author_email="your-email@example.com",
    url="https://github.com/yourusername/xTech-AI-Trader",
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
