import unittest
from unittest.mock import MagicMock
from app.logger import configure_logging, log_event

class TestLogger(unittest.TestCase):
    def setUp(self):
        self.logger_mock = MagicMock()
        self.metadata = {"url": "http://test.com", "user_agent": "Test-Agent"}

    def test_configure_logging(self):
        logger = configure_logging()
        self.assertIsNotNone(logger)
        self.assertEqual(logger.level, 20)  # Nível INFO (numericamente igual a 20)

    def test_log_event_info(self):
        log_event(self.logger_mock, "info", "test-info-event", **self.metadata)
        self.logger_mock.info.assert_called_once()

        # Verifica os argumentos do log gerado
        log_data = self.logger_mock.info.call_args[0][0]
        self.assertIn('"event": "test-info-event"', log_data)
        self.assertIn('"url": "http://test.com"', log_data)
        self.assertIn('"user_agent": "Test-Agent"', log_data)

    def test_log_event_error(self):
        log_event(self.logger_mock, "error", "test-error-event", **self.metadata, error_message="Test Error")
        self.logger_mock.error.assert_called_once()

        # Verifica os argumentos do log gerado
        log_data = self.logger_mock.error.call_args[0][0]
        self.assertIn('"event": "test-error-event"', log_data)
        self.assertIn('"url": "http://test.com"', log_data)
        self.assertIn('"user_agent": "Test-Agent"', log_data)
        self.assertIn('"error_message": "Test Error"', log_data)