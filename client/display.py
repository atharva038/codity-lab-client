"""User payload consumer; fetching is injected by callers."""
def display_user(payload):
    return payload["name"]

def load_user(fetch_user, user_id):
    return display_user(fetch_user(str(user_id)))
