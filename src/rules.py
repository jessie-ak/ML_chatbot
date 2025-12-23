import re

def check_rules(user_text):
    '''checks hard-coded rules for input matches'''
    cleaned_input = user_text.lower().strip()
    if cleaned_input in ['exit','bye','stop','quit']:
        return 'Goodbye! Thanks for chatting.'
    if cleaned_input == 'help':
        return 'I can answer questions about our hours, services, or just say hello!'
    if re.search(r"id-\d+", cleaned_input):
        return "I noticed you mentioned a Tracking ID. Let me check the database..."
    '''if rules don't match ask model'''
    return None