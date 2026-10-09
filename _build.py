"""Builds the RankRoot site. Edit the settings below, then run:  py _build.py"""
import pathlib

OUT = pathlib.Path(__file__).parent

# ---------- SETTINGS (must match your Payoneer application) ----------
BRAND = "RankRoot"
COUNTRY = "United States"
EMAIL = "contact@rankroot.store"
WHATSAPP = "32497063717"          # international format, digits only, e.g. 212600000000
WHATSAPP_DISPLAY = "+32 497 06 37 17"
TELEGRAM = ""  # without @; leave empty to hide Telegram
YEAR = "2026"
UPDATED = "9 October 2026"
# ---------------------------------------------------------------------

TG = ", Telegram" if TELEGRAM else ""
TG_SLASH = "/Telegram" if TELEGRAM else ""
TG_LI = f'<li><i class="fa-brands fa-telegram"></i> <a href="https://t.me/{TELEGRAM}">@{TELEGRAM}</a></li>' if TELEGRAM else ""
TG_BTN = '<button class="btn btn-tg" type="button" data-send="tg"><i class="fa-brands fa-telegram"></i> Send via Telegram</button>' if TELEGRAM else ""

HEAD = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Nunito:wght@700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
<link rel="stylesheet" href="styles.css">
</head>
<body>
<header>
  <nav class="container nav">
    <a class="logo" href="index.html"><i class="fa-solid fa-seedling"></i> {brand}</a>
    <button class="nav-toggle" aria-label="Menu" onclick="this.nextElementSibling.classList.toggle('open')"><i class="fa-solid fa-bars"></i></button>
    <ul>
      <li><a href="index.html#services">Services</a></li>
      <li><a href="index.html#plans">Plans</a></li>
      <li><a href="index.html#process">Process</a></li>
      <li><a href="index.html#payment">Payment</a></li>
      <li><a class="btn" href="index.html#plans"><i class="fa-solid fa-bolt"></i> Get Started</a></li>
    </ul>
  </nav>
</header>
"""

FOOT = f"""<footer>
  <div class="container">
    <div class="footer-grid">
      <div>
        <h4>About Us</h4>
        <p style="font-size:.93rem">{BRAND} is an independent SEO studio based in {COUNTRY}. We help small businesses rank with technical SEO, on-page optimisation, quality content and fast websites. White-hat methods only.</p>
      </div>
      <div>
        <h4>Quick Links</h4>
        <ul>
          <li><a href="index.html#services">Our Services</a></li>
          <li><a href="index.html#plans">Plans &amp; Pricing</a></li>
          <li><a href="index.html#process">How It Works</a></li>
          <li><a href="index.html#payment">Payment Methods</a></li>
          <li><a href="index.html#faq">FAQ</a></li>
        </ul>
      </div>
      <div>
        <h4>Services</h4>
        <ul>
          <li><a href="index.html#plan-audit">SEO Audit</a></li>
          <li><a href="index.html#plan-monthly">Monthly SEO</a></li>
          <li><a href="index.html#plan-content">SEO Content Writing</a></li>
          <li><a href="index.html#plan-web">Website Design</a></li>
        </ul>
      </div>
      <div class="contact">
        <h4>Contact Us</h4>
        <ul>
          <li><i class="fa-regular fa-envelope"></i> <a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li><i class="fa-brands fa-whatsapp"></i> <a href="https://wa.me/{WHATSAPP}">{WHATSAPP_DISPLAY}</a></li>
          {TG_LI}
          <li><i class="fa-solid fa-location-dot"></i> {COUNTRY}</li>
        </ul>
      </div>
    </div>
    <p class="copy">&copy; {YEAR} {BRAND}. All rights reserved. | <a href="privacy.html">Privacy Policy</a> | <a href="terms.html">Terms</a></p>
  </div>
</footer>
"""


def write(fname, title, desc, body, extra=""):
    html = HEAD.format(title=title, desc=desc, brand=BRAND) + "<main>\n" + body + "\n</main>\n" + FOOT + extra + "</body>\n</html>\n"
    (OUT / fname).write_text(html, encoding="utf-8")


def checks(items):
    return '<ul class="checks">' + "".join(f'<li><i class="fa-solid fa-check"></i>{i}</li>' for i in items) + "</ul>"


def pkg(plan, label, price, unit, items, ribbon=None):
    cls = "pkg featured" if ribbon else "pkg"
    rib = f'<span class="ribbon">{ribbon}</span>' if ribbon else ""
    return (f'<div class="{cls}">{rib}<div><span class="badge">{label}</span></div>'
            f'<div class="price">${price} <small>/{unit}</small></div>{checks(items)}'
            f'<button class="btn btn-block" data-plan="{plan} - {label}" data-price="${price}/{unit}">'
            f'<i class="fa-solid fa-cart-shopping"></i> Place Order</button></div>')


def panel(pid, color, tag, title, intro, why, side, pk_icon, pk_title, pk_note, packages):
    why_html = '<ul class="why">' + "".join(
        f'<li><i class="fa-regular fa-circle-check"></i><strong>{a}:</strong> {b}</li>' for a, b in why) + "</ul>"
    side_html = "".join(f'<div class="row"><span>{a}</span><span>{b}</span></div>' for a, b in side)
    return f"""
<div id="{pid}" style="--panel: var({color})">
  <div class="panel">
    <div class="panel-head"><div class="panel-tag">{tag}</div><h3>{title}</h3></div>
    <div class="panel-body">
      <div>{intro}<h4>Why clients choose this service:</h4>{why_html}</div>
      <div class="side-box"><h5>Service Details</h5>{side_html}</div>
    </div>
  </div>
  <div class="packages">
    <div class="pk-head"><h4><i class="{pk_icon}"></i>{pk_title}</h4><small>{pk_note}</small></div>
    <div class="grid grid-4">{''.join(packages)}</div>
  </div>
</div>"""


# ================= HOME =================
services = [
    ("fa-solid fa-magnifying-glass-chart", "SEO Audit", "A full health check of your website with a clear, prioritised list of what to fix first.",
     ["Crawl &amp; indexing check", "Core Web Vitals review", "On-page analysis", "PDF action plan"]),
    ("fa-solid fa-gears", "Technical SEO", "We fix the problems that stop Google from crawling, indexing and understanding your pages.",
     ["Sitemaps &amp; robots.txt", "Redirects &amp; 404s", "Schema markup", "Speed optimisation"]),
    ("fa-solid fa-file-pen", "On-Page Optimization", "Titles, headings, meta descriptions and internal links tuned for the keywords that matter.",
     ["Keyword mapping", "Meta tags", "Internal linking", "Image alt text"]),
    ("fa-solid fa-pen-nib", "SEO Content Writing", "Researched, original articles written to answer real search intent and convert readers.",
     ["Keyword research", "1,500+ words", "Topic clusters", "100% original"]),
    ("fa-solid fa-location-dot", "Local SEO", "Help nearby customers find you on Google Search and Google Maps.",
     ["Google Business Profile", "Local landing pages", "LocalBusiness schema", "NAP consistency"]),
    ("fa-solid fa-laptop-code", "Website Design", "Fast, mobile-first WordPress and static websites built to rank from day one.",
     ["WordPress / Elementor", "Mobile-first design", "Core Web Vitals ready", "SEO setup included"]),
]
svc_html = "".join(
    f'<div class="card"><div class="ico"><i class="{ic}"></i></div><h3>{t}</h3><p>{d}</p>{checks(c)}</div>'
    for ic, t, d, c in services)

plans_html = "".join([
    panel("plan-audit", "--c-audit", "AU", "Complete SEO Audit Service",
          "<p>An SEO audit is the starting point of every successful SEO project. We crawl your website the way search engines do and review its technical health, on-page optimisation, content quality and page speed.</p>"
          "<p>You receive a clear report that explains every issue in plain language, ranked by impact, so you or your developer know exactly what to fix first.</p>",
          [("Full Site Crawl", "Every page checked for errors"), ("Prioritised Fixes", "High-impact issues first"),
           ("Core Web Vitals", "LCP, INP and CLS reviewed"), ("Search Console Review", "Indexing and coverage issues"),
           ("Competitor Snapshot", "See what top-ranking pages do"), ("Plain-English Report", "No jargon, clear next steps")],
          [("Delivery", "2&ndash;5 days"), ("Format", "PDF + spreadsheet"), ("Revisions", "1 Q&amp;A call"), ("Support", "Email / WhatsApp")],
          "fa-solid fa-magnifying-glass-chart", "SEO Audit Packages", "Choose by website size",
          [pkg("SEO Audit", "Starter", 59, "audit", ["Up to 25 pages", "Technical check", "PDF report"]),
           pkg("SEO Audit", "Standard", 99, "audit", ["Up to 100 pages", "Technical + on-page", "Priority fix list"], "POPULAR"),
           pkg("SEO Audit", "Advanced", 179, "audit", ["Up to 500 pages", "Content + speed review", "Competitor snapshot"]),
           pkg("SEO Audit", "E-commerce", 299, "audit", ["Up to 2,000 pages", "Product &amp; category SEO", "30-min review call"])]),
    panel("plan-monthly", "--c-monthly", "SEO", "Monthly On-Page &amp; Technical SEO",
          "<p>SEO is not a one-time task. Our monthly plans keep improving your site every month: fixing technical issues, optimising existing pages and publishing new content around the keywords your customers search for.</p>"
          "<p>Each month you get a report based on your own Google Search Console data, so you always see what changed and what comes next.</p>",
          [("Ongoing Optimisation", "Steady month-by-month improvements"), ("Keyword Strategy", "Focus on terms that bring customers"),
           ("Technical Monitoring", "Problems fixed before they hurt rankings"), ("Fresh Content", "New articles every month"),
           ("Transparent Reports", "Based on your Search Console data"), ("No Lock-In", "Cancel with 30 days' notice")],
          [("Billing", "Monthly in advance"), ("Reporting", "Monthly PDF"), ("Contract", "Month to month"), ("Support", "Email / WhatsApp")],
          "fa-solid fa-chart-line", "Monthly SEO Plans", "Cancel anytime",
          [pkg("Monthly SEO", "Basic", 149, "month", ["10 pages optimised", "1 article / month", "Monthly report"]),
           pkg("Monthly SEO", "Growth", 249, "month", ["25 pages optimised", "2 articles / month", "Technical fixes"], "POPULAR"),
           pkg("Monthly SEO", "Pro", 399, "month", ["50 pages optimised", "4 articles / month", "Schema &amp; speed work"]),
           pkg("Monthly SEO", "Business", 599, "month", ["Unlimited pages", "6 articles / month", "Monthly strategy call"], "PREMIUM")]),
    panel("plan-content", "--c-content", "CW", "SEO Content Writing Service",
          "<p>Great content is what Google ranks and what turns visitors into customers. Every article starts with keyword and search-intent research, then is written by hand to be genuinely useful to your readers.</p>"
          "<p>Articles are delivered ready to publish, with an SEO title, meta description, heading structure and internal-link suggestions.</p>",
          [("Intent Research", "Written for what searchers really want"), ("Original Writing", "No copy-paste, no spun text"),
           ("SEO Structure", "Headings, meta tags and FAQs included"), ("Internal Linking", "Suggestions to connect your pages"),
           ("Topic Clusters", "Articles that support each other"), ("Ready to Publish", "Delivered in Google Docs or HTML")],
          [("Length", "1,500&ndash;2,500 words"), ("Delivery", "2&ndash;3 days / article"), ("Revisions", "2 free rounds"), ("Languages", "English, French")],
          "fa-solid fa-pen-nib", "Content Packages", "Price per package",
          [pkg("Content", "1 Article", 29, "package", ["1,500+ words", "Keyword research", "Meta title &amp; description"]),
           pkg("Content", "5 Articles", 129, "package", ["1,500+ words each", "Topic cluster plan", "Internal link map"], "POPULAR"),
           pkg("Content", "10 Articles", 239, "package", ["2,000+ words each", "Topic cluster plan", "FAQ sections"]),
           pkg("Content", "20 Articles", 449, "package", ["2,000+ words each", "Full content strategy", "Priority delivery"])]),
    panel("plan-web", "--c-web", "WEB", "SEO-Ready Website Design",
          "<p>A website that loads slowly or breaks on mobile will struggle to rank, however good the content is. We build fast, clean websites with SEO built in from the first line of code.</p>"
          "<p>Choose WordPress if you want to edit content yourself, or a static website for top speed and near-zero hosting costs.</p>",
          [("Mobile-First", "Designed for phones first"), ("Fast Loading", "Optimised for Core Web Vitals"),
           ("SEO Setup", "Meta tags, sitemap and schema"), ("Easy Editing", "WordPress + Elementor option"),
           ("Secure Hosting Setup", "HTTPS and domain connection"), ("Handover Guide", "You own everything we build")],
          [("Delivery", "5&ndash;21 days"), ("Payment", "50% upfront"), ("Revisions", "2&ndash;3 rounds"), ("Support", "30 days free")],
          "fa-solid fa-laptop-code", "Website Packages", "One-time price",
          [pkg("Website", "Landing Page", 199, "project", ["1 page", "Contact form", "Basic SEO setup"]),
           pkg("Website", "Business Site", 399, "project", ["Up to 6 pages", "WordPress or static", "Full SEO setup"], "POPULAR"),
           pkg("Website", "Pro Website", 699, "project", ["Up to 12 pages", "Blog setup", "Speed optimisation"]),
           pkg("Website", "Online Store", 999, "project", ["WooCommerce", "Up to 50 products", "Product SEO"], "PREMIUM")]),
])

steps = [("Choose a plan", "Pick the package that fits your goals and click Place Order."),
         ("Share details", "Send your website, target keywords and any notes."),
         ("We get to work", "You receive a timeline and updates while we work."),
         ("Report &amp; results", "You get the deliverables and a clear report of everything done.")]
steps_html = "".join(f'<div class="step"><div class="num">{i}</div><h3>{t}</h3><p>{d}</p></div>' for i, (t, d) in enumerate(steps, 1))

pays = [("fa-solid fa-building-columns", "Bank Transfer", "Local / International"),
        ("fa-solid fa-wallet", "Payoneer", "Payment request / invoice"),
        ("fa-solid fa-globe", "Wise", "International transfer"),
        ("fa-regular fa-credit-card", "Visa / Mastercard", "Via secure invoice link")]
pay_html = "".join(f'<div class="pay"><i class="{i}"></i><h3>{t}</h3><p>{d}</p></div>' for i, t, d in pays)

whys = [("fa-solid fa-rocket", "Fast Delivery", "A clear timeline is agreed before any work starts."),
        ("fa-solid fa-shield-halved", "White-Hat Only", "We follow Google's guidelines. No link schemes or shortcuts that risk penalties."),
        ("fa-solid fa-chart-line", "Real Reporting", "Reports based on your own Search Console and analytics data."),
        ("fa-solid fa-headset", "Direct Support", "Talk to the person doing the work by WhatsApp" + TG + " or email."),
        ("fa-solid fa-file-invoice", "Invoice for Every Order", "Every payment comes with a proper invoice."),
        ("fa-solid fa-lock", "Your Data Stays Private", "Access to your site and accounts is only used for your project.")]
why_html = "".join(f'<div class="why-card"><i class="{i}"></i><div><h3>{t}</h3><p>{d}</p></div></div>' for i, t, d in whys)

faqs = [("How long does SEO take to show results?", "Technical fixes can show up in Search Console within a few weeks. Content-led growth usually takes 3&ndash;6 months. Anyone who promises page-one rankings in days is not being honest."),
        ("Do you guarantee rankings?", "No. Rankings depend on Google's algorithm and your competition. We guarantee professional, guideline-compliant work and transparent reporting."),
        ("Do you sell backlinks or PBN links?", "No. We focus on technical SEO, on-page optimisation and content. Buying links breaks Google's guidelines and can get a site penalised."),
        ("What do you need from me to start?", "Your website URL, your main goals and target keywords, and for some services, access to Google Search Console or your WordPress dashboard."),
        ("How do I pay?", "By bank transfer, Payoneer, Wise or card through a secure invoice link. You receive an invoice for every order."),
        ("Can I cancel a monthly plan?", "Yes. Monthly plans run month to month and can be cancelled with 30 days' notice.")]
faq_html = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faqs)

home = f"""
<section class="hero"><div class="container">
  <h1>Grow Your Organic Traffic with Professional SEO</h1>
  <p>Technical SEO, on-page optimisation, SEO content and fast websites for businesses that want to be found on Google.</p>
  <a class="btn" href="#plans"><i class="fa-solid fa-tag"></i> View Plans</a>
  <div class="trust">
    <span><i class="fa-regular fa-circle-check"></i>White-Hat Methods</span>
    <span><i class="fa-solid fa-truck-fast"></i>Fast Delivery</span>
    <span><i class="fa-solid fa-file-lines"></i>Clear Reports</span>
    <span><i class="fa-solid fa-headset"></i>Support via WhatsApp{TG_SLASH}</span>
  </div>
</div></section>

<section id="services" class="alt"><div class="container">
  <div class="section-title"><h2>Our SEO Services</h2><p>Everything your website needs to rank, built on Google's guidelines for steady, long-term growth.</p></div>
  <div class="grid grid-3">{svc_html}</div>
</div></section>

<section id="plans"><div class="container">
  <div class="section-title"><h2>Plans &amp; Pricing</h2><p>All plans are on one page. Click &ldquo;Place Order&rdquo; to send your order details directly to us.</p></div>
  {plans_html}
</div></section>

<section id="process" class="alt"><div class="container">
  <div class="section-title"><h2>How It Works</h2><p>A simple, transparent process from order to results.</p></div>
  <div class="grid grid-4">{steps_html}</div>
</div></section>

<section id="payment"><div class="container">
  <div class="section-title"><h2>Secure Payment Methods</h2><p>We accept several payment options and send an invoice for every order.</p></div>
  <div class="pay-grid">{pay_html}</div>
</div></section>

<section class="alt"><div class="container">
  <div class="section-title"><h2>Why Choose Us?</h2><p>Clear communication, honest methods and real reporting.</p></div>
  <div class="grid grid-3">{why_html}</div>
</div></section>


<section id="faq" class="alt"><div class="container">
  <div class="section-title"><h2>Frequently Asked Questions</h2></div>
  <div class="faq">{faq_html}</div>
</div></section>
"""

MODAL = f"""
<div class="modal" id="orderModal" role="dialog" aria-modal="true" aria-labelledby="orderTitle">
  <div class="modal-box">
    <button class="modal-close" aria-label="Close">&times;</button>
    <h3 id="orderTitle">Place Order</h3>
    <p>Fill in your details and send them by WhatsApp{TG} or email. We reply with a confirmation and an invoice.</p>
    <label for="oPlan">Selected plan</label><input id="oPlan" readonly>
    <label for="oPrice">Price</label><input id="oPrice" readonly>
    <label>Payment via</label>
    <div class="pay-pick" id="oPay">
      <button type="button" class="on">Payoneer</button><button type="button">Bank Transfer</button><button type="button">Wise</button><button type="button">Card</button>
    </div>
    <label for="oName">Your name</label><input id="oName">
    <label for="oSite">Website URL</label><input id="oSite" placeholder="https://">
    <label for="oKw">Target keywords</label><input id="oKw" placeholder="e.g. dentist in Lyon, best running shoes">
    <label for="oNotes">Notes (optional)</label><textarea id="oNotes"></textarea>
    <div class="send">
      <button class="btn" type="button" data-send="wa"><i class="fa-brands fa-whatsapp"></i> Send via WhatsApp</button>
      {TG_BTN}
      <button class="btn btn-mail" type="button" data-send="mail"><i class="fa-regular fa-envelope"></i> Send via Email</button>
    </div>
  </div>
</div>
<script>
(function () {{
  var modal = document.getElementById('orderModal');
  var $ = function (id) {{ return document.getElementById(id); }};
  document.querySelectorAll('[data-plan]').forEach(function (b) {{
    b.addEventListener('click', function () {{
      $('oPlan').value = b.dataset.plan; $('oPrice').value = b.dataset.price;
      modal.classList.add('open'); $('oName').focus();
    }});
  }});
  function close() {{ modal.classList.remove('open'); }}
  modal.querySelector('.modal-close').onclick = close;
  modal.addEventListener('click', function (e) {{ if (e.target === modal) close(); }});
  document.addEventListener('keydown', function (e) {{ if (e.key === 'Escape') close(); }});
  $('oPay').addEventListener('click', function (e) {{
    if (e.target.tagName !== 'BUTTON') return;
    this.querySelectorAll('button').forEach(function (x) {{ x.classList.remove('on'); }});
    e.target.classList.add('on');
  }});
  function message() {{
    var pay = $('oPay').querySelector('.on').textContent;
    return 'New order - {BRAND}\\n' +
      'Plan: ' + $('oPlan').value + '\\nPrice: ' + $('oPrice').value + '\\nPayment: ' + pay +
      '\\nName: ' + $('oName').value + '\\nWebsite: ' + $('oSite').value +
      '\\nKeywords: ' + $('oKw').value + '\\nNotes: ' + $('oNotes').value;
  }}
  modal.querySelectorAll('[data-send]').forEach(function (b) {{
    b.addEventListener('click', function () {{
      var m = message(), how = b.dataset.send;
      if (how === 'wa') window.open('https://wa.me/{WHATSAPP}?text=' + encodeURIComponent(m), '_blank');
      if (how === 'mail') location.href = 'mailto:{EMAIL}?subject=' + encodeURIComponent('Order: ' + $('oPlan').value) + '&body=' + encodeURIComponent(m);
      if (how === 'tg') {{
        // Telegram can't pre-fill a direct message, so copy the order text first.
        try {{ navigator.clipboard.writeText(m); }} catch (e) {{}}
        alert('Order details copied. Paste them into the Telegram chat that opens next.');
        window.open('https://t.me/{TELEGRAM}', '_blank');
      }}
    }});
  }});
}})();
</script>
"""

write("index.html", f"{BRAND} - Professional SEO Services | Audits, Content &amp; Websites",
      "White-hat SEO services: SEO audits, monthly on-page and technical SEO, SEO content writing and fast SEO-ready websites. Clear pricing and real reporting.",
      home, MODAL)

# ================= LEGAL =================
write("privacy.html", f"Privacy Policy | {BRAND}", f"Privacy policy for {BRAND}.", f"""
<section class="legal-page"><div class="container prose">
  <h1>Privacy Policy</h1>
  <p>Last updated: {UPDATED}</p>
  <p>This website is operated by {BRAND}, based in {COUNTRY}. This policy explains what personal data we collect and how we use it.</p>
  <h2>Data we collect</h2>
  <ul><li>Details you send us by email, WhatsApp{TG} or the order form: your name, contact details, website URL, keywords and notes.</li>
  <li>Billing details needed to issue invoices.</li></ul>
  <h2>How we use it</h2>
  <p>Only to reply to your enquiry, deliver the services you order and send invoices. We never sell or rent your data.</p>
  <h2>Access to your accounts</h2>
  <p>If you give us access to your website, Google Search Console or analytics, we use it only for your project and you can revoke it at any time.</p>
  <h2>Third parties</h2>
  <p>Data may be processed by the services we use to run the business: email and messaging providers, website hosting and payment providers such as Payoneer, Wise and banks. Each has its own privacy policy.</p>
  <h2>Retention</h2>
  <p>Enquiries are kept for up to 24 months. Invoices are kept for as long as tax law requires.</p>
  <h2>Your rights</h2>
  <p>You can ask to access, correct or delete your personal data at any time by emailing <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
  <h2>Cookies</h2>
  <p>This website does not use advertising or tracking cookies.</p>
</div></section>""")

write("terms.html", f"Terms of Service | {BRAND}", f"Terms of service for {BRAND}.", f"""
<section class="legal-page"><div class="container prose">
  <h1>Terms of Service</h1>
  <p>Last updated: {UPDATED}</p>
  <p>These terms apply to all services provided by {BRAND}, {COUNTRY}.</p>
  <h2>Orders</h2>
  <p>An order is confirmed when we accept it in writing and the invoice is paid. The deliverables are those listed in the chosen package. Extra work is quoted separately.</p>
  <h2>Payment</h2>
  <p>One-time services (audits, content) are paid before work starts. Websites: 50% upfront and 50% on delivery. Monthly plans are billed monthly in advance. We accept bank transfer, Payoneer, Wise and card payments through invoice links.</p>
  <h2>Delivery</h2>
  <p>Delivery times are estimates given at order confirmation. They start once we receive payment and everything we need from you, such as access and content.</p>
  <h2>Revisions and refunds</h2>
  <p>Each package includes the revisions listed. Work that has not started can be refunded in full. Work already delivered is not refundable.</p>
  <h2>Cancellation</h2>
  <p>Monthly plans can be cancelled with 30 days' written notice.</p>
  <h2>No ranking guarantees</h2>
  <p>Search rankings depend on factors outside our control, including search engine algorithms and competition. We guarantee professional, guideline-compliant work, not specific positions or traffic numbers.</p>
  <h2>Prohibited sites</h2>
  <p>We do not work on websites that promote illegal activity, copyright infringement, gambling, adult content or deceptive schemes.</p>
  <h2>Ownership</h2>
  <p>Once paid in full, you own the content and website files delivered for your project.</p>
  <h2>Liability</h2>
  <p>Our total liability for any order is limited to the amount paid for that order.</p>
  <h2>Contact</h2>
  <p><a href="mailto:{EMAIL}">{EMAIL}</a></p>
</div></section>""")

print("built:", ", ".join(sorted(p.name for p in OUT.glob("*.html"))))
