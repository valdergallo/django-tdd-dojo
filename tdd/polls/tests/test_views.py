import datetime
from django.test import TestCase
from polls.models import Poll, Choice


class PollsViewsTestCase(TestCase):

    def test_index(self):
        poll_1 = Poll.objects.create(
            question='Are you learning about testing in Django?',
            pub_date=datetime.datetime(2011, 04, 10, 0, 37)
        )

        choice_1 = Choice.objects.create(
            poll=poll_1,
            choice='Yes',
            votes=0
        )

        choice_2 = Choice.objects.create(
            poll=poll_1,
            choice='No',
            votes=0
        )

        resp = self.client.get('/polls/')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('latest_poll_list' in resp.context)
        self.assertEqual([poll.pk for poll in resp.context['latest_poll_list']], [1])
