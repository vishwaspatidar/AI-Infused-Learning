# AI Infused Learning 🚀
### My Journey into AI Engineering — Session 01

Every AI application starts with a simple question: *What can I build with a model that understands and generates language?*

This repository captures the beginning of my hands-on journey into AI Engineering. Instead of stopping at understanding LLM concepts theoretically, I wanted to turn them into working applications, one step at a time.

What started as a simple terminal-based chatbot gradually evolved into experimenting with model behaviour and building an application that can summarize website content.

Three small projects. One learning journey. A first step towards building practical AI applications.

---

## 🧭 The Journey: From Conversation to Application

### 01. Chat Model — My First Conversation with an LLM 💬

**The starting point: making a machine respond to me.**

I began with the simplest possible interface: the terminal.

The goal was to connect a Python application to a large language model, send a prompt, receive a response, and understand the basic interaction behind an LLM-powered application.

Without a graphical interface or extra layers of abstraction, I could focus on the fundamentals: how prompts are sent, how responses are received, and how an application communicates with a model.

**What I explored**
- Connecting Python to an LLM API.
- Sending prompts and handling model responses.
- Understanding the basic request–response workflow.
- Working with environment variables to manage API credentials.

**The takeaway:** Before building an AI product, understand the conversation happening behind the interface.

---

### 02. LLM Arena — Exploring Model Behaviour ⚔️

**The next question: what happens when we experiment with model responses?**

Once I had a working terminal chatbot, I wanted to move beyond a single conversation. I built an LLM Arena with an interactive interface to explore how an LLM application feels when users can experiment with it more conveniently.

This project represents the transition from a basic script to a more interactive application. It also gave me an opportunity to explore how model outputs can vary depending on the prompts and settings used.

**What I explored**
- Building an interactive interface with Gradio.
- Connecting an interface to an LLM-powered Python workflow.
- Experimenting with prompts and model-generation settings.
- Understanding the relationship between user input, model configuration, and generated output.

**The takeaway:** An LLM is not just an API call. The way users interact with it—and the choices we expose to them—can shape their experience.

---

### 03. AI Website Summarizer — Giving the Model a Job 🌐

**The next step: moving from conversation to solving a practical problem.**

A chatbot can respond to questions, but what if I want an application to work with information from a website?

That question led to the AI Website Summarizer.

Instead of asking users to manually copy and paste an entire article, the application follows a workflow: retrieve webpage content, extract useful text, and pass that content to an LLM to generate a summary.

The project brings together multiple components into one application rather than relying on a model call alone.

**What I explored**
- Retrieving webpage content using Python.
- Extracting text with web-scraping tools.
- Passing extracted content to an LLM for summarization.
- Connecting the workflow to an interactive Gradio interface.
- Handling the practical challenges of combining data extraction and language generation.

**The takeaway:** The real value of AI engineering emerges when models become part of a larger workflow that solves a specific problem.

---

## 🛠️ Tech Stack

- **Language:** Python
- **LLM integration:** API-based model interaction
- **Interface:** Gradio
- **Web content extraction:** Requests and BeautifulSoup, where used
- **Configuration:** Environment variables and `.env`
- **Version control:** Git and GitHub

*The exact models, providers, and dependencies are determined by each project's implementation.*

---

## 📁 Repository Structure

```text
AI-Infused-Learning/
├── README.md
├── .gitignore
└── 1st Session/
    ├── chat_model/
    │   └── app.py
    ├── llm_arena/
    │   └── arena_app.py
    ├── summarizer/
    │   ├── app.py
    │   ├── scrapper.py
    │   └── summarize.py
    ├── requirements.txt
    └── .env.example
```

The repository may evolve as I add documentation, improve project organization, and build more applications.

---

## 🚀 Getting Started

### Prerequisites
- Python installed on your system.
- API credentials for the model provider used by the relevant project.
- Git, if you want to clone the repository.

### Setup

Clone the repository:

```bash
git clone https://github.com/vishwaspatidar/AI-Infused-Learning.git
cd AI-Infused-Learning
```

Navigate to the first session:

```bash
cd "1st Session"
```

Create and activate a virtual environment:

```bash
python -m venv .venv
```

macOS/Linux:

```bash
source .venv/bin/activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Create your own local `.env` file using `.env.example` as a reference. Add your own API credentials using the exact variable names expected by the code.

**Never commit your actual `.env` file or API keys.**

### Run the projects

Run each project from its respective directory, using the relevant entry point:

| Project | Entry point |
|---|---|
| Chat Model | `chat_model/app.py` |
| LLM Arena | `llm_arena/arena_app.py` |
| Website Summarizer | `summarizer/app.py` |

For example, from the `1st Session` directory:

```bash
python chat_model/app.py
```

For the Gradio-based projects, run the corresponding entry point in the same way. If the dependencies or environment variables differ by project, follow that project's setup instructions.

---

## 🧠 What This Session Taught Me

The biggest lesson was that building an AI application involves more than sending a prompt to a model.

It means connecting components, managing configuration, designing an interaction, processing information, and making the entire workflow usable.

These projects are early experiments, not production-ready systems. They are a foundation I can build upon as I deepen my understanding of LLMs, evaluation, retrieval, and AI application development.

---

## 🔭 What's Next?

This is the first session, not the finish line.

As I continue learning, I want to move beyond making AI applications work and start understanding how to make them more reliable, evaluate their behaviour, handle failure cases, and solve increasingly meaningful problems.

I'll use this repository to document that progression—what I build, what I learn, what breaks, and how I improve.

**Learning by building. Improving through experimentation. One project at a time.**

