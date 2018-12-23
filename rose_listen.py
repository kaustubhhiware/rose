import requests
import re
import subprocess
from urllib.parse import unquote

floating_point = '[-+]?[0-9]*\.?[0-9]*'


def episode_scrape(show, season_num, episode_num):
    imdburl = get_link(show, ' imdb', 'https://www.imdb.com')
    imdburl = imdburl + 'episodes?season=' + str(season_num)
    r = requests.get(imdburl)
    season_txt = r.text

    cast = []

    s = '.?ref_=ttep_ep' + str(episode_num) + '"'
    end = [m.start() for m in re.finditer(s, season_txt)]
    each = end[0]
    season = season_txt[each - 30:each]
    p = [f.start() for f in re.finditer("/title/", season)][0]
    season_url = 'https://www.imdb.com' + season[p:]
    r = requests.get(season_url)
    episode_txt = r.text
    s = '"ratingValue":'
    end = [m.start() for m in re.finditer(s, episode_txt)]
    each = end[0]
    value = episode_txt[each:each + 25]
    rating = float([k for k in [_f for _f in re.findall(floating_point, value) if _f] if k != '-'][0])

    print(show + ' Season ' + str(season_num) + ' Episode ' + str(episode_num))
    print('IMDB rating:', rating)

    each = [m.start() for m in re.finditer(':</td></tr>', episode_txt)]
    si = each[0]
    each = [m.start() for m in re.finditer('</table>', episode_txt)]
    ei = each[0]
    cast_txt = episode_txt[si + 11:ei]

    start = [m.start() for m in re.finditer('<tr', cast_txt)]
    end = [m.start() for m in re.finditer('</tr>', cast_txt)]
    for j in range(len(end)):
        si = start[j]
        ei = end[j]
        char_txt = cast_txt[si:ei]
        a_start = [m.start() for m in re.finditer('<a', char_txt)]
        a_end = [m.start() for m in re.finditer('</a>', char_txt)]
        for k in range(len(a_end)):
            if k == 1:
                s = a_start[k]
                e = a_end[k]
                a_txt = char_txt[s:e]
                cast.append(a_txt[a_txt.rfind('>') + 2:])

    count = 1
    print("Cast:")
    for actor in cast:
        print('\t' + str(count) + '. ' + actor)
        count += 1


def get_link(show, key, starturl):
    key = show + key
    search = 'https://www.google.co.in/search?q=' + key.replace(' ', '+')
    r = requests.get(search)

    end = '&amp;'
    start_index = r.text.find(starturl)
    end_index = start_index + r.text[start_index:].find(end)
    url = unquote(r.text[start_index: end_index])

    return url


if __name__ == '__main__':
    try:
        result = subprocess.run(['playerctl', 'metadata', 'xesam:url'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        file_location = result.stdout.decode('utf-8')
        error = result.stderr.decode('utf-8')

        if error == "Connection to player failed: No players found\n":
            print("You aren't playing any episode currently.")
        else:
            filename = unquote(file_location[file_location.rfind('/') + 1:file_location.rfind('.')])

            try:
                s = '[Ss][0-9]+[Ee][0-9]+'
                end = [m.start() for m in re.finditer(s, filename)]
                each = end[0]
                name = filename[0:each]
                epi = filename[each:each + 6]
                epi = epi.upper()

                s_index = epi.index('S')
                e_index = epi.index('E')
                season_num = int(epi[s_index + 1:e_index])
                episode_num = int(epi[e_index + 1:])

                show = ''
                for i in range(len(name)):
                    if name[i] == '.':
                        show += ' '
                    else:
                        show += name[i]
                while show[len(show) - 1] == '-' or show[len(show) - 1] == ' ':
                    show = show[:-1]

                episode_scrape(show, season_num, episode_num)
            except (ValueError, IndexError) as e:
                print('Invalid episode nomenclature')

    except FileNotFoundError:
        print('Please install playerctl to continue using this feature.')
