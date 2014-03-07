from music_brainz import *

def test_main():
    results = query_by_name(ARTIST_URL, query_type["simple"], "First Aid Kit")
    print "%s artists named 'First Aid Kit'" % len([x for x in results['artist'] if x['name'] == "First Aid Kit"])

    results = query_by_name(ARTIST_URL, query_type["simple"], "Queen")
    queens = [x for x in results["artist"] if x.get("disambiguation", '') == "UK rock group" ]
    #queens = [ "%s : %s" % (x['id'], x.get('disambiguation','')) for x in results["artist"] ]
    for q in queens:
        print "Queen begin area: %s " % q['begin-area']['name']

    results = query_by_name(ARTIST_URL, query_type["simple"], "Beatles")
    beatles = results['artist'][0]
    spanish_name = [x['name'] for x in beatles['aliases'] if x['locale'] == 'es']
    print spanish_name[0]


    results = query_by_name(ARTIST_URL, query_type["simple"], "nirvana")
    nirvans = [x for x in results['artist'] if x.get('country', "") == 'US']
    print [x.get("disambiguation", "NA") for x in nirvans]

    results = query_by_name(ARTIST_URL, query_type["simple"], "One Direction")
    artist_id = results["artist"][0]["id"]

    artist_data = query_site(ARTIST_URL, query_type["releases"], artist_id)
    releases = artist_data["releases"]
    #print "\nONE RELEASE:"
    #pretty_print(releases[0], indent=2)
    release_titles = [r["title"] for r in releases]
    print "One direction release date: %s " % releases[0]['date']
    #print "\nALL TITLES:"
    #for t in release_titles:
        #print t
