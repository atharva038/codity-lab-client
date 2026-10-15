"""User payload consumer; fetching is injected by callers."""
def display_user(payload):
    return f"Hello, {payload['name']}!"
