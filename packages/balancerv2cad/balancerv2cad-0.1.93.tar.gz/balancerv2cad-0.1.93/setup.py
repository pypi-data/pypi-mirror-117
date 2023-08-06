# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['balancerv2cad', 'balancerv2cad.logger']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['analyze = scripts.project_helper:run_analyzer',
                     'drive = balancerv2cad.main:run',
                     'stubs = scripts.project_helper:stub_gen',
                     'tests = scripts.project_helper:run_tests']}

setup_kwargs = {
    'name': 'balancerv2cad',
    'version': '0.1.93',
    'description': 'A preconfigured Python package, using python poetry',
    'long_description': '# <img src="https://github.com/balancer-labs/balancer-core-v2/blob/master/logo.svg" alt="Balancer" height="128px">\n\n## Overview\n\nThe BalancerV2 model is a python implementation of the balancerv2 protocol funded by Balancer and the Token Engineering community. In collaboration with Ocean Protocol and PowerPool. \nWe hope to build a resiliant, easy, and simple to use access to balancer pools for simulations, and build a brighter tomorrow for Token Engineers. Feel free to play and use this model for your own simulations and grow token engineering everywhere.\n\n- Copy BalancerV2 Pools from on chain, being able to pull weights from chain based on the symbols provided, this will reduce friction for new users.\n- Ease access into BalancerV2 pools for anyone wanting to make a trade and see the ending result of the pool\n- Provide an interface for easy swapping, adding liquidity, and removing it. This can be done with ipython or Jupyter\n- Develop rigorous testing for math functions to assure decimals are flowing exactly as EVM\n- Model ecosystem with agents using these balancer pools as an interactive objects.\n\nAll research is open source and transparent. For more information please visit the [BalancerV2 Simulations Documentation](https://metavision.gitbook.io/balancerv2-py-twin/).\n\n## Balancer V2 Model\n\nInstallation \n```\npip install balancerv2cad\n```\n\n## Sample Usage\n```\nfrom balancerv2cad.WeightedPool import WeightedPool\nwp = WeightedPool()\n# amounts of tokens to join pool, weights of tokens\nwp.join_pool({\'WETH\':19609,\'DAI\':30776582},{\'WETH\':0.6,\'DAI\':0.4})\nwp.swap(\'WETH\',\'DAI\',2)\n```\n\n',
    'author': 'Nico Rodriguez, Thomas Liu, Marcin Jaczynski',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/officialnico/balancerv2cad.git',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
