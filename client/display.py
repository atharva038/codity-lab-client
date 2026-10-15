"""User payload consumer; fetching is injected by callers."""
def display_user(payload):
    return payload["fullName"]
