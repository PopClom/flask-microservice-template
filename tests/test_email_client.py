import unittest
from unittest.mock import Mock, patch
from app.clients.email_client import EmailClient


class TestEmailClient(unittest.TestCase):
    def setUp(self):
        self.email_client = EmailClient('https://test.example.com')

    @patch('app.clients.email_client.requests.post')
    def test_send_registration_email_success(self, mock_post):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"message": "Email sent successfully"}
        mock_post.return_value = mock_response

        email_address = "test@example.com"
        response = self.email_client.send_registration_email(email_address)

        self.assertEqual(response, {"message": "Email sent successfully"})

        url = self.email_client.BASE_URL + '/welcome-email'
        body = {'address': email_address}
        mock_post.assert_called_once_with(url, json=body)

    @patch('app.clients.email_client.requests.post')
    def test_send_registration_email_failure(self, mock_post):
        mock_response = Mock()
        mock_response.status_code = 404
        mock_post.return_value = mock_response

        email_address = "test@example.com"
        response = self.email_client.send_registration_email(email_address)

        self.assertIsNone(response)

        url = self.email_client.BASE_URL + '/welcome-email'
        body = {'address': email_address}
        mock_post.assert_called_once_with(url, json=body)


if __name__ == '__main__':
    unittest.main()
