import unittest
from unittest.mock import MagicMock
from app.app import app

class AppTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.logger_mock = MagicMock()
        app.logger = self.logger_mock  # Substitui o logger global do app pelo mock

    def test_print_health_check(self):
        response = self.app.get('/health-check')
        self.assertEqual(200, response.status_code, "Erro no test_http_code!")
        self.assertEqual("<h1>Hello, I'm Alive!</h1>", response.get_data(as_text=True))

    def test_hello_success(self):
        response = self.app.get('/hello?name=guijac')
        self.assertEqual(200, response.status_code)
        self.assertEqual("Hello, guijac!", response.get_data(as_text=True))

        # Verifica se o logger.info foi chamado
        self.logger_mock.info.assert_called_once()
        log_data = self.logger_mock.info.call_args[0][0]
        self.assertIn('"event": "hello-success"', log_data)
        self.assertIn('"nome": "guijac"', log_data)

    def test_hello_error(self):
        response = self.app.get('/hello')
        self.assertEqual(400, response.status_code)
        self.assertEqual("Nome não informado", response.get_data(as_text=True))

        # Verifica se o logger.error foi chamado
        self.logger_mock.error.assert_called_once()
        log_data = self.logger_mock.error.call_args[0][0]
        self.assertIn('"event": "hello-error"', log_data)
        self.assertIn('"error_message": "Nome n\\u00e3o informado"', log_data)