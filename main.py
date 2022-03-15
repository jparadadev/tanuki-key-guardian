import argparse

from src.apps.backoffice.backend.boot import boot as boot_backoffice
from src.apps.ca.boot import boot as boot_ca


service_mapping = {
    'backoffice': boot_backoffice,
    'ca': boot_ca,
}

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--service',
        type=str,
        nargs='?',
        help='Service to run must be one of ["backoffice", "ca"]',
    )
    params = vars(parser.parse_args())
    service_name = params['service']
    service_booter = service_mapping[service_name]

    print(f'Booting {service_name} server')
    service_booter()
    print(f'{service_name} server start success')
