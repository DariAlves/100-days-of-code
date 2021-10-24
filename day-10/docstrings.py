def format_name(f_name, l_name):
    """Take a first and last name and format it to return the title case version of the name."""
    formated_f_name = f_name.title() 
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"

formated_full_name = format_name('terry', 'bOGard')

print(formated_full_name)