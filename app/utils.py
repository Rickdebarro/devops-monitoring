from flask import request

def get_request_metadata():
    return {
        "url": request.url,
        "user_agent": request.headers.get("User-Agent")
    }