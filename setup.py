import os
import sys

if sys.version_info < (3, 6):
    sys.exit('ERROR: lucit-backtesting requires Python 3.6+')


if __name__ == '__main__':
    from setuptools import setup, find_packages

    setup(
        name='lucit-backtesting',
        description="Backtest trading strategies in Python",
        license='AGPL-3.0',
        url='https://github.com/LUCIT-Systems-and-Development/lucit-backtesting',
        project_urls={
            'Documentation': 'https://lucit-backtesting.docs.lucit.tech',
            'Source': 'https://github.com/LUCIT-Systems-and-Development/lucit-backtesting',
            'Wiki': 'https://github.com/LUCIT-Systems-and-Development/lucit-backtesting/wiki',
            'Author': 'https://www.lucit.tech',
            'Changes': 'https://lucit-backtesting.docs.lucit.tech/changelog.html',
            'License': 'https://lucit-backtesting.docs.lucit.tech/license.html',
            'Issue Tracker': 'https://github.com/LUCIT-Systems-and-Development/lucit-backtesting/issues',
            'Telegram': 'https://t.me/unicorndevs',
            'Get Support': 'https://www.lucit.tech/get-support.html',
        },
        long_description=open(os.path.join(os.path.dirname(__file__), 'README.md'),
                              encoding='utf-8').read(),
        long_description_content_type='text/markdown',
        packages=find_packages(),
        include_package_data=True,
        setup_requires=[
            'setuptools_git',
            'setuptools_scm',
        ],
        use_scm_version={
            'write_to': os.path.join('backtesting', '_version.py'),
        },
        install_requires=[
            'numpy >= 1.17.0',
            'pandas >= 0.25.0, != 0.25.0',
            'bokeh == 2.4.3',
        ],
        extras_require={
            'doc': [
                'pdoc3',
                'jupytext >= 1.3',
                'nbconvert',
                'ipykernel',       # for nbconvert
                'jupyter_client',  # for nbconvert
            ],
            'test': [
                'seaborn',
                'matplotlib',
                'scikit-learn <= 1.1.3',  # Pinned due to boken scikit-optimize
                'scikit-optimize',
            ],
            'dev': [
                'ruff==0.0.160',
                'coverage',
                'mypy',
            ],
        },
        test_suite="backtesting.test",
        python_requires='>=3.6',
        author="LUCIT Systems and Development",
        classifiers=[
            'Intended Audience :: Financial and Insurance Industry',
            'Intended Audience :: Science/Research',
            'Framework :: Jupyter',
            'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
            'Operating System :: OS Independent',
            'Programming Language :: Python :: 3 :: Only',
            'Topic :: Office/Business :: Financial :: Investment',
            'Topic :: Scientific/Engineering :: Visualization',
        ],
        keywords=[
            'algo',
            'algorithmic',
            'ashi',
            'backtest',
            'backtesting',
            'bitcoin',
            'bokeh',
            'bonds',
            'candle',
            'candlestick',
            'cboe',
            'chart',
            'cme',
            'commodities',
            'crash',
            'crypto',
            'currency',
            'doji',
            'drawdown',
            'equity',
            'etf',
            'ethereum',
            'exchange',
            'finance',
            'financial',
            'forecast',
            'forex',
            'fund',
            'futures',
            'fx',
            'fxpro',
            'gold',
            'heiken',
            'historical',
            'indicator',
            'invest',
            'investing',
            'investment',
            'macd',
            'market',
            'mechanical',
            'money',
            'oanda',
            'ohlc',
            'ohlcv',
            'order',
            'price',
            'profit',
            'quant',
            'quantitative',
            'rsi',
            'silver',
            'simulation',
            'stocks',
            'strategy',
            'ticker',
            'trader',
            'trading',
            'tradingview',
            'usd',
        ],
    )
