from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "cv.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Aazim Athar"
PAGE_ICON = ":wave:"
NAME = "Aazim Athar"
DESCRIPTION = """
Cloud Engineer, Responsible for the configuration and maintenance of a cloud infrastructure.
"""
EMAIL = "aazim6102@gmail.com"
SOCIAL_MEDIA = {
    "Linkedin": "https://www.linkedin.com/in/aazim-athar/",
    "Github": "https://github.com/aazim-github",
    "Credly": "https://www.credly.com/users/aazim-athar",
}
PROJECTS = {
    "🏆 Digital CV -- Digital Resume using Python & Streamlit": "https://github.com/aazim-github/aazim-digital-resume",
    "🏆 Digital Portfolio -- Digital Portfolio using JavaScript": "https://github.com/aazim-github/aazim-portfolio",
    "🏆 go-serverless-aws -- Serverless stack using Golang, API Gateway, Lambda & DynamoDB": "https://github.com/aazim-github/go-serverless-aws",
    "🏆 go-email-checker-tool -- Email Checker tool using Golang": "https://github.com/aazim-github/email-checker-tool",
    "🏆 go-movies-crud -- Movies project with CRUD operations using Golang": "https://github.com/aazim-github/go-movies-crud",
    "🏆 go-slack-age-bot -- Age Bot integrated with Slack using Golang": "https://github.com/aazim-github/slack-age-bot",
    "🏆 go-slack-file-bot -- File Upload Bot integrated with Slack using Golang": "https://github.com/aazim-github/slack-file-bot",
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)



# --- LOAD CSS, PDF & PROFILE PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width= 230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label="📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qualifications")
st.write(
    """
- ✔️ Experience on Azure Kubernetes, Containers, Container Registries, Container Orchestration, Nodes, Pods, Workloads, Storage and Persistence.
- ✔️ Manage full application stacks with Azure cloud-based computing environments.
- ✔️ Analyze metrics to identify bottlenecks and improve performance.
- ✔️ Improved monitoring process and regular maintenance checks which in turn reduced server downtime.
- ✔️ Exposure to Azure Cloud, Kubernetes, Docker, Containerization, Virtualization, Lens IDE, Azure CLI, kubectl, CI/CD.
- ✔️ Supported production environment including Monitoring application, resolving any production-related, and functional issues.
- ✔️ Oversee the continuous integration of our server technologies.
- ✔️ Work closely with business executives to develop cloud solutions that would lead to better client satisfaction.
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks.
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: GO, Python, Java
- 📊 Cloud Service Providers: Azure, AWS, OpenStack
- 📊 Containerization Platform: AKS(Azure Kubernetes Service), Docker
- 📊 Development and Operations Skills: (CI/CD), Azure, Docker and Jenkins
- 🗄️ Database Skills: Microsoft SQL Server (SSMS), MongoDB
- 📚 Version Control: Team Foundation Server (TFS) / Git, GitHub
- 📚  IDE's and Source: Azure DevOps (Project Management), Lens(Kubernetes IDE), Visual Studio, Visual Studio Code
"""
)



# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Engineer | Aptean**")
st.write("10/2020 - Present")
st.write(
    """
- ► Knowledge on Azure Cloud: 
- ► Implement and manage storage in Azure.
- ► Deploy and manage Azure compute resources.
- ► Backup and Monitor Azure resources.
- ► Implement infrastructure as a service solutions. 
- ► Instrument solutions to support monitoring and logging.
- ► Involved in setting up test environments from scratch on AKS having same configuration as production environments.
- ► Experience in updating components parameters in K8s YAML configuration file for a Kubernetes namespaces.
- ► Exposure on setting up build pipeline configured to run scheduled performance test using PowerShell & Python scripts.     
- ► Knowledge on applying TLS certificates in the test & production environment.
- ► Developed a bash script which can be executed to take thread & heap dumps for every specified set of interval of time.
"""
)


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")



# --- CERTIFICATIONS ---
st.write('\n')
st.subheader("Certifications")
st.write(
    """
- ► Microsoft Certified Azure Developer Associate : Developing Solutions for Microsoft Azure (AZ-204) 
- ► Microsoft Certified Azure Administrator Associate (AZ-104)
- ► Microsoft Certified Azure Cloud Fundamentals (AZ-900) 
"""
)











