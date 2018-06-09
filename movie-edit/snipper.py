import random, math

'''
Stitch two videos together for a total of 'number' clips,
where stitches last 'time' seconds.

returns list of clips
'''
def snip_clips(clip1, clip2, time, number):
    snips = []

    len1 = clip1.duration
    len2 = clip2.duration

    if (time / 2) > min(len1, len2):
        raise Exception("Time interval cannot be greater than the length of clip!")

    # pick random starting point
    # make sure is between 0 and total duration - 'time'
    start1 = (len1 - time - 0.1)
    start1 = start1 * random.random()

    # same for second clip
    start2 = (len2 - time - 0.1) * random.random()

    for i in range(0, number):
        snips.append(clip1.subclip(start1, start1 + (time / 2)))
        snips.append(clip2.subclip(start2, start2 + (time / 2)))

        start1 = (len1 - (time / 2) - 0.1) * random.random()
        start2 = (len2 - (time / 2) - 0.1) * random.random()

        print([start1, start1 + (time / 2)], [start2, start2 + (time / 2)])

    return snips

def weird_colors(image):
    return image[:,:,[0,2,1]]