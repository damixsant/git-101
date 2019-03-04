suffixes= ['KB','MB','GB','TB','PB','EB','ZB','YB']


def approximate_size(size):
    multiple= 1024
    for suffix in suffixes:
        size/=suffixes[multiple]:
        if size < multiple:
            return f'{size} {suffix}'


