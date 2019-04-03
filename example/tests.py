from django.test import TestCase
from django.urls import reverse
from example.forms import GiftListForm
from example.models import Gift, GiftList


class SimpleTestCase(TestCase):
    def setUp(self):
        self.gift_list = GiftList.objects.create(name="Christmas presents")
        self.gift = Gift.objects.create(name="RC Car", gift_list=self.gift_list)

    def tearDown(self):
        self.gift.delete()
        self.gift_list.delete()

    def test_max_length(self):
        gf = GiftListForm(data={"name": "X" * 100})
        self.assertFalse(gf.is_valid())

    def test_initial(self):
        gf = GiftListForm(instance=self.gift_list)
        self.assertEqual(gf.initial["name"], self.gift_list.name)


class SimpleTestCase2(TestCase):
    hello_world_url = reverse("hello")

    def test_display_view(self):
        response = self.client.get(self.hello_world_url)
        content = str(response.content)
        self.assertIn("Hello World", content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.resolver_match.view_name, "hello")


class SimpleTestCase3(TestCase):
    form_view_url = reverse("add_gfl")

    def test_display_view(self):
        field_name = "name"
        data = {field_name: ""}
        expected_error = "This field is required."
        response = self.client.post(self.form_view_url, data)

        self.assertFormError(response, "form", field_name, expected_error)
