from googlesearch import search
import utils
import threading
import requests

url_list = []

class dork:
    depth = 0
    def processurls_dork(query):
            for j in search(query, tld="co.in", num=dork.depth, stop=dork.depth):
                if dork.shouldprinturl(j):
                    utils.betterprint(j)
                    url_list.append(j)
    def shouldprinturl(j):
        for x in url_list:
            if x == j:
                return False
        return True
    def setdepth(self):
        f = open("CONFIG/dorksdepth.txt", "w")
        f.write(input("Insert dorking depth: "))
        f.close()
    def dorkingmodule(self, mode):
        url_list = []
        utils.set_target()
        target = open("CONFIG/target.txt", "r").readline()
        if mode == "normal":
            depth = int(input("Max urls per request: "))
        else:
            try:
                depth = int(open("CONFIG/dorksdepth.txt", "r").readline())
            except Exception as e:
                print(e)
                exit()
                depth = 30
        dork.depth = depth
        utils.betterprint(f"Using the dork module against '{target}' with depth {str(depth)}..")
        for line in open("CONFIG/dorks.txt","r").readlines():
            exec(f"dork.processurls_dork(f\"{line.strip()}\")")
    def main(self, mode):
        dork.dorkingmodule(self, mode)

class instagrambio:
    def searchmybio(query):
        r = requests.get(f"https://www.searchmy.bio/search?q={query}")
        result = r.text.split("const initial_results = '[")[1].split("]';")[0].split('],"username":"')
        for x in range(len(result)-1):
            user = result[x+1].split('","')[0]
            followers = result[x].split('","followers_count":')[1].split(',')[0]
            utils.betterprint(f"Matching bio with username: '{user}' -> followers: {followers}")

    def main(self):
        target = open("CONFIG/target.txt", "r").readline()
        utils.betterprint(f"Using instagrambio against '{target}'..")
        try:
            instagrambio.searchmybio(target)
        except IndexError:
            utils.betterprint("No result found with instagrambio module")

class usernamesearch:
    def searchusername(url):
        try:
            domain = url.split("https://")[1].split("/")[0]
            r = requests.get(url, headers={"Accept-Language": "en-US,en;q=0.5", 'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36'})
            for line in open("CONFIG/usernamesearchresults.txt", "r").readlines():
                line = line.strip()
                if domain == line.split(' :: ')[0]:
                    if line.split(f"{domain} :: ")[1].startswith("CONTENT"):
                        utils.betterprint(str(line.split(f"{domain} :: ")[1].split(" :: ")[1] in r.text).replace("False", f"Target found at -> {url}").replace("True", f"Target ·NOT· found at -> {url}"))
                    if line.split(f"{domain} :: ")[1].startswith("STATUSCODE"):
                        utils.betterprint(str(line.split("STATUSCODE :: ")[1] == str(r.status_code)).replace("False", f"Target found at -> {url}").replace("True", f"Target ·NOT· found at -> {url}"))

                    break
        except KeyboardInterrupt:
                return

    def main(self):
        utils.set_target()
        target = open("CONFIG/target.txt", "r").readline()
        utils.betterprint(f"Searching '{target}'..")
        if " " in target:
            utils.betterprint("Skipping the usernamesearchmodule as the target contains spaces")
        else:
            for line in open("CONFIG/usernamesearch.txt", "r").readlines():
                try:
                    exec("threading.Thread(target=usernamesearch.searchusername, args=(line.strip().replace('{target}','"+target+"'),)).start()")
                except KeyboardInterrupt:
                    break

class peoplesearch:
    def radaris(name):
        r = requests.get(name)
        try:
            found = r.text.split('<p class="narrow-normal-small pft-top-text">')[1].split("</span>")[0].replace("<span>", "")
        except:
            found = f"No pepole found for '{name}' in the US using radaris"
        utils.betterprint(f"---\n{name} -> \n{found}\n---")

    def peopledorks():
        dorklist = ["paginebianche {target}", "paginegialle {target}"]
        for d in dorklist:
            for j in search(d, tld="co.in", num=15, stop=15):
                if dork.shouldprinturl(j):
                    utils.betterprint(f"---\nPeopleSearch dorks -> \n{j}\n---")
                    url_list.append(j)

    def main(self):
        target = open("CONFIG/target.txt", "r").readline()
        query = f"https://radaris.com/p/{target.replace(' ', '/')}/"
        utils.betterprint(f"Starting peoplesearch against '{target}'")
        peoplesearch.radaris(query)
        peoplesearch.peopledorks()
