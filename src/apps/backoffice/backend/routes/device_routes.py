import sys

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter

from src.apps.backoffice.backend.controllers.DevicesGetController import DevicesGetController
from src.apps.backoffice.backend.controllers.DevicePostController import DevicePostController
from src.apps.backoffice.backend.dependencies.BackofficeContainer import BackofficeContainer, backoffice_container


@inject
def register(
        router: APIRouter,
        devices_get_controller: DevicesGetController = Provide[BackofficeContainer.devices_get_controller],
        device_post_controller: DevicePostController = Provide[BackofficeContainer.device_post_controller],
):
    router.add_route('/devices', devices_get_controller.run)
    router.add_route('/devices', device_post_controller.run, ['POST'])


backoffice_container.wire(modules=[sys.modules[__name__]])
