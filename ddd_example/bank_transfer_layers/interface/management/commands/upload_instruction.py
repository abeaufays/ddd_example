from django.core.management.base import BaseCommand
from ddd_example.bank_transfer_layers.interface.text_input import instruction_parser

class Command(BaseCommand):
    help = 'Uploads instructions for bank transfers'

    def add_arguments(self, parser):
        parser.add_argument('instruction', type=str)

    def handle(self, *args, **options):
        try:
            instruction = instruction_parser.parse(options['instruction'])
            instruction()
        except ValueError as e:
            self.stdout.write(self.style.ERROR(str(e)))