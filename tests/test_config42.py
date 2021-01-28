import unittest

from webhook.config import config


class MyTestCase(unittest.TestCase):

    def test_create_config(self):
        self.assertIsNotNone(config)
        environment = config.get("environment")

        self.assertEqual(environment, 'production')
        self.assertEqual(config.get("dev.dev_mode"), False)


if __name__ == '__main__':
    unittest.main()
