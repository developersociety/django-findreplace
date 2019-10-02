from unittest import mock

from django.core.management import call_command
from django.test import TestCase
from django.utils.six import StringIO

from findreplace.management.commands.findreplace import Command

from .models import Author


class TestFindReplaceCommand(TestCase):
    def test_get_fields(self):
        command = Command()

        fields = command.get_fields()

        expected_fields = [
            Author._meta.get_field("name"),
            Author._meta.get_field("slug"),
            Author._meta.get_field("url"),
            Author._meta.get_field("notes"),
        ]
        self.assertEqual(fields, expected_fields)

    def test_find_replace(self):
        Author.objects.create(name="Alice")
        Author.objects.create(name="Bob")

        command = Command()
        changed = command.find_replace(
            field=Author._meta.get_field("name"), find="Alice", replace="Carol"
        )

        self.assertEqual(changed, 1)
        self.assertEqual(Author.objects.filter(name="Carol").count(), 1)

    def test_command(self):
        Author.objects.create(name="Alice", url="http://www.example.org/")

        out = StringIO()
        call_command("findreplace", "--no-input", "http://", "https://", stdout=out)

        self.assertEqual(Author.objects.filter(url__startswith="https://").count(), 1)

    @mock.patch("builtins.input")
    def test_command_cancelled(self, mock_input):
        Author.objects.create(name="Alice", url="http://www.example.org/")

        mock_input.return_value = "no\n"
        stdout_ = StringIO()
        call_command("findreplace", "http://", "https://", stdout=stdout_)

        self.assertIn("Find and replace cancelled", stdout_.getvalue())
        self.assertEqual(Author.objects.filter(url__startswith="https://").count(), 0)
