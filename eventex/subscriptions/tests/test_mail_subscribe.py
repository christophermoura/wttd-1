from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name="Vicente Marçal", cpf="12345678911",
                    email="vicente.marcal@gmail.com", phone = "69-98114-6191")
        self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de Inscrição'

        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventex.com.br', 'vicente.marcal@gmail.com']

        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):

        contents = ['Vicente Marçal',
                    '12345678911',
                    'vicente.marcal@gmail.com',
                    '69-98114-6191']

        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)