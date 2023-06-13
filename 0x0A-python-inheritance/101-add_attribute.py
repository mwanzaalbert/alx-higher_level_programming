def add_attribute(obj, attribute_name, value):
    if hasattr(obj, attribute_name):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, attribute_name, value)
