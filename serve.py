#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Prosty serwer statyczny z wyłączonym cache (świeże pliki przy każdym żądaniu)."""
import sys
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer


class NoCacheHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate, max-age=0")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        super().end_headers()


if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
    print(f"Serwuję http://localhost:{port}  (cache wyłączony)")
    ThreadingHTTPServer(("0.0.0.0", port), NoCacheHandler).serve_forever()
