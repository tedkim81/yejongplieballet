import user_agents

class UserAgentMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ua_string = request.META.get("HTTP_USER_AGENT", "")
        request.user_agent = user_agents.parse(ua_string)
        response = self.get_response(request)
        return response