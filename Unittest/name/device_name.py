def parse_device_name(vendor, device_type, platform):
    full_name = vendor + ' '+device_type+' '+platform
    return full_name.title()


def parse_device_name(vendor, device_type,platform, spec=''):
    if spec !='':
        full_name = vendor +' '+device_type+' '+platform+' '+spec
    else:
        full_name = vendor +' '+device_type+' '+platform
    return full_name.title()
