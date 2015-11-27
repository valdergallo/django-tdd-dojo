import datetime
from django.test import TestCase
from polls.models import Question
from polls.models import Choice


class PollsViewsTestCase(TestCase):

    def test_create_one_question(self):
        poll_1 = Question.objects.create(
            question='Are you learning about testing in Django?',
            pub_date=datetime.datetime(2011, 04, 10, 0, 37)
        )

        Choice.objects.create(
            poll=poll_1,
            choice='Yes',
            votes=0
        )

        Choice.objects.create(
            poll=poll_1,
            choice='No',
            votes=0
        )

        resp = self.client.get('/polls/')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('latest_polls_list' in resp.context)
        self.assertEqual([poll.pk for poll in resp.context['latest_polls_list']], [1])
