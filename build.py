import re

# ---------- shared head ----------
def head(title, desc):
    return f"""<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,500;9..144,600;9..144,700&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">

<link rel="stylesheet" href="css/style.css">"""

# ---------- shared sidebar (identical on every page — edit once, copy to all 7 files) ----------
SIDEBAR = """  <aside class="sidebar">
    <div class="sidebar-inner">
      <div class="avatar">
        <img src="images/profile.jpg" alt="Osama" onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';">
        <div class="avatar-fallback">O</div>
      </div>

      <h1 class="name">Osama</h1>
      <p class="role">M.Sc.(Ongoing), CSE, RUET · B.Sc. in CSE, CUET</p>

      <div class="contact-block">
        <p><span>Personal</span><a href="mailto:osamasohag39@gmail.com">osamasohag39@gmail.com</a></p>
        <p><span>Official</span><a href="mailto:your.official@university.edu">your.official@university.edu</a></p>
      </div>

      <p class="tagline">
        M.Sc. researcher studying machine unlearning for morphologically rich languages.
        Also building hands-on engineering skills, one project at a time.
      </p>

      <nav class="social-links" aria-label="Social links">
        <a href="https://github.com/123Osama" target="_blank" rel="noopener">GitHub</a>
        <a href="https://www.linkedin.com/in/osama39/" target="_blank" rel="noopener">LinkedIn</a>
        <a href="https://scholar.google.com/citations?user=UkB_a_IAAAAJ&hl=en" target="_blank" rel="noopener">Google Scholar</a>
        <a href="https://aclanthology.org/people/md-osama/unverified/" target="_blank" rel="noopener">ACL Anthology</a>
      </nav>

      <a class="cv-btn" href="cv.pdf" target="_blank" rel="noopener">Download CV ↓</a>

      <ul class="quick-facts">
        <li><span>Focus</span>Machine Unlearning · Bangla NLP</li>
        <li><span>Target venue</span>ACM TALLIP</li>
        <li><span>Lab</span>Your Lab / Advisor Name</li>
      </ul>
    </div>

    <p class="sidebar-footer">© <span id="year"></span> Osama</p>
  </aside>"""

PAGES = [
    ("index",        "Home"),
    ("research",     "Research"),
    ("projects",     "Projects"),
    ("publications", "Publications"),
    ("skills",       "Skills"),
    ("thoughts",     "My Thought"),
    ("contact",      "Contact"),
]

def nav(current):
    parts = []
    for slug, label in PAGES:
        href = "index.html" if slug == "index" else f"{slug}.html"
        cls = ' class="active"' if slug == current else ''
        parts.append(f'<a href="{href}"{cls}>{label}</a>')
    return "\n      ".join(parts)

def assemble(slug, title, desc, body):
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
{head(title, desc)}
</head>
<body>

<div class="layout">

  <!-- ============ SIDEBAR (same on every page — edit here, then copy into the other 6 files) ============ -->
{SIDEBAR}

  <!-- ============ MAIN CONTENT — THIS PAGE ONLY: {slug}.html ============ -->
  <main class="content">

    <nav class="topnav" aria-label="Section navigation">
      {nav(slug)}
    </nav>

{body}

    <footer class="page-footer">
      <p>Built with plain HTML/CSS/JS · Hosted on GitHub Pages</p>
    </footer>

  </main>
</div>

<script src="js/script.js"></script>
</body>
</html>
"""
    fname = "index.html" if slug == "index" else f"{slug}.html"
    with open(fname, "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", fname)


# =========================================================
# HOME — hero + morpheme demo + bio + scrollable Updates window
# =========================================================
home_body = """    <section class="section hero">
      <p class="eyebrow">Hello, I'm Osama</p>
      <h2 class="hero-line">I build benchmarks for <span class="hl">unlearning</span><br>in languages that don't forget easily.</h2>

      <p class="hero-sub">
        Most machine unlearning research is built and tested on English. My thesis asks what
        happens when you ask a model to <em>forget</em> something in a language like Bangla,
        where a single word can carry a root, tense, number, and case all stitched together.
        Does that structure make forgetting harder to verify — or easier to fake?
      </p>

      <!-- Signature interactive element: morpheme decomposition, English example -->
      <div class="morph-demo" id="morphDemo">
        <p class="morph-caption">Tap a piece of the word</p>
        <div class="morph-word" role="group" aria-label="Word broken into morphemes">
          <button class="morph" data-gloss="un- — negation prefix, “not”">un</button>
          <button class="morph" data-gloss="forget — the root verb, what's being removed">forget</button>
          <button class="morph" data-gloss="-table — suffix, “capable of being”">table</button>
        </div>
        <p class="morph-meaning">unforgettable <span>→</span> <span id="morphGloss">one word, three layers of meaning fused together — the same layering that makes Bangla unlearning hard to measure.</span></p>
      </div>

      <!-- Personal info / bio -->
      <div class="bio">
        <p>
          I'm an M.Sc. student in Computer Science &amp; Engineering, currently in the early
          phase of my thesis. I work at the intersection of <strong>machine unlearning</strong>
          and <strong>Bangla NLP</strong> — figuring out whether existing unlearning methods,
          mostly designed and tested on English, actually hold up against a morphologically
          rich, low-resource language.
        </p>
        <p>
          Outside of research, I'm slowly building up hands-on engineering skills — Python,
          Flask, Django, and full-stack project work — and I have a long-running interest in
          Islamic history. [Edit this paragraph to make it sound like you.]
        </p>
      </div>

      <!-- Scrollable updates window — lives ONLY on Home, per your request -->
      <div class="updates-box">
        <h3 class="updates-title">Updates</h3>
        <ul class="timeline">
          <li><span class="tdate">[Month, Year]</span> Selected thesis direction: machine unlearning for morphologically rich Bangla text.</li>
          <li><span class="tdate">[Month, Year]</span> Began benchmark schema design for the unlearning study.</li>
          <li><span class="tdate">[Month, Year]</span> [Add your next milestone here.]</li>
          <li><span class="tdate">[Month, Year]</span> [Add another update here.]</li>
          <li><span class="tdate">[Month, Year]</span> [Add another update here.]</li>
        </ul>
      </div>
    </section>"""
assemble("index", "Md. Osama — Home | Bangla NLP &amp; Machine Unlearning",
         "Md. Osama — M.Sc.(Ongoing) in CSE, RUET, researching machine unlearning for morphologically rich Bangla text.",
         home_body)


# =========================================================
# RESEARCH
# =========================================================
research_body = """    <section class="section">
      <h3 class="section-title">Research — M.Sc. Thesis</h3>

      <div class="research-card">
        <p class="research-tag">Working title</p>
        <h4>Machine Unlearning in Morphologically Rich Bangla Text: A Benchmark Study</h4>

        <p>
          Most machine unlearning research benchmarks are built for English. This thesis
          constructs a benchmark for Bangla and studies how unlearning methods behave when
          the language itself encodes meaning through dense inflection and compounding —
          asking whether "forgetting" a root concept in Bangla also forgets its many
          morphological variants, or leaves them dangerously intact.
        </p>

        <div class="research-grid">
          <div>
            <p class="research-tag">Target models</p>
            <p>BanglaT5, BanglaNLG</p>
          </div>
          <div>
            <p class="research-tag">Unlearning methods</p>
            <p>Gradient ascent · NPO / APO-style preference optimization · embedding-corrupted prompts</p>
          </div>
          <div>
            <p class="research-tag">Target venue</p>
            <p>ACM TALLIP</p>
          </div>
          <div>
            <p class="research-tag">Timeline</p>
            <p>~24–34 weeks, phased</p>
          </div>
        </div>

        <p class="research-tag" style="margin-top: 1.5rem;">Research questions</p>
        <ul class="rq-list">
          <li>Do unlearning methods forget a concept's morphological variants along with its base form, in a morphologically rich language?</li>
          <li>How does Bangla's morphological complexity affect the accuracy–forgetting tradeoff compared to English benchmarks?</li>
          <li>Can a benchmark be built that fairly measures unlearning quality across inflected and compound Bangla forms?</li>
        </ul>
        <p class="edit-note">[Replace the RQs above with your actual finalized versions.]</p>
      </div>
    </section>"""
assemble("research", "Md. Osama — Research", "Research overview and M.Sc. thesis details for Md. Osama.", research_body)


# =========================================================
# PROJECTS
# =========================================================
projects_body = """    <section class="section">
      <h3 class="section-title">Projects</h3>

      <div class="project-grid">
        <article class="project-card">
          <h4>Bangla Book Recommendation System</h4>
          <p>Flask-based collaborative filtering recommender built on the Book-Crossing dataset.</p>
          <div class="tags"><span>Python</span><span>Flask</span><span>Collaborative Filtering</span></div>
          <a href="#" target="_blank" rel="noopener">View repo →</a>
        </article>

        <article class="project-card">
          <h4>Daily Muslim Life Manager</h4>
          <p>Full-stack app for daily prayer, habit, and routine tracking, built end-to-end.</p>
          <div class="tags"><span>Django</span><span>React</span></div>
          <a href="#" target="_blank" rel="noopener">View repo →</a>
        </article>

        <article class="project-card">
          <h4>Git &amp; GitHub Lab Manual</h4>
          <p>A university-standard lab manual walking students through Git and GitHub fundamentals.</p>
          <div class="tags"><span>Documentation</span><span>Git</span></div>
          <a href="#" target="_blank" rel="noopener">View doc →</a>
        </article>
      </div>
      <p class="edit-note">[Swap in real repo links, and add/remove project cards as needed.]</p>
    </section>"""
assemble("projects", "Md. Osama — Projects", "Selected projects by Md. Osama.", projects_body)


# =========================================================
# PUBLICATIONS
# =========================================================
publications_body = """    <section class="section">
      <h3 class="section-title">Publications</h3>
      <p class="edit-note">
        No publications yet — this section is ready for when your thesis work turns into a
        paper. Suggested format for each entry:
      </p>
      <div class="pub-item">
        <p class="pub-title">[Paper title]</p>
        <p class="pub-meta">[Authors] · [Venue, Year] · <a href="#">[PDF]</a> · <a href="#">[Code]</a></p>
      </div>
    </section>"""
assemble("publications", "Md. Osama — Publications", "Publications by Md. Osama.", publications_body)


# =========================================================
# SKILLS
# =========================================================
skills_body = """    <section class="section">
      <h3 class="section-title">Skills</h3>
      <div class="skills-grid">
        <div>
          <p class="research-tag">Languages</p>
          <p>Python, JavaScript</p>
        </div>
        <div>
          <p class="research-tag">ML / NLP</p>
          <p>PyTorch, Transformers (Hugging Face), scikit-learn</p>
        </div>
        <div>
          <p class="research-tag">Web</p>
          <p>Flask, Django, React</p>
        </div>
        <div>
          <p class="research-tag">Tools</p>
          <p>Git, GitHub, LaTeX</p>
        </div>
      </div>
    </section>"""
assemble("skills", "Md. Osama — Skills", "Technical skills of Md. Osama.", skills_body)


# =========================================================
# MY THOUGHT (blog)
# =========================================================
thoughts_body = """    <section class="section">
      <h3 class="section-title">My Thought</h3>
      <p class="edit-note">A running collection of lines and observations from life. Add a new entry any time — newest at the top.</p>

      <div class="thought-list">
        <article class="thought-item">
          <p class="tdate">[Month, Year]</p>
          <p class="thought-text">[Write a line or short reflection you want to remember.]</p>
        </article>
        <article class="thought-item">
          <p class="tdate">[Month, Year]</p>
          <p class="thought-text">[Another observation goes here.]</p>
        </article>
        <article class="thought-item">
          <p class="tdate">[Month, Year]</p>
          <p class="thought-text">[Keep adding — copy this block for each new entry.]</p>
        </article>
      </div>
    </section>"""
assemble("thoughts", "Md. Osama — My Thought", "Personal reflections and observations by Md. Osama.", thoughts_body)


# =========================================================
# CONTACT
# =========================================================
contact_body = """    <section class="section">
      <h3 class="section-title">Contact</h3>
      <p>Best way to reach me is by email — happy to talk Bangla NLP, unlearning, or Islamic history.</p>

      <div class="contact-details">
        <p><span>Personal email</span><a href="mailto:osamasohag39@gmail.com">osamasohag39@gmail.com</a></p>
        <p><span>Official email</span><a href="mailto:your.official@university.edu">your.official@university.edu</a></p>
        <p><span>Address</span>Nilphamari, Rangpur Division, Bangladesh</p>
      </div>
    </section>"""
assemble("contact", "Md. Osama — Contact", "Contact details for Md. Osama.", contact_body)

print("Done — 7 independent pages generated.")
