# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pytest_hpfeeds']

package_data = \
{'': ['*']}

install_requires = \
['hpfeeds>=3.0.0,<4.0.0',
 'pytest-docker-tools>=3.1.0,<4.0.0',
 'pytest>=6.2.4,<7.0.0']

entry_points = \
{'pytest11': ['hpfeeds = pytest_hpfeeds.plugin']}

setup_kwargs = {
    'name': 'pytest-hpfeeds',
    'version': '0.1.0',
    'description': 'Helpers for testing hpfeeds in your python project',
    'long_description': '# pytest-hpfeeds\n\npytest-hpfeeds is a collection of boilerplate to help with smoke/integration testing of honeypots against a hpfeeds broker. It leverages pytest-docker-tools to manage running a test broker inside docker. It provides a `hpfeeds_client` fixture to provide your pytest with a client connected to that broker.\n\n\n## hpfeeds_broker\n\nThis package provides a `hpfeeds_broker` fixture. By referencing this fixture from a test pytest-hpfeeds will automatically start a broker (in a container) before your test and destroy it after the test is completed.\n\n```python\ndef test_my_broker(hpfeeds_broker):\n    assert hpfeeds_broker.ips.primary is not None\n```\n\nBy default the broker is configured with a single user (`test` with a secret of `test`) and a single channel called `test`.\n\n\n## hpfeeds_client\n\nThe package also provides a `hpfeeds_client` fixture. This is an instance of `hpfeeds.asyncio.ClientSession` that is already connected to your broker. Because the client depends on the `hpfeeds_broker` you don\'t need to reference it, pytest will still automatically start and stop the broker as needed.\n\n```python\nasync def test_my_client(hpfeeds_client):\n    hpfeeds_client.subscribe(\'test\')\n    hpfeeds_client.publish(\'test\', \'hello\')\n    assert await hpfeeds_client.read() == (\'test\', \'test\', b\'hello\')\n```\n\n\n## hpfeeds_broker_channels\n\nYou can implement this fixture in your `conftest.py` to change which channels your broker knows about.\n\n```python\nimport pytest\n\n@pytest.fixture()\ndef hpfeeds_broker_channels():\n    return ["cowrie.sessions"]\n\nasync def test_my_client(hpfeeds_client):\n    hpfeeds_client.subscribe(\'cowrie.sessions"\')\n    hpfeeds_client.publish(\'cowrie.sessions"\', \'hello\')\n    assert await hpfeeds_client.read() == (\'test\', \'cowrie.sessions"\', b\'hello\')\n```\n\n\n## Testing a honeypot in practice\n\nYou have packaged a honeypot and you want to write an end to end test to make sure that it functions as expected.\n\nIf you have a honeypot in the current directory with a `Dockerfile` you can write a `conftest.py` like this:\n\n```python\nimport pathlib\n\nfrom pytest_docker_tools import image_or_build\n\nCURRENT_DIR = pathlib.Path(__file__).parent\n\nimage = image_or_build(\n    environ_key=\'IMAGE_ID\',\n    path=CURRENT_DIR,\n)\n\nhoneypot = container(\n    image=image,\n    environment={\n        "OUTPUT_HPFEEDS_HOST": "{hpfeeds_broker.ips.primary}",\n        "OUTPUT_HPFEEDS_PORT": "20000",\n        "OUTPUT_HPFEEDS_IDENT": "test",\n        "OUTPUT_HPFEEDS_SECRET": "test",\n        "OUTPUT_HPFEEDS_CHANNEL": "test",\n    },\n    ports={"8443/tcp": None},\n    user="nobody",\n    read_only=True,\n)\n```\n\nTo learn more about what this is doing, you should read the pytest-docker-tools [README])(https://github.com/Jc2k/pytest-docker-tools/blob/main/README.md). But some key points are:\n\n* Variables are automatically interpolated against pytest fixtures. So `"{hpfeeds_broker.ips.primary}"` resolves the `hpfeeds_broker` fixture (causing an ephemeral broker container to be started) and gets its main IP to pass to your honeypot image.\n* The `image` fixture lets you test an existing image (one that exists locally). The `build` fixture lets you do iterative development - it effectively does `docker build` every time you run your tests. Sometimes you want both. You want your development environment to use the `buld` fixture, but your release pipeline should use the `image` fixture so that it is testing the exact image (bit for bit) that will be deployed. That\'s what the `image_or_build` fixture is for. If your CI pipeline sets the `IMAGE_ID` environment variable then the existing image is tested. Otherwise pytest will `docker build` a new image.\n\nNow to test this honeypot you can write a test:\n\n```python\nimport json\n\nimport httpx\n\n\nasync def test_honeypot_logs_data(honeypot, hpfeeds_client):\n    hpfeeds_client.subscribe("test")\n\n    ip, port = honeypot.get_addr("8443/tcp")\n\n    # Simulate simulating an attack on the honeypot\n    async with httpx.AsyncClient() as client:\n        response = await client.get(f"http://{ip}:{port}/some-endpoint")\n        assert r.status_code == 200\n\n    ident, channel, event = await hpfeeds_client.read()\n\n    # Verify the event is correct and that the structure hasn\'t changed\n    assert json.loads(event) == {\n        "event": "http.get",\n        # ....\n    }\n\n```\n\nBy using `pytest-hpfeeds` and `pytest-docker-tools` most of the heavy lifting of build and starting your containerised honeypot and connecting it to a hpfeeds broker is hidden away. You can concentrating on simulating attacks against the honeypot and verifying the hpfeeds output, making it safe to rapidly deploy to your production environment without regressing your event processing backend.\n',
    'author': 'John Carr',
    'author_email': 'john.carr@unrouted.co.uk',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/hpfeeds/pytest-hpfeeds',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
