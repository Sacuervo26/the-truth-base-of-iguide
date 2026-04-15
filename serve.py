"""Tiny zero-dep static server for The Truth Base.

Routes:
  /            → index.html (landing page)
  /home        → index.html
  /search      → search.html
  /doc/<id>    → search.html (hash routing handles the rest)
  /shelf/<x>   → search.html
  /q/<term>    → search.html

Run:  python serve.py [port]
"""
import http.server
import socketserver
import sys
import os
from urllib.parse import unquote

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8080
ROOT = os.path.dirname(os.path.abspath(__file__))


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=ROOT, **kwargs)

    def do_GET(self):
        path = self.path.split('?', 1)[0].split('#', 1)[0]
        # Pretty routes → map to the static HTML, preserve any hash fragment
        if path in ('/', '/search', '/search/', '/home', '/home/'):
            self.path = '/search.html'
        elif path.startswith('/doc/') or path.startswith('/shelf/') or path.startswith('/q/'):
            # Let the search SPA handle the fragment; convert path into hash
            slug = unquote(path.lstrip('/'))
            # 302 to /search.html#/<slug>
            self.send_response(302)
            self.send_header('Location', '/search.html#/' + slug)
            self.end_headers()
            return
        return super().do_GET()

    def log_message(self, fmt, *args):
        sys.stdout.write("%s - %s\n" % (self.address_string(), fmt % args))


if __name__ == '__main__':
    os.chdir(ROOT)
    with socketserver.ThreadingTCPServer(('0.0.0.0', PORT), Handler) as httpd:
        url = 'http://localhost:%d' % PORT
        print('The Truth Base  --  serving %s' % ROOT)
        print('  Landing : %s/' % url)
        print('  Search  : %s/search' % url)
        print('  Example : %s/doc/1  (deep link)' % url)
        print('Press Ctrl+C to stop.')
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print('\nStopped.')
