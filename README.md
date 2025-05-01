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
  "name": "Jane Doe",
  "title": "Software Developer",
  "email": "jane.doe@example.com",
  "phone": "+1234567890",
  "address": "New York, USA",
  "linkedin": "https://linkedin.com/in/janedoe",
  "github": "https://github.com/janedoe",
  "professional_summary": "Passionate developer with experience in Python, AI, and scalable backend systems.",
  "skills": ["Python", "Django", "Machine Learning", "Docker", "PostgreSQL"],
  "work_experience": [
    {
      "company": "TechCorp",
      "position": "Backend Developer",
      "date": "2022 - Present",
      "location": "Remote",
      "bullets": [
        "Developed REST APIs for fintech applications.",
        "Integrated CI/CD pipelines and improved deployment efficiency."
      ]
    }
  ],
  "education": {
    "institution": "XYZ University",
    "degree": "B.Sc. in Computer Science",
    "duration": "2018 - 2022",
    "location": "City, Country",
    "gpa": "8.9 / 10"
  },
  "projects": [
    {
      "name": "Resume PDF Generator",
      "link": "https://github.com/janedoe/resume-gen",
      "bullets": [
        "Automatically creates styled PDF resumes from structured JSON.",
        "Used ReportLab for PDF layout and formatting."
      ]
    }
  ],
  "achievements": [
    "1st Place - XYZ Hackathon 2021",
    "Dean’s List - 2020, 2021"
  ],
  "certifications": [
    {
      "name": "Full Stack Web Development",
      "link": "https://coursera.org/certificate/abc123"
    }
  ],
  "languages": [
    {
      "name": "English",
      "proficiency": "Fluent"
    },
    {
      "name": "Spanish",
      "proficiency": "Intermediate"
    }
  ]
}
