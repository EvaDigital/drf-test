from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    '''
        Django command to create a new administrator user.

        The command creates a new administrator with the given parameters (username and password).

        Usage:
            python manage.py createadmin <username> <password>

        Attributes:
            help (str): Command description for the help output.
    '''
    help = 'Create a new admin user'

    def add_arguments(self, parser):
        '''
            Adds command line arguments for username and password.

            Args:
                parser (ArgumentParser): A parser object for adding arguments.
        '''

        parser.add_argument('username', type=str, help='Username for the new admin user')
        parser.add_argument('password', type=str, help='Password for the new admin user')

    def handle(self, *args, **kwargs):
        """
            Command handler for creating an admin user.

            Args:
                *args: Positional arguments (not used).
                **kwargs: Named arguments containing the username and password.

            Raises:
                Exception: If an error occurs while creating a user.
        """

        username = kwargs['username']
        password = kwargs['password']
        try:
            user = User.objects.create_superuser(username, '', password)
            self.stdout.write(self.style.SUCCESS(f'Admin user "{username}" created successfully.'))
        except Exception as err:
            self.stdout.write(self.style.ERROR(f'Error creating admin user: {str(err)}'))
