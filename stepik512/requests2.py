"""
Вашей программе на вход подается ссылка на HTML файл.
Вам необходимо скачать этот файл, затем найти в нем все ссылки вида <a ... href="..." ... >
и вывести список сайтов, на которые есть ссылка.

Сайтом в данной задаче будем называть имя домена вместе с именами поддоменов.
То есть, это последовательность символов, которая следует сразу после символов протокола, если он есть,
до символов порта или пути, если они есть, за исключением случаев с относительными ссылками вида
<a href="../some_path/index.html">.

Сайты следует выводить в алфавитном порядке.

Пример HTML файла:

<a href="http://stepic.org/courses">
<a href='https://stepic.org'>
<a href='http://neerc.ifmo.ru:1345'>
<a href="ftp://mail.ru/distib" >
<a href="ya.ru">
<a href="www.ya.ru">
<a href="../skip_relative_links">

Пример ответа:

mail.ru
neerc.ifmo.ru
stepic.org
www.ya.ru
ya.ru

Ответ на текст http://pastebin.com/raw/7543p0ns

adworker.ru
banner.rbc.ru
biztorg.ru
blogi.rbc.ru
cnews.ru
consensus.rbc.ru
conv.rbc.ru
credit.rbc.ru
data.rbc.ru
dict.rbc.ru
drinktime.ru
events.cnews.ru
export.rbc.ru
finolymp.ru
gift.cnews.ru
graph.rbc.ru
magazine.rbc.ru
map.rbc.ru
marketing.rbc.ru
memori.ru
otc-pif.rbc.ru
otc-stock.rbc.ru
pda.rbc.ru
pogoda.rbc.ru
portfolio.rbc.ru
quote-otc.rbc.ru
quote.ru
raiting.rbc.ru
rating.rbc.ru
realty.rbc.ru
redir.rbc.ru
rss.rbc.ru
seminar.rbc.ru
spb.rbc.ru
sport.rbc.ru
static.feed.rbc.ru
stock.rbc.ru
style.rbc.ru
ta.rbc.ru
tata.ru
top.rbc.ru
top100.rambler.ru
turbo.ru
tv.rbc.ru
ug.rbc.ru
ulov-umov.ru
videoarchive.rbc.ru
www.5ballov.ru
www.armd.ru
www.autonews.ru
www.biztorg.ru
www.cnews.ru
www.conf.rbc.ru
www.event.rbc.ru
www.iglobe.ru
www.informer.ru
www.ivd.ru
www.liveinternet.ru
www.m-2.ru
www.nashidengi.ru
www.pochta.ru
www.quote.ru
www.quoterate.ru
www.quotetotal.ru
www.rbc.ru
www.rbc.ua
www.rbcdaily.ru
www.rbcinfosystems.com
www.rbcnews.com
www.rbctv.ru
www.refunder.ru
www.salon.ru
www.seminar.rbc.ru
www.top.rbc.ru
www.turbo.ru
www.turist.ru
www.utro.ru
www.worldclass.ru
zoom.cnews.ru

"""
import requests
import re


def main():
    start_url = input()
    resp = requests.get(start_url)
    pattern = re.compile(r'<a.*href=[\'\"]((http://)|(https://)|(ftp://))?([\w\.-]{3,}).*?>')

    urls = re.findall(pattern, resp.text)
    ans = set()
    for url in urls:
        ans.add(url[4])
    for url in sorted(ans):
        print(url)


if __name__ == '__main__':
    main()
