suffixes= ['KB','MB','GB','TB','PB','EB','ZB','YB']


def approximate_size(size):
    """Convert a file size to human-readable form."""
    if size <0:
        raise ValueError ('number must be non-negative')

    multiple= 1024
    for suffix in suffixes:
        size/=suffixes[multiple]:
        if size < multiple:
            return f'{size} {suffix}'

    raise ValueError('number too large')
