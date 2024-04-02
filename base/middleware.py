# middleware.py
from .models import TempUser
from user_agents import parse

class SaveUserDeviceInfoMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user_agent_string = request.META.get('HTTP_USER_AGENT', '')
        user_agent = parse(user_agent_string)
        if request.path == "/":
            TempUser.objects.create(
                user_agent=user_agent,
                device_family=user_agent.device.family,
                device_brand=user_agent.device.brand,
                device_model=user_agent.device.model,
                browser_family=user_agent.browser.family,
                browser_version_string=user_agent.browser.version_string,
                device_os_family=user_agent.os.family,
                device_os_version_string=user_agent.os.version_string,
                is_mobile=user_agent.is_mobile,
                is_tablet=user_agent.is_tablet,
                is_touch_capable=user_agent.is_touch_capable,
                is_pc=user_agent.is_pc,
                is_bot=user_agent.is_bot,
                ip_address=request.META.get('REMOTE_ADDR', '')
            )

        response = self.get_response(request)
        return response
