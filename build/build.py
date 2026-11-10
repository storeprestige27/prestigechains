"""Builds index.html, chains.html and bracelets.html from shared pieces.

Run from the repo root:  python3 build/build.py
Product names, specs and photos live in CHAINS / BRACELETS below.
"""
import os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EM = '<em style="font-style: italic; color: #E9CC6E">'

# ---------- catalogue (names are provisional English names) ----------
CHAINS = [
    ('cuban', 'Cuban', 'Cubana', 'cuban-trio', '3, 4, 6 and 9 mm', True),
    ('figaro', 'Figaro', 'Cartier', 'figaro-model', '3, 6 and 8 mm', True),
    ('curb', 'Curb', 'Barbada', 'curb-model', '[WIDTHS]', False),
    ('rose-herringbone', 'Rose Herringbone', 'Egipcia rosa', 'ch-rose', '[WIDTHS]', False),
    ('flat-mesh', 'Flat Mesh', 'Chinesca premium', 'ch-premium-mesh', '[WIDTHS]', False),
    ('mesh', 'Mesh', 'Chinesca', 'ch-mesh', '[WIDTHS]', False),
    ('bismark', 'Bismark', 'China', 'ch-bismark', '[WIDTHS]', False),
    ('round-snake', 'Round Snake', 'Cordón', 'ch-cord', '[WIDTHS]', False),
    ('serpentine', 'Serpentine', 'Serpiente', 'ch-serpentine', '6 mm', False),
    ('rectangle', 'Rectangle Link', 'Cubos', 'ch-box', '[WIDTHS]', False),
    ('clip', 'Clip Link', 'Clip', 'ch-fancy', '[WIDTHS]', False),
]
BRACELETS = [
    ('cuban', 'Cuban', 'Cubana', 'br-cuban', '[WIDTHS]', False),
    ('figaro', 'Figaro', 'Cartier', 'br-figaro', '[WIDTHS]', False),
    ('franco', 'Franco', 'Franco', 'br-franco', '[WIDTHS]', False),
    ('flat-mesh', 'Flat Mesh', 'Chinesca premium', 'br-premium-mesh', '[WIDTHS]', False),
    ('bismark', 'Bismark', 'China', 'br-bismark', '[WIDTHS]', False),
    ('interlocked', 'Interlocked', 'Entrelazada', 'br-interlocked', '[WIDTHS]', False),
    ('block', 'Block', 'Bloques', 'br-block', '[WIDTHS]', False),
]

# ---------- shared pieces ----------
def head(title, extra=''):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="robots" content="noindex">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;1,300;1,400;1,500&family=Inter:wght@300;400;500&display=swap">
<link rel="stylesheet" href="assets/site.css">{extra}
</head>
<body>
'''

def menu_list(items, page):
    return '\n'.join(f'<li><a href="{page}#{slug}">{name}</a></li>' for slug, name, *_ in items)

def header(current):
    def cur(k):
        return ' aria-current="page"' if k == current else ''
    return f'''<header class="pc-header">
<button type="button" class="pc-menu-btn" id="menu-open" aria-expanded="false" aria-controls="menu">
<svg aria-hidden="true" viewBox="0 0 24 24"><path d="M3 7h18M3 12h18M3 17h18"></path></svg>
<span>Menu</span>
</button>
<nav class="pc-quick" aria-label="Collections">
<a href="chains.html"{cur('chains')}>Chains</a>
<a href="bracelets.html"{cur('bracelets')}>Bracelets</a>
</nav>
<a class="pc-logo" href="index.html" aria-label="Prestige, home">PRESTIGE</a>
<div class="pc-right">
<a href="index.html#try-on">360° Try-On</a>
<a href="#" aria-label="Bag, 0 items">Bag (0)</a>
</div>
</header>

<div class="pc-menu" id="menu" role="dialog" aria-modal="true" aria-label="Menu" hidden>
<div class="pc-menu-inner">
<button type="button" class="pc-menu-close" id="menu-close" aria-label="Close menu">
<svg aria-hidden="true" viewBox="0 0 24 24"><path d="M5 5l14 14M19 5L5 19"></path></svg>
</button>
<div class="pc-menu-grid">
<div class="pc-menu-main">
<nav aria-label="Main">
<ul class="pc-menu-big">
<li><a href="index.html"{cur('home')}>Home</a></li>
<li><a href="chains.html"{cur('chains')}>Chains</a></li>
<li><a href="bracelets.html"{cur('bracelets')}>Bracelets</a></li>
<li><a href="index.html#try-on">360° Try-On</a></li>
<li><a href="index.html#gold">Our Gold</a></li>
</ul>
</nav>
<ul class="pc-menu-util">
<li><a href="#"><svg aria-hidden="true" viewBox="0 0 24 24"><path d="M6 8h12l-1 12H7L6 8z"></path><path d="M9 8V6a3 3 0 0 1 6 0v2"></path></svg>Bag</a></li>
<li><a href="index.html#gold"><svg aria-hidden="true" viewBox="0 0 24 24"><path d="M12 3l7 3v6c0 4-3 7-7 9-4-2-7-5-7-9V6l7-3z"></path></svg>Warranty &amp; care</a></li>
<li><span><svg aria-hidden="true" viewBox="0 0 24 24"><path d="M4 6h16v12H4z"></path><path d="M4 7l8 6 8-6"></path></svg>[SUPPORT EMAIL]</span></li>
<li><span><svg aria-hidden="true" viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"></circle><path d="M3 12h18M12 3c3 3.5 3 14.5 0 18M12 3c-3 3.5-3 14.5 0 18"></path></svg>United States / English</span></li>
</ul>
</div>
<div class="pc-menu-side">
<p class="pc-menu-head">Chains</p>
<ul>
<li><a href="chains.html">All chains</a></li>
{menu_list(CHAINS, 'chains.html')}
</ul>
<p class="pc-menu-head">Bracelets</p>
<ul>
<li><a href="bracelets.html">All bracelets</a></li>
{menu_list(BRACELETS, 'bracelets.html')}
</ul>
</div>
</div>
</div>
</div>
'''

FOOTER = '''<footer class="pc-footer">
<div class="pc-wrap pc-footer-row">
<a class="pc-logo" href="index.html">PRESTIGE</a>
<nav aria-label="Footer">
<a href="chains.html">Chains</a>
<a href="bracelets.html">Bracelets</a>
<a href="index.html#try-on">360° Try-On</a>
<a href="index.html#gold">Warranty</a>
<a href="index.html#gold">Shipping &amp; returns</a>
</nav>
<span>[SUPPORT EMAIL]</span>
</div>
</footer>
<script src="assets/site.js"></script>
</body>
</html>
'''

NEWSLETTER = f'''<section class="pc-news">
<div class="pc-wrap pc-news-inner">
<h2 class="pc-h2">Receive the {EM}latest</em></h2>
<form class="pc-news-form" onsubmit="event.preventDefault()">
<div class="pc-field">
<label for="nl-email">Email</label>
<input id="nl-email" type="email" autocomplete="email">
</div>
<button type="submit" class="pc-textlink">Subscribe</button>
</form>
</div>
</section>
'''

def card(item, page_kind):
    slug, name, _, img, widths, tryon = item
    extra = '<a class="pc-textlink" href="index.html#try-on">Try it in 360°</a>' if tryon else ''
    noun = 'chain' if page_kind == 'chains' else 'bracelet'
    return f'''<article class="pc-card" id="{slug}">
<div class="pc-card-img"><img src="img/{img}.jpg" alt="Gold plated {name.lower()} {noun}" loading="lazy"></div>
<h3>{name}</h3>
<p class="pc-card-spec">{widths} · [KARAT]K gold plated</p>
<p class="pc-card-price">From [PRICE]</p>
{extra}
</article>'''

def collection(kind, title_word, lead, items, other_href, other_word, other_img, hero_img):
    cards = '\n'.join(card(i, kind) for i in items)
    return head(f'{title_word} — Prestige Chains') + header(kind) + f'''<main>
<section class="pc-coll-hero">
<img class="pc-coll-hero-img" src="img/{hero_img}.jpg" alt="">
<div class="pc-coll-hero-shade" aria-hidden="true"></div>
<div class="pc-wrap pc-coll-hero-text">
<p class="pc-eyebrow">Collection · {len(items)} styles</p>
<h1 class="pc-h1">The {EM}{title_word}</em></h1>
<p class="pc-lead">{lead}</p>
</div>
</section>
<section class="pc-wrap pc-grid-wrap" aria-label="All {title_word.lower()}">
<div class="pc-grid">
{cards}
</div>
</section>
<section class="pc-cross">
<a class="pc-cross-card" href="{other_href}">
<img src="img/{other_img}.jpg" alt="" loading="lazy">
<span class="pc-cross-shade" aria-hidden="true"></span>
<span class="pc-cross-text"><span class="pc-eyebrow">Complete the set</span><span class="pc-h2">Explore {EM}{other_word}</em></span></span>
</a>
</section>
{NEWSLETTER}</main>
''' + FOOTER

# ---------- home: reuse sections from the current page ----------
def home(src):
    def grab(start_pat, end_tag, start=0):
        a = src.index(start_pat, start)
        b = src.index(end_tag, a) + len(end_tag)
        return src[a:b]
    hero = grab('<section id="top"', '</section>')
    statement = grab('<section class="pc-panel" style="overflow: hidden; background: #050505', '</section>')
    cuban = grab('<article id="chains"', '</article>')
    tryon = grab('<section id="try-on"', '</section>')
    gold = grab('<section id="gold"', '</section>')
    # hero tiles open the collections
    hero = hero.replace('href="#chains" class="pc-tile pc-m-l1"', 'href="chains.html#cuban" class="pc-tile pc-m-l1"')
    hero = hero.replace('href="#chains" class="pc-tile pc-m-l2"', 'href="chains.html#figaro" class="pc-tile pc-m-l2"')
    hero = hero.replace('href="#chains" class="pc-tile pc-m-r1"', 'href="chains.html#rose-herringbone" class="pc-tile pc-m-r1"')
    hero = hero.replace('href="#chains" class="pc-tile pc-m-r2"', 'href="chains.html#curb" class="pc-tile pc-m-r2"')
    assert '#chains"' not in hero
    statement = re.sub(r'<a href="#chains"[^>]*>Discover the collection</a>',
        '<div class="pc-cta-row"><a class="pc-textlink" href="chains.html">Shop chains</a><a class="pc-textlink" href="bracelets.html">Shop bracelets</a></div>', statement)
    assert 'Shop chains' in statement
    cuban = cuban.replace('<article id="chains"', '<article id="featured"')
    cuban = cuban.replace('<p style="margin: 0; font-size: 12px; letter-spacing: 0.32em; color: #D4AF37">01</p>',
                          '<p style="margin: 0; font-size: 12px; letter-spacing: 0.32em; text-transform: uppercase; color: #D4AF37">Signature</p>')
    cuban = re.sub(r'<a href="#try-on"[^>]*>Discover</a>',
        '<div class="pc-cta-row"><a class="pc-textlink" href="chains.html#cuban">Discover</a><a class="pc-textlink" href="#try-on">Try it in 360°</a></div>', cuban)
    assert 'chains.html#cuban' in cuban
    categories = f'''<section class="pc-panel pc-bg-b pc-cats" aria-label="Shop by category">
<a class="pc-cat" href="chains.html">
<img src="img/cuban-trio.jpg" alt="Gold plated Cuban chains on black suede">
<span class="pc-cat-shade" aria-hidden="true"></span>
<span class="pc-cat-text"><span class="pc-eyebrow">{len(CHAINS)} styles</span><span class="pc-h2">{EM}Chains</em></span><span class="pc-textlink">Explore</span></span>
</a>
<a class="pc-cat" href="bracelets.html">
<img src="img/bracelet-franco.jpg" alt="Gold plated Franco bracelet on black suede">
<span class="pc-cat-shade" aria-hidden="true"></span>
<span class="pc-cat-text"><span class="pc-eyebrow">{len(BRACELETS)} styles</span><span class="pc-h2">{EM}Bracelets</em></span><span class="pc-textlink">Explore</span></span>
</a>
</section>
'''
    pause = '''<script>
(function(){
var hero=document.querySelector('.pc-kb'),pb=document.getElementById('pause'),ip=document.getElementById('ic-pause'),iy=document.getElementById('ic-play'),paused=false;
if(pb)pb.addEventListener('click',function(){paused=!paused;hero.style.animationPlayState=paused?'paused':'running';ip.hidden=paused;iy.hidden=!paused;pb.setAttribute('aria-label',paused?'Play':'Pause');});
})();
</script>
'''
    body = '\n'.join([hero, statement, categories, cuban, tryon, gold])
    return head('Prestige Chains') + header('home') + '<main class="pc-home">\n' + body + '\n' + NEWSLETTER + '</main>\n' + pause + FOOTER

if __name__ == '__main__':
    src = open(os.path.join(ROOT, 'build', 'home-source.html'), encoding='utf-8').read()
    pages = {
        'index.html': home(src),
        'chains.html': collection('chains', 'Chains',
            'Eleven links, from the everyday Cuban to the flat mesh. Every one gold plated, every one shown worn.',
            CHAINS, 'bracelets.html', 'Bracelets', 'bracelet-franco', 'cuban-layered'),
        'bracelets.html': collection('bracelets', 'Bracelets',
            'Seven links cut to match your chain, so the wrist and the neck read as one set.',
            BRACELETS, 'chains.html', 'Chains', 'cuban-trio', 'br-block'),
    }
    for name, html in pages.items():
        assert '{{' not in html
        open(os.path.join(ROOT, name), 'w', encoding='utf-8').write(html)
        print(name, len(html))
