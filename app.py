from flask import Flask, render_template_string

app = Flask(__name__)

# Portfolio & Resume Data
PROFILE_DATA = {
    "name": "Mohammed Nishan",
    "brand_text": "NISHAN",
    "location_upper": "AL KHOBAR, SAUDI ARABIA",
    "origin": "Mangalore, Karnataka, India",
    "eyebrow": "THE SPECIALIST",
    "headline_top": "SECURITY MEETS",
    "headline_bottom": "INFRASTRUCTURE.",
    # Hero portrait inside static/profile.png
    "photo_url": "/static/profile.png",
    # Dedicated passport photo inside static/pass.jpg
    "passport_photo_url": "/static/pass.jpg",
    "contact": {
        "email": "nishannish96@gmail.com",
        "phone_sa": "+966 54 989 6686",
        "whatsapp_sa": "966549896686",
        "phone_in": "+91 85488 45597",
        "whatsapp_in": "918548845597",
        "linkedin": "https://www.linkedin.com/in/your-profile"
    },
    "bio_p1": (
        "I design, install, and commission enterprise IP CCTV architectures, biometric access control, "
        "speed gates, and structured TCP/IP network infrastructure, backed by certified Health, Safety & "
        "Environment (HSE) leadership."
    ),
    "bio_p2": (
        "Originally from Mangalore, Karnataka, I'm based in Al Khobar, Saudi Arabia, where my work "
        "spans large-scale surveillance deployments, VMS/SIMS operations, and industrial site safety."
    ),
    "it_summary": (
        "Results-driven Network and Surveillance Technician with 4+ years of hands-on experience designing, "
        "installing, and commissioning enterprise IP CCTV systems, VMS/SIMS platforms, biometric access control, "
        "speed gates, and structured TCP/IP network infrastructure across commercial and retail environments."
    ),
    "hse_summary": (
        "NEBOSH-certified Health, Safety & Environment (HSE) Officer and Engineer with 3+ years of field "
        "experience in hazard identification, risk assessments, scaffolding and fall protection compliance, "
        "incident investigation, and toolbox talks across large-scale construction projects."
    ),
    "experience": [
        {
            "role": "Network and Surveillance Technician",
            "company": "Vision Angle Security Est",
            "location": "Al Khobar, Saudi Arabia",
            "period": "April 2023 – Present",
            "track": "it",
            "highlights": [
                "Design, install, and commission IP camera networks, PTZ systems, NVRs/DVRs, and speed gates.",
                "Configure managed switches (Cisco, Hikvision, TP-Link), VLANs, firewall rules, and Cat6/Fiber infrastructure.",
                "Manage Video Management Software (VMS), video analytics, motion detection, and Security Information Management Systems (SIMS)."
            ]
        },
        {
            "role": "Safety Officer",
            "company": "Infiniti Building Solution Pvt Ltd",
            "location": "India",
            "period": "September 2021 – March 2022",
            "track": "hse",
            "highlights": [
                "Conducted site hazard identifications, risk assessments, and daily toolbox talks.",
                "Supervised safe handling, storage, and disposal of hazardous materials and maintained statutory HSE compliance records."
            ]
        },
        {
            "role": "Safety Engineer",
            "company": "Westline Builders Pvt Ltd",
            "location": "India",
            "period": "September 2019 – February 2021",
            "track": "hse",
            "highlights": [
                "Monitored high-rise construction safety, scaffolding integrity, and fall protection compliance.",
                "Led incident investigations, prepared risk assessments, and enforced site-wide safety protocols across engineering teams."
            ]
        }
    ],
    "education": [
        {
            "degree": "Diploma in Fire and Safety",
            "institution": "Fire & Safety Engineering Institute",
            "details": "Specialized in industrial safety, fire prevention, and hazard management."
        },
        {
            "degree": "Pre-University Commerce (CEBA)",
            "institution": "St. Aloysius PU College, Mangalore",
            "details": "Computer Science, Economics, Business Studies, and Accountancy."
        }
    ],
    "certifications": [
        "NEBOSH International General Certificate (IG1)",
        "Risk Assessment & Hazard Identification",
        "Internal Auditor Training",
        "Fall Protection & Scaffold Safety",
        "Confined Space Safety",
        "Offshore Oil and Gas Introduction",
        "Behavior-Based Safety (BBS)",
        "Food and Hygiene Safety",
        "Accident Investigation & Environmental Awareness"
    ],
    "skills": {
        "Surveillance & Security": ["IP CCTV", "Analog-to-IP Migration", "VMS / SIMS", "Access Control & Speed Gates", "PTZ & Video Analytics"],
        "Networking & IT": ["TCP/IP & VLANs", "Cisco / Hikvision / TP-Link", "Firewall Configuration", "Cat6 / Fiber Termination", "PoE"],
        "HSE Management": ["Risk Assessment", "NEBOSH IG1 Standards", "Safety Auditing", "Scaffold & Fall Protection", "Toolbox Talks", "Incident Investigation"]
    }
}

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ data.name }} | Portfolio</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Archivo+Black&family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg-primary: #06080b;
            --bg-surface: #0c1016;
            --border-subtle: #1e2530;
            --text-primary: #f1f5f9;
            --text-secondary: #9ca3af;
            --accent-blue: #38bdf8;
            --accent-blue-hover: #7dd3fc;
            --gold-accent: #d4af37;
            --logo-color: #f6e3a1;
        }
        body.light-theme {
            --bg-primary: #f4f6f9;
            --bg-surface: #ffffff;
            --border-subtle: #cbd5e1;
            --text-primary: #0f172a;
            --text-secondary: #475569;
            --accent-blue: #0284c7;
            --accent-blue-hover: #0369a1;
            --logo-color: #9a6b09;
        }
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }
        html {
            scroll-behavior: smooth;
        }
        body {
            background-color: var(--bg-primary);
            color: var(--text-primary);
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            line-height: 1.65;
            transition: background-color 0.25s ease, color 0.25s ease;
            -webkit-font-smoothing: antialiased;
        }

        /* Full-width Top Navbar */
        header.site-header {
            border-bottom: 1px solid var(--border-subtle);
            position: sticky;
            top: 0;
            z-index: 50;
            background-color: rgba(6, 8, 11, 0.92);
            backdrop-filter: blur(10px);
            transition: background-color 0.25s ease, border-color 0.25s ease;
        }
        body.light-theme header.site-header {
            background-color: rgba(244, 246, 249, 0.92);
        }
        .nav-inner {
            max-width: 1240px;
            margin: 0 auto;
            padding: 1rem 2rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .brand-lockup {
            display: inline-flex;
            align-items: center;
            gap: 0.7rem;
            text-decoration: none;
        }
        .brand-monogram {
            height: 36px;
            width: auto;
            color: var(--logo-color);
            transition: color 0.25s ease;
        }
        .brand-wordmark {
            font-family: 'Archivo Black', 'Inter', sans-serif;
            font-size: 1rem;
            letter-spacing: 0.14em;
            color: var(--text-primary);
            text-transform: uppercase;
        }
        .brand-wordmark span {
            color: var(--accent-blue);
        }
        .nav-right {
            display: flex;
            align-items: center;
            gap: 2rem;
        }
        .nav-links {
            display: flex;
            align-items: center;
            gap: 1.75rem;
        }
        .nav-links a {
            color: var(--text-secondary);
            text-decoration: none;
            font-size: 0.875rem;
            font-weight: 500;
            transition: color 0.2s;
        }
        .nav-links a:hover,
        .nav-links a.active {
            color: var(--accent-blue);
        }
        .btn-contact-nav {
            display: inline-flex;
            align-items: center;
            gap: 0.4rem;
            padding: 0.55rem 1.1rem;
            border: 1px solid var(--border-subtle);
            border-radius: 6px;
            color: var(--text-primary);
            text-decoration: none;
            font-size: 0.85rem;
            font-weight: 500;
            transition: border-color 0.2s, color 0.2s;
        }
        .btn-contact-nav:hover {
            border-color: var(--accent-blue);
            color: var(--accent-blue);
        }
        .theme-toggle {
            width: 38px;
            height: 38px;
            border-radius: 50%;
            border: 1px solid var(--border-subtle);
            background: transparent;
            color: var(--text-secondary);
            display: inline-flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            transition: border-color 0.2s, color 0.2s;
        }
        .theme-toggle:hover {
            border-color: var(--accent-blue);
            color: var(--accent-blue);
        }

        /* Main Container */
        .wrapper {
            max-width: 1240px;
            margin: 0 auto;
            padding: 0 2rem;
        }

        /* Split Hero Section */
        .hero-split {
            display: grid;
            grid-template-columns: 0.82fr 1.18fr;
            gap: 4rem;
            align-items: start;
            padding-top: 2rem;
            padding-bottom: 4.5rem;
            border-bottom: 1px solid var(--border-subtle);
        }
        .hero-left-col {
            display: flex;
            flex-direction: column;
            background: transparent;
        }
        .profile-photo-img {
            width: 100%;
            max-width: 400px;
            margin: 0 auto;
            height: auto;
            max-height: 550px;
            object-fit: cover;
            object-position: top center;
            display: block;
            background: transparent;
            border: none;
            box-shadow: none;
            border-radius: 0;
        }
        .identity-block {
            border-top: 1px solid var(--border-subtle);
            padding-top: 1.35rem;
        }
        .identity-block h2 {
            font-family: 'Inter', sans-serif;
            font-size: clamp(1.85rem, 3vw, 2.35rem);
            font-weight: 700;
            color: var(--text-primary);
            letter-spacing: -0.02em;
            line-height: 1.15;
            margin-bottom: 0.45rem;
        }
        .identity-block .location-upper {
            font-size: 0.72rem;
            font-weight: 700;
            letter-spacing: 0.22em;
            text-transform: uppercase;
            color: var(--text-secondary);
        }

        /* Right Column */
        .hero-right-col {
            padding-top: 0.5rem;
        }
        .eyebrow {
            display: flex;
            align-items: center;
            gap: 0.75rem;
            color: var(--accent-blue);
            font-size: 0.75rem;
            font-weight: 700;
            letter-spacing: 0.18em;
            text-transform: uppercase;
            margin-bottom: 1.1rem;
        }
        .eyebrow::before {
            content: "";
            display: inline-block;
            width: 24px;
            height: 2px;
            background-color: var(--accent-blue);
        }
        .hero-headline {
            font-family: 'Archivo Black', 'Inter', sans-serif;
            font-size: clamp(2.4rem, 4.6vw, 4rem);
            line-height: 1.03;
            letter-spacing: -0.02em;
            text-transform: uppercase;
            margin-bottom: 1.75rem;
        }
        .hero-headline .line-white {
            display: block;
            color: var(--text-primary);
        }
        .hero-headline .line-blue {
            display: block;
            color: var(--accent-blue);
        }
        .hero-bio {
            color: var(--text-secondary);
            font-size: 0.98rem;
            max-width: 580px;
            margin-bottom: 1.1rem;
        }
        .hero-actions {
            display: flex;
            flex-wrap: wrap;
            gap: 0.85rem;
            margin-top: 1.85rem;
            margin-bottom: 2rem;
        }
        .btn-primary {
            display: inline-flex;
            align-items: center;
            gap: 0.45rem;
            background-color: var(--accent-blue);
            color: #041019;
            font-weight: 600;
            font-size: 0.88rem;
            padding: 0.78rem 1.3rem;
            border-radius: 6px;
            text-decoration: none;
            transition: background-color 0.2s, transform 0.15s;
        }
        .btn-primary:hover {
            background-color: var(--accent-blue-hover);
            transform: translateY(-1px);
        }
        .btn-outline {
            display: inline-flex;
            align-items: center;
            gap: 0.45rem;
            background-color: transparent;
            color: var(--text-primary);
            font-weight: 500;
            font-size: 0.88rem;
            padding: 0.78rem 1.3rem;
            border-radius: 6px;
            border: 1px solid var(--border-subtle);
            text-decoration: none;
            transition: border-color 0.2s, color 0.2s;
        }
        .btn-outline:hover {
            border-color: var(--accent-blue);
            color: var(--accent-blue);
        }

        /* Education & Certifications Accordion */
        details.edu-accordion {
            border-top: 1px solid var(--border-subtle);
            padding-top: 1.1rem;
            margin-bottom: 1.5rem;
            max-width: 620px;
        }
        details.edu-accordion summary {
            list-style: none;
            cursor: pointer;
            font-size: 0.92rem;
            font-weight: 600;
            color: var(--text-primary);
            display: flex;
            align-items: center;
            gap: 0.6rem;
            user-select: none;
        }
        details.edu-accordion summary::-webkit-details-marker {
            display: none;
        }
        details.edu-accordion summary .arrow {
            font-size: 0.68rem;
            transition: transform 0.2s ease;
        }
        details.edu-accordion[open] summary .arrow {
            transform: rotate(90deg);
            color: var(--accent-blue);
        }
        .accordion-body {
            padding-top: 1.1rem;
            display: grid;
            gap: 0.9rem;
        }
        .edu-item {
            background: var(--bg-surface);
            border: 1px solid var(--border-subtle);
            border-radius: 8px;
            padding: 1rem 1.15rem;
        }
        .edu-item h4 {
            font-size: 0.95rem;
            color: var(--text-primary);
            margin-bottom: 0.2rem;
        }
        .edu-item .inst {
            font-size: 0.85rem;
            color: var(--accent-blue);
            margin-bottom: 0.3rem;
        }
        .edu-item p {
            font-size: 0.85rem;
            color: var(--text-secondary);
        }
        .cert-pills {
            display: flex;
            flex-wrap: wrap;
            gap: 0.45rem;
            margin-top: 0.45rem;
        }
        .cert-pill {
            font-size: 0.78rem;
            color: var(--text-primary);
            background: rgba(56, 189, 248, 0.08);
            border: 1px solid rgba(56, 189, 248, 0.25);
            padding: 0.25rem 0.65rem;
            border-radius: 4px;
        }

        /* "Watch portfolio reel" Banner Card */
        details.reel-card {
            max-width: 620px;
            border: 1px solid #1e293b;
            border-radius: 10px;
            overflow: hidden;
            background:
                linear-gradient(90deg, rgba(8, 13, 22, 0.94) 0%, rgba(12, 24, 42, 0.82) 55%, rgba(14, 34, 62, 0.72) 100%),
                repeating-linear-gradient(90deg, rgba(56, 189, 248, 0.06) 0px, rgba(56, 189, 248, 0.06) 1px, transparent 1px, transparent 18px);
        }
        details.reel-card summary {
            list-style: none;
            cursor: pointer;
            padding: 1.15rem 1.35rem;
            display: flex;
            align-items: center;
            justify-content: space-between;
            user-select: none;
        }
        details.reel-card summary::-webkit-details-marker {
            display: none;
        }
        .reel-left {
            display: flex;
            align-items: center;
            gap: 1rem;
        }
        .play-circle {
            width: 42px;
            height: 42px;
            border-radius: 50%;
            border: 1.5px solid var(--accent-blue);
            background: rgba(56, 189, 248, 0.12);
            color: var(--accent-blue);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 0.85rem;
            flex-shrink: 0;
        }
        .reel-title {
            font-size: 1.15rem;
            font-weight: 700;
            color: #ffffff;
        }
        .reel-chevron {
            color: #94a3b8;
            font-size: 0.9rem;
            transition: transform 0.2s ease;
        }
        details.reel-card[open] .reel-chevron {
            transform: rotate(180deg);
            color: var(--accent-blue);
        }
        .reel-body {
            padding: 0 1.35rem 1.35rem 1.35rem;
            border-top: 1px solid rgba(56, 189, 248, 0.15);
            padding-top: 1rem;
            color: #cbd5e1;
            font-size: 0.9rem;
            display: grid;
            gap: 0.65rem;
        }

        /* Below-the-fold Sections */
        .section-block {
            padding: 4.5rem 0;
            border-bottom: 1px solid var(--border-subtle);
        }
        .section-header {
            margin-bottom: 2.5rem;
        }
        .section-title {
            font-family: 'Archivo Black', 'Inter', sans-serif;
            font-size: 1.85rem;
            text-transform: uppercase;
            letter-spacing: -0.01em;
            color: var(--text-primary);
        }
        .exp-list {
            display: grid;
            gap: 1.5rem;
        }
        .exp-card {
            background: var(--bg-surface);
            border: 1px solid var(--border-subtle);
            border-radius: 10px;
            padding: 1.75rem;
            transition: border-color 0.2s;
        }
        .exp-card:hover {
            border-color: rgba(56, 189, 248, 0.45);
        }
        .exp-top {
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            flex-wrap: wrap;
            gap: 0.5rem;
            margin-bottom: 0.9rem;
        }
        .exp-role {
            font-size: 1.15rem;
            font-weight: 700;
            color: var(--text-primary);
        }
        .exp-company {
            color: var(--accent-blue);
            font-size: 0.92rem;
            font-weight: 500;
        }
        .exp-period {
            font-size: 0.82rem;
            color: var(--text-secondary);
            border: 1px solid var(--border-subtle);
            padding: 0.25rem 0.75rem;
            border-radius: 999px;
        }
        .exp-card ul {
            padding-left: 1.2rem;
            color: var(--text-secondary);
            font-size: 0.94rem;
        }
        .exp-card li {
            margin-bottom: 0.4rem;
        }
        .skills-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 1.5rem;
        }
        .skill-box {
            background: var(--bg-surface);
            border: 1px solid var(--border-subtle);
            border-radius: 10px;
            padding: 1.5rem;
        }
        .skill-box h3 {
            font-size: 1rem;
            color: var(--text-primary);
            margin-bottom: 1rem;
        }
        .skill-tags {
            display: flex;
            flex-wrap: wrap;
            gap: 0.5rem;
        }
        .skill-tag {
            font-size: 0.82rem;
            color: var(--text-primary);
            background: rgba(56, 189, 248, 0.06);
            border: 1px solid var(--border-subtle);
            padding: 0.35rem 0.75rem;
            border-radius: 6px;
        }

        /* Contact Grid */
        .contact-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 1.25rem;
        }
        .contact-card {
            background: var(--bg-surface);
            border: 1px solid var(--border-subtle);
            border-radius: 10px;
            padding: 1.4rem 1.5rem;
            text-decoration: none;
            display: flex;
            flex-direction: column;
            gap: 0.4rem;
            transition: border-color 0.2s, transform 0.15s;
        }
        .contact-card:hover {
            border-color: var(--accent-blue);
            transform: translateY(-2px);
        }
        .contact-label {
            font-size: 0.72rem;
            font-weight: 700;
            letter-spacing: 0.16em;
            text-transform: uppercase;
            color: var(--accent-blue);
        }
        .contact-value {
            font-size: 0.98rem;
            font-weight: 600;
            color: var(--text-primary);
            word-break: break-word;
            text-decoration: none;
        }
        .contact-sub {
            font-size: 0.8rem;
            color: var(--text-secondary);
        }
        .wa-link {
            margin-top: 0.25rem;
            font-size: 0.8rem;
            font-weight: 600;
            color: var(--accent-blue);
            text-decoration: none;
        }

        footer {
            padding: 2.5rem 0;
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 1rem;
            color: var(--text-secondary);
            font-size: 0.85rem;
        }

        @media (max-width: 920px) {
            .hero-split {
                grid-template-columns: 1fr;
                gap: 2.5rem;
            }
            .profile-photo-img {
                max-width: 300px;
                max-height: 420px;
            }
            .nav-links {
                display: none;
            }
        }
    </style>
</head>
<body>
    <!-- Full-Width Top Navigation -->
    <header class="site-header">
        <div class="nav-inner">
            <a href="#" class="brand-lockup" aria-label="{{ data.name }}">
                <svg class="brand-monogram" viewBox="0 0 110 150" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M26 15 V110" stroke="currentColor" stroke-width="5.5" stroke-linecap="butt"/>
                    <circle cx="26" cy="122" r="3.4" fill="currentColor"/>
                    <path d="M88 15 V135" stroke="currentColor" stroke-width="5.5" stroke-linecap="butt"/>
                    <path d="M26 16 L49 52" stroke="currentColor" stroke-width="5.5" stroke-linecap="butt"/>
                    <path d="M51 64 L88 134" stroke="currentColor" stroke-width="5.5" stroke-linecap="butt"/>
                    <path d="M88 53 H36 C21 53 16 68 26 78 C36 88 64 93 64 113 C64 131 46 139 32 135 C27 133.5 25 131 23 129"
                          stroke="currentColor" stroke-width="5.5" stroke-linecap="butt" fill="none"/>
                </svg>
                <span class="brand-wordmark">{{ data.brand_text }}<span>.</span></span>
            </a>

            <div class="nav-right">
                <div class="nav-links">
                    <a href="#specialist" class="active">Specialist</a>
                    <a href="#skills">Expertise</a>
                    <a href="#experience">Work</a>
                    <a href="#journey">Journey</a>
                </div>
                <a href="#contact" class="btn-contact-nav">Get in touch &#8599;</a>
                <button class="theme-toggle" id="themeToggle" aria-label="Toggle color theme" title="Toggle light/dark mode">&#9788;</button>
            </div>
        </div>
    </header>

    <div class="wrapper">
        <!-- Two-Column Hero Section -->
        <section id="specialist" class="hero-split">
            <!-- Left Column: Frameless Transparent Portrait + Horizontal Line + Name + Location -->
            <div class="hero-left-col">
                <img id="profilePhoto"
                     class="profile-photo-img"
                     src="{{ data.photo_url }}"
                     alt="{{ data.name }}"
                     onerror="this.style.display='none';">
                <div class="identity-block">
                    <h2>{{ data.name }}</h2>
                    <div class="location-upper">{{ data.location_upper }}</div>
                </div>
            </div>

            <!-- Right Column: Headline, Bio, Action Buttons, Education Accordion, Reel Card -->
            <div class="hero-right-col">
                <div class="eyebrow">{{ data.eyebrow }}</div>
                <h1 class="hero-headline">
                    <span class="line-white">{{ data.headline_top }}</span>
                    <span class="line-blue">{{ data.headline_bottom }}</span>
                </h1>

                <p class="hero-bio">{{ data.bio_p1 }}</p>
                <p class="hero-bio">{{ data.bio_p2 }}</p>

                <div class="hero-actions">
                    <a href="/resume/it" target="_blank" rel="noopener" class="btn-primary">IT &amp; Surveillance Resume &#8599;</a>
                    <a href="/resume/hse" target="_blank" rel="noopener" class="btn-outline">HSE Safety Resume &#8599;</a>
                </div>

                <!-- Education and certifications accordion -->
                <details class="edu-accordion">
                    <summary>
                        <span class="arrow">&#9654;</span>
                        Education and certifications
                    </summary>
                    <div class="accordion-body">
                        {% for edu in data.education %}
                        <div class="edu-item">
                            <h4>{{ edu.degree }}</h4>
                            <div class="inst">{{ edu.institution }}</div>
                            <p>{{ edu.details }}</p>
                        </div>
                        {% endfor %}

                        <div class="edu-item">
                            <h4>HSE &amp; Technical Certifications</h4>
                            <div class="cert-pills">
                                {% for cert in data.certifications %}
                                <span class="cert-pill">{{ cert }}</span>
                                {% endfor %}
                            </div>
                        </div>
                    </div>
                </details>

                <!-- Watch portfolio reel expandable card -->
                <details class="reel-card">
                    <summary>
                        <div class="reel-left">
                            <div class="play-circle">&#9654;</div>
                            <span class="reel-title">Watch portfolio reel</span>
                        </div>
                        <span class="reel-chevron">&#8964;</span>
                    </summary>
                    <div class="reel-body">
                        <p><strong>Field Deployments &amp; Operations Highlights:</strong></p>
                        <p>&bull; Enterprise IP CCTV, PTZ calibration, NVR/DVR commissioning, and VMS/SIMS integration across commercial sites in Saudi Arabia.</p>
                        <p>&bull; Speed gate &amp; biometric access control installations paired with structured Cat6 and PoE switch infrastructure.</p>
                        <p>&bull; Full-cycle HSE site auditing, risk assessments, and NEBOSH-compliant safety supervision across major construction projects.</p>
                    </div>
                </details>
            </div>
        </section>

        <!-- Expertise / Skills Section -->
        <section id="skills" class="section-block">
            <div class="section-header">
                <div class="eyebrow">EXPERTISE</div>
                <h2 class="section-title">Core Competencies</h2>
            </div>

            <div class="skills-grid">
                {% for category, items in data.skills.items() %}
                <div class="skill-box">
                    <h3>{{ category }}</h3>
                    <div class="skill-tags">
                        {% for skill in items %}
                        <span class="skill-tag">{{ skill }}</span>
                        {% endfor %}
                    </div>
                </div>
                {% endfor %}
            </div>
        </section>

        <!-- Work Experience / Journey Section -->
        <section id="experience" class="section-block">
            <div id="journey" class="section-header">
                <div class="eyebrow">WORK &amp; JOURNEY</div>
                <h2 class="section-title">Experience</h2>
            </div>

            <div class="exp-list">
                {% for job in data.experience %}
                <div class="exp-card" {% if 'Safety' in job.role %}id="hse-experience"{% endif %}>
                    <div class="exp-top">
                        <div>
                            <div class="exp-role">{{ job.role }}</div>
                            <div class="exp-company">{{ job.company }} &bull; {{ job.location }}</div>
                        </div>
                        <div class="exp-period">{{ job.period }}</div>
                    </div>
                    <ul>
                        {% for item in job.highlights %}
                        <li>{{ item }}</li>
                        {% endfor %}
                    </ul>
                </div>
                {% endfor %}
            </div>
        </section>

        <!-- Contact Details Section -->
        <section id="contact" class="section-block">
            <div class="section-header">
                <div class="eyebrow">GET IN TOUCH</div>
                <h2 class="section-title">Contact Details</h2>
            </div>

            <div class="contact-grid">
                <a href="mailto:{{ data.contact.email }}" class="contact-card">
                    <span class="contact-label">Email &#8599;</span>
                    <span class="contact-value">{{ data.contact.email }}</span>
                    <span class="contact-sub">Direct email &amp; inquiries</span>
                </a>

                <div class="contact-card">
                    <span class="contact-label">Saudi Arabia (Call &amp; WhatsApp)</span>
                    <a href="tel:+{{ data.contact.whatsapp_sa }}" class="contact-value">{{ data.contact.phone_sa }}</a>
                    <span class="contact-sub">Al Khobar, Saudi Arabia</span>
                    <a href="https://wa.me/{{ data.contact.whatsapp_sa }}" target="_blank" rel="noopener" class="wa-link">Chat on WhatsApp &#8599;</a>
                </div>

                <div class="contact-card">
                    <span class="contact-label">India (Call &amp; WhatsApp)</span>
                    <a href="tel:+{{ data.contact.whatsapp_in }}" class="contact-value">{{ data.contact.phone_in }}</a>
                    <span class="contact-sub">Mangalore, Karnataka</span>
                    <a href="https://wa.me/{{ data.contact.whatsapp_in }}" target="_blank" rel="noopener" class="wa-link">Chat on WhatsApp &#8599;</a>
                </div>
            </div>
        </section>

        <!-- Footer -->
        <footer>
            <span>&copy; {{ data.name }} &bull; Al Khobar, Saudi Arabia &amp; Mangalore, India</span>
            <a href="#specialist" class="btn-outline">Back to top &#8593;</a>
        </footer>
    </div>

    <script>
        const toggleBtn = document.getElementById('themeToggle');
        toggleBtn.addEventListener('click', () => {
            document.body.classList.toggle('light-theme');
        });

        function removeOuterWhiteBackground(imgEl) {
            if (!imgEl || !imgEl.naturalWidth || imgEl.dataset.cutoutDone) return;
            const w = imgEl.naturalWidth;
            const h = imgEl.naturalHeight;
            const canvas = document.createElement('canvas');
            canvas.width = w;
            canvas.height = h;
            const ctx = canvas.getContext('2d');
            ctx.drawImage(imgEl, 0, 0);

            const imgData = ctx.getImageData(0, 0, w, h);
            const data = imgData.data;
            const visited = new Uint8Array(w * h);
            const queue = new Int32Array(w * h);
            let head = 0, tail = 0;

            function isBackdropWhite(idx) {
                const p = idx * 4;
                const r = data[p], g = data[p + 1], b = data[p + 2];
                const minC = Math.min(r, g, b);
                const maxC = Math.max(r, g, b);
                return minC >= 246 && (maxC - minC) <= 6;
            }

            function enqueue(idx) {
                if (idx >= 0 && idx < w * h && !visited[idx] && isBackdropWhite(idx)) {
                    visited[idx] = 1;
                    queue[tail++] = idx;
                }
            }

            for (let x = 0; x < w; x++) {
                enqueue(x);
            }
            for (let y = 0; y < h; y++) {
                enqueue(y * w);
                enqueue(y * w + (w - 1));
            }

            const startY = Math.floor(h * 0.62);
            const endY = Math.floor(h * 0.85);
            const midX = Math.floor(w * 0.5);
            for (let y = startY; y < endY; y++) {
                for (let dx = -12; dx <= 12; dx++) {
                    enqueue(y * w + (midX + dx));
                }
            }

            while (head < tail) {
                const idx = queue[head++];
                const x = idx % w;
                const y = (idx - x) / w;
                data[idx * 4 + 3] = 0;

                if (x > 0) enqueue(idx - 1);
                if (x < w - 1) enqueue(idx + 1);
                if (y > 0) enqueue(idx - w);
                if (y < h - 1) enqueue(idx + w);
            }

            for (let y = 1; y < h - 1; y++) {
                for (let x = 1; x < w - 1; x++) {
                    const idx = y * w + x;
                    if (data[idx * 4 + 3] === 255) {
                        const n1 = data[(idx - 1) * 4 + 3] === 0;
                        const n2 = data[(idx + 1) * 4 + 3] === 0;
                        const n3 = data[(idx - w) * 4 + 3] === 0;
                        const n4 = data[(idx + w) * 4 + 3] === 0;
                        if ((n1 || n2 || n3 || n4) && isBackdropWhite(idx)) {
                            data[idx * 4 + 3] = 0;
                        }
                    }
                }
            }

            ctx.putImageData(imgData, 0, 0);
            imgEl.dataset.cutoutDone = "1";
            imgEl.src = canvas.toDataURL('image/png');
        }

        const profilePhoto = document.getElementById('profilePhoto');
        if (profilePhoto.complete) {
            removeOuterWhiteBackground(profilePhoto);
        } else {
            profilePhoto.addEventListener('load', () => removeOuterWhiteBackground(profilePhoto));
        }
    </script>
</body>
</html>
"""

RESUME_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ data.name }} — {{ role_title }} Resume</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <style>
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }
        body {
            background-color: #0f172a;
            color: #0f172a;
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            line-height: 1.55;
            padding: 2rem 1rem;
        }
        .toolbar {
            max-width: 820px;
            margin: 0 auto 1.25rem auto;
            display: flex;
            justify-content: space-between;
            align-items: center;
            gap: 1rem;
            flex-wrap: wrap;
        }
        .toolbar a,
        .toolbar button {
            font-family: inherit;
            font-size: 0.88rem;
            font-weight: 600;
            padding: 0.65rem 1.15rem;
            border-radius: 6px;
            text-decoration: none;
            cursor: pointer;
            border: 1px solid #334155;
        }
        .btn-back {
            background: #1e293b;
            color: #f8fafc;
        }
        .btn-switch {
            background: transparent;
            color: #38bdf8;
            border-color: #38bdf8;
        }
        .btn-print {
            background: #38bdf8;
            color: #041019;
            border-color: #38bdf8;
        }
        .sheet {
            max-width: 820px;
            margin: 0 auto;
            background: #ffffff;
            padding: 2.75rem 3rem;
            border-radius: 8px;
            box-shadow: 0 20px 45px rgba(0, 0, 0, 0.45);
        }
        .resume-header {
            border-bottom: 2px solid #0f172a;
            padding-bottom: 1.15rem;
            margin-bottom: 1.4rem;
            display: flex;
            justify-content: space-between;
            align-items: stretch;
            gap: 1.25rem;
        }
        .header-main {
            flex: 1;
            min-width: 240px;
            display: flex;
            flex-direction: column;
            justify-content: center;
        }
        .resume-header h1 {
            font-size: 1.85rem;
            font-weight: 800;
            letter-spacing: -0.02em;
            line-height: 1.15;
            color: #0f172a;
        }
        .resume-header .subtitle {
            font-size: 0.92rem;
            font-weight: 700;
            color: #0284c7;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            margin-top: 0.2rem;
            margin-bottom: 0.55rem;
        }
        .contact-lines {
            font-size: 0.84rem;
            color: #334155;
        }
        .contact-lines div {
            margin-bottom: 0.2rem;
        }
        .passport-photo {
            width: 96px;
            height: 100%;
            min-height: 104px;
            max-height: 122px;
            object-fit: cover;
            object-position: top center;
            border: none;
            border-radius: 0;
            background: transparent;
            flex-shrink: 0;
            align-self: stretch;
        }
        .section {
            margin-bottom: 1.5rem;
        }
        .section-heading {
            font-size: 0.82rem;
            font-weight: 800;
            letter-spacing: 0.14em;
            text-transform: uppercase;
            color: #0284c7;
            border-bottom: 1px solid #cbd5e1;
            padding-bottom: 0.35rem;
            margin-bottom: 0.85rem;
        }
        .summary-text {
            font-size: 0.92rem;
            color: #334155;
        }
        .job-item {
            margin-bottom: 1.1rem;
        }
        .job-row {
            display: flex;
            justify-content: space-between;
            align-items: baseline;
            flex-wrap: wrap;
            gap: 0.5rem;
        }
        .job-title {
            font-size: 1rem;
            font-weight: 700;
            color: #0f172a;
        }
        .job-date {
            font-size: 0.82rem;
            font-weight: 600;
            color: #475569;
        }
        .job-company {
            font-size: 0.88rem;
            font-weight: 600;
            color: #0284c7;
            margin-bottom: 0.35rem;
        }
        .job-item ul {
            padding-left: 1.2rem;
            font-size: 0.88rem;
            color: #334155;
        }
        .job-item li {
            margin-bottom: 0.28rem;
        }
        .skills-list {
            display: grid;
            gap: 0.5rem;
            font-size: 0.88rem;
            color: #334155;
        }
        .skills-list strong {
            color: #0f172a;
        }
        .two-col {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 1.5rem;
        }
        .edu-row {
            margin-bottom: 0.65rem;
            font-size: 0.88rem;
        }
        .edu-row strong {
            display: block;
            color: #0f172a;
        }
        .cert-list {
            padding-left: 1.15rem;
            font-size: 0.85rem;
            color: #334155;
        }
        .cert-list li {
            margin-bottom: 0.22rem;
        }

        @media print {
            body {
                background: #ffffff;
                padding: 0;
            }
            .toolbar {
                display: none;
            }
            .sheet {
                box-shadow: none;
                padding: 0.5in;
                max-width: 100%;
            }
            .passport-photo {
                -webkit-print-color-adjust: exact;
                print-color-adjust: exact;
            }
        }
        @media (max-width: 680px) {
            .sheet {
                padding: 1.75rem 1.35rem;
            }
            .resume-header {
                flex-direction: column-reverse;
                align-items: flex-start;
            }
            .passport-photo {
                height: 110px;
                width: 90px;
            }
            .two-col {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <div class="toolbar">
        <a href="/" class="btn-back">&#8592; Back to Portfolio</a>
        <div style="display:flex; gap:0.65rem; flex-wrap:wrap;">
            <a href="{{ switch_url }}" class="btn-switch">{{ switch_label }}</a>
            <button onclick="window.print()" class="btn-print">Download / Save as PDF</button>
        </div>
    </div>

    <div class="sheet">
        <div class="resume-header">
            <div class="header-main">
                <h1>{{ data.name }}</h1>
                <div class="subtitle">{{ role_title }}</div>
                <div class="contact-lines">
                    <div>Al Khobar, Saudi Arabia | Origin: {{ data.origin }}</div>
                    <div>{{ data.contact.email }}</div>
                    <div>KSA: {{ data.contact.phone_sa }} | IND: {{ data.contact.phone_in }}</div>
                </div>
            </div>
            <img src="{{ data.passport_photo_url }}"
                 alt="{{ data.name }} passport photo"
                 class="passport-photo"
                 onerror="this.style.display='none';">
        </div>

        <div class="section">
            <div class="section-heading">Professional Summary</div>
            <p class="summary-text">{{ summary }}</p>
        </div>

        <div class="section">
            <div class="section-heading">Work Experience</div>
            {% for job in ordered_experience %}
            <div class="job-item">
                <div class="job-row">
                    <span class="job-title">{{ job.role }}</span>
                    <span class="job-date">{{ job.period }}</span>
                </div>
                <div class="job-company">{{ job.company }} &bull; {{ job.location }}</div>
                <ul>
                    {% for item in job.highlights %}
                    <li>{{ item }}</li>
                    {% endfor %}
                </ul>
            </div>
            {% endfor %}
        </div>

        <div class="section">
            <div class="section-heading">Core Technical &amp; Safety Competencies</div>
            <div class="skills-list">
                {% for category, items in data.skills.items() %}
                <div><strong>{{ category }}:</strong> {{ items | join(', ') }}</div>
                {% endfor %}
            </div>
        </div>

        <div class="two-col">
            <div class="section">
                <div class="section-heading">Education</div>
                {% for edu in data.education %}
                <div class="edu-row">
                    <strong>{{ edu.degree }}</strong>
                    <span>{{ edu.institution }}</span>
                </div>
                {% endfor %}
            </div>

            <div class="section">
                <div class="section-heading">Certifications</div>
                <ul class="cert-list">
                    {% for cert in data.certifications %}
                    <li>{{ cert }}</li>
                    {% endfor %}
                </ul>
            </div>
        </div>
    </div>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML_TEMPLATE, data=PROFILE_DATA)

@app.route("/resume/it")
def resume_it():
    ordered = sorted(PROFILE_DATA["experience"], key=lambda j: 0 if j["track"] == "it" else 1)
    return render_template_string(
        RESUME_TEMPLATE,
        data=PROFILE_DATA,
        role_title="Network & Surveillance Technician",
        summary=PROFILE_DATA["it_summary"],
        ordered_experience=ordered,
        switch_url="/resume/hse",
        switch_label="Switch to HSE Resume"
    )

@app.route("/resume/hse")
def resume_hse():
    ordered = sorted(PROFILE_DATA["experience"], key=lambda j: 0 if j["track"] == "hse" else 1)
    return render_template_string(
        RESUME_TEMPLATE,
        data=PROFILE_DATA,
        role_title="HSE Safety Officer & Engineer",
        summary=PROFILE_DATA["hse_summary"],
        ordered_experience=ordered,
        switch_url="/resume/it",
        switch_label="Switch to IT & Surveillance Resume"
    )

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)