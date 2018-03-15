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

def average(l):
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
		print 'Season ',i
		season = txt[start[i]:end[i]]
		epstart = [m.start() for m in re.finditer('<tr', season)]
		epend = [m.start() for m in re.finditer('tr>', season)]
		season_views = []

		for j in range(1, len(epstart)):
			print '\t\tEpisode', j,
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

	v, a = [], [] # views, average

	for i in range(num_seasons):
		av = average(all_views[i])
		for each in all_views[i]:
			if not isinstance(each, float):
				each = 0
			a.append(float(each)-av)
			v.append(av)

		# for j in range(8):
		# 	a.append(0.0-av)
		# 	v.append(0)

	# print '\n\n\n\n'

	# for i in range(num_seasons):
	# 	for each in all_views[i]:
	# 		print str(av)+'\t',
	# 	print '0\t0\t0\t0\t0\t0\t0\t0\t',
	return a, v


def tabprint(l):
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
		av = average(season)
		av_season = []
		for episode in season:
			av_season.append(av)
		avg.append(av_season)

	tabprint(all_views)
	tabprint(avg)

	return all_views, avg



def plotting(views, average):
	small = min([i for i in views if i!=0])
	large = max([i for i in views if i!='-'])

	fig, ax1 = plt.subplots()
	xaxis = range(0, len(views) )
	ax1.plot(xaxis, views, 'ro')
	ax2 = ax1.twinx()
	ax2.plot(xaxis, average, 'b.')

	ax1.set_ylim(small, large)
	ax2.set_ylim(small, large)

	fig.tight_layout()
	plt.show()



if __name__ == '__main__':
	# views, average = wikiscrape('https://en.wikipedia.org/wiki/List_of_Two_and_a_Half_Men_episodes')
	views, average = imdbscrape('http://www.imdb.com/title/tt0369179/')
	# plotting(views, average)