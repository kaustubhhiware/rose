##
## Scrape wikipedia to get number of views.
## author: @kaustubhhiware
##

import requests
import re
import matplotlib.pyplot as plt

floating_point = '[-+]?[0-9]*\.?[0-9]*'
not_found = 'N/A'
num_seasons = 12

def average_function(l):
    l2 = [i for i in l if i!= '-']
    return sum(l2) / len(l2)

def wikiscrape(wikiurl):
    # imdb page: http://www.imdb.com/title/tt0369179/
    r = requests.get(wikiurl)
    txt = r.content

    start = [m.start() for m in re.finditer('<table', txt)]
    end = [m.start() for m in re.finditer('/table>', txt)]

    # first table is premier dates. Next 12 are only needed
    print 'len', len(start), 'len', len(end)
    # The first table should probably give the number of seasons

    start = start[1:num_seasons + 1]
    end = end[1:num_seasons + 1]
    all_views = []

    print 'len', len(start), 'len', len(end)

    for i in range(num_seasons):
        print 'Season ',i+1
        season = txt[start[i]:end[i]]
        epstart = [m.start() for m in re.finditer('<tr', season)]
        epend = [m.start() for m in re.finditer('tr>', season)]
        season_views = []

        for j in range(1, len(epstart)):
            print '\t\tEpisode', j+1,
            episode = season[epstart[j]:epend[j]]
            view_start = [m.start() for m in re.finditer('<td', episode)][-1]
            view_end = [m.start() for m in re.finditer('/td>', episode)][-1]
        
            views = episode[view_start:view_end]
            found = re.findall(not_found, views)
            if len(found) > 0:
                episodeviews = '-'
            else:
                numviews = float(filter(None, re.findall(floating_point, views))[0])
                episodeviews = numviews

            print episodeviews
            season_views.append(episodeviews)

        print season_views
        all_views.append(season_views)


    # for i in range(num_seasons):
    # 	print 'Season ',i
    # 	for each in all_views[i]:
    # 		print each
    # 	print '\n\n'
    for i in range(num_seasons):
        print len(all_views[i]),

    print ''

    v, a, avg = [], [], [] # views, average

    for i in range(num_seasons):
        av = average_function(all_views[i])
        season_av = []
        for each in all_views[i]:
            if not isinstance(each, float):
                each = 0
            a.append(float(each)-av)
            v.append(av)
            season_av.append(av)
        avg.append(season_av)

        # for j in range(8):
        # 	a.append(0.0-av)
        # 	v.append(0)

    # tabprint(a)
    # tabprint(v)

    return all_views, avg


def tabprint(l):
    print l
    for season in l:
        for episode in season:
            print str(episode)+'\t',
        print '0\t0\t0\t0\t0\t0\t0\t0\t',

    print '\n\n\n'


def imdbscrape(imdburl):
    all_views = []
    for i in range(1, num_seasons+1):
        season_views = []
        url = imdburl + 'episodes?season='+str(i)
        r = requests.get(url)
        txt = r.content
        print 'Season ',i
        
        end = [m.start() for m in re.finditer('<span class="ipl-rating-star__total-votes">', txt)]
        for j in range(len(end)):
            each = end[j]
            episode = txt[each-100:each]
            numviews = float([k for k in filter(None, re.findall(floating_point, episode)) if k!='-'][0])
            # print numviews
            print numviews
            season_views.append(numviews)
        all_views.append(season_views)

    avg = []
    for season in all_views:
        av = average_function(season)
        av_season = []
        for episode in season:
            av_season.append(av)
        avg.append(av_season)

    # tabprint(all_views)
    # tabprint(avg)

    return all_views, avg



def averaged(views, average, loc='lower center'):

    views2, average2 = [], []
    for each in views:
        views2 += [j if isinstance(j, float) else 0 for j in each] + [0]*8
    for each in average:
        average2 += [j if isinstance(j, float) else 0 for j in each] + [0]*8
    
    small = min([i for i in views2 if i!=0])
    large = max([i for i in views2 if i!='-'])
    x = range(len(average2))
    plt.plot(x, views2, label='Views')
    plt.plot(x, average2, label='Average')
    
    plt.legend(loc=loc, ncol=4)
    # plt.ylim(int(small), int(large+1))
    plt.show()


def barchart(views, loc='upper center'):
    maxep = 0
    for i in range(len(views)):
        # views[i] = [j if isinstance(j, float) else 0 for j in views[i]]
        for j in range(len(views[i])):
            episode = views[i][j]
            if not isinstance(episode, float):
                views[i][j] = 0 if j==0 else views[i][j]

        maxep = max(maxep, len(views[i]))
    
    xaxis = range(maxep)
    for i in range(len(views)):
        views[i] += [views[i][-1]]* ( maxep - len(views[i]) )
    
    for i in range(len(views)):
        plt.plot(xaxis, views[i], label=str(i+1))
    
    plt.legend(loc=loc, ncol = 4)
    plt.show()


if __name__ == '__main__':
    views, average = wikiscrape('https://en.wikipedia.org/wiki/List_of_Two_and_a_Half_Men_episodes')
    v2 = views
    print 'TV views barchart'
    # barchart(v2)
    print 'TV views average plot'
    averaged(views, average)
    views, average = imdbscrape('http://www.imdb.com/title/tt0369179/')
    v2 = views
    print 'IMDB ratings barchart'
    # barchart(v2, loc='lower center')
    print 'IMDB ratings average plot'
    # averaged(views, average)
