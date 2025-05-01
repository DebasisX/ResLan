# ResLan
A high - level JSON language to create ATS - friendly Resume with perfect control. Currently supports PDF.


Docs:

The input JSON file must follow a specific structure to correctly populate the resume. Below is a breakdown of all supported fields, along with examples.

# Required Field

"name": "Your Full Name"

(Optional) Top Section

"title": "Your Title or Role (e.g., Software Engineer)",
"email": "your.email@example.com",
"phone": "+1234567890",
"address": "City, Country",
"linkedin": "https://www.linkedin.com/in/yourprofile",
"github": "https://github.com/yourhandle"

Note: Any key whose value starts with http will automatically be interpreted as a social link and hyperlinked.

Professional Summary

"professional_summary": "A short paragraph describing your experience, goals, or specialization."

Skills

"skills": [
  "Python",
  "Machine Learning",
  "Docker",
  "SQL"
]

Work Experience

"work_experience": [
  {
    "company": "Company Name",
    "position": "Job Title",
    "date": "Jan 2023 - Present",
    "location": "City, Country",
    "bullets": [
      "Led development of a data pipeline for real-time analytics.",
      "Reduced API response time by 40% through optimization."
    ]
  }
]

Notes:

- Each entry must include company and position.

- bullets is optional but recommended.

Education

"education": {
  "institution": "University Name",
  "degree": "B.Tech in Computer Science",
  "duration": "2021 - 2025",
  "location": "City, Country",
  "gpa": "9.1 / 10"
}

Projects

"projects": [
  {
    "name": "AI Resume Screener",
    "link": "https://github.com/yourhandle/ai-resume-screener",
    "bullets": [
      "Built a PDF parser and a scoring system to rank resumes.",
      "Integrated Flask and deployed on Heroku."
    ]
  }
]

Note: name is required; link and bullets are optional.

Achievements

"achievements": [
  "Won 1st place at ABC Hackathon (2024)",
  "Published research paper in IEEE Xplore"
]

Certifications

"certifications": [
  {
    "name": "AWS Certified Solutions Architect",
    "link": "https://example.com/certificate/aws"
  },
  "Google Data Analytics Specialization"
]

Note: You can use either string-only entries or object entries with name and link.

Languages

"languages": [
  {
    "name": "English",
    "proficiency": "Fluent"
  },
  {
    "name": "Hindi",
    "proficiency": "Native"
  }
]


# Example JSON Template
{
  "name": "Debasis Sikdar",
  "title": "Software Engineer (AI/ML)",
  "address": "Airport Gate No. 1, Kolkata, WB – 700028",
  "phone": "+91 7477 333 298",
  "email": "debasis.sikder123@gmail.com",
 "github": "https://github.com/DebasisX",
 "leetcode": "https://leetcode.com/u/IncinerateX/", 
 "linkedin": "https://www.linkedin.com/in/debasis-sikdar-4a197b25a/",
  "professional_summary": "Passionate and results-driven Software Engineer with a strong foundation in AI/ML, full-stack development, and system-level programming. Proven leadership experience in community and project management, with a history of mentoring, contributing to open source, and delivering high-impact solutions. Strong problem-solving skills backed by academic excellence and hands-on projects.",
  "skills": [
    "Python",
    "C/C++",
    "Java",
    "React.js",
    "HTML",
    "CSS",
    "Bootstrap",
    "Flask",
    "Django",
    "MongoDB",
    "MySQL",
    "SQLite",
    "TensorFlow",
    "Scikit-learn",
    "Pandas",
    "NumPy",
    "Matplotlib",
    "Git",
    "VSCode",
    "Jupyter",
    "Linux",
    "Google Cloud",
    "Docker",
    "Selenium"
  ],
  "work_experience": [
    {
      "company": "UiPath Community",
      "position": "Development Team Lead",
      "location": "On-Site",
      "date": "Jan 2025 – Present",
      "bullets": [
        "Lead development teams for hackathons and innovation challenges.",
        "Spearheaded impactful tech projects by translating problem statements into functional applications."
      ]
    },
    {
      "company": "GirlScript Foundation",
      "position": "Open Source Contributor",
      "location": "Remote",
      "date": "May 2024 – Jul 2024",
      "bullets": [
        "Successfully delivered a Level 3 PR during GSSoC.",
        "Dockerized core application, optimizing the deployment process."
      ]
    },
    {
      "company": "Code Social",
      "position": "Community Manager",
      "location": "Remote",
      "date": "Apr 2023 – Oct 2023",
      "bullets": [
        "Mentored 5,000+ members, driving a 15% boost in community engagement.",
        "Orchestrated 5+ technical events and competitions to foster learning."
      ]
    }
  ], "education": {
       "institution": "KIIT University, Odisha",
       "degree": "B.Tech in Computer Science and Engineering",
       "duration": "2022-2026",
       "location": "Bhubaneswar, Odisha",
       "gpa": "7.97"
     },
  "projects": [
    {
      "name": "KIRA KIIT – KIIT Intelligent Response Assistant",
      "bullets": [
        "RAG-based AI chatbot for KIIT students.",
        "24/7 assistant for academic/admin queries with secure OTP, CSRF, and rate limiting.",
        "Tech: Flask, MongoDB, FAISS, Ollama, Mistral-7B, LangChain, Docker"
      ]
    },
    {
      "name": "ML Model for Hyperspace Classification",
      "bullets": [
        "Designed an adaptive classification model outperforming k-NN by 10% in runtime.",
        "Used multi-feature selection for robust performance."
      ]
    },
    {
      "name": "Finance – Real-Time Trading Platform (CS50 Final Project)",
      "bullets": [
        "Simulates stock trading with real-time updates, secure login, portfolio tracking.",
        "Tech: Flask, SQLite, Yahoo Finance API"
      ]
    },
    {
      "name": "DecisionHub – Rule-Based Decision Engine",
      "bullets": [
        "Parses user-defined logical rules and computes dynamic values accordingly.",
        "Tech: Flask, SQLite, Jinja, HTML/CSS"
      ]
    },
    {
      "name": "Note-Ninja – Smart Meeting Summarizer",
      "bullets": [
        "Extracts and summarizes meeting content using Gemini AI and audio transcriptions.","Tech: Flask, Google Gemini, SpeechRecognition"
      ]
    },
    {
      "name": "ResLan – JSON-to-Resume Generator",
      "bullets": [
        "High-level JSON-based resume language to produce ATS-compliant PDFs.",
        "Libraries: ReportLab, argparse, textwrap"
      ]
    },
    {
      "name": "Low-Level Systems Projects (C)",
      "bullets": [
        "USB Driver for Linux Kernel (SanDisk) with multi-threaded I/O for speed optimization.",
        "Image Filters on .bmp (grayscale, edge detection, blur).",
        "Custom C Library for Linked Lists & Graphs."
      ]
    }
  ],
  "achievements": [
    "Hack-A-Bot (USC.KIIT) – 3rd Place",
    "CodeKaze (Coding Ninjas) – AIR 650",
    "KIITEE – Rank 1644",
    "CS50X & CS50 AI Graduate – Harvard University"
  ],
  "certifications": [],
  "languages": [
    {
      "name": "English",
      "proficiency": ""
    },
    {
      "name": "Hindi",
      "proficiency": ""
    },
    {
      "name": "Bengali",
      "proficiency": ""
    }
  ]
}
